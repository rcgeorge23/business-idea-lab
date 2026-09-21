"""Deduplication and independence accounting (issue #9 Part 3, step 3).

Two signals are the same evidence when their prose is near-identical (reposts,
cross-posts, quote-tweets of the same complaint). We canonicalise greedily by
Jaccard similarity over word shingles and mark every non-canonical signal with
``duplicate_of``. Recurrence counting only ever uses canonicals, so 17 copies
of one complaint count as one independent source.
"""
from __future__ import annotations

from .util import jaccard, normalize_text, sha1_hex, shingles, tokenize

DEFAULT_SHINGLE_K = 5
DEFAULT_THRESHOLD = 0.62


def _dedup_text(signal: dict) -> str:
    return " ".join(
        [
            signal.get("pain_statement") or "",
            signal.get("current_workaround") or "",
            signal.get("task") or "",
        ]
    )


def dedupe(
    signals: list[dict],
    threshold: float = DEFAULT_THRESHOLD,
    shingle_k: int = DEFAULT_SHINGLE_K,
) -> dict:
    """Annotate signals with duplicate_of, returning canonical groups and stats."""
    ordered = sorted(signals, key=lambda s: (-float(s.get("confidence", 0)), s.get("signal_id", "")))
    canonicals: list[dict] = []
    canonical_shingles: list[set[str]] = []
    canonical_exact: dict[str, str] = {}
    duplicate_of: dict[str, str] = {}
    duplicate_reason: dict[str, str] = {}

    for signal in ordered:
        text = _dedup_text(signal)
        exact_key = sha1_hex(normalize_text(text), 20)
        sh = shingles(tokenize(text), shingle_k)

        if exact_key in canonical_exact:
            duplicate_of[signal["signal_id"]] = canonical_exact[exact_key]
            duplicate_reason[signal["signal_id"]] = "identical normalized text (repost/copy)"
            continue

        best_idx, best_sim = None, 0.0
        for idx, candidate_shingles in enumerate(canonical_shingles):
            sim = jaccard(sh, candidate_shingles)
            if sim >= threshold and sim > best_sim:
                best_idx, best_sim = idx, sim
        if best_idx is not None:
            canonical_id = canonicals[best_idx]["signal_id"]
            duplicate_of[signal["signal_id"]] = canonical_id
            duplicate_reason[signal["signal_id"]] = f"near-duplicate prose (jaccard={best_sim:.2f})"
        else:
            canonicals.append(signal)
            canonical_shingles.append(sh)
            canonical_exact[exact_key] = signal["signal_id"]

    for signal in signals:
        signal["duplicate_of"] = duplicate_of.get(signal["signal_id"])

    groups = {c["signal_id"]: [c["signal_id"]] for c in canonicals}
    for dup_id, canonical_id in duplicate_of.items():
        groups.setdefault(canonical_id, [canonical_id]).append(dup_id)

    stats = {
        "input_signals": len(signals),
        "canonical_signals": len(canonicals),
        "duplicates_removed": len(duplicate_of),
        "duplicate_ratio": round(len(duplicate_of) / len(signals), 3) if signals else 0.0,
        "groups": {k: v for k, v in groups.items() if len(v) > 1},
        "reasons": duplicate_reason,
    }
    return {"canonicals": canonicals, "duplicate_of": duplicate_of, "stats": stats}


def independence_key(signal: dict) -> tuple[str, str]:
    """Identity used for recurrence counting: source class + author (or signal id)."""
    author = (signal.get("source_author") or "").strip().lower()
    if author:
        return signal.get("source_type", "?"), author
    return signal.get("source_type", "?"), signal.get("signal_id", "?")


def independent_count(signals: list[dict]) -> int:
    return len({independence_key(s) for s in signals if not s.get("duplicate_of")})
