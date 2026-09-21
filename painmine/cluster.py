"""Cheap semantic grouping into opportunity clusters (issue #9 Part 3, step 4).

Embeddings are not available in this stdlib-only spike, so grouping uses an
explicit TF-IDF + cosine agglomeration: a "similarly cheap semantic grouping"
that needs no model call. A cluster is only formed from signals whose buyer
(role family) is compatible and whose composite buyer+job+pain/workaround text
is close, so clusters represent patterns rather than shared keywords.
"""
from __future__ import annotations

import math
from collections import Counter

from .dedupe import independence_key
from .util import sha1_hex, tokenize

ROLE_FAMILIES: dict[str, str] = {
    "accountant": "accounting",
    "bookkeeper": "accounting",
    "practice manager (clinic/health)": "health_practice",
    "e-commerce operator": "ecommerce",
    "property/lettings professional": "property",
    "legal professional": "legal",
    "recruiter/hr": "hr",
    "hr/recruiter": "hr",
    "warehouse/logistics operator": "logistics",
    "construction/trade operator": "construction",
    "hospitality operator": "hospitality",
    "salon/spa operator": "personal_services",
    "education administrator": "education",
    "charity administrator": "charity",
    "operations manager": "operations",
    "office manager": "office_admin",
    "administrator": "office_admin",
    "procurement/purchasing": "procurement",
    "small business owner/operator": "micro_business",
    "sole trader/freelancer": "micro_business",
    "software developer": "software",
}

FAMILY_COMPATIBLE: set[frozenset[str]] = {
    frozenset({"accounting"}),
    frozenset({"micro_business", "accounting"}),
    frozenset({"office_admin", "operations"}),
    frozenset({"micro_business", "ecommerce"}),
    frozenset({"micro_business", "property"}),
    frozenset({"micro_business", "legal"}),
    frozenset({"micro_business", "construction"}),
    frozenset({"micro_business", "hospitality"}),
    frozenset({"micro_business", "personal_services"}),
    frozenset({"micro_business", "health_practice"}),
    frozenset({"micro_business", "logistics"}),
    frozenset({"micro_business", "hr"}),
}


def role_family(role: str | None) -> str | None:
    if not role:
        return None
    return ROLE_FAMILIES.get(role.strip().lower(), role.strip().lower())


def roles_compatible(a: str | None, b: str | None) -> bool:
    fam_a, fam_b = role_family(a), role_family(b)
    if not fam_a or not fam_b:
        return True  # an unknown role must not prevent grouping
    if fam_a == fam_b:
        return True
    return frozenset({fam_a, fam_b}) in FAMILY_COMPATIBLE


def composite_text(signal: dict) -> str:
    role = signal.get("target_role") or ""
    parts = [
        (role + " ") * 2,  # buyer/job weighting
        signal.get("task") or "",
        signal.get("pain_statement") or "",
        signal.get("current_workaround") or "",
        " ".join(signal.get("named_systems") or []),
        signal.get("integration_clue") or "",
    ]
    return " ".join(part for part in parts if part)


def build_tfidf(signals: list[dict]) -> dict[str, dict[str, float]]:
    docs = {s["signal_id"]: tokenize(composite_text(s)) for s in signals}
    df: Counter = Counter()
    for tokens in docs.values():
        for term in set(tokens):
            df[term] += 1
    n_docs = max(1, len(docs))
    vectors: dict[str, dict[str, float]] = {}
    for sid, tokens in docs.items():
        if not tokens:
            vectors[sid] = {}
            continue
        tf = Counter(tokens)
        vec = {
            term: (count / len(tokens)) * (math.log((1 + n_docs) / (1 + df[term])) + 1.0)
            for term, count in tf.items()
        }
        norm = math.sqrt(sum(value * value for value in vec.values())) or 1.0
        vectors[sid] = {term: value / norm for term, value in vec.items()}
    return vectors


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    if not a or not b:
        return 0.0
    if len(a) > len(b):
        a, b = b, a
    return sum(value * b.get(term, 0.0) for term, value in a.items())


def _centroid(vectors: list[dict[str, float]]) -> dict[str, float]:
    total: dict[str, float] = {}
    for vec in vectors:
        for term, value in vec.items():
            total[term] = total.get(term, 0.0) + value
    norm = math.sqrt(sum(value * value for value in total.values())) or 1.0
    return {term: value / norm for term, value in total.items()}


def _label(signals: list[dict], vectors: dict[str, dict[str, float]], key_terms_n: int) -> str:
    roles = Counter(s.get("target_role") for s in signals if s.get("target_role"))
    role = roles.most_common(1)[0][0] if roles else "unclassified buyer"
    totals: dict[str, float] = {}
    for signal in signals:
        for term, value in vectors.get(signal["signal_id"], {}).items():
            totals[term] = totals.get(term, 0.0) + value
    terms = [term for term, _ in sorted(totals.items(), key=lambda item: -item[1])[:key_terms_n]]
    return f"{role}: " + ", ".join(terms)


def _key_terms(signals: list[dict], vectors: dict[str, dict[str, float]], limit: int) -> list[str]:
    totals: dict[str, float] = {}
    for signal in signals:
        for term, value in vectors.get(signal["signal_id"], {}).items():
            totals[term] = totals.get(term, 0.0) + value
    return [term for term, _ in sorted(totals.items(), key=lambda item: -item[1])[:limit]]


def cluster(signals: list[dict], limits: dict) -> list[dict]:
    """Agglomerate canonical signals into clusters. Duplicates travel with their canonical."""
    cfg = limits.get("cluster", {})
    threshold = float(cfg.get("similarity_threshold", 0.17))
    max_clusters = int(cfg.get("max_clusters", 40))
    key_terms_n = int(cfg.get("key_terms", 8))

    all_vectors = build_tfidf(signals)
    canonicals = [s for s in signals if not s.get("duplicate_of")]
    duplicates_by_canonical: dict[str, list[dict]] = {}
    for signal in signals:
        if signal.get("duplicate_of"):
            duplicates_by_canonical.setdefault(signal["duplicate_of"], []).append(signal)

    canonicals.sort(key=lambda s: (-float(s.get("confidence", 0)), s["signal_id"]))
    clusters: list[dict] = []
    for signal in canonicals:
        vec = all_vectors.get(signal["signal_id"], {})
        best_index, best_sim = None, 0.0
        for index, group in enumerate(clusters):
            if not roles_compatible(signal.get("target_role"), group["role"]):
                continue
            sim = cosine(vec, group["_centroid"])
            if sim >= threshold and sim > best_sim:
                best_index, best_sim = index, sim
        if best_index is None:
            clusters.append(
                {
                    "role": signal.get("target_role"),
                    "_members": [signal],
                    "_vectors": [vec],
                    "_centroid": vec,
                }
            )
        else:
            group = clusters[best_index]
            group["_members"].append(signal)
            group["_vectors"].append(vec)
            group["_centroid"] = _centroid(group["_vectors"])
            if not group.get("role") and signal.get("target_role"):
                group["role"] = signal["target_role"]

    # Merge pass: clusters whose centroids are close and roles compatible.
    merged = True
    while merged and len(clusters) > 1:
        merged = False
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                a, b = clusters[i], clusters[j]
                if not roles_compatible(a["role"], b["role"]):
                    continue
                if cosine(a["_centroid"], b["_centroid"]) >= threshold:
                    a["_members"].extend(b["_members"])
                    a["_vectors"].extend(b["_vectors"])
                    a["_centroid"] = _centroid(a["_vectors"])
                    if not a.get("role") and b.get("role"):
                        a["role"] = b["role"]
                    del clusters[j]
                    merged = True
                    break
            if merged:
                break

    if len(clusters) > max_clusters:
        clusters.sort(key=lambda c: -len(c["_members"]))
        clusters = clusters[:max_clusters]

    # A cluster must recur: isolate signals are not opportunity patterns.
    min_size = int(cfg.get("min_cluster_size", 3))
    clusters = [c for c in clusters if len(c["_members"]) >= min_size]

    result: list[dict] = []
    for group in clusters:
        members = group["_members"]
        duplicates = [d for m in members for d in duplicates_by_canonical.get(m["signal_id"], [])]
        dates = sorted(
            [s["published_at"] for s in members if s.get("published_at")]
        )
        systems = sorted({sys for s in members for sys in (s.get("named_systems") or [])})
        source_types = sorted({s.get("source_type", "?") for s in members if not s.get("duplicate_of")})
        independent = len({independence_key(s) for s in members if not s.get("duplicate_of")})
        cluster_id = "c-" + sha1_hex(
            "|".join(sorted(s["signal_id"] for s in members))[:400], 8
        )
        result.append(
            {
                "cluster_id": cluster_id,
                "role": group.get("role"),
                "role_family": role_family(group.get("role")),
                "label": _label(members, all_vectors, key_terms_n),
                "key_terms": _key_terms(members, all_vectors, key_terms_n),
                "member_signal_ids": [s["signal_id"] for s in members],
                "duplicate_signal_ids": [d["signal_id"] for d in duplicates],
                "member_count": len(members),
                "duplicate_count": len(duplicates),
                "independent_sources": independent,
                "source_types": source_types,
                "named_systems": systems,
                "first_seen": dates[0] if dates else None,
                "last_seen": dates[-1] if dates else None,
                "runs_seen": 1,
                "evidence": [
                    {
                        "signal_id": s["signal_id"],
                        "source_type": s.get("source_type"),
                        "source_url": s.get("source_url"),
                        "published_at": s.get("published_at"),
                        "author": s.get("source_author"),
                        "statement": s.get("pain_statement"),
                        "systems": s.get("named_systems"),
                        "confidence": s.get("confidence"),
                    }
                    for s in sorted(members, key=lambda s: -float(s.get("confidence", 0)))
                ],
            }
        )

    result.sort(key=lambda c: (-c["independent_sources"], -c["member_count"]))
    return result
