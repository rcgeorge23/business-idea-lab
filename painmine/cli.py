"""Command-line entry point for the painmine spike.

Examples:
    python3 -m painmine.cli pipeline --family a_manual_rekey --out painmine/poc/latest
    python3 -m painmine.cli pipeline --offline-fixture painmine/tests/fixtures/raw_items.jsonl --out painmine/poc/fixture
    python3 -m painmine.cli validate --run-dir painmine/poc/latest
    python3 -m painmine.cli observations --run-dir painmine/poc/latest
"""
from __future__ import annotations

import argparse
import os
import sys
import time

from .budget import Budget
from .cluster import cluster as cluster_signals
from .dedupe import dedupe
from .extract import extract_many
from .fetch import ENABLED_SOURCES, collect, load_fixture_items, summarise_statuses
from .llm import OpenCodeGo
from .persistence import cluster_archetype, persistence_thesis
from .rank import rank_clusters
from .schema import validate_signal
from .state import State
from .synthesis import independent_synthesis
from .to_observation import render_pool, to_observations
from .util import (
    read_json,
    read_jsonl,
    sha1_hex,
    utcnow,
    utcnow_iso,
    write_json,
    write_jsonl,
)

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_LIMITS = os.path.join(HERE, "limits.json")
DEFAULT_SOURCES = os.path.join(HERE, "sources.json")
VERSION = "0.1.0"


# ----------------------------------------------------------------- helpers
def load_limits(path: str) -> dict:
    limits = read_json(path, None)
    if not isinstance(limits, dict) or "fetch" not in limits:
        raise SystemExit(f"limits file not usable: {path}")
    return limits


def family_queries(sources_path: str, family: str) -> list[str]:
    data = read_json(sources_path, {}) or {}
    raw_families = data.get("query_families") or {}
    families = {name: value for name, value in raw_families.items() if isinstance(value, list)}
    if family == "all":
        queries: list[str] = []
        for name in sorted(families):
            for query in families[name]:
                if query not in queries:
                    queries.append(query)
        if not queries:
            raise SystemExit("no query families configured")
        return queries
    if family not in families:
        raise SystemExit(f"unknown query family '{family}'; available: {', '.join(sorted(families))}, all")
    return list(families[family])


def make_run_id() -> str:
    stamp = utcnow().strftime("%Y%m%dT%H%M%SZ")
    return f"pm-{stamp}-{sha1_hex(stamp + str(time.time()), 4)}"


def _print(msg: str) -> None:
    print(msg, flush=True)


# ----------------------------------------------------------------- pipeline
def run_pipeline(args: argparse.Namespace) -> int:
    limits = load_limits(args.limits)
    if args.max_requests:
        limits["fetch"]["max_requests_per_run"] = min(
            int(args.max_requests), int(limits["fetch"]["max_requests_per_run"])
        )
    if args.enable_llm:
        limits["llm"]["enabled"] = True
    run_id = args.run_id or make_run_id()
    out_dir = os.path.abspath(args.out)
    os.makedirs(out_dir, exist_ok=True)
    budget = Budget(limits)
    state = State(args.state, seen_cap=int(limits.get("retention", {}).get("state_seen_ids_cap", 5000))) if args.state else None
    queries = family_queries(args.sources_file, args.family)
    sources = [s.strip() for s in args.sources.split(",") if s.strip()]

    meta = {
        "run_id": run_id,
        "version": VERSION,
        "generated_at": utcnow_iso(),
        "mode": "offline-fixture" if args.offline_fixture else "live-public-sources",
        "family": args.family,
        "queries": queries,
        "sources_requested": sources,
        "limits_file": os.path.relpath(args.limits),
        "llm_requested": bool(args.enable_llm),
    }

    # 1. collect ------------------------------------------------------------
    if args.offline_fixture:
        items = load_fixture_items(args.offline_fixture)
        statuses = [{"source_id": "fixture", "ok": True, "items": len(items), "error": None}]
    else:
        items, statuses = collect(queries, sources, budget, state=state)
    for item in items:
        item.setdefault("retrieved_at", utcnow_iso())
    write_jsonl(os.path.join(out_dir, "raw-items.jsonl"), items)

    # 2. extract ------------------------------------------------------------
    signals, rejects = extract_many(items, limits)
    write_jsonl(os.path.join(out_dir, "extraction-rejects.jsonl"), rejects)

    # 3. dedupe -------------------------------------------------------------
    dedupe_result = dedupe(
        signals,
        threshold=float(limits.get("dedupe", {}).get("jaccard_threshold", 0.62)),
        shingle_k=int(limits.get("dedupe", {}).get("shingle_size", 5)),
    )

    # 4. cluster ------------------------------------------------------------
    clusters = cluster_signals(signals, limits)
    signals_by_id = {s["signal_id"]: s for s in signals}
    for cluster in clusters:
        member_signals = [signals_by_id[sid] for sid in cluster["member_signal_ids"] if sid in signals_by_id]
        cluster["archetype"] = cluster_archetype(member_signals)
        cluster["persistence"] = persistence_thesis(cluster, member_signals)
        for signal in member_signals:
            signal["cluster_id"] = cluster["cluster_id"]
    clusters = rank_clusters(clusters, signals, limits)

    # 5. synthesis (only when explicitly enabled) ---------------------------
    synthesis_records: dict[str, dict] = {}
    if args.synthesis:
        llm = OpenCodeGo(limits, budget)
        for cluster in clusters[: args.synthesis_top]:
            member_signals = [signals_by_id[sid] for sid in cluster["member_signal_ids"] if sid in signals_by_id]
            synthesis_records[cluster["cluster_id"]] = independent_synthesis(cluster, member_signals, llm)

    # 6. observations -------------------------------------------------------
    observations = to_observations(clusters, max_promote=args.max_promote)
    pool_text = render_pool(
        observations,
        {
            "generated_at": meta["generated_at"],
            "version": VERSION,
            "run_id": run_id,
        },
    )
    with open(os.path.join(out_dir, "observations.md"), "w", encoding="utf-8") as handle:
        handle.write(pool_text)
    write_json(os.path.join(out_dir, "observations.json"), observations)
    write_json(os.path.join(out_dir, "synthesis.json"), synthesis_records)

    # 7. persist ------------------------------------------------------------
    write_jsonl(os.path.join(out_dir, "signals.jsonl"), signals)
    write_json(os.path.join(out_dir, "dedupe-stats.json"), dedupe_result["stats"])
    write_json(os.path.join(out_dir, "clusters.json"), clusters)

    report = build_report(meta, budget, statuses, items, signals, rejects, dedupe_result, clusters)
    write_json(os.path.join(out_dir, "report.json"), report)
    with open(os.path.join(out_dir, "report.md"), "w", encoding="utf-8") as handle:
        handle.write(render_report_markdown(report))
    meta["budget"] = budget.summary()
    meta["source_status"] = summarise_statuses(statuses)
    write_json(os.path.join(out_dir, "run-meta.json"), meta)
    if state is not None:
        state.record_run({"run_id": run_id, "generated_at": meta["generated_at"], "signals": len(signals)})
        state.record_clusters(clusters)
        state.save()

    band_a = [c for c in clusters if (c.get("priority") or {}).get("band") == "A"]
    _print(
        f"painmine {run_id}: {len(items)} raw items -> {len(signals)} signals "
        f"({dedupe_result['stats']['duplicates_removed']} duplicates removed) -> {len(clusters)} clusters; "
        f"band A: {len(band_a)}; requests {budget.requests}/{budget.max_requests}; "
        f"elapsed {budget.elapsed():.1f}s; stop: {budget.stop_reason or 'none'}"
    )
    _print(f"artefacts: {out_dir}")
    return 0


# ----------------------------------------------------------------- report
def build_report(meta, budget, statuses, items, signals, rejects, dedupe_result, clusters) -> dict:
    top_clusters = []
    for cluster in clusters[:10]:
        priority = cluster.get("priority") or {}
        persistence = cluster.get("persistence") or {}
        top_clusters.append(
            {
                "cluster_id": cluster.get("cluster_id"),
                "label": cluster.get("label"),
                "role": cluster.get("role"),
                "independent_sources": cluster.get("independent_sources"),
                "member_count": cluster.get("member_count"),
                "duplicate_count": cluster.get("duplicate_count"),
                "source_types": cluster.get("source_types"),
                "named_systems": cluster.get("named_systems"),
                "priority_score": priority.get("score"),
                "priority_band": priority.get("band"),
                "vendor_led_risk": priority.get("vendor_led_risk"),
                "persistence_strength": persistence.get("strength"),
                "archetype": (cluster.get("archetype") or {}).get("archetype"),
                "first_seen": cluster.get("first_seen"),
                "last_seen": cluster.get("last_seen"),
            }
        )
    low_confidence = sorted(signals, key=lambda s: s.get("confidence", 1))[:5]
    reject_reasons: dict[str, int] = {}
    for reject in rejects:
        reject_reasons[reject["reason"]] = reject_reasons.get(reject["reason"], 0) + 1
    bands = {}
    for cluster in clusters:
        band = (cluster.get("priority") or {}).get("band", "?")
        bands[band] = bands.get(band, 0) + 1
    vendor_risks: dict[str, int] = {}
    for cluster in clusters:
        risk = (cluster.get("priority") or {}).get("vendor_led_risk", "unknown")
        vendor_risks[risk] = vendor_risks.get(risk, 0) + 1
    with_buyer = sum(1 for c in clusters if c.get("role"))
    recurrence = any((c.get("independent_sources") or 0) >= 3 for c in clusters)

    if not clusters:
        preliminary = "STOP"
        preliminary_note = "No clusters formed at this access level; do not build the crawler yet."
    elif any(b == "A" for b in bands) and any(
        (c.get("persistence") or {}).get("strength") in ("strong", "weak") for c in clusters
    ):
        preliminary = "ITERATE"
        preliminary_note = "At least one band-A cluster with a persistence thesis; iterate sources and run dual synthesis."
    else:
        preliminary = "ITERATE"
        preliminary_note = "Some signal found but no strong cluster yet; iterate on access/volume before PROCEED."

    return {
        "meta": meta,
        "budget": budget.summary(),
        "source_status": summarise_statuses(statuses),
        "volumes": {
            "raw_items": len(items),
            "extracted_signals": len(signals),
            "extraction_rejects": len(rejects),
            "extraction_reject_reasons": reject_reasons,
            "duplicates_removed": dedupe_result["stats"]["duplicates_removed"],
            "duplicate_ratio": dedupe_result["stats"]["duplicate_ratio"],
            "clusters_total": len(clusters),
            "clusters_with_buyer": with_buyer,
            "clusters_band_a": bands.get("A", 0),
            "clusters_band_b": bands.get("B", 0),
            "clusters_band_c": bands.get("C", 0),
            "clusters_independent_ge_3": sum(1 for c in clusters if (c.get("independent_sources") or 0) >= 3),
        },
        "top_clusters": top_clusters,
        "vendor_led_risk_mix": vendor_risks,
        "recurrence_measurable": recurrence,
        "low_confidence_extraction_examples": [
            {"signal_id": s.get("signal_id"), "confidence": s.get("confidence"), "statement": s.get("pain_statement")}
            for s in low_confidence
        ],
        "preliminary_recommendation": preliminary,
        "preliminary_recommendation_note": preliminary_note,
        "disclaimer": (
            "Discovery-priority scores are not business scores and not market validation. "
            "Method 1.6 scoring, hard filters and lifecycle gates are unchanged and still apply downstream."
        ),
    }


def render_report_markdown(report: dict) -> str:
    lines: list[str] = []
    meta = report["meta"]
    lines.append(f"# painmine run report — {meta.get('run_id')}")
    lines.append("")
    lines.append(f"- Generated: {meta.get('generated_at')}")
    lines.append(f"- Mode: {meta.get('mode')} | family: {meta.get('family')}")
    lines.append(f"- Queries: {', '.join('`' + q + '`' for q in meta.get('queries', []))}")
    lines.append(f"- Sources requested: {', '.join(meta.get('sources_requested', []))}")
    lines.append("")
    lines.append("## Volumes")
    lines.append("")
    for key, value in report["volumes"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Cost, runtime and limits")
    lines.append("")
    for key, value in report["budget"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Source access (attempted)")
    lines.append("")
    lines.append("| source | requests | ok | failed | items | errors |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for source, data in report["source_status"].items():
        lines.append(
            f"| {source} | {data.get('requests')} | {data.get('ok_requests')} | {data.get('failed_requests')} | "
            f"{data.get('items')} | {'; '.join(data.get('errors', []))[:180]} |"
        )
    lines.append("")
    lines.append("## Top clusters")
    lines.append("")
    lines.append("| cluster | role | indep | members | priority | band | persistence | archetype | systems |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for cluster in report["top_clusters"]:
        lines.append(
            f"| {cluster['cluster_id']} | {cluster.get('role') or '?'} | {cluster.get('independent_sources')} | "
            f"{cluster.get('member_count')} | {cluster.get('priority_score')} | {cluster.get('priority_band')} | "
            f"{cluster.get('persistence_strength')} | {cluster.get('archetype')} | "
            f"{', '.join(cluster.get('named_systems') or []) or '-'} |"
        )
    lines.append("")
    lines.append("## Quality checks")
    lines.append("")
    lines.append(f"- Recurrence measurable (>=3 independent sources in a cluster): {report['recurrence_measurable']}")
    lines.append(f"- Vendor-led risk mix: {report['vendor_led_risk_mix']}")
    lines.append("- Lowest-confidence extractions (manual audit targets):")
    for example in report["low_confidence_extraction_examples"]:
        lines.append(f"  - {example['signal_id']} (conf {example['confidence']}): {(example['statement'] or '')[:160]}")
    lines.append("")
    lines.append(f"## Preliminary recommendation: {report['preliminary_recommendation']}")
    lines.append("")
    lines.append(report["preliminary_recommendation_note"])
    lines.append("")
    lines.append(report["disclaimer"])
    lines.append("")
    return "\n".join(lines)


# ----------------------------------------------------------------- other cmds
def cmd_validate(args: argparse.Namespace) -> int:
    run_dir = os.path.abspath(args.run_dir)
    signals = read_jsonl(os.path.join(run_dir, "signals.jsonl"))
    problems = 0
    for signal in signals:
        for problem in validate_signal(signal):
            problems += 1
            _print(f"{signal.get('signal_id')}: {problem}")
        if signal.get("duplicate_of") and signal.get("duplicate_of") == signal.get("signal_id"):
            problems += 1
            _print(f"{signal.get('signal_id')}: duplicate_of self-reference")
    _print(f"validated {len(signals)} signal(s); {problems} problem(s)")
    return 1 if problems else 0


def cmd_observations(args: argparse.Namespace) -> int:
    run_dir = os.path.abspath(args.run_dir)
    clusters = read_json(os.path.join(run_dir, "clusters.json"), []) or []
    observations = to_observations(clusters, max_promote=args.max_promote)
    text = render_pool(
        observations,
        {
            "generated_at": utcnow_iso(),
            "version": VERSION,
            "run_id": os.path.basename(run_dir),
        },
    )
    with open(os.path.join(run_dir, "observations.md"), "w", encoding="utf-8") as handle:
        handle.write(text)
    write_json(os.path.join(run_dir, "observations.json"), observations)
    _print(f"wrote {len(observations)} observation(s) to {run_dir}/observations.md")
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    run_dir = os.path.abspath(args.run_dir)
    report = read_json(os.path.join(run_dir, "report.json"), None)
    if not report:
        raise SystemExit(f"no report.json in {run_dir}; run the pipeline first")
    with open(os.path.join(run_dir, "report.md"), "w", encoding="utf-8") as handle:
        handle.write(render_report_markdown(report))
    _print(f"rewrote {run_dir}/report.md")
    return 0


# ----------------------------------------------------------------- argparse
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python3 -m painmine.cli", description="painmine spike (issue #9)")
    parser.add_argument("--version", action="version", version=f"painmine {VERSION}")
    sub = parser.add_subparsers(dest="command", required=True)

    pipeline = sub.add_parser("pipeline", help="collect -> extract -> dedupe -> cluster -> rank -> observations")
    pipeline.add_argument("--out", required=True, help="output run directory")
    pipeline.add_argument("--family", default="a_manual_rekey", help="query family name, or 'all'")
    pipeline.add_argument("--sources", default=",".join(ENABLED_SOURCES))
    pipeline.add_argument("--sources-file", default=DEFAULT_SOURCES)
    pipeline.add_argument("--limits", default=DEFAULT_LIMITS)
    pipeline.add_argument("--max-requests", type=int, default=0, help="lower the request cap for this run")
    pipeline.add_argument("--max-promote", type=int, default=3)
    pipeline.add_argument("--state", default="", help="state json path (seen ids / cluster history)")
    pipeline.add_argument("--run-id", default="")
    pipeline.add_argument("--offline-fixture", default="", help="read raw items from JSONL instead of the network")
    pipeline.add_argument("--enable-llm", action="store_true", help="enable OpenCode Go spend for this run (owner approval)")
    pipeline.add_argument("--synthesis", action="store_true", help="run Part 6 synthesis for top clusters")
    pipeline.add_argument("--synthesis-top", type=int, default=2)
    pipeline.set_defaults(func=run_pipeline)

    validate = sub.add_parser("validate", help="validate signals.jsonl against the pain-signal schema")
    validate.add_argument("--run-dir", required=True)
    validate.set_defaults(func=cmd_validate)

    observations = sub.add_parser("observations", help="re-render observations.md from clusters.json")
    observations.add_argument("--run-dir", required=True)
    observations.add_argument("--max-promote", type=int, default=3)
    observations.set_defaults(func=cmd_observations)

    report = sub.add_parser("report", help="re-render report.md from report.json")
    report.add_argument("--run-dir", required=True)
    report.set_defaults(func=cmd_report)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())
