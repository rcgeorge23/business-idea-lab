"""Convert ranked clusters into ranked observation inputs for a Method 1.6 run (#9 Part 9).

This module only *renders* ranked observation inputs. It does not run Method 1.6
triage, does not emit `promote`/`watch`/`reject` labels, does not select
candidates and does not consume the method's three-candidate limit. The method
run that consumes this pool must perform its own observation sweep, shallow
triage, negative-evidence recording, sampled false-negative audit and promotion
decision.
"""
from __future__ import annotations

import re

from .util import truncate

REGULATORY_CUE = re.compile(
    r"\b(hmrc|gdpr|vat|payroll|compliance|regulat\w*|legislat\w*|tax return|mtd|making tax digital|cqc|fca|ofsted|companies house|hmrc)\b",
    re.IGNORECASE,
)


def _evidence_rows(cluster: dict, limit: int = 8) -> list[dict]:
    rows = []
    for item in (cluster.get("evidence") or [])[:limit]:
        rows.append(
            {
                "source": item.get("source_type"),
                "url": item.get("source_url"),
                "date": (item.get("published_at") or "")[:10] or "unknown",
                "type": "practitioner",
                "excerpt": truncate(item.get("statement") or "", 180),
                "systems": item.get("systems") or [],
                "confidence": item.get("confidence"),
            }
        )
    return rows


def cluster_to_observation(cluster: dict, index: int) -> dict:
    """Render one cluster as a ranked observation input (no Method labels)."""
    priority = cluster.get("priority") or {}
    persistence = cluster.get("persistence") or {}
    archetype = cluster.get("archetype") or {}
    role = cluster.get("role") or "unidentified buyer"
    systems = cluster.get("named_systems") or []
    evidence = cluster.get("evidence") or []
    statements = [e.get("statement") or "" for e in evidence]
    joined = " ".join(statements)
    regulatory = bool(REGULATORY_CUE.search(joined))
    confidences = [
        e.get("confidence")
        for e in evidence
        if isinstance(e.get("confidence"), (int, float))
    ]

    problem = truncate(
        f"{role} repeatedly report: {statements[0]}" if statements else cluster.get("label", ""),
        400,
    )
    incumbent_check = (
        f"Named systems in evidence: {', '.join(systems) if systems else 'none'}. "
        f"Practitioners still describe workarounds despite these products (see evidence). "
        f"Persistence mechanisms supported: {', '.join(persistence.get('limb2_persistence_mechanism', {}).get('supported_mechanisms', [])) or 'none'}. "
        f"Hypotheses only; a Method 1.6 novelty/incumbent check is still required downstream."
    )
    caveats = [
        "Deterministic cue extraction from public posts; no model or human validation.",
        "Clusters are lexical-similarity groups, not verified businesses, budgets or buyer commitments.",
        "Discovery priority is a ranking input for the consuming method run, not a business score or a lifecycle state.",
    ]
    if not confidences:
        caveats.append("No extraction-confidence values were available for this cluster.")
    if priority.get("vendor_led_risk") == "unknown":
        caveats.append("Vendor-led risk unknown: the source mix may include vendor or marketing material.")

    return {
        "id": f"PM-{index:02d}",
        "cluster_id": cluster.get("cluster_id"),
        "problem_workflow": problem,
        "target_user_buyer": role,
        "source_class": ", ".join(cluster.get("source_types") or []),
        "regulatory_derived": regulatory,
        "archetype": archetype.get("archetype", "persistent"),
        "why_now": archetype.get("why_now"),
        "evidence": _evidence_rows(cluster),
        "incumbent_free_alternative_check": incumbent_check,
        "discovery_priority": priority,
        "persistence_thesis": persistence,
        "recurrence": {
            "independent_source_count": cluster.get("independent_sources"),
            "source_type_count": len(cluster.get("source_types") or []),
            "duplicate_count": cluster.get("duplicate_count"),
            "runs_seen": cluster.get("runs_seen", 1),
            "note": (
                "Independent authors/sources within this run. Reposts are linked via "
                "duplicate_of and never counted twice; cross-run recurrence lives in the "
                "state history, not in this field."
            ),
        },
        "extraction": {
            "evidence_rows": len(evidence),
            "min_confidence": round(min(confidences), 3) if confidences else None,
            "max_confidence": round(max(confidences), 3) if confidences else None,
            "caveats": caveats,
        },
    }


def to_observations(clusters: list[dict], max_observations: int = 20) -> list[dict]:
    """Render the top clusters (by discovery priority) as ranked observation inputs.

    No triage labels, no candidate selection and no consumption of the Method
    1.6 three-candidate limit. Fewer than 15 observations is a valid outcome and
    is never padded with filler.
    """
    ranked = sorted(
        clusters, key=lambda c: -(c.get("priority", {}).get("score") or 0)
    )[:max_observations]
    return [
        cluster_to_observation(cluster, index + 1)
        for index, cluster in enumerate(ranked)
    ]


def render_pool(observations: list[dict], meta: dict) -> str:
    lines: list[str] = []
    lines.append("# painmine observation pool (ranked inputs for Method 1.6)")
    lines.append("")
    lines.append(f"- Generated: {meta.get('generated_at', 'unknown')}")
    lines.append(f"- painmine version: {meta.get('version', '0.1.0')}")
    lines.append(f"- Source run: {meta.get('run_id', 'n/a')}")
    lines.append("- Method version targeted: 1.6.0")
    lines.append(
        "- Contract: evidence-backed ranked observation INPUTS only. painmine emits no Method "
        "triage labels (promote/watch/reject), selects no candidates and does not consume the "
        "method's three-candidate limit. The consuming Method 1.6 run performs its own 15-20 "
        "observation sweep/merge, shallow triage, negative-evidence recording, sampled "
        "false-negative audit and promotion decision (at most 3)."
    )
    lines.append(
        f"- Pool size: {len(observations)} (fewer than 15 is expected and is never padded with filler)"
    )
    archetypes = {o.get("archetype", "persistent") for o in observations}
    lines.append(f"- Archetype mix: {', '.join(sorted(archetypes)) or 'n/a'}")
    source_classes = sorted(
        {
            s.strip()
            for o in observations
            for s in (o.get("source_class") or "").split(",")
            if s.strip()
        }
    )
    lines.append(f"- Source mix: {', '.join(source_classes) or 'n/a'}")
    lines.append("")
    lines.append(
        "| ID | Observation (problem / workflow) | Buyer | Source class | Reg? | Archetype | "
        "Evidence (source, date) | Discovery priority | Persistence | Independent sources | "
        "Incumbent / free-alternative check |"
    )
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for obs in observations:
        evidence = "; ".join(
            f"{e.get('source')} {e.get('date')} {e.get('url') or ''}".strip()
            for e in obs.get("evidence", [])[:4]
        )
        priority = obs.get("discovery_priority") or {}
        persistence = obs.get("persistence_thesis") or {}
        recurrence = obs.get("recurrence") or {}
        lines.append(
            "| {id} | {problem} | {buyer} | {source_class} | {reg} | {archetype} | {evidence} | "
            "{priority} | {persistence} | {independent} | {incumbent} |".format(
                id=obs.get("id"),
                problem=_cell(obs.get("problem_workflow")),
                buyer=_cell(obs.get("target_user_buyer")),
                source_class=_cell(obs.get("source_class")),
                reg="yes" if obs.get("regulatory_derived") else "no",
                archetype=obs.get("archetype"),
                evidence=_cell(evidence),
                priority=f"{priority.get('score', 'n/a')}/100 band {priority.get('band', 'n/a')}",
                persistence=persistence.get("strength", "not-assessed"),
                independent=recurrence.get("independent_source_count", "n/a"),
                incumbent=_cell(obs.get("incumbent_free_alternative_check")),
            )
        )
    lines.append("")
    lines.append("## Recurrence, persistence and extraction confidence")
    lines.append("")
    lines.append(
        "| ID | Independent sources (this run) | Source types | Persistence thesis | Priority band | "
        "Extraction confidence (min-max) | Caveats |"
    )
    lines.append("| --- | --- | --- | --- | --- | --- | --- |")
    if observations:
        for obs in observations:
            recurrence = obs.get("recurrence") or {}
            persistence = obs.get("persistence_thesis") or {}
            priority = obs.get("discovery_priority") or {}
            extraction = obs.get("extraction") or {}
            low = extraction.get("min_confidence")
            high = extraction.get("max_confidence")
            if low is None or high is None:
                confidence = "n/a"
            else:
                confidence = f"{low}-{high}"
            lines.append(
                f"| {obs.get('id')} | {recurrence.get('independent_source_count', 'n/a')} | "
                f"{recurrence.get('source_type_count', 'n/a')} | "
                f"{persistence.get('strength', 'not-assessed')} | {priority.get('band', 'n/a')} | "
                f"{confidence} | {_cell('; '.join(extraction.get('caveats') or []))} |"
            )
    else:
        lines.append("| - | 0 | 0 | not-assessed | n/a | n/a | no clusters met the minimum size in this run |")
    lines.append("")
    lines.append("## Triage false-negative audit (not performed here)")
    lines.append("")
    lines.append(
        "painmine does not triage observations, so it cannot select or audit a triage rejection. "
        "The consuming Method 1.6 run must select exactly one of its own triage-rejected "
        "observations, cheaply re-check it and record the outcome in its own run summary."
    )
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append(
        "- No Method triage labels are emitted; discovery priority bands are ranking inputs, not lifecycle states."
    )
    lines.append(
        "- A discovery-priority band change cannot advance, park or kill an idea: this package never writes "
        "`ideas/index.json` or any `ideas/` dossier."
    )
    lines.append(
        "- Evidence excerpts are limited for copyright and auditability; each row links to its public source."
    )
    lines.append(
        "- Recurrence counts independent authors across source classes; reposts/copies are linked via `duplicate_of` "
        "and never counted twice."
    )
    lines.append(
        "- Discovery-priority ranking (Part 4) is separate from Method 1.6 business scoring and must not be used as "
        "market validation."
    )
    lines.append(
        "- No source was accessed through authentication, anti-bot circumvention or paywall bypass."
    )
    lines.append("")
    return "\n".join(lines)


def _cell(text: str | None) -> str:
    return (text or "").replace("|", "/").replace("\n", " ").strip()
