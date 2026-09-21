"""Pain-signal schema construction and validation (issue #9 Part 1).

Uses the stdlib only: the JSON Schema file documents the contract for external
consumers, while this module performs the authoritative runtime validation.
"""
from __future__ import annotations

from typing import Any

from .util import sha1_hex, strip_html, truncate

SCHEMA_VERSION = "0.1.0"

REQUIRED_STRINGS = (
    "signal_id",
    "source_type",
    "source_id",
    "source_url",
    "retrieved_at",
    "pain_statement",
    "raw_excerpt",
)
OPTIONAL_STRINGS = (
    "published_at",
    "source_author",
    "target_role",
    "organisation_hint",
    "task",
    "current_workaround",
    "frequency_clue",
    "time_cost_clue",
    "money_cost_clue",
    "dissatisfaction_clue",
    "integration_clue",
    "duplicate_of",
    "cluster_id",
)


def new_signal_id(source_type: str, source_id: str, statement: str) -> str:
    key = f"{source_type}|{source_id}|{strip_html(statement).lower()[:200]}"
    return sha1_hex(key, 16)


def make_signal(**kwargs: Any) -> dict:
    """Build a schema-shaped signal with defaults; caller supplies the content fields."""
    source_type = kwargs.get("source_type", "") or ""
    source_id = kwargs.get("source_id", "") or ""
    statement = truncate(strip_html(kwargs.get("pain_statement", "") or ""), 400)
    sig: dict[str, Any] = {
        "signal_id": kwargs.get("signal_id")
        or new_signal_id(source_type, source_id, statement),
        "source_type": source_type,
        "source_id": source_id,
        "source_url": kwargs.get("source_url", "") or "",
        "retrieved_at": kwargs.get("retrieved_at", "") or "",
        "published_at": kwargs.get("published_at"),
        "source_author": kwargs.get("source_author"),
        "target_role": kwargs.get("target_role"),
        "organisation_hint": kwargs.get("organisation_hint"),
        "task": kwargs.get("task"),
        "pain_statement": statement,
        "current_workaround": kwargs.get("current_workaround"),
        "named_systems": sorted({s for s in (kwargs.get("named_systems") or []) if s}),
        "frequency_clue": kwargs.get("frequency_clue"),
        "time_cost_clue": kwargs.get("time_cost_clue"),
        "money_cost_clue": kwargs.get("money_cost_clue"),
        "dissatisfaction_clue": kwargs.get("dissatisfaction_clue"),
        "integration_clue": kwargs.get("integration_clue"),
        "confidence": float(kwargs.get("confidence", 0.0)),
        "extraction_provenance": kwargs.get("extraction_provenance")
        or {"method": "deterministic-cues", "version": SCHEMA_VERSION, "cue_groups": [], "patterns_matched": []},
        "raw_excerpt": truncate(kwargs.get("raw_excerpt", "") or "", 600),
        "duplicate_of": kwargs.get("duplicate_of"),
        "cluster_id": kwargs.get("cluster_id"),
    }
    return sig


def validate_signal(sig: dict) -> list[str]:
    """Return a list of human-readable problems; empty list means valid."""
    problems: list[str] = []
    if not isinstance(sig, dict):
        return ["signal is not an object"]
    for field in REQUIRED_STRINGS:
        value = sig.get(field)
        if not isinstance(value, str) or not value.strip():
            problems.append(f"missing/empty required field: {field}")
    for field in OPTIONAL_STRINGS:
        value = sig.get(field)
        if value is not None and not isinstance(value, str):
            problems.append(f"field {field} must be string or null")
    if not isinstance(sig.get("named_systems"), list):
        problems.append("named_systems must be a list")
    conf = sig.get("confidence")
    if not isinstance(conf, (int, float)) or not (0 <= float(conf) <= 1):
        problems.append("confidence must be a number in [0, 1]")
    prov = sig.get("extraction_provenance")
    if not isinstance(prov, dict) or not prov.get("method") or not prov.get("version"):
        problems.append("extraction_provenance must include method and version")
    if len(sig.get("pain_statement", "")) > 400:
        problems.append("pain_statement exceeds 400 chars")
    if len(sig.get("raw_excerpt", "")) > 600:
        problems.append("raw_excerpt exceeds 600 chars")
    return problems
