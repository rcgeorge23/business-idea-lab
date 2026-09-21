"""Discovery-priority ranking (issue #9 Part 4).

This score decides where to spend discovery effort. It is NOT a business score,
NOT market validation, and is never an input to Method 1.6 evaluation. The
breakdown is retained for every cluster so the ranking is auditable.

Bands: A >= promote_band_a_min (70) = promote into the observation funnel;
B >= watch_band_b_min (50) = watch list; C = archive.
"""
from __future__ import annotations

import re
from typing import Any

from .util import days_since

CONSUMER_CUES = re.compile(
    r"\b(my (iphone|phone|laptop|pc|personal|netflix|spotify|steam|gym)|video game|"
    r"gaming|my steam deck|personal (budget|tax return)|hobby)\b",
    re.IGNORECASE,
)
TRANSIENT_CUES = re.compile(
    r"\b(outage|down since|is down|went down|currently down|broken today|outage yesterday)\b",
    re.IGNORECASE,
)

VENDOR_SOURCE_TYPES = {"vendor_support_community", "vendor_forums", "vendor_marketing"}
USER_SOURCE_TYPES = {"hn_algolia", "stack_exchange", "github_issues", "reddit_public_json"}


def _fraction(members: list[dict], predicate) -> float:
    if not members:
        return 0.0
    return sum(1 for m in members if predicate(m)) / len(members)


def _has_clue(signal: dict, field: str) -> bool:
    return bool(signal.get(field))


def _cue_groups(signal: dict) -> set[str]:
    provenance = signal.get("extraction_provenance") or {}
    return set(provenance.get("cue_groups") or [])


def rank_cluster(cluster: dict, signals_by_id: dict[str, dict], limits: dict) -> dict[str, Any]:
    members = [signals_by_id[sid] for sid in cluster.get("member_signal_ids", []) if sid in signals_by_id]
    independent = int(cluster.get("independent_sources", 0))
    systems = cluster.get("named_systems") or []
    role = cluster.get("role")

    frac_money = _fraction(members, lambda s: _has_clue(s, "money_cost_clue"))
    frac_workaround = _fraction(
        members, lambda s: bool(s.get("current_workaround")) or "workaround" in _cue_groups(s)
    )
    frac_dissat = _fraction(members, lambda s: _has_clue(s, "dissatisfaction_clue"))
    frac_integration = _fraction(members, lambda s: _has_clue(s, "integration_clue"))
    frac_manual = _fraction(members, lambda s: "manual" in _cue_groups(s))

    positives: dict[str, float] = {}
    positives["recurrence"] = min(30.0, 10.0 * independent)
    positives["economic_buyer"] = 15.0 if role else 0.0
    positives["explicit_cost_evidence"] = round(15.0 * min(1.0, frac_money * 2.0), 1)
    positives["manual_workaround"] = round(15.0 * min(1.0, max(frac_workaround, frac_manual) * 1.5), 1)
    positives["dissatisfaction_switching"] = round(10.0 * min(1.0, frac_dissat * 2.0), 1)
    positives["integration_seam"] = round(
        10.0 * (1.0 if len(systems) >= 2 else 0.0) * min(1.0, frac_integration * 1.5 + 0.3), 1
    )

    recency_days = days_since(cluster.get("last_seen"))
    if recency_days is None:
        positives["recency"] = 3.0
    elif recency_days <= 365:
        positives["recency"] = 10.0
    elif recency_days <= 730:
        positives["recency"] = 6.0
    else:
        positives["recency"] = 2.0

    family = cluster.get("role_family")
    narrow_segment = bool(role) and family not in (None, "software", "operations", "office_admin")
    positives["narrow_reachable_segment"] = 5.0 if narrow_segment else 0.0

    penalties: dict[str, float] = {}
    total_members = len(members) + int(cluster.get("duplicate_count", 0))
    duplicate_ratio = (int(cluster.get("duplicate_count", 0)) / total_members) if total_members else 0.0
    if duplicate_ratio > 0.3:
        penalties["high_duplicate_ratio"] = -10.0
    if role is None and not frac_money and not frac_workaround:
        penalties["no_identifiable_economic_buyer"] = -10.0
    if CONSUMER_CUES.search(" ".join(s.get("pain_statement") or "" for s in members)) and not (
        frac_money or frac_workaround
    ):
        penalties["consumer_only"] = -15.0
    if recency_days is not None and recency_days > 1095:
        penalties["stale_evidence"] = -10.0
    if TRANSIENT_CUES.search(" ".join(s.get("pain_statement") or "" for s in members)) and independent <= 2:
        penalties["transient_incident"] = -8.0

    score = sum(positives.values()) + sum(penalties.values())
    score = max(0.0, min(100.0, round(score, 1)))
    promote_min = float(limits.get("ranking", {}).get("promote_band_a_min", 70))
    watch_min = float(limits.get("ranking", {}).get("watch_band_b_min", 50))
    if score >= promote_min:
        band = "A"
    elif score >= watch_min:
        band = "B"
    else:
        band = "C"

    vendor_types = {t for t in cluster.get("source_types", []) if t in VENDOR_SOURCE_TYPES}
    if vendor_types:
        vendor_led_risk = "medium"
    elif set(cluster.get("source_types", [])) <= USER_SOURCE_TYPES:
        vendor_led_risk = "low"
    else:
        vendor_led_risk = "unknown"

    return {
        "score": score,
        "band": band,
        "positive_signals": positives,
        "penalties": penalties,
        "duplicate_ratio": round(duplicate_ratio, 3),
        "vendor_led_risk": vendor_led_risk,
        "explanation": (
            f"{independent} independent source(s); role={role or 'unknown'}; "
            f"machinery={len(systems)} named system(s); last evidence {recency_days if recency_days is not None else '?'} day(s) old"
        ),
        "disclaimer": "Discovery priority only; not a business score and not market validation.",
    }


def rank_clusters(clusters: list[dict], signals: list[dict], limits: dict) -> list[dict]:
    signals_by_id = {s["signal_id"]: s for s in signals}
    for cluster in clusters:
        cluster["priority"] = rank_cluster(cluster, signals_by_id, limits)
    return sorted(clusters, key=lambda c: -c["priority"]["score"])
