"""Cross-run state for painmine (issue #10).

State v0.2.0 keeps four things:

- ``seen_ids``: raw-item ids already collected (collection-time filter).
- ``signals``: bounded records of canonical evidence, each with a deterministic
  fingerprint so a later run can link a repost, mirror or paraphrase back to
  the evidence it restates instead of counting it again.
- ``clusters``: bounded records of cluster lineage. Cluster ids are stable
  across runs: a run that matches retained evidence reuses the retained id and
  accumulates recurrence; unmatched clusters get a new run-scoped id.
- ``runs``: bounded run metadata.

Correctness rules enforced here (issue #10 acceptance criteria):

- Restatements never increase recurrence: linked signals are annotated with
  ``duplicate_of`` and are not registered as new evidence.
- Repeat collection of the same source does not increase recurrence either:
  re-collected signal ids refresh ``last_seen_at`` but are not new keys.
- Independent new evidence increases the retained cluster's cumulative counts.
- Cluster identity is stable and explainable: ``assign_cluster_lineage``
  returns per-cluster match score, matched dimensions and competing candidates.
- Source, author and organisation independence are tracked separately.
- Retention (TTL days and record caps) is explicit and enforced on load/save.
- Corrupt or unreadable state degrades safely: the damaged file is quarantined,
  history is reported unavailable, and recurrence is never silently inflated.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone

from .dedupe import independence_key
from .fingerprint import (
    NEAR_DUPLICATE_THRESHOLD,
    band_keys,
    estimated_jaccard,
    make_fingerprint,
)
from .util import (
    jaccard,
    parse_date,
    sha1_hex,
    tokenize,
    truncate,
    utcnow,
    utcnow_iso,
)

STATE_VERSION = "0.2.0"
DEFAULT_SEEN_CAP = 5000
DEFAULT_SIGNAL_CAP = 2000
DEFAULT_CLUSTER_CAP = 200
DEFAULT_SIGNAL_TTL_DAYS = 180
DEFAULT_CLUSTER_TTL_DAYS = 365
DEFAULT_MEMBER_CAP = 60
DEFAULT_INDEPENDENT_CAP = 60
DEFAULT_EXCERPT_CHARS = 240
DEFAULT_LINEAGE_MIN_SCORE = 0.35
DIMENSIONS = ("primary", "source", "author", "organisation")


def _age_days(iso_value, now_dt: datetime) -> int | None:
    parsed = parse_date(iso_value)
    if not parsed:
        return None
    try:
        moment = datetime.strptime(parsed, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return None
    return max(0, (now_dt - moment).days)


class State:
    """Bounded, corruption-safe cross-run state (schema version 0.2.0)."""

    def __init__(
        self,
        path: str,
        seen_cap: int = DEFAULT_SEEN_CAP,
        signal_cap: int = DEFAULT_SIGNAL_CAP,
        cluster_cap: int = DEFAULT_CLUSTER_CAP,
        signal_ttl_days: int = DEFAULT_SIGNAL_TTL_DAYS,
        cluster_ttl_days: int = DEFAULT_CLUSTER_TTL_DAYS,
        member_cap: int = DEFAULT_MEMBER_CAP,
        independent_cap: int = DEFAULT_INDEPENDENT_CAP,
        excerpt_chars: int = DEFAULT_EXCERPT_CHARS,
        near_threshold: float = NEAR_DUPLICATE_THRESHOLD,
        lineage_min_score: float = DEFAULT_LINEAGE_MIN_SCORE,
        now: datetime | None = None,
    ) -> None:
        self.path = path
        self.seen_cap = int(seen_cap)
        self.signal_cap = int(signal_cap)
        self.cluster_cap = int(cluster_cap)
        self.signal_ttl_days = int(signal_ttl_days)
        self.cluster_ttl_days = int(cluster_ttl_days)
        self.member_cap = int(member_cap)
        self.independent_cap = int(independent_cap)
        self.excerpt_chars = int(excerpt_chars)
        self.near_threshold = float(near_threshold)
        self.lineage_min_score = float(lineage_min_score)
        self._now = now

        self.seen_ids: list[str] = []
        self.signals: list[dict] = []
        self.clusters: list[dict] = []
        self.runs: list[dict] = []
        self.health: dict = self._empty_health()

        self._seen_set: set[str] = set()
        self._signal_index: dict[str, dict] = {}
        self._cluster_map: dict[str, dict] = {}
        self._exact_index: dict[str, dict] = {}
        self._band_index: dict[tuple, list[dict]] = {}

        self._load()

    # ------------------------------------------------------------------ load
    @staticmethod
    def _empty_health() -> dict:
        return {
            "status": "empty",
            "detail": "no state file yet",
            "degraded": False,
            "corrupt_backup": None,
            "migrated_from": None,
            "repaired_records": 0,
            "pruned": {},
        }

    def _now_dt(self) -> datetime:
        return self._now or utcnow()

    def _load(self) -> None:
        self.health = self._empty_health()
        if not self.path or not os.path.exists(self.path):
            return
        try:
            with open(self.path, "r", encoding="utf-8") as handle:
                data = json.load(handle)
        except (json.JSONDecodeError, OSError, UnicodeDecodeError, ValueError) as exc:
            backup = self._quarantine()
            self.health.update(
                {
                    "status": "degraded",
                    "detail": (
                        f"state unreadable ({type(exc).__name__}); recurrence history treated as "
                        "unavailable so it cannot be silently inflated"
                    ),
                    "degraded": True,
                    "corrupt_backup": backup,
                }
            )
            return
        if not isinstance(data, dict):
            backup = self._quarantine()
            self.health.update(
                {
                    "status": "degraded",
                    "detail": "state root is not an object; recurrence history treated as unavailable",
                    "degraded": True,
                    "corrupt_backup": backup,
                }
            )
            return

        version = data.get("state_version")
        repaired = 0
        if version is None:
            self.health.update(
                {
                    "status": "migrated",
                    "detail": "upgraded legacy state v0.1 (seen ids, cluster history)",
                    "migrated_from": "0.1",
                }
            )
            self.seen_ids = [value for value in data.get("seen_ids") or [] if isinstance(value, str)]
            self.runs = [run for run in data.get("runs") or [] if isinstance(run, dict)][-50:]
            for legacy in data.get("cluster_history") or []:
                if isinstance(legacy, dict) and isinstance(legacy.get("cluster_id"), str):
                    self.clusters.append(self._normalise_cluster_record(legacy))
        elif version == STATE_VERSION:
            self.health.update({"status": "ok", "detail": "state loaded"})
            self.seen_ids = [value for value in data.get("seen_ids") or [] if isinstance(value, str)]
            self.runs = [run for run in data.get("runs") or [] if isinstance(run, dict)][-50:]
            for record in data.get("signals") or []:
                if self._valid_signal_record(record):
                    self.signals.append(self._normalise_signal_record(record))
                else:
                    repaired += 1
            for record in data.get("clusters") or []:
                if self._valid_cluster_record(record):
                    self.clusters.append(self._normalise_cluster_record(record))
                else:
                    repaired += 1
        else:
            backup = self._quarantine()
            self.health.update(
                {
                    "status": "degraded",
                    "detail": (
                        f"state_version {version!r} is not understood by this build; history treated "
                        "as unavailable rather than guessed"
                    ),
                    "degraded": True,
                    "corrupt_backup": backup,
                }
            )
            return

        self.health["repaired_records"] = repaired
        self._rebuild_indexes()
        self._prune(record_health=True)

    def _quarantine(self) -> str | None:
        stamp = utcnow().strftime("%Y%m%dT%H%M%SZ")
        backup = f"{self.path}.corrupt-{stamp}"
        try:
            os.replace(self.path, backup)
            return backup
        except OSError:
            return None

    @staticmethod
    def _valid_signal_record(record) -> bool:
        if not isinstance(record, dict):
            return False
        if not isinstance(record.get("signal_id"), str) or not record["signal_id"]:
            return False
        if not isinstance(record.get("exact"), str) or not record["exact"]:
            return False
        return True

    @staticmethod
    def _valid_cluster_record(record) -> bool:
        return (
            isinstance(record, dict)
            and isinstance(record.get("cluster_id"), str)
            and bool(record["cluster_id"])
        )

    def _normalise_signal_record(self, record: dict) -> dict:
        record.setdefault("fingerprint_version", "0.1.0")
        record.setdefault("minhash", [])
        record.setdefault("source_type", "")
        record.setdefault("source_id", "")
        record.setdefault("source_url", "")
        record.setdefault("author", None)
        record.setdefault("organisation", None)
        record.setdefault("published_at", None)
        record.setdefault("first_seen_run", None)
        record.setdefault("last_seen_run", None)
        record.setdefault("first_seen_at", None)
        record.setdefault("last_seen_at", None)
        record.setdefault("last_matched_run", None)
        record.setdefault("cluster_id", None)
        record.setdefault("independence_key", [])
        record.setdefault("source_key", ["source", record.get("source_type"), record.get("source_id")])
        record.setdefault("author_key", None)
        record.setdefault("organisation_key", None)
        record.setdefault("statement_excerpt", "")
        return record

    def _normalise_cluster_record(self, record: dict) -> dict:
        record.setdefault("label", None)
        record.setdefault("role", None)
        record.setdefault("role_family", None)
        record.setdefault("key_terms", [])
        record.setdefault("named_systems", [])
        record.setdefault("priority_score", None)
        record.setdefault("priority_band", None)
        record.setdefault("independent_sources", 0)
        record.setdefault("member_signal_ids", [])
        record.setdefault("member_count_total", len(record.get("member_signal_ids") or []))
        record.setdefault("member_ids_truncated", False)
        record.setdefault("runs_seen", 1)
        record.setdefault("first_seen", None)
        record.setdefault("last_seen", None)
        record.setdefault("first_seen_run", None)
        record.setdefault("last_seen_run", None)
        record.setdefault("last_run_id", None)
        record.setdefault("last_seen_at", None)
        record.setdefault("lineage_actions", [])
        independence = record.setdefault("independence", {})
        if not isinstance(independence, dict):
            independence = {}
            record["independence"] = independence
        for dimension in DIMENSIONS:
            entry = independence.setdefault(dimension, {"keys": [], "total": 0, "truncated": False})
            if not isinstance(entry, dict):
                entry = {"keys": [], "total": 0, "truncated": False}
                independence[dimension] = entry
            entry.setdefault("keys", [])
            entry.setdefault("total", 0)
            entry.setdefault("truncated", False)
        record.setdefault("independent_sources_total", independence.get("primary", {}).get("total", 0))
        return record

    def _rebuild_indexes(self) -> None:
        self._seen_set = set(self.seen_ids)
        self._signal_index = {record["signal_id"]: record for record in self.signals}
        self._cluster_map = {record["cluster_id"]: record for record in self.clusters}
        self._exact_index = {}
        self._band_index = {}
        for record in self.signals:
            exact = record.get("exact")
            if exact and exact not in self._exact_index:
                self._exact_index[exact] = record
            for key in band_keys(record.get("minhash")):
                self._band_index.setdefault(key, []).append(record)

    # ------------------------------------------------------------- retention
    def prune(self) -> dict:
        return self._prune(record_health=True)

    def _prune(self, record_health: bool = False) -> dict:
        now_dt = self._now_dt()
        stats = {"expired_signals": 0, "trimmed_signals": 0, "expired_clusters": 0, "trimmed_clusters": 0}

        kept_signals = []
        for record in self.signals:
            age = _age_days(record.get("last_seen_at"), now_dt)
            if age is not None and age > self.signal_ttl_days:
                stats["expired_signals"] += 1
                continue
            kept_signals.append(record)
        if len(kept_signals) > self.signal_cap:
            kept_signals.sort(key=lambda item: (item.get("last_seen_at") or "", item.get("signal_id") or ""))
            stats["trimmed_signals"] = len(kept_signals) - self.signal_cap
            kept_signals = kept_signals[-self.signal_cap :]

        kept_clusters = []
        for record in self.clusters:
            age = _age_days(record.get("last_seen_at"), now_dt)
            if age is not None and age > self.cluster_ttl_days:
                stats["expired_clusters"] += 1
                continue
            kept_clusters.append(record)
        if len(kept_clusters) > self.cluster_cap:
            kept_clusters.sort(key=lambda item: (item.get("last_seen_at") or "", item.get("cluster_id") or ""))
            stats["trimmed_clusters"] = len(kept_clusters) - self.cluster_cap
            kept_clusters = kept_clusters[-self.cluster_cap :]

        changed = (
            stats["expired_signals"]
            or stats["trimmed_signals"]
            or stats["expired_clusters"]
            or stats["trimmed_clusters"]
        )
        self.signals = kept_signals
        self.clusters = kept_clusters
        if changed:
            self._rebuild_indexes()
        if record_health:
            self.health["pruned"] = stats
        return stats

    # ---------------------------------------------------------------- seen ids
    def is_new(self, source_id: str) -> bool:
        return source_id not in self._seen_set

    def filter_new(self, items: list[dict]) -> list[dict]:
        return [item for item in items if item.get("source_id") not in self._seen_set]

    def mark_seen(self, items: list[dict]) -> None:
        for item in items:
            source_id = item.get("source_id")
            if not source_id or source_id in self._seen_set:
                continue
            self._seen_set.add(source_id)
            self.seen_ids.append(source_id)
        if len(self.seen_ids) > self.seen_cap:
            self.seen_ids = self.seen_ids[-self.seen_cap :]
            self._seen_set = set(self.seen_ids)

    # --------------------------------------------------------------- run meta
    def record_run(self, meta: dict) -> None:
        self.runs.append(dict(meta))
        if len(self.runs) > 50:
            self.runs = self.runs[-50:]

    # ---------------------------------------------------------- cross-run link
    def find_match(self, fingerprint: dict) -> tuple[dict, str, float] | None:
        """Find retained evidence this fingerprint restates, if any."""
        exact = fingerprint.get("exact")
        record = self._exact_index.get(exact) if exact else None
        if record is not None:
            return record, "exact", 1.0

        best: dict | None = None
        best_similarity = 0.0
        seen_ids: set[str] = set()
        for key in band_keys(fingerprint.get("minhash")):
            for candidate in self._band_index.get(key, []):
                candidate_id = candidate.get("signal_id")
                if not candidate_id or candidate_id in seen_ids:
                    continue
                seen_ids.add(candidate_id)
                similarity = estimated_jaccard(fingerprint.get("minhash"), candidate.get("minhash"))
                if similarity > best_similarity:
                    best_similarity = similarity
                    best = candidate
                elif similarity == best_similarity and best is not None:
                    if candidate_id < (best.get("signal_id") or ""):
                        best = candidate
        if best is not None and best_similarity >= self.near_threshold:
            return best, "near", best_similarity
        return None

    def link_signals(self, signals: list[dict], run_id: str) -> dict:
        """Annotate signals that restate retained evidence.

        Linked signals get ``duplicate_of`` (plus scope/match/similarity and the
        prior cluster id) and are never registered as new evidence, so a repost
        or mirror cannot inflate recurrence.
        """
        summary = {"checked": 0, "linked": 0, "exact": 0, "near": 0, "details": []}
        for signal in signals:
            if signal.get("duplicate_of"):
                continue  # already a within-run duplicate; never counted twice
            summary["checked"] += 1
            fingerprint = make_fingerprint(signal)
            match = self.find_match(fingerprint)
            if match is None:
                continue
            record, match_type, similarity = match
            if record.get("signal_id") == signal.get("signal_id"):
                # The same evidence was re-collected (e.g. a seen-id cap evicted
                # the source id). That is a refresh, not a restatement: never
                # point a signal at itself or count it as new.
                continue
            signal["duplicate_of"] = record["signal_id"]
            signal["duplicate_scope"] = "previous-run"
            signal["duplicate_match"] = match_type
            signal["duplicate_similarity"] = round(similarity, 4)
            signal["duplicate_of_cluster_id"] = record.get("cluster_id")
            record["last_matched_run"] = run_id
            record["last_matched_at"] = utcnow_iso()
            summary["linked"] += 1
            summary[match_type] += 1
            if len(summary["details"]) < 50:
                summary["details"].append(
                    {
                        "signal_id": signal.get("signal_id"),
                        "restates_signal_id": record["signal_id"],
                        "restates_first_seen_run": record.get("first_seen_run"),
                        "match": match_type,
                        "similarity": round(similarity, 4),
                        "prior_cluster_id": record.get("cluster_id"),
                    }
                )
        return summary

    # ---------------------------------------------------------- registration
    def register_signals(self, signals: list[dict], run_id: str) -> dict:
        """Retain canonical (non-duplicate) evidence. Repeats refresh, never add."""
        added = refreshed = skipped_duplicates = 0
        now = utcnow_iso()
        for signal in signals:
            if signal.get("duplicate_of"):
                skipped_duplicates += 1
                continue
            signal_id = signal.get("signal_id")
            if not signal_id:
                continue
            existing = self._signal_index.get(signal_id)
            if existing is not None:
                existing["last_seen_run"] = run_id
                existing["last_seen_at"] = now
                refreshed += 1
                continue
            record = self._signal_record(signal, run_id, now)
            self.signals.append(record)
            self._signal_index[signal_id] = record
            exact = record.get("exact")
            if exact and exact not in self._exact_index:
                self._exact_index[exact] = record
            for key in band_keys(record.get("minhash")):
                self._band_index.setdefault(key, []).append(record)
            added += 1
        return {"added": added, "refreshed": refreshed, "skipped_duplicates": skipped_duplicates}

    def _signal_record(self, signal: dict, run_id: str, now: str) -> dict:
        fingerprint = make_fingerprint(signal)
        source_type = signal.get("source_type") or ""
        source_id = signal.get("source_id") or ""
        author = (signal.get("source_author") or "").strip().lower() or None
        organisation = (signal.get("organisation_hint") or "").strip().lower() or None
        key = independence_key(signal)
        return {
            "signal_id": signal.get("signal_id"),
            "fingerprint_version": fingerprint["fingerprint_version"],
            "exact": fingerprint["exact"],
            "minhash": fingerprint["minhash"],
            "source_type": source_type,
            "source_id": source_id,
            "source_url": signal.get("source_url") or "",
            "author": author,
            "organisation": organisation,
            "published_at": signal.get("published_at"),
            "first_seen_run": run_id,
            "last_seen_run": run_id,
            "first_seen_at": now,
            "last_seen_at": now,
            "last_matched_run": None,
            "cluster_id": signal.get("cluster_id"),
            "independence_key": list(key),
            "source_key": ["source", source_type, source_id],
            "author_key": ["author", source_type, author] if author else None,
            "organisation_key": ["organisation", organisation] if organisation else None,
            "statement_excerpt": truncate(signal.get("pain_statement") or "", self.excerpt_chars),
        }

    # ------------------------------------------------------------- lineage
    def assign_cluster_lineage(
        self, clusters: list[dict], signals_by_id: dict[str, dict], run_id: str
    ) -> dict[str, dict]:
        """Assign stable cluster ids and explainable lineage.

        Matching is deterministic and input-order independent: clusters are
        processed in sorted run-local id order, candidate scores are sorted by
        score then prior id, and a prior cluster can be claimed by at most one
        current cluster (the highest scorer; others are recorded as splits).
        """
        restated_by_prior: dict[str, list[dict]] = {}
        for signal in signals_by_id.values():
            prior = signal.get("duplicate_of_cluster_id")
            if prior:
                restated_by_prior.setdefault(prior, []).append(signal)

        ordered = sorted(clusters, key=lambda item: item.get("cluster_id") or "")
        scored: list[tuple[dict, list[tuple[float, str, list[str]]]]] = []
        for cluster in ordered:
            best_by_prior: dict[str, tuple[float, list[str]]] = {}
            for record in self.clusters:
                score, matched_via = self._cluster_match(cluster, record)
                if score >= self.lineage_min_score:
                    best_by_prior[record["cluster_id"]] = (score, matched_via)
            for prior_id, restated in restated_by_prior.items():
                record = self._cluster_map.get(prior_id)
                if record is None:
                    continue
                if not self._families_compatible(cluster.get("role_family"), record.get("role_family")):
                    continue
                overlap = set(record.get("key_terms") or []) & set(cluster.get("key_terms") or [])
                if not overlap:
                    continue
                boost = min(0.8, 0.5 + 0.1 * min(3, len(restated)))
                previous = best_by_prior.get(prior_id)
                if previous is None or boost > previous[0]:
                    best_by_prior[prior_id] = (
                        boost,
                        [f"restated_evidence({len(restated)})", f"key_terms({len(overlap)})"],
                    )
            candidates = sorted(
                ((score, prior_id, matched_via) for prior_id, (score, matched_via) in best_by_prior.items()),
                key=lambda item: (-item[0], item[1]),
            )
            scored.append((cluster, candidates))

        claimed: dict[str, str] = {}
        assignments: dict[str, tuple[float, str, list[str], list[tuple[float, str, list[str]]]] | None] = {}
        for cluster, candidates in scored:
            local_id = str(cluster.get("cluster_id") or "")
            if not local_id:
                continue
            if not candidates:
                assignments[local_id] = None
                continue
            score, prior_id, matched_via = candidates[0]
            if prior_id in claimed:
                cluster["_lineage_split_from"] = prior_id
                assignments[local_id] = None
            else:
                claimed[prior_id] = local_id
                assignments[local_id] = (score, prior_id, matched_via, candidates[1:3])

        lineage: dict[str, dict] = {}
        for cluster, _candidates in scored:
            local_id = str(cluster.get("cluster_id") or "")
            assignment = assignments.get(local_id)
            cluster["cluster_id_local"] = local_id
            if assignment is not None:
                score, prior_id, matched_via, others = assignment
                record = self._cluster_map.get(prior_id) or {}
                cluster["cluster_id"] = prior_id
                action = "merged" if others else "matched"
                lineage[prior_id] = {
                    "stable_cluster_id": prior_id,
                    "action": action,
                    "match_score": round(score, 4),
                    "matched_via": matched_via,
                    "other_candidates": [
                        {"cluster_id": candidate_id, "score": round(candidate_score, 4)}
                        for candidate_score, candidate_id, _ in others
                    ],
                    "first_seen_run": record.get("first_seen_run"),
                    "prior_runs_seen": record.get("runs_seen"),
                    "prior_independent_sources": record.get("independent_sources_total"),
                }
            else:
                split_from = cluster.pop("_lineage_split_from", None)
                stable_id = self._new_cluster_id(cluster, run_id)
                cluster["cluster_id"] = stable_id
                lineage[stable_id] = {
                    "stable_cluster_id": stable_id,
                    "action": "split" if split_from else "created",
                    "match_score": None,
                    "matched_via": [f"claimed_by_other_cluster({split_from})"] if split_from else [],
                    "other_candidates": [],
                    "first_seen_run": run_id,
                    "prior_runs_seen": 0,
                    "prior_independent_sources": 0,
                }
        return lineage

    def _new_cluster_id(self, cluster: dict, run_id: str) -> str:
        members = "|".join(sorted(cluster.get("member_signal_ids") or []))
        seed = f"{run_id or 'norun'}|{members}|{cluster.get('label') or ''}"
        return "c-" + sha1_hex(seed, 8)

    def _families_compatible(self, left: str | None, right: str | None) -> bool:
        if not left or not right:
            return True
        if left == right:
            return True
        from .cluster import roles_compatible

        return roles_compatible(left, right)

    def _cluster_match(self, cluster: dict, record: dict) -> tuple[float, list[str]]:
        current_family = cluster.get("role_family")
        prior_family = record.get("role_family")
        if not self._families_compatible(current_family, prior_family):
            return 0.0, []
        matched_via: list[str] = []
        family_match = bool(current_family and current_family == prior_family)
        role_match = bool(cluster.get("role") and cluster.get("role") == record.get("role"))
        if family_match:
            matched_via.append("role_family")
        if role_match:
            matched_via.append("role")
        terms = jaccard(set(cluster.get("key_terms") or []), set(record.get("key_terms") or []))
        systems = jaccard(set(cluster.get("named_systems") or []), set(record.get("named_systems") or []))
        labels = jaccard(set(tokenize(cluster.get("label") or "")), set(tokenize(record.get("label") or "")))
        if terms > 0:
            matched_via.append(f"key_terms({round(terms, 2)})")
        if systems > 0:
            matched_via.append(f"named_systems({round(systems, 2)})")
        if labels > 0:
            matched_via.append(f"label({round(labels, 2)})")
        score = (
            0.30 * (1.0 if family_match else 0.0)
            + 0.15 * (1.0 if role_match else 0.0)
            + 0.35 * terms
            + 0.15 * systems
            + 0.05 * labels
        )
        return score, matched_via

    # --------------------------------------------------------- cluster history
    @property
    def cluster_history(self) -> list[dict]:
        """Legacy alias retained for older callers/tests."""
        return self.clusters

    def record_clusters(self, clusters: list[dict], run_id: str | None = None) -> dict:
        now = utcnow_iso()
        created = matched = 0
        for cluster in clusters:
            cluster_id = cluster.get("cluster_id")
            if not cluster_id:
                continue
            existing = self._cluster_map.get(cluster_id)
            if existing is None:
                existing = self._new_cluster_record(cluster, run_id, now)
                self.clusters.append(existing)
                self._cluster_map[cluster_id] = existing
                created += 1
            else:
                self._update_cluster_record(existing, cluster, run_id, now)
                matched += 1
            for signal_id in cluster.get("member_signal_ids") or []:
                record = self._signal_index.get(signal_id)
                if record is not None:
                    record["cluster_id"] = cluster_id
        return {"created": created, "matched": matched}

    def _new_cluster_record(self, cluster: dict, run_id: str | None, now: str) -> dict:
        members = [sid for sid in cluster.get("member_signal_ids") or [] if sid in self._signal_index]
        priority = cluster.get("priority") or {}
        record = self._normalise_cluster_record(
            {
                "cluster_id": cluster.get("cluster_id"),
                "label": cluster.get("label"),
                "role": cluster.get("role"),
                "role_family": cluster.get("role_family"),
                "key_terms": list(cluster.get("key_terms") or [])[:16],
                "named_systems": list(cluster.get("named_systems") or [])[:16],
                "priority_score": priority.get("score"),
                "priority_band": priority.get("band"),
                "independent_sources": cluster.get("independent_sources") or 0,
                "member_signal_ids": members[-self.member_cap :],
                "member_ids_truncated": len(members) > self.member_cap,
                "member_count_total": len(members),
                "runs_seen": 1 if run_id else 0,
                "first_seen": cluster.get("first_seen"),
                "last_seen": cluster.get("last_seen"),
                "first_seen_run": run_id,
                "last_seen_run": run_id,
                "last_run_id": run_id,
                "last_seen_at": now,
            }
        )
        self._merge_cluster_keys(record, members)
        return record

    def _update_cluster_record(self, record: dict, cluster: dict, run_id: str | None, now: str) -> None:
        if cluster.get("label"):
            record["label"] = cluster["label"]
        if cluster.get("role"):
            record["role"] = cluster["role"]
        if cluster.get("role_family"):
            record["role_family"] = cluster["role_family"]
        if cluster.get("key_terms"):
            record["key_terms"] = list(cluster["key_terms"])[:16]
        if cluster.get("named_systems"):
            record["named_systems"] = list(cluster["named_systems"])[:16]
        priority = cluster.get("priority") or {}
        if priority.get("score") is not None:
            record["priority_score"] = priority["score"]
        if priority.get("band"):
            record["priority_band"] = priority["band"]
        record["independent_sources"] = cluster.get("independent_sources") or 0

        members = [sid for sid in cluster.get("member_signal_ids") or [] if sid in self._signal_index]
        known = list(record.get("member_signal_ids") or [])
        new_members = [sid for sid in members if sid not in known]
        record["member_count_total"] = int(record.get("member_count_total") or 0) + len(new_members)
        combined = known + new_members
        if len(combined) > self.member_cap:
            record["member_ids_truncated"] = True
        record["member_signal_ids"] = combined[-self.member_cap :]
        self._merge_cluster_keys(record, new_members)

        if run_id and record.get("last_run_id") != run_id:
            record["runs_seen"] = int(record.get("runs_seen") or 0) + 1
            record["last_run_id"] = run_id
        if run_id:
            record["last_seen_run"] = run_id
        if cluster.get("last_seen"):
            record["last_seen"] = cluster["last_seen"]
        record["last_seen_at"] = now
        lineage = cluster.get("lineage") or {}
        if lineage:
            actions = record.setdefault("lineage_actions", [])
            actions.append(
                {
                    "run_id": run_id,
                    "action": lineage.get("action"),
                    "match_score": lineage.get("match_score"),
                }
            )
            del actions[:-10]

    def _merge_cluster_keys(self, record: dict, members: list[str]) -> None:
        independence = record.setdefault("independence", {})
        for dimension in DIMENSIONS:
            entry = independence.setdefault(dimension, {"keys": [], "total": 0, "truncated": False})
            self._merge_keys(entry, self._member_keys(members, dimension))
        record["independent_sources_total"] = independence.get("primary", {}).get("total", 0)

    def _merge_keys(self, entry: dict, new_keys: list[list[str]]) -> None:
        keys = list(entry.get("keys") or [])
        known = {tuple(key) for key in keys}
        for key in new_keys:
            tkey = tuple(key)
            if not tkey or tkey in known:
                continue
            if len(keys) >= self.independent_cap:
                entry["truncated"] = True
                continue  # never count what we cannot store (avoids later double-count)
            keys.append(list(tkey))
            known.add(tkey)
            entry["total"] = int(entry.get("total") or 0) + 1
        entry["keys"] = keys

    def _member_keys(self, members: list[str], dimension: str) -> list[list[str]]:
        keys: list[list[str]] = []
        seen: set[tuple] = set()
        for signal_id in members:
            record = self._signal_index.get(signal_id)
            if record is None:
                continue
            if dimension == "primary":
                key = record.get("independence_key")
            else:
                key = record.get(f"{dimension}_key")
            if not key:
                continue
            tkey = tuple(key)
            if tkey in seen:
                continue
            seen.add(tkey)
            keys.append(list(tkey))
        return keys

    # -------------------------------------------------------------- reporting
    def history_summary(self, clusters: list[dict] | None = None) -> dict:
        per_cluster: dict[str, dict] = {}
        for cluster in clusters or []:
            cluster_id = str(cluster.get("cluster_id") or "")
            if not cluster_id:
                continue
            record = self._cluster_map.get(cluster_id) or {}
            lineage = cluster.get("lineage") or {}
            independence = record.get("independence") or {}
            per_cluster[cluster_id] = {
                "stable_cluster_id": cluster_id,
                "runs_seen": record.get("runs_seen"),
                "first_seen_run": record.get("first_seen_run"),
                "current_independent_sources": cluster.get("independent_sources"),
                "cumulative_independent_sources": record.get("independent_sources_total"),
                "cumulative_member_count": record.get("member_count_total"),
                "lineage_action": lineage.get("action"),
                "match_score": lineage.get("match_score"),
                "matched_via": lineage.get("matched_via"),
                "independence": {
                    dimension: {
                        "total": (independence.get(dimension) or {}).get("total"),
                        "truncated": (independence.get(dimension) or {}).get("truncated"),
                    }
                    for dimension in DIMENSIONS
                },
            }
        return {
            "state_version": STATE_VERSION,
            "state_health": dict(self.health),
            "history_available": not self.health.get("degraded", False),
            "retained_signals": len(self.signals),
            "retained_clusters": len(self.clusters),
            "retained_runs": len(self.runs),
            "clusters": per_cluster,
            "disclaimer": (
                "Cumulative recurrence counts distinct retained evidence keys and never counts "
                "restatements; it is discovery evidence, not Method validation."
            ),
        }

    # -------------------------------------------------------------------- save
    def save(self) -> None:
        self._prune(record_health=True)
        payload = {
            "state_version": STATE_VERSION,
            "updated_at": utcnow_iso(),
            "seen_ids": self.seen_ids,
            "signals": self.signals,
            "clusters": self.clusters,
            "runs": self.runs,
        }
        directory = os.path.dirname(os.path.abspath(self.path))
        os.makedirs(directory, exist_ok=True)
        tmp_path = f"{self.path}.tmp"
        with open(tmp_path, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
        os.replace(tmp_path, self.path)
