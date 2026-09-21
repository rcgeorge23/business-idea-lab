"""Compact run state: seen source ids and cluster history (issue #9 Part 7).

Retention strategy: only compact structured state lives in Git (or in the
Actions cache); raw collected items stay in run artefacts with short
retention and are never committed by default.
"""
from __future__ import annotations

import os
from typing import Iterable

from .util import read_json, write_json

DEFAULT_SEEN_CAP = 5000


class State:
    def __init__(self, path: str, seen_cap: int = DEFAULT_SEEN_CAP) -> None:
        self.path = path
        self.seen_cap = seen_cap
        data = read_json(path, {}) or {}
        self.seen_ids: list[str] = list(data.get("seen_ids", []))
        self.cluster_history: list[dict] = list(data.get("cluster_history", []))
        self.runs: list[dict] = list(data.get("runs", []))
        self._seen_set = set(self.seen_ids)

    def is_new(self, source_id: str) -> bool:
        return source_id not in self._seen_set

    def filter_new(self, items: Iterable[dict]) -> list[dict]:
        fresh = []
        for item in items:
            if item.get("source_id") and self.is_new(item["source_id"]):
                fresh.append(item)
        return fresh

    def mark_seen(self, items: Iterable[dict]) -> None:
        for item in items:
            sid = item.get("source_id")
            if sid and sid not in self._seen_set:
                self._seen_set.add(sid)
                self.seen_ids.append(sid)
        if len(self.seen_ids) > self.seen_cap:
            self.seen_ids = self.seen_ids[-self.seen_cap :]
            # Evicted ids become "new" again; the cap bounds state growth and
            # re-collection of old items is harmless (dedupe still applies).
            self._seen_set = set(self.seen_ids)

    def record_run(self, meta: dict) -> None:
        self.runs = (self.runs + [meta])[-50:]

    def record_clusters(self, clusters: list[dict]) -> None:
        for cluster in clusters:
            self.cluster_history = [
                c for c in self.cluster_history if c.get("cluster_id") != cluster.get("cluster_id")
            ]
        self.cluster_history = (self.cluster_history + [
            {
                "cluster_id": c.get("cluster_id"),
                "label": c.get("label"),
                "priority_score": c.get("priority", {}).get("score"),
                "independent_sources": c.get("independent_sources"),
                "first_seen": c.get("first_seen"),
                "last_seen": c.get("last_seen"),
                "runs_seen": c.get("runs_seen", 1),
            }
            for c in clusters
        ])[-200:]

    def save(self) -> None:
        os.makedirs(os.path.dirname(os.path.abspath(self.path)), exist_ok=True)
        write_json(
            self.path,
            {
                "seen_ids": self.seen_ids,
                "cluster_history": self.cluster_history,
                "runs": self.runs,
            },
        )
