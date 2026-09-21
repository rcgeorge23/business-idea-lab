"""Contradiction / persistence mining (issue #9 Part 5, and method/discovery.md
archetype B).

A valuable pattern is: recurring pain + money/time spent + existing products +
continued workaround. Competitor existence alone is NOT evidence against a
cluster. This module:
  1. classifies each signal as change-driven (a datable change cue) or persistent;
  2. derives mechanism hypotheses for why pain persists despite alternatives;
  3. evaluates the two-part persistence thesis: (a) continued pain/workaround
     despite alternatives and (b) a credible persistence mechanism.

The result is recorded for the observation record, never used as a scoring
bonus and never used to upgrade a hard filter.
"""
from __future__ import annotations

import re

from .util import truncate

CHANGE_CUE_PATTERNS = [
    r"\bsince (the |a )?(new|recent|latest)\b",
    r"\bsince (january|february|march|april|may|june|july|august|september|october|november|december)\b",
    r"\b(new|incoming) (regulation|legislation|law|rule|mandate|directive|tax)\b",
    r"\bmaking tax digital\b",
    r"\bshutting down\b",
    r"\bshutdown\b",
    r"\bdiscontinu\w*\b",
    r"\bdeprecat\w*\b",
    r"\bend of life\b",
    r"\b(price|pricing) (increase|change|hike)\b",
    r"\bnew (api|version|policy|rules?)\b",
    r"\bfrom (january|april|july|october|20\d\d)\b",
    r"\bdeadline (is|was|of)\b",
    r"\bwe (just )?(migrated|switched|moved) (to|from)\b",
]

MECHANISM_PATTERNS: dict[str, list[str]] = {
    "price_or_minimum_contract": [
        r"\btoo expensive\b",
        r"\bexpensive\b",
        r"\bprice\w* (increase|hike|change)\b",
        r"\bper (seat|user) pricing\b",
        r"\bminimum (contract|term|spend|users?|seats?)\b",
        r"\benterprise (plan|tier|pricing|only)\b",
        r"\bpremium (plan|tier|only)\b",
        r"\bcustom pricing\b",
        r"\bquote[- ]only\b",
        r"\bwe can'?t justify\b",
    ],
    "partial_or_manual_integration": [
        r"\bread[- ]only\b",
        r"\bone[- ]way\b",
        r"\bno (api|integration|sync|export)\b",
        r"\bexport\w* (only|just|csv)\b",
        r"\bcsv (only|import|export)\b",
        r"\bmanual(ly)?\s+(sync|export|import|entry|re[- ]?key\w*|copy|type|enter|download|upload)\b",
        r"\b(do(es)?n'?t|do not|does not) (integrate|sync|export|import)\b",
        r"\bcan'?t (sync|integrate|export|import)\b",
        r"\bno webhooks?\b",
        r"\bpartial (integration|sync)\b",
    ],
    "implementation_complexity": [
        r"\bsetup (takes|is|was)\b",
        r"\bonboarding (takes|is|was|required)\b",
        r"\bimplement\w* (takes|is|was|required|team)\b",
        r"\bmigration (takes|is|was)\b",
        r"\bconsultant\w*\b",
        r"\btraining (takes|required|needed)\b",
        r"\btoo complex\b",
        r"\bconfiguration\b",
        r"\bsteep learning curve\b",
    ],
    "excluded_segment": [
        r"\bsmall (business|practice|firm|company|charity|shop)\b",
        r"\bsole trader\b",
        r"\bfreelanc\w*\b",
        r"\bstartup\b",
        r"\bmicro\b",
        r"\bunder \d+ (users?|employees|seats?)\b",
        r"\bnot worth it for\b",
        r"\bonly makes sense (for|if)\b",
    ],
    "legacy_architecture": [
        r"\blegacy\b",
        r"\bold (software|system|version)\b",
        r"\bdesktop (app|software|version)\b",
        r"\bon[- ]prem(ises)?\b",
        r"\bno longer (supported|updated|maintained)\b",
        r"\bwindows (7|xp|vista)\b",
    ],
    "low_vendor_priority": [
        r"\bfeature request (ignored|open|unanswered)\b",
        r"\bbeen waiting (for )?(months|years)\b",
        r"\bno one (cares|is working on)\b",
        r"\bvote(d)? (for|it) \d+\b",
        r"\bniche\b",
        r"\bunlikely to (be )?(built|implemented)\b",
    ],
}

CHANGE_CUES = [(pattern, re.compile(pattern, re.IGNORECASE)) for pattern in CHANGE_CUE_PATTERNS]
MECHANISMS = {
    name: [(pattern, re.compile(pattern, re.IGNORECASE)) for pattern in patterns]
    for name, patterns in MECHANISM_PATTERNS.items()
}


def detect_archetype(signal: dict) -> dict:
    """Return {'archetype': 'change_driven'|'persistent', ...} for one signal."""
    text = " ".join(
        [signal.get("pain_statement") or "", signal.get("task") or "", signal.get("current_workaround") or ""]
    )
    for pattern, regex in CHANGE_CUES:
        match = regex.search(text)
        if match:
            return {
                "archetype": "change_driven",
                "change_cue": truncate(match.group(0), 120),
                "change_sentence": truncate(_sentence_around(text, match.start()), 300),
                "published_at": signal.get("published_at"),
                "signal_id": signal.get("signal_id"),
            }
    return {"archetype": "persistent", "change_cue": None, "change_sentence": None, "signal_id": signal.get("signal_id")}


def _sentence_around(text: str, index: int) -> str:
    start = max(0, text.rfind(".", 0, index) + 1)
    end = text.find(".", index)
    if end == -1:
        end = len(text)
    return text[start : end + 1].strip()


def mechanism_hypotheses(signals: list[dict]) -> dict[str, dict]:
    """Count support for each persistence mechanism across independent signals."""
    result: dict[str, dict] = {}
    for name, patterns in MECHANISMS.items():
        evidence: list[dict] = []
        for signal in signals:
            if signal.get("duplicate_of"):
                continue
            text = " ".join(
                [
                    signal.get("pain_statement") or "",
                    signal.get("current_workaround") or "",
                    signal.get("dissatisfaction_clue") or "",
                    signal.get("money_cost_clue") or "",
                    signal.get("integration_clue") or "",
                ]
            )
            matched = [pattern for pattern, regex in patterns if regex.search(text)]
            if matched:
                evidence.append(
                    {
                        "signal_id": signal.get("signal_id"),
                        "source_type": signal.get("source_type"),
                        "patterns": matched,
                        "excerpt": truncate(signal.get("pain_statement") or "", 200),
                    }
                )
        result[name] = {
            "supported": len(evidence) >= 2,
            "evidence_count": len(evidence),
            "evidence": evidence[:8],
        }
    return result


def persistence_thesis(cluster: dict, signals: list[dict]) -> dict:
    """Evaluate the two-part persistence test for one persistent-archetype cluster."""
    members = [s for s in signals if s["signal_id"] in set(cluster.get("member_signal_ids", []))]
    independent = int(cluster.get("independent_sources", 0))
    workaround_or_cost = [
        s
        for s in members
        if s.get("current_workaround")
        or s.get("money_cost_clue")
        or s.get("time_cost_clue")
        or "workaround" in ((s.get("extraction_provenance") or {}).get("cue_groups") or [])
    ]
    limb1 = independent >= 2 and len(workaround_or_cost) >= 2
    mechanisms = mechanism_hypotheses(members)
    supported = {name: data for name, data in mechanisms.items() if data["supported"]}
    limb2 = len(supported) >= 1

    if limb1 and limb2 and independent >= 3:
        strength = "strong"
    elif (limb1 and limb2) or (limb1 and independent >= 3):
        strength = "weak"
    else:
        strength = "absent"

    return {
        "strength": strength,
        "limb1_continued_pain_despite_alternatives": {
            "pass": limb1,
            "independent_sources": independent,
            "members_with_workaround_or_cost_evidence": len(workaround_or_cost),
            "note": "Competitor existence is not treated as a disconfirming signal.",
        },
        "limb2_persistence_mechanism": {
            "pass": limb2,
            "supported_mechanisms": sorted(supported.keys()),
            "all_mechanisms": {
                name: {"supported": data["supported"], "evidence_count": data["evidence_count"]}
                for name, data in mechanisms.items()
            },
        },
        "mechanism_detail": supported,
        "disclaimer": "Hypotheses for the lab to test; not an assertion of a defensible wedge.",
    }


def cluster_archetype(signals: list[dict]) -> dict:
    """Cluster-level archetype: change-driven only if most independent signals cite a change."""
    classified = [detect_archetype(s) for s in signals if not s.get("duplicate_of")]
    change = [c for c in classified if c["archetype"] == "change_driven"]
    if classified and len(change) / len(classified) >= 0.5:
        return {
            "archetype": "change_driven",
            "change_evidence": change[:5],
            "why_now": {
                "changed": change[0]["change_sentence"] if change else None,
                "changed_date": change[0]["published_at"] if change else None,
                "evidence": [c["signal_id"] for c in change],
                "why_it_matters": "UNVERIFIED HYPOTHESIS: derived from mined change cues; requires human validation.",
                "competitors_responded": "unknown",
            },
        }
    return {"archetype": "persistent", "change_evidence": change[:3], "why_now": None}
