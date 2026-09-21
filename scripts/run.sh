#!/usr/bin/env bash
# Deterministic, non-interactive runner for the business-idea-lab discovery loop.
#
# Usage:
#   scripts/run.sh [--dry-run] [--smoke] [--allow-dirty]
#                  [--timeout SECONDS] [--max-cost USD] [--max-attempts N]
#                  [--model provider/model] [--agent NAME]
#
# Modes:
#   normal   run the worker against the live repository and write run metadata
#   --dry-run  run the worker against a throwaway copy under runs/<id>/repo,
#              leave the live ledger untouched, and write runs/<id>/dry-run.diff
#   --smoke  plumbing check only: one trivial model call, no ledger changes
#   --dry-run --smoke  exercise the dry-run copy/diff mechanics cheaply
#              (trivial prompt, throwaway copy)
#
# Every invocation writes runs/<run-id>/ (raw output, usage, validation, summary)
# and appends one line to runs/index.jsonl via scripts/finalize_run.py.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OPENCODE_BIN="${OPENCODE_BIN:-opencode}"
PROMPT_FILE="$ROOT/scripts/prompts/lab-run.md"
SMOKE_PROMPT="Reply with exactly: LAB_SMOKE_OK. Do not use any tools."

MODE="normal"
SMOKE=0
DRY=0
ALLOW_DIRTY=0
TIMEOUT=3600
MAX_COST="1.00"
MAX_ATTEMPTS=3
MODEL="opencode-go/deepseek-v4.1-flash"
AGENT="idea-worker"

usage() {
    sed -n '2,17p' "$0" | sed 's/^# \{0,1\}//'
    exit "${1:-0}"
}

while [ $# -gt 0 ]; do
    case "$1" in
        --dry-run)      DRY=1 ;;
        --smoke)        SMOKE=1 ;;
        --allow-dirty)  ALLOW_DIRTY=1 ;;
        --timeout)      TIMEOUT="$2"; shift ;;
        --max-cost)     MAX_COST="$2"; shift ;;
        --max-attempts) MAX_ATTEMPTS="$2"; shift ;;
        --model)        MODEL="$2"; shift ;;
        --agent)        AGENT="$2"; shift ;;
        -h|--help)      usage 0 ;;
        *) echo "error: unknown argument: $1" >&2; usage 1 ;;
    esac
    shift
done

command -v "$OPENCODE_BIN" >/dev/null 2>&1 || {
    echo "error: opencode binary not found on PATH (set OPENCODE_BIN)" >&2
    exit 1
}

if [ "$DRY" -eq 1 ]; then
    MODE="dry-run"
elif [ "$SMOKE" -eq 1 ]; then
    MODE="smoke"
fi
if [ "$SMOKE" -eq 1 ]; then
    PROMPT="$SMOKE_PROMPT"
else
    PROMPT="$(cat "$PROMPT_FILE")"
fi
git -C "$ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1 || {
    echo "error: $ROOT is not a git repository" >&2
    exit 1
}

# --- preconditions -----------------------------------------------------------
if [ "$ALLOW_DIRTY" -ne 1 ]; then
    dirty="$(git -C "$ROOT" status --porcelain -- . ':(exclude)runs' || true)"
    if [ -n "$dirty" ]; then
        echo "error: working tree is dirty (runs/ excluded). Commit or stash first," >&2
        echo "       or pass --allow-dirty to run anyway." >&2
        echo "$dirty" | sed 's/^/       /' >&2
        exit 1
    fi
fi

METHOD_VERSION="$(tr -d '[:space:]' < "$ROOT/method/VERSION")"
STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)-${MODE}"
RUN_DIR="$ROOT/runs/$RUN_ID"
INPUT_REVISION="$(git -C "$ROOT" rev-parse --short HEAD 2>/dev/null || echo uncommitted)"
mkdir -p "$RUN_DIR"

tree_fingerprint() {
    git -C "$ROOT" status --porcelain -- . ':(exclude)runs' | sha1sum | cut -d' ' -f1
}

run_worker() {
    # $1 = directory to run in
    local workdir="$1"
    set +e
    LAB_RUN_ID="$RUN_ID" timeout "$TIMEOUT" \
        "$OPENCODE_BIN" run --dir "$workdir" --agent "$AGENT" --model "$MODEL" \
        --format json "$PROMPT" > "$RUN_DIR/raw.jsonl" 2> "$RUN_DIR/stderr.log"
    local rc=$?
    set -e
    return $rc
}

ATTEMPT=0
RC=1
TREE_BEFORE="$(tree_fingerprint)"
LAST_ATTEMPT_DIR="$ROOT"

while [ "$ATTEMPT" -lt "$MAX_ATTEMPTS" ]; do
    ATTEMPT=$((ATTEMPT + 1))
    echo "run $RUN_ID: attempt $ATTEMPT/$MAX_ATTEMPTS (mode=$MODE)"
    if [ "$MODE" = "dry-run" ]; then
        WORKDIR="$RUN_DIR/repo"
        rm -rf "$WORKDIR"
        mkdir -p "$WORKDIR"
        tar -C "$ROOT" --exclude=./runs -cf - . | tar -C "$WORKDIR" -xf -
    else
        WORKDIR="$ROOT"
    fi
    LAST_ATTEMPT_DIR="$WORKDIR"
    if run_worker "$WORKDIR"; then
        RC=0
        break
    fi
    RC=$?
    echo "run $RUN_ID: attempt $ATTEMPT failed (exit $RC)" >&2
    if [ "$ATTEMPT" -ge "$MAX_ATTEMPTS" ]; then
        break
    fi
    # only retry when the tree is unchanged (no partial edits to build on)
    if [ "$(tree_fingerprint)" != "$TREE_BEFORE" ] || [ "$INPUT_REVISION" = "uncommitted" ]; then
        echo "run $RUN_ID: tree changed or no revision to restore to; not retrying" >&2
        break
    fi
    TREE_BEFORE="$(tree_fingerprint)"
done

# --- collect usage -----------------------------------------------------------
python3 "$ROOT/scripts/extract_usage.py" < "$RUN_DIR/raw.jsonl" > "$RUN_DIR/usage.json"
COST="$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1])).get("cost_usd") or "")' "$RUN_DIR/usage.json")"

# --- validate ----------------------------------------------------------------
if [ "$MODE" = "dry-run" ]; then
    VALIDATION_ROOT="$RUN_DIR/repo"
    (
        cd "$VALIDATION_ROOT"
        git add -A >/dev/null 2>&1 || true
        git diff --cached > "$RUN_DIR/dry-run.diff" 2>/dev/null || true
    )
    if [ -f "$WORKDIR/runs/$RUN_ID/summary.md" ]; then
        cp "$WORKDIR/runs/$RUN_ID/summary.md" "$RUN_DIR/summary.md"
    fi
else
    VALIDATION_ROOT="$ROOT"
fi

set +e
python3 "$ROOT/scripts/validate_repo.py" --root "$VALIDATION_ROOT" --json > "$RUN_DIR/validation.json" 2>"$RUN_DIR/validation.stderr.log"
VALIDATION_RC=$?
set -e
if [ "$VALIDATION_RC" -ne 0 ]; then
    if [ ! -s "$RUN_DIR/validation.json" ]; then
        printf '{"status":"error","errors":["validator crashed; see validation.stderr.log"],"warnings":[]}\n' > "$RUN_DIR/validation.json"
    fi
fi

# --- decide status -----------------------------------------------------------
STATUS="success"
if [ "$RC" -ne 0 ]; then
    STATUS="failed"
elif [ "$VALIDATION_RC" -ne 0 ]; then
    STATUS="invalid-output"
elif [ -n "$COST" ] && python3 -c 'import sys;sys.exit(0 if float(sys.argv[1])>float(sys.argv[2]) else 1)' "$COST" "$MAX_COST"; then
    STATUS="over-budget"
fi

if [ "$MODE" = "dry-run" ]; then
    CHANGED_SOURCE="$VALIDATION_ROOT"
else
    CHANGED_SOURCE="$ROOT"
fi
CHANGED_FILES="$(git -C "$CHANGED_SOURCE" status --porcelain -- . ':(exclude)runs' | cut -c4- || true)"

OUTPUT_REVISION="$(git -C "$ROOT" rev-parse --short HEAD 2>/dev/null || echo uncommitted)"
SUMMARY_PATH=""
[ -f "$RUN_DIR/summary.md" ] && SUMMARY_PATH="runs/$RUN_ID/summary.md"

FINISHED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
FINALIZE_ARGS=(
    --root "$ROOT" --run-id "$RUN_ID" --mode "$MODE" --status "$STATUS"
    --started "$STARTED" --finished "$FINISHED"
    --agent "$AGENT" --model "$MODEL" --method-version "$METHOD_VERSION"
    --input-revision "$INPUT_REVISION" --output-revision "$OUTPUT_REVISION"
    --attempts "$ATTEMPT" --timeout "$TIMEOUT" --max-cost "$MAX_COST"
)
if [ -n "$SUMMARY_PATH" ]; then
    FINALIZE_ARGS+=(--summary "$SUMMARY_PATH")
fi
while IFS= read -r f; do
    [ -n "$f" ] && FINALIZE_ARGS+=(--changed-file "$f")
done <<< "$CHANGED_FILES"
python3 "$ROOT/scripts/finalize_run.py" "${FINALIZE_ARGS[@]}"

# --- report ------------------------------------------------------------------
echo
echo "run id:        $RUN_ID"
echo "mode:          $MODE"
echo "status:        $STATUS"
echo "cost (USD):    ${COST:-unknown} (bound $MAX_COST)"
echo "attempts:      $ATTEMPT/$MAX_ATTEMPTS"
echo "validation:    $([ "$VALIDATION_RC" -eq 0 ] && echo pass || echo fail)"
echo "run dir:       runs/$RUN_ID"
[ -n "$SUMMARY_PATH" ] && echo "summary:       $SUMMARY_PATH"
[ "$MODE" = "dry-run" ] && echo "dry-run diff:  runs/$RUN_ID/dry-run.diff"
[ "$STATUS" = "success" ] || exit 1
