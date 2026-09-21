# runs/ — operational run metadata

One directory per invocation of `scripts/run.sh`, named
`<UTC timestamp>-<mode>` (`normal`, `dry-run`, `smoke`).

| File | Contents |
|---|---|
| `run.json` | Full record: mode, status, timestamps, agent, model, method version, input/output revision, attempts, timeout, cost bound, cost, tokens, changed files, validation result, summary path |
| `usage.json` | Cost and token counts extracted from the worker output |
| `validation.json` | Result of `scripts/validate_repo.py --json` for this run |
| `summary.md` | The worker's run summary (advances, kills, decisions needed, boundaries confirmed) |
| `raw.jsonl` | Raw `opencode run --format json` output (gitignored) |
| `stderr.log` | Worker stderr (gitignored) |
| `dry-run.diff` | `git diff --cached` of the throwaway copy for `--dry-run` runs |
| `repo/` | Throwaway repository copy for `--dry-run` runs (gitignored) |

`index.jsonl` is an append-only line-per-run index written by
`scripts/finalize_run.py`; `run.json` files are the detailed record. Both are
tracked in git for audit. A run directory is never rewritten.
