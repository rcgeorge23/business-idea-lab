#!/usr/bin/env python3
"""Generate a review request package from repository artefacts.

Usage:
    python3 scripts/build_review_request.py --slug geonerd \
        --trigger "proposed for validation-ready" \
        --transition "adversarially-researched -> validation-ready"

Reads ideas/index.json, ideas/<slug>/{scorecard.json,dossier.md,decision.md},
experiments/index.json and writes reviews/<date>-<slug>-review-request.md.
Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

DIM_ORDER = [
    "problem_severity_frequency",
    "buyer_budget_clarity",
    "evidence_strength",
    "distribution",
    "differentiation",
    "validation_speed_cost",
    "feasibility",
    "economics",
    "founder_fit",
    "risk",
]


def load(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def dim_table(scorecard: dict) -> str:
    lines = [
        "| Dimension | Weight | Score | Confidence | Evidence |",
        "|---|---|---|---|---|",
    ]
    for key in DIM_ORDER:
        dim = scorecard["dimensions"][key]
        score = "unscored" if dim.get("score") is None else str(dim["score"])
        refs = dim.get("evidence") or []
        evidence = ", ".join(f"`{r}`" for r in refs) if refs else "-"
        lines.append(f"| {key} | {dim['weight']} | {score} | {dim['confidence']} | {evidence} |")
    return "\n".join(lines)


def filter_table(scorecard: dict) -> str:
    lines = ["| Filter | Status | Note |", "|---|---|---|"]
    for key, item in scorecard["hard_filters"].items():
        lines.append(f"| {key} | {item['status']} | {item.get('note', '')} |")
    return "\n".join(lines)


def extract_section(path: Path, heading: str) -> str:
    """Return the body of a '## <heading>' section from a Markdown file."""
    if not path.exists():
        return "(file missing)"
    text = path.read_text(encoding="utf-8")
    marker = f"## {heading}"
    index = text.find(marker)
    if index == -1:
        return f"(section '{heading}' not found in {path.name})"
    rest = text[index + len(marker):]
    end = rest.find("\n## ")
    return (rest[:end] if end != -1 else rest).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--trigger", required=True)
    parser.add_argument("--transition", required=True)
    parser.add_argument("--revision", default="uncommitted")
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    index = load(root / "ideas" / "index.json")
    entry = next((i for i in index["ideas"] if i["slug"] == args.slug), None)
    if entry is None:
        print(f"ERROR: idea '{args.slug}' not found in ideas/index.json", file=sys.stderr)
        return 1
    scorecard = load(root / "ideas" / args.slug / "scorecard.json")
    dossier = root / "ideas" / args.slug / "dossier.md"
    decision = root / "ideas" / args.slug / "decision.md"

    experiments = []
    exp_index_path = root / "experiments" / "index.json"
    if exp_index_path.exists():
        experiments = [
            e for e in load(exp_index_path).get("experiments", []) if e.get("idea_id") == args.slug
        ]

    agg = scorecard["aggregate"]
    vetoes = scorecard.get("vetoes") or []
    review = scorecard["review"]

    out_path = Path(args.out) if args.out else root / "reviews" / f"{args.date}-{args.slug}-review-request.md"

    lines = [
        f"# Review request: {entry['title']}",
        "",
        f"- **Idea:** `{args.slug}`",
        f"- **Date:** {args.date}",
        f"- **Trigger:** {args.trigger}",
        f"- **State:** `{entry['state']}`",
        f"- **Proposed transition:** {args.transition}",
        f"- **Reviewed revision:** `{args.revision}`",
        "- **Requested from:** ChatGPT (independent reviewer; not market validation)",
        "",
        "## What the reviewer must decide",
        "",
        f"Whether `{args.transition}` is justified by the evidence in this repository, or whether "
        "the idea should receive `changes-requested` or be `killed`.",
        "",
        "## State and scores",
        "",
        dim_table(scorecard),
        "",
        f"- Weighted total: **{agg['weighted_total']} / 100** (threshold {agg['threshold']}, "
        f"meets_threshold={agg['meets_threshold']})",
        f"- Scored weight: {agg['scored_weight']} / 100",
        f"- Overall confidence: **{scorecard['confidence']}**",
        f"- Evidence level: `{entry['evidence_level']}`",
        f"- Vetoes: {('none' if not vetoes else json.dumps(vetoes))}",
        "",
        "## Hard filters",
        "",
        filter_table(scorecard),
        "",
        "## Strongest supporting case",
        "",
        extract_section(dossier, "Strongest supporting case"),
        "",
        "## Strongest disconfirming case",
        "",
        extract_section(dossier, "Adversarial case (strongest case this is wrong)"),
        "",
        "## Unresolved assumptions",
        "",
        extract_section(dossier, "Unresolved assumptions"),
        "",
        "## Cheapest decisive experiment",
        "",
        extract_section(dossier, "Cheapest decisive experiment"),
        "",
        "## Experiment register",
        "",
    ]
    if experiments:
        for exp in experiments:
            lines += [
                f"- `{exp['id']}` status=`{exp['status']}` approval.granted=`{exp['approval']['granted']}` "
                f"plan=`{exp['plan']}` results=`{exp.get('results') or 'none'}`",
                f"  - Central assumption: {exp['central_assumption']}",
                f"  - Kill condition: {exp['kill_condition']}",
            ]
    else:
        lines.append("(no experiment registered)")

    lines += [
        "",
        "## Decision record",
        "",
        extract_section(decision, "What changed"),
        "",
        "## Machine-readable review block",
        "",
        "```json",
        json.dumps(review, indent=2),
        "```",
        "",
        "## Instructions to the reviewer",
        "",
        "1. Work only from the repository artefacts listed below. Do not fetch or assume outside data.",
        "2. Attack the weakest link: unsupported inference, convenience evidence, mis-scored dimension, "
        "premature advancement, missed legal/platform risk, or a hard filter that should have failed.",
        "3. State a verdict: `changes-requested`, `approved`, or `killed`.",
        "4. For each finding, give the evidence checked and the condition that would change the verdict.",
        f"5. Write the response as `reviews/{args.date}-{args.slug}-<reviewer>-<model>.md` following "
        "`templates/review/response.md`.",
        "6. A second model is not market validation. Agreement is not demand evidence and cannot "
        "advance the idea beyond `validation-ready`.",
        "",
        "## Artefacts for review",
        "",
        f"- `ideas/{args.slug}/dossier.md`",
        f"- `ideas/{args.slug}/scorecard.json`",
        f"- `ideas/{args.slug}/decision.md`",
        f"- `evidence/{args.slug}/`",
        "- `experiments/index.json`",
        "- `ideas/index.json`",
        "",
    ]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
