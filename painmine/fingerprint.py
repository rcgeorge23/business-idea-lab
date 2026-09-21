"""Deterministic cross-run signal fingerprints (issue #10).

A fingerprint is two things:

- ``exact``: a SHA-1 of the normalised prose basis used by ``dedupe`` (pain
  statement + workaround + task). Byte-identical reposts and mirrors collide
  here even when the URL, source id or author differs.
- ``minhash``: a 24-value MinHash sketch over 5-word shingles of the same
  prose. Banded signatures are used as a cheap candidate index; an estimated
  Jaccard >= the near-duplicate threshold marks a paraphrased repost.

Everything here is deterministic and local: no network, no model calls, no
retention of the full text (state keeps only a bounded excerpt). Fingerprints
are used to *link* restatements to the evidence they restate. They are never
used to claim that restated evidence is new or independent.
"""
from __future__ import annotations

import hashlib

from .util import normalize_text, sha1_hex, shingles, tokenize

FINGERPRINT_VERSION = "0.1.0"
PERMUTATIONS = 24
BANDS = 6
ROWS_PER_BAND = PERMUTATIONS // BANDS
SHINGLE_K = 5
NEAR_DUPLICATE_THRESHOLD = 0.62
_MAX_HASH = (1 << 64) - 1


def signal_text(signal: dict) -> str:
    """Prose basis shared with ``dedupe._dedup_text`` so within-run and
    cross-run duplicate detection agree on what counts as the same evidence."""
    return " ".join(
        [
            signal.get("pain_statement") or "",
            signal.get("current_workaround") or "",
            signal.get("task") or "",
        ]
    )


def exact_fingerprint(signal_or_text) -> str:
    text = signal_or_text if isinstance(signal_or_text, str) else signal_text(signal_or_text)
    return sha1_hex(normalize_text(text), 20)


def _permuted_hash(permutation: int, shingle: str) -> int:
    digest = hashlib.sha1(f"{permutation}:{shingle}".encode("utf-8")).hexdigest()
    return int(digest[:16], 16)


def minhash_signature(
    text: str, permutations: int = PERMUTATIONS, shingle_k: int = SHINGLE_K
) -> list[int]:
    """MinHash sketch of ``text``. Empty/short text still yields a valid sketch."""
    shingle_set = shingles(tokenize(text), shingle_k)
    if not shingle_set:
        return [0] * permutations
    signature = [_MAX_HASH] * permutations
    for shingle in shingle_set:
        for index in range(permutations):
            value = _permuted_hash(index, shingle)
            if value < signature[index]:
                signature[index] = value
    return signature


def make_fingerprint(signal: dict) -> dict:
    """Fingerprint record for one signal (all values JSON-serialisable)."""
    text = signal_text(signal)
    tokens = tokenize(text)
    shingle_set = shingles(tokens, SHINGLE_K)
    return {
        "fingerprint_version": FINGERPRINT_VERSION,
        "exact": exact_fingerprint(text),
        "minhash": minhash_signature(text),
        "token_count": len(tokens),
        "shingle_count": len(shingle_set),
    }


def is_valid_signature(signature, permutations: int = PERMUTATIONS) -> bool:
    return (
        isinstance(signature, list)
        and len(signature) == permutations
        and all(isinstance(value, int) and 0 <= value <= _MAX_HASH for value in signature)
    )


def estimated_jaccard(a, b) -> float:
    """Fraction of MinHash positions that agree (a Jaccard estimate)."""
    if not is_valid_signature(a) or not is_valid_signature(b):
        return 0.0
    if not any(a) or not any(b):
        # Empty text has no shingles: it must never look similar to anything.
        return 0.0
    matches = sum(1 for left, right in zip(a, b) if left == right)
    return matches / len(a)


def band_keys(signature, bands: int = BANDS, rows: int = ROWS_PER_BAND) -> list[tuple[int, ...]]:
    """LSH band keys for candidate lookup. In-memory only (tuples, not JSON)."""
    if not is_valid_signature(signature) or not any(signature):
        return []
    return [tuple(signature[index * rows : (index + 1) * rows]) for index in range(bands)]


def compare(a: dict, b: dict, threshold: float = NEAR_DUPLICATE_THRESHOLD) -> tuple[str | None, float]:
    """Return (match_type, similarity) where match_type is 'exact', 'near' or None."""
    if a.get("exact") and a.get("exact") == b.get("exact"):
        return "exact", 1.0
    similarity = estimated_jaccard(a.get("minhash"), b.get("minhash"))
    if similarity >= threshold:
        return "near", similarity
    return None, similarity
