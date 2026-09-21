"""Independent synthesis reliability test (issue #9 Part 6).

For the strongest clusters only, two interpreters describe the same evidence
cluster without seeing each other's output. Agreement and disagreement are both
recorded; disagreement is never averaged away.

Two modes:
- deterministic baseline: a single local interpretation derived only from
  extracted fields (no model call). Agreement is trivially 1.0 and is marked
  ``mode=deterministic-baseline`` so it is not mistaken for an independent test.
- dual-model mode: when LLM spend is enabled, two OpenCode Go calls with
  different, order-scrambled prompts; the two JSON interpretations are compared
  field by field.
"""
from __future__ import annotations

from typing import Any

from .llm import OpenCodeGo, extract_json_blob
from .util import jaccard, tokenize, truncate

SYNTH_FIELDS = ("buyer", "job", "pain", "current_workaround", "opportunity_seam")

PROMPT = """You are one of two independent analysts. You have NOT seen and must not
assume any other analysis. Given ONLY the mined evidence below, return strict JSON
with exactly these keys: buyer, job, pain, current_workaround, opportunity_seam.
Each value is one plain sentence. If the evidence does not support a field, use
"insufficient evidence". Do not invent companies, budgets or sources. Do not
describe a product or market size; only describe the pattern in the evidence.

EVIDENCE CLUSTER (JSON; signal list order: {order}):
{payload}
"""


def deterministic_interpretation(cluster: dict, signals: list[dict]) -> dict:
    """Local field-derived reading of a cluster; no model call."""
    role = cluster.get("role") or "unidentified buyer"
    systems = ", ".join(cluster.get("named_systems") or []) or "no named systems"
    top = cluster.get("evidence") or []
    pain = (top[0].get("statement") if top else "") or ""
    workarounds = [
        str(s.get("current_workaround")) for s in signals if s.get("current_workaround")
    ]
    seam = (
        f"evidence repeatedly names {systems}, suggesting the buyer reconciles between them manually"
        if cluster.get("named_systems")
        else "insufficient evidence"
    )
    return {
        "buyer": role,
        "job": truncate((top[0].get("statement") if top else "") or "", 160) or "insufficient evidence",
        "pain": truncate(pain, 200) or "insufficient evidence",
        "current_workaround": truncate(workarounds[0], 200) if workarounds else "insufficient evidence",
        "opportunity_seam": seam,
    }


def _payload(cluster: dict, signals: list[dict], order: str) -> str:
    evidence = [
        {
            "source_type": s.get("source_type"),
            "published_at": s.get("published_at"),
            "role": s.get("target_role"),
            "pain_statement": s.get("pain_statement"),
            "workaround": s.get("current_workaround"),
            "systems": s.get("named_systems"),
            "clues": {
                "frequency": s.get("frequency_clue"),
                "time": s.get("time_cost_clue"),
                "money": s.get("money_cost_clue"),
                "dissatisfaction": s.get("dissatisfaction_clue"),
                "integration": s.get("integration_clue"),
            },
        }
        for s in signals
    ]
    if order == "confidence":
        evidence.sort(key=lambda e: -(e.get("clues") is not None))
    else:
        evidence.sort(key=lambda e: str(e.get("published_at") or ""))
    return __import__("json").dumps({"cluster_label": cluster.get("label"), "signals": evidence}, ensure_ascii=False)


def synthesis_prompts(cluster: dict, signals: list[dict]) -> tuple[str, str]:
    payload_a = _payload(cluster, signals, "date")
    payload_b = _payload(cluster, signals, "confidence")
    return (
        PROMPT.format(order="oldest first", payload=payload_a),
        PROMPT.format(order="strongest evidence first", payload=payload_b),
    )


def compare_interpretations(a: dict, b: dict) -> dict:
    agree: list[str] = []
    disagree: list[dict] = []
    for field in SYNTH_FIELDS:
        value_a = str((a or {}).get(field, "")).strip()
        value_b = str((b or {}).get(field, "")).strip()
        if not value_a and not value_b:
            continue
        similarity = jaccard(set(tokenize(value_a)), set(tokenize(value_b)))
        if similarity >= 0.5:
            agree.append(field)
        else:
            disagree.append({"field": field, "interpreter_a": value_a, "interpreter_b": value_b, "token_overlap": round(similarity, 2)})
    total = len(agree) + len(disagree)
    return {
        "agree": agree,
        "disagree": disagree,
        "agreement_ratio": round(len(agree) / total, 2) if total else None,
    }


def independent_synthesis(
    cluster: dict, signals: list[dict], llm: OpenCodeGo | None
) -> dict[str, Any]:
    """Run the Part 6 test for one cluster. Always returns an auditable record."""
    if llm is None or not llm.budget.llm_enabled:
        interpretation = deterministic_interpretation(cluster, signals)
        return {
            "mode": "deterministic-baseline",
            "status": "skipped-llm-disabled",
            "note": (
                "Independent dual-model synthesis was not run because LLM spend is disabled by "
                "limits.json (owner approval required). Baseline interpretation recorded; the "
                "dual-call path is implemented and costs are bounded."
            ),
            "baseline_interpretation": interpretation,
            "interpreters": {},
            "comparison": {"agree": [], "disagree": [], "agreement_ratio": None},
        }
    prompt_a, prompt_b = synthesis_prompts(cluster, signals)
    result_a = llm.run(prompt_a)
    result_b = llm.run(prompt_b)
    interpretation_a = extract_json_blob(result_a.get("text", "")) or {}
    interpretation_b = extract_json_blob(result_b.get("text", "")) or {}
    comparison = compare_interpretations(interpretation_a, interpretation_b)
    return {
        "mode": "two-independent-model-calls",
        "status": "completed" if result_a.get("ok") and result_b.get("ok") else "partial",
        "note": "Interpreters never saw each other's output; disagreements are preserved verbatim below.",
        "interpreters": {
            "a": {"ok": result_a.get("ok"), "model": result_a.get("model"), "cost_usd": result_a.get("cost_usd")},
            "b": {"ok": result_b.get("ok"), "model": result_b.get("model"), "cost_usd": result_b.get("cost_usd")},
        },
        "interpretation_a": interpretation_a,
        "interpretation_b": interpretation_b,
        "comparison": comparison,
    }
