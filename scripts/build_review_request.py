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

SCHEMA_VERSION_LEGACY = 1
SCHEMA_VERSION = 2

# Schema v1 (legacy): rendered with its own ten keys, exactly as recorded.
DIM_ORDER_V1 = [
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

# Schema v2 (weights 1.3.0): twelve dimensions, with readable labels.
DIM_ORDER = [
    "problem_severity_frequency",
    "buyer_budget_clarity",
    "evidence_strength",
    "seo_discoverability",
    "self_service_fit",
    "distribution",
    "founder_fit",
    "economics",
    "validation_speed_cost",
    "feasibility",
    "differentiation",
    "risk",
]

DIM_LABELS = {
    "problem_severity_frequency": "Problem severity / frequency",
    "buyer_budget_clarity": "Buyer budget clarity",
    "evidence_strength": "Evidence strength",
    "seo_discoverability": "SEO discoverability",
    "self_service_fit": "Self-service fit",
    "distribution": "Distribution",
    "founder_fit": "Founder fit",
    "economics": "Economics",
    "validation_speed_cost": "Validation speed / cost",
    "feasibility": "Feasibility",
    "differentiation": "Differentiation",
    "risk": "Risk",
}


def load(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def as_dict(value) -> dict:
    return value if isinstance(value, dict) else {}


def as_list(value) -> list:
    return value if isinstance(value, list) else []


def schema_version_of(scorecard: dict) -> int:
    """Schema version named by a scorecard; cards without one are legacy v1."""
    if not isinstance(scorecard, dict):
        return SCHEMA_VERSION_LEGACY
    try:
        return int(scorecard.get("schema_version", SCHEMA_VERSION_LEGACY))
    except (TypeError, ValueError):
        return SCHEMA_VERSION_LEGACY


def dim_table(scorecard: dict) -> str:
    dimensions = as_dict(scorecard.get("dimensions"))
    version = schema_version_of(scorecard)
    keys = DIM_ORDER if version >= SCHEMA_VERSION else DIM_ORDER_V1
    lines = [
        "| Dimension | Weight | Score | Confidence | Evidence |",
        "|---|---|---|---|---|",
    ]
    for key in keys:
        label = DIM_LABELS.get(key, key) if version >= SCHEMA_VERSION else key
        dim = as_dict(dimensions.get(key))
        score = "unscored" if dim.get("score") is None else str(dim.get("score"))
        refs = dim.get("evidence") or []
        evidence = ", ".join(f"`{r}`" for r in refs) if refs else "-"
        lines.append(
            f"| {label} | {dim.get('weight', '-')} | {score} | "
            f"{dim.get('confidence', 'unknown')} | {evidence} |"
        )
    return "\n".join(lines)


def filter_table(scorecard: dict) -> str:
    lines = ["| Filter | Status | Note | Evidence / resolve_via |", "|---|---|---|---|"]
    for key, item in as_dict(scorecard.get("hard_filters")).items():
        item = as_dict(item)
        if item.get("status") == "pass":
            detail = item.get("evidence") or []
        elif item.get("status") == "unknown":
            detail = [f"resolve via: {item.get('resolve_via', '')}"]
        else:
            detail = []
        rendered = "; ".join(f"`{r}`" for r in detail) if detail else "-"
        lines.append(f"| {key} | {item.get('status', 'unknown')} | {item.get('note', '')} | {rendered} |")
    return "\n".join(lines)


def seo_section(scorecard: dict) -> str:
    """Compact Markdown summary of a schema-v2 seo_assessment block."""
    seo = scorecard.get("seo_assessment")
    if not isinstance(seo, dict) or not seo:
        return "(no seo_assessment recorded)"
    lines = []

    queries = as_list(seo.get("seed_queries"))
    if queries:
        lines.append("**Seed queries**")
        for query in queries:
            query = as_dict(query)
            evidence = []
            for entry in as_list(query.get("demand_evidence")):
                entry = as_dict(entry)
                evidence.append(f"{entry.get('source', 'unknown')} ({entry.get('date', 'unknown')})")
            lines.append(
                f"- `{query.get('query', 'unknown')}` - intent: {query.get('intent_cluster', 'unknown')}; "
                f"demand evidence: {'; '.join(evidence) or 'not recorded'}"
            )
    else:
        lines.append("**Seed queries:** not recorded")

    serp = as_dict(seo.get("serp_landscape"))
    checked = serp.get("queries_checked") or []
    lines.append(
        f"**SERP landscape:** checked {serp.get('checked_date', 'unknown')}; "
        f"queries: {', '.join(str(q) for q in checked) or 'not recorded'}; "
        f"AI overview observed: {serp.get('ai_overview_observed', 'unknown')}"
    )
    pages = as_list(serp.get("pages"))
    if pages:
        for page in pages:
            page = as_dict(page)
            note = f" - {page.get('notes')}" if page.get("notes") else ""
            lines.append(f"- [{page.get('type', 'other')}] {page.get('url', 'unknown')}{note}")
    else:
        lines.append("- SERP pages: not recorded")

    feasibility = as_dict(seo.get("organic_entry_feasibility"))
    lines.append(
        f"**Organic entry feasibility:** {feasibility.get('assessment', 'not recorded')} "
        f"(unknowns: {', '.join(str(u) for u in as_list(feasibility.get('unknowns'))) or 'none recorded'})"
    )

    conversion = as_dict(seo.get("conversion_mechanics"))
    lines.append(
        f"**Conversion mechanics:** {conversion.get('path', 'not recorded')} "
        f"(requirements: {', '.join(str(r) for r in as_list(conversion.get('requirements'))) or 'not recorded'})"
    )

    scenarios = as_dict(seo.get("traffic_to_revenue_scenarios"))
    lines.append(f"**Traffic-to-revenue scenarios** (assumptions: {scenarios.get('assumptions_label', 'not recorded')})")
    for key in ("conservative", "modest", "optimistic"):
        lines.append(f"- {key}: {scenarios.get(key, 'not recorded')}")

    risks = as_dict(seo.get("seo_risks"))
    lines.append(
        "**SEO risks:** zero-click/AI: {zero_click_ai}; seasonality: {seasonality}; "
        "platform dependency: {platform_dependency}; other: {other}".format(
            zero_click_ai=risks.get("zero_click_ai", "not recorded"),
            seasonality=risks.get("seasonality", "not recorded"),
            platform_dependency=risks.get("platform_dependency", "not recorded"),
            other=risks.get("other", "not recorded"),
        )
    )

    unknowns = as_list(seo.get("unknowns"))
    if unknowns:
        lines.append("**Unknowns and cheapest next checks**")
        for unknown in unknowns:
            unknown = as_dict(unknown)
            lines.append(f"- {unknown.get('item', 'unknown')} -> {unknown.get('next_check', 'not recorded')}")
    else:
        lines.append("**Unknowns:** none recorded")
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
            e for e in as_list(as_dict(load(exp_index_path)).get("experiments"))
            if isinstance(e, dict) and e.get("idea_id") == args.slug
        ]

    scorecard = as_dict(scorecard)
    agg = as_dict(scorecard.get("aggregate"))
    vetoes = scorecard.get("vetoes") or []
    review = as_dict(scorecard.get("review"))
    version = schema_version_of(scorecard)
    schema_label = "legacy v1" if version == SCHEMA_VERSION_LEGACY else f"v{version}"

    out_path = Path(args.out) if args.out else root / "reviews" / f"{args.date}-{args.slug}-review-request.md"

    lines = [
        f"# Review request: {entry.get('title', args.slug)}",
        "",
        f"- **Idea:** `{args.slug}`",
        f"- **Date:** {args.date}",
        f"- **Trigger:** {args.trigger}",
        f"- **State:** `{entry.get('state', 'unknown')}`",
        f"- **Proposed transition:** {args.transition}",
        f"- **Reviewed revision:** `{args.revision}`",
        f"- **Scorecard:** {schema_label} (weights `{scorecard.get('weights_version') or 'unknown'}`, "
        f"method `{scorecard.get('method_version') or 'unknown'}`)",
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
        f"- Weighted total: **{agg.get('weighted_total', 'unknown')} / 100** "
        f"(threshold {agg.get('threshold', 'unknown')}, meets_threshold={agg.get('meets_threshold', 'unknown')})",
        f"- Scored weight: {agg.get('scored_weight', 'unknown')} / 100",
        f"- Overall confidence: **{scorecard.get('confidence', 'unknown')}**",
        f"- Evidence level: `{entry.get('evidence_level', 'unknown')}`",
        f"- Vetoes: {('none' if not vetoes else json.dumps(vetoes))}",
        "",
        "## Hard filters",
        "",
        filter_table(scorecard),
        "",
    ]
    if version >= SCHEMA_VERSION:
        lines += [
            "## SEO assessment",
            "",
            seo_section(scorecard),
            "",
        ]
    lines += [
        "## Strongest supporting case",
        "",
        extract_section(dossier, "Strongest supporting case"),
        "",
        "## Why now?",
        "",
        extract_section(dossier, "Why now?"),
        "",
        "## Novelty / incumbent sanity check",
        "",
        extract_section(dossier, "Novelty / incumbent sanity check"),
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
            approval = as_dict(exp.get("approval"))
            lines += [
                f"- `{exp.get('id', 'unknown')}` status=`{exp.get('status', 'unknown')}` "
                f"approval.granted=`{approval.get('granted')}` "
                f"plan=`{exp.get('plan') or 'not recorded'}` results=`{exp.get('results') or 'none'}`",
                f"  - Central assumption: {exp.get('central_assumption') or 'not recorded'}",
                f"  - Kill condition: {exp.get('kill_condition') or 'not recorded'}",
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
        "a `pass` hard filter that is only an assumption, an over-generous why-now claim, premature "
        "advancement, missed legal/platform risk, or a hard filter that should have failed.",
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
