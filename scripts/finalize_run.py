#!/usr/bin/env python3
"""Write run metadata (`runs/<run-id>/run.json`) and append to `runs/index.jsonl`.

Called by scripts/run.sh at the end of every run (including failures). Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_json(path: Path):
    if not path.exists():
        return None
    try:
        with path.open(encoding="utf-8") as fh:
            return json.load(fh)
    except (json.JSONDecodeError, OSError):
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--mode", required=True, choices=["normal", "dry-run", "smoke"])
    parser.add_argument("--status", required=True, choices=["success", "failed", "invalid-output", "over-budget"])
    parser.add_argument("--started", required=True)
    parser.add_argument("--finished", required=True)
    parser.add_argument("--agent", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--method-version", required=True)
    parser.add_argument("--input-revision", required=True)
    parser.add_argument("--output-revision", required=True)
    parser.add_argument("--attempts", type=int, required=True)
    parser.add_argument("--timeout", type=int, required=True)
    parser.add_argument("--max-cost", type=float, required=True)
    parser.add_argument("--changed-file", action="append", default=[])
    parser.add_argument("--summary", default="")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    run_dir = root / "runs" / args.run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    usage = load_json(run_dir / "usage.json") or {}
    validation = load_json(run_dir / "validation.json") or {"status": "not-run", "errors": [], "warnings": []}

    record = {
        "schema_version": 1,
        "run_id": args.run_id,
        "mode": args.mode,
        "status": args.status,
        "started_at": args.started,
        "finished_at": args.finished,
        "agent": args.agent,
        "model": args.model,
        "method_version": args.method_version,
        "input_revision": args.input_revision,
        "output_revision": args.output_revision,
        "attempts": args.attempts,
        "timeout_seconds": args.timeout,
        "max_cost_usd": args.max_cost,
        "cost_usd": usage.get("cost_usd"),
        "tokens": usage.get("tokens", {"input": None, "output": None, "total": None}),
        "changed_files": sorted(args.changed_file),
        "validation": {
            "status": validation.get("status", "not-run"),
            "errors": validation.get("errors", []),
        },
        "summary_path": args.summary or None,
    }
    with (run_dir / "run.json").open("w", encoding="utf-8") as fh:
        json.dump(record, fh, indent=2)
        fh.write("\n")

    index_line = {
        "run_id": args.run_id,
        "mode": args.mode,
        "status": args.status,
        "started_at": args.started,
        "finished_at": args.finished,
        "agent": args.agent,
        "model": args.model,
        "method_version": args.method_version,
        "input_revision": args.input_revision,
        "output_revision": args.output_revision,
        "cost_usd": usage.get("cost_usd"),
        "tokens_total": (usage.get("tokens") or {}).get("total"),
        "validation": validation.get("status", "not-run"),
        "summary": args.summary or None,
    }
    index_path = root / "runs" / "index.jsonl"
    existing = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
    if args.run_id in existing:
        pass  # never duplicate a run record
    else:
        with index_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(index_line) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
