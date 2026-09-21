#!/usr/bin/env python3
"""Extract cost and token usage from `opencode run --format json` output.

Reads JSONL events on stdin, prints a usage summary as JSON on stdout.

The event stream is not a documented interface, so this walks each event
recursively looking for cost/token fields. For cumulative fields (opencode emits
progressively updated message records) the maximum seen is used rather than the
sum, to avoid double counting. `found: false` is reported honestly when nothing
is recognised.
"""
from __future__ import annotations

import json
import sys


def walk(obj, costs: list[float], tokens: dict[str, float]) -> None:
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "cost" and isinstance(value, (int, float)) and not isinstance(value, bool):
                costs.append(float(value))
            elif key == "tokens" and isinstance(value, dict):
                for token_key, token_value in value.items():
                    if isinstance(token_value, (int, float)) and not isinstance(token_value, bool):
                        tokens[token_key] = max(tokens.get(token_key, 0.0), float(token_value))
            elif (
                key in {"input_tokens", "output_tokens", "total_tokens", "reasoning_tokens",
                        "cache_read_tokens", "cache_write_tokens"}
                and isinstance(value, (int, float))
                and not isinstance(value, bool)
            ):
                tokens[key] = max(tokens.get(key, 0.0), float(value))
            else:
                walk(value, costs, tokens)
    elif isinstance(obj, list):
        for item in obj:
            walk(item, costs, tokens)


def pick(tokens: dict[str, float], *names: str):
    for name in names:
        if name in tokens:
            return int(tokens[name])
    return None


def main() -> int:
    costs: list[float] = []
    tokens: dict[str, float] = {}
    events = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        events += 1
        walk(event, costs, tokens)

    input_tokens = pick(tokens, "input", "input_tokens")
    output_tokens = pick(tokens, "output", "output_tokens")
    total = pick(tokens, "total", "total_tokens")
    if total is None and (input_tokens is not None or output_tokens is not None):
        total = (input_tokens or 0) + (output_tokens or 0)

    result = {
        "found": events > 0,
        "events": events,
        "cost_usd": round(max(costs), 6) if costs else None,
        "tokens": {
            "input": input_tokens,
            "output": output_tokens,
            "reasoning": pick(tokens, "reasoning", "reasoning_tokens"),
            "cache_read": pick(tokens, "cache_read", "cache_read_tokens"),
            "cache_write": pick(tokens, "cache_write", "cache_write_tokens"),
            "total": total,
        },
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
