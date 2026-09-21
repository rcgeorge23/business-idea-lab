"""Convert ranked clusters into Method 1.6 observation-pool format (#9 Part 9).

This module only *renders* observations. It does not run Method 1.6 triage, does
not score business ideas, and does not alter any method semantics. The method
run that consumes this pool must perform its own shallow triage and its own
sampled false-negative audit.
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
            }
        )
    return rows


def cluster_to_observation(cluster: dict, index: int) -> dict:
    priority = cluster.get("priority") or {}
    persistence = cluster.get("persistence") or {}
    archetype = cluster.get("archetype") or {}
    role = cluster.get("role") or "unidentified buyer"
    systems = cluster.get("named_systems") or []
    statements = [e.get("statement") or "" for e in cluster.get("evidence") or []]
    joined = " ".join(statements)
    regulatory = bool(REGULATORY_CUE.search(joined))

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
    band = priority.get("band")
    if band == "A" and persistence.get("strength") in ("strong", "weak"):
        triage = "promote"
    elif band in ("A", "B"):
        triage = "watch"
    else:
        triage = "reject"
    reason = (
        f"painmine discovery priority {priority.get('score')}/100 (band {band}); "
        f"{cluster.get('independent_sources')} independent source(s); "
        f"persistence thesis {persistence.get('strength', 'not-assessed')}; "
        f"vendor-led risk {priority.get('vendor_led_risk', 'unknown')}. "
        "Not a business score; Method 1.6 triage still applies."
    )
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
        "triage": triage,
        "triage_reason": reason,
        "discovery_priority": priority,
        "persistence_thesis": persistence,
        "independent_source_count": cluster.get("independent_sources"),
    }


def to_observations(clusters: list[dict], max_promote: int = 3, max_observations: int = 20) -> list[dict]:
    """Render the top clusters (by priority) into observation records."""
    ranked = sorted(clusters, key=lambda c: -(c.get("priority", {}).get("score") or 0))[:max_observations]
    observations = [cluster_to_observation(cluster, index + 1) for index, cluster in enumerate(ranked)]
    promoted = 0
    for obs in observations:
        if obs["triage"] == "promote":
            promoted += 1
            if promoted > max_promote:
                obs["triage"] = "watch"
                obs["triage_reason"] += " (demoted: max 3 promotions per run)"
    return observations


def render_pool(observations: list[dict], meta: dict) -> str:
    lines: list[str] = []
    lines.append("# painmine observation pool (Method 1.6 format)")
    lines.append("")
    lines.append(f"- Generated: {meta.get('generated_at', 'unknown')}")
    lines.append(f"- painmine version: {meta.get('version', '0.1.0')}")
    lines.append(f"- Source run: {meta.get('run_id', 'n/a')}")
    lines.append(f"- Method version targeted: 1.6.0 (this file is an input candidate; it does not run method triage)")
    lines.append(f"- Pool size: {len(observations)}")
    archetypes = {o.get("archetype", "persistent") for o in observations}
    lines.append(f"- Archetype mix: {', '.join(sorted(archetypes)) or 'n/a'}")
    source_classes = sorted({s.strip() for o in observations for s in (o.get("source_class") or "").split(",") if s.strip()})
    lines.append(f"- Source mix: {', '.join(source_classes) or 'n/a'}")
    lines.append("- Triage: painmine preliminary triage only; the consuming method run must perform its own triage and sampled false-negative audit.")
    lines.append("")
    lines.append(
        "| ID | Observation (problem / workflow) | Buyer | Source class | Reg? | Archetype | Evidence (source, date) | Type | Incumbent / free-alternative check | Triage | Triage reason |"
    )
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for obs in observations:
        evidence = "; ".join(
            f"{e.get('source')} {e.get('date')} {e.get('url') or ''}".strip() for e in obs.get("evidence", [])[:4]
        )
        lines.append(
            "| {id} | {problem} | {buyer} | {source_class} | {reg} | {archetype} | {evidence} | {etype} | {incumbent} | {triage} | {reason} |".format(
                id=obs.get("id"),
                problem=_cell(obs.get("problem_workflow")),
                buyer=_cell(obs.get("target_user_buyer")),
                source_class=_cell(obs.get("source_class")),
                reg="yes" if obs.get("regulatory_derived") else "no",
                archetype=obs.get("archetype"),
                evidence=_cell(evidence),
                etype="practitioner",
                incumbent=_cell(obs.get("incumbent_free_alternative_check")),
                triage=obs.get("triage"),
                reason=_cell(obs.get("triage_reason")),
            )
        )
    lines.append("")
    lines.append("## Promoted observations")
    lines.append("")
    lines.append("| ID | Promoted to candidate | Why |")
    lines.append("| --- | --- | --- |")
    promoted = [o for o in observations if o.get("triage") == "promote"]
    if promoted:
        for obs in promoted:
            priority = obs.get("discovery_priority") or {}
            lines.append(
                f"| {obs.get('id')} | (decision for the consuming method run) | discovery priority {priority.get('score')}/100; "
                f"independent sources {obs.get('independent_source_count')}; provenance {obs.get('evidence', [{}])[0].get('source', 'n/a')} |"
            )
    else:
        lines.append("| - | none | no cluster met the promotion threshold |")
    lines.append("")
    lines.append("## Triage false-negative audit")
    lines.append("")
    lines.append("| Observation selected | Why selected | Original triage reasoning | Additional evidence checked | Outcome | Implication for triage depth |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    lines.append(
        "| n/a | Generated by the painmine spike, not by a method discovery run | n/a | n/a | n/a | "
        "The next Method 1.6 run that consumes this pool must select and record exactly one triage-rejected "
        "observation for its own sampled audit. |"
    )
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- Evidence excerpts are limited for copyright and auditability; each row links to its public source.")
    lines.append("- Recurrence counts independent authors across source classes; reposts/copies are linked via `duplicate_of` and never counted twice.")
    lines.append("- Discovery-priority ranking (Part 4) is separate from Method 1.6 business scoring and must not be used as market validation.")
    lines.append("- No source was accessed through authentication, anti-bot circumvention or paywall bypass.")
    lines.append("")
    return "\n".join(lines)


def _cell(text: str | None) -> str:
    return (text or "").replace("|", "/").replace("\n", " ").strip()
