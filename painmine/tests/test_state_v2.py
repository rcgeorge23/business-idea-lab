import glob
import json
import os
import sys
import tempfile
import unittest
from datetime import datetime, timezone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine.state import STATE_VERSION, State  # noqa: E402


ORIGINAL = (
    "I spend three hours every week exporting invoices from Xero into CSV and "
    "re-keying them into Excel for the bookkeeping reconciliation."
)
MIRROR = (
    "I spend three hours every week exporting invoices from Xero into CSV and "
    "re-keying them into Excel for the bookkeeping reconciliation, and it is still painful."
)
IND1 = (
    "Our accounts team exports the weekly sales ledger from Sage and types every "
    "line into a spreadsheet before the management accounts go out."
)
IND2 = (
    "I reconcile Stripe payouts against QuickBooks by hand in Google Sheets, which "
    "takes a full afternoon every month and still leaves gaps."
)
IND3 = (
    "The finance team copies invoice totals from the billing portal into Xero "
    "manually because the two systems have never been connected."
)


def make_signal(text, source_type="hn", source_id="1", author="alice", organisation=None):
    return {
        "signal_id": f"{source_type}:{source_id}",
        "source_type": source_type,
        "source_id": source_id,
        "source_url": f"https://example.com/{source_type}/{source_id}",
        "source_author": author,
        "organisation_hint": organisation,
        "published_at": "2026-08-01",
        "pain_statement": text,
        "current_workaround": "",
        "task": "",
        "cluster_id": None,
    }


def make_cluster(cluster_id, members, independent=1, role="Bookkeeper", family="accounting"):
    return {
        "cluster_id": cluster_id,
        "role": role,
        "role_family": family,
        "key_terms": ["invoices", "xero", "reconciliation"],
        "named_systems": ["Xero", "Excel"],
        "label": "Bookkeeper: xero invoices reconciliation",
        "member_signal_ids": list(members),
        "independent_sources": independent,
        "priority": {"score": 70, "band": "A"},
        "first_seen": "2026-08-01",
        "last_seen": "2026-08-01",
    }


class TestStateV2(unittest.TestCase):
    def test_exact_repost_links_and_does_not_inflate(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = State(os.path.join(tmp, "state.json"))
            first = make_signal(ORIGINAL, "hn", "1", "alice")
            state.register_signals([first], "run1")

            restatement = make_signal(ORIGINAL, "reddit", "999", "bob")
            links = state.link_signals([restatement], "run2")
            self.assertEqual(links["linked"], 1)
            self.assertEqual(links["exact"], 1)
            self.assertEqual(restatement["duplicate_of"], first["signal_id"])
            self.assertEqual(restatement["duplicate_scope"], "previous-run")

            registration = state.register_signals([restatement], "run2")
            self.assertEqual(registration, {"added": 0, "refreshed": 0, "skipped_duplicates": 1})
            self.assertEqual(len(state.signals), 1)

            state.record_clusters([make_cluster("c-1", [first["signal_id"]])], "run2")
            history = state.history_summary([make_cluster("c-1", [first["signal_id"]])])
            self.assertEqual(history["clusters"]["c-1"]["cumulative_independent_sources"], 1)
            self.assertEqual(history["clusters"]["c-1"]["runs_seen"], 1)

    def test_mirror_is_linked_as_near_duplicate(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = State(os.path.join(tmp, "state.json"))
            first = make_signal(ORIGINAL, "hn", "1", "alice")
            state.register_signals([first], "run1")

            mirror = make_signal(MIRROR, "reddit", "999", "bob")
            links = state.link_signals([mirror], "run2")
            self.assertEqual(links["linked"], 1)
            self.assertEqual(links["near"], 1)
            self.assertGreaterEqual(mirror["duplicate_similarity"], state.near_threshold)
            self.assertEqual(mirror["duplicate_of"], first["signal_id"])

    def test_repeat_collection_refreshes_without_self_link_or_inflation(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = State(os.path.join(tmp, "state.json"))
            first = make_signal(ORIGINAL, "hn", "1", "alice")
            state.register_signals([first], "run1")

            recollected = make_signal(ORIGINAL, "hn", "1", "alice")
            links = state.link_signals([recollected], "run2")
            self.assertEqual(links["linked"], 0)
            self.assertNotIn("duplicate_of", recollected)

            registration = state.register_signals([recollected], "run2")
            self.assertEqual(registration, {"added": 0, "refreshed": 1, "skipped_duplicates": 0})
            self.assertEqual(len(state.signals), 1)
            self.assertEqual(state.signals[0]["last_seen_run"], "run2")

    def test_independent_new_evidence_increases_cumulative_recurrence(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = State(os.path.join(tmp, "state.json"))
            one = make_signal(IND1, "hn", "1", "alice")
            two = make_signal(IND2, "se", "2", "bob")
            state.register_signals([one, two], "run1")
            state.record_clusters(
                [make_cluster("c-1", [one["signal_id"], two["signal_id"]], independent=2)],
                "run1",
            )
            history = state.history_summary(
                [make_cluster("c-1", [one["signal_id"], two["signal_id"]], independent=2)]
            )
            self.assertEqual(history["clusters"]["c-1"]["cumulative_independent_sources"], 2)

            three = make_signal(IND3, "gh", "3", "carol")
            links = state.link_signals([three], "run2")
            self.assertEqual(links["linked"], 0)
            state.register_signals([three], "run2")
            state.record_clusters([make_cluster("c-1", [three["signal_id"]], independent=1)], "run2")

            history = state.history_summary([make_cluster("c-1", [three["signal_id"]], independent=1)])
            self.assertEqual(history["clusters"]["c-1"]["cumulative_independent_sources"], 3)
            self.assertEqual(history["clusters"]["c-1"]["current_independent_sources"], 1)
            self.assertEqual(history["clusters"]["c-1"]["runs_seen"], 2)

    def test_stable_cluster_identity_across_membership_change(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = State(os.path.join(tmp, "state.json"))
            first = make_signal(IND1, "hn", "1", "alice")
            state.register_signals([first], "run1")
            state.record_clusters([make_cluster("c-1", [first["signal_id"]])], "run1")

            grown = make_cluster("c-local-run2", [first["signal_id"], "hn:9"], independent=2)
            lineage = state.assign_cluster_lineage([grown], {}, "run2")
            self.assertEqual(grown["cluster_id"], "c-1")
            self.assertEqual(lineage["c-1"]["action"], "matched")
            self.assertGreaterEqual(lineage["c-1"]["match_score"], state.lineage_min_score)
            self.assertIn("role_family", lineage["c-1"]["matched_via"])
            self.assertIn("role", lineage["c-1"]["matched_via"])
            self.assertTrue(any(item.startswith("key_terms(") for item in lineage["c-1"]["matched_via"]))
            self.assertEqual(lineage["c-1"]["first_seen_run"], "run1")

    def test_competing_clusters_split_with_explanation(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = State(os.path.join(tmp, "state.json"))
            first = make_signal(IND1, "hn", "1", "alice")
            state.register_signals([first], "run1")
            state.record_clusters([make_cluster("c-1", [first["signal_id"]])], "run1")

            left = make_cluster("c-a", ["hn:9"], independent=1)
            right = make_cluster("c-b", ["hn:10"], independent=1)
            lineage = state.assign_cluster_lineage([right, left], {}, "run2")
            self.assertEqual(left["cluster_id"], "c-1")
            self.assertEqual(lineage["c-1"]["action"], "matched")
            split = [entry for entry in lineage.values() if entry["action"] == "split"]
            self.assertEqual(len(split), 1)
            self.assertTrue(split[0]["matched_via"][0].startswith("claimed_by_other_cluster("))
            self.assertNotEqual(right["cluster_id"], "c-1")

    def test_input_order_independence(self):
        with tempfile.TemporaryDirectory() as tmp:
            signals = [
                make_signal(IND1, "hn", "1", "alice"),
                make_signal(IND2, "se", "2", "bob"),
                make_signal(IND3, "gh", "3", "carol"),
            ]
            members = [item["signal_id"] for item in signals]
            summaries = []
            for order in (signals, list(reversed(signals))):
                state = State(os.path.join(tmp, f"state-{len(summaries)}.json"))
                state.register_signals(order, "run1")
                state.record_clusters([make_cluster("c-1", members, independent=3)], "run1")
                summaries.append(state.history_summary([make_cluster("c-1", members, independent=3)]))
            self.assertEqual(
                summaries[0]["clusters"]["c-1"]["cumulative_independent_sources"],
                summaries[1]["clusters"]["c-1"]["cumulative_independent_sources"],
            )
            self.assertEqual(
                summaries[0]["clusters"]["c-1"]["independence"],
                summaries[1]["clusters"]["c-1"]["independence"],
            )

    def test_independence_dimensions_are_tracked_separately(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = State(os.path.join(tmp, "state.json"))
            one = make_signal(IND1, "hn", "1", "alice")
            two = make_signal(IND2, "hn", "2", "alice")
            state.register_signals([one, two], "run1")
            state.record_clusters([make_cluster("c-1", [one["signal_id"], two["signal_id"]])], "run1")
            history = state.history_summary([make_cluster("c-1", [one["signal_id"], two["signal_id"]])])
            dimensions = history["clusters"]["c-1"]["independence"]
            self.assertEqual(dimensions["primary"]["total"], 1)  # same source class + author
            self.assertEqual(dimensions["source"]["total"], 2)  # different source ids
            self.assertEqual(dimensions["author"]["total"], 1)

    def test_independent_and_member_caps_never_overcount(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = State(os.path.join(tmp, "state.json"), independent_cap=2, member_cap=2)
            signals = [
                make_signal(IND1, "hn", "1", "alice"),
                make_signal(IND2, "se", "2", "bob"),
                make_signal(IND3, "gh", "3", "carol"),
            ]
            state.register_signals(signals, "run1")
            members = [item["signal_id"] for item in signals]
            state.record_clusters([make_cluster("c-1", members, independent=3)], "run1")
            record = state.clusters[0]
            self.assertEqual(record["independence"]["primary"]["total"], 2)
            self.assertTrue(record["independence"]["primary"]["truncated"])
            self.assertTrue(record["member_ids_truncated"])
            self.assertEqual(record["member_count_total"], 3)
            self.assertEqual(len(record["member_signal_ids"]), 2)

    def test_legacy_state_migrates(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "state.json")
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(
                    {
                        "seen_ids": ["hn:1"],
                        "cluster_history": [
                            {"cluster_id": "c-1", "label": "x", "independent_sources": 3, "priority_score": 80}
                        ],
                        "runs": [{"run_id": "r0"}],
                    },
                    handle,
                )
            state = State(path)
            self.assertEqual(state.health["status"], "migrated")
            self.assertFalse(state.is_new("hn:1"))
            self.assertEqual(state.cluster_history[0]["cluster_id"], "c-1")
            self.assertEqual(state.cluster_history[0]["priority_score"], 80)
            self.assertEqual(state.runs[0]["run_id"], "r0")

    def test_corrupt_state_quarantines_and_degrades(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "state.json")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write("{not valid json")
            state = State(path)
            self.assertTrue(state.health["degraded"])
            self.assertEqual(state.health["status"], "degraded")
            self.assertTrue(state.health["corrupt_backup"])
            self.assertTrue(glob.glob(path + ".corrupt-*"))
            history = state.history_summary([])
            self.assertFalse(history["history_available"])
            self.assertEqual(history["retained_signals"], 0)

            restatement = make_signal(ORIGINAL, "reddit", "999", "bob")
            links = state.link_signals([restatement], "run2")
            self.assertEqual(links["linked"], 0)  # no history: recurrence cannot be inflated
            state.save()
            reloaded = State(path)
            self.assertEqual(reloaded.health["status"], "ok")

    def test_unknown_state_version_is_not_guessed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "state.json")
            with open(path, "w", encoding="utf-8") as handle:
                json.dump({"state_version": "99.0.0", "signals": [{"signal_id": "x", "exact": "y"}]}, handle)
            state = State(path)
            self.assertTrue(state.health["degraded"])
            self.assertEqual(state.signals, [])
            self.assertTrue(glob.glob(path + ".corrupt-*"))

    def test_expiry_prunes_old_records(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "state.json")
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(
                    {
                        "state_version": STATE_VERSION,
                        "seen_ids": [],
                        "signals": [
                            {
                                "signal_id": "hn:old",
                                "exact": "abc",
                                "minhash": [],
                                "last_seen_at": "2020-01-01T00:00:00Z",
                            }
                        ],
                        "clusters": [
                            {
                                "cluster_id": "c-old",
                                "label": "old",
                                "last_seen_at": "2020-01-01T00:00:00Z",
                            }
                        ],
                        "runs": [],
                    },
                    handle,
                )
            state = State(
                path,
                signal_ttl_days=30,
                cluster_ttl_days=30,
                now=datetime(2026, 9, 21, tzinfo=timezone.utc),
            )
            self.assertEqual(state.signals, [])
            self.assertEqual(state.clusters, [])
            self.assertEqual(state.health["pruned"]["expired_signals"], 1)
            self.assertEqual(state.health["pruned"]["expired_clusters"], 1)

    def test_save_is_atomic_and_versioned(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "state.json")
            state = State(path)
            state.mark_seen([{"source_id": "hn:1"}])
            state.save()
            self.assertFalse(os.path.exists(path + ".tmp"))
            with open(path, "r", encoding="utf-8") as handle:
                payload = json.load(handle)
            self.assertEqual(payload["state_version"], STATE_VERSION)
            self.assertEqual(payload["seen_ids"], ["hn:1"])


if __name__ == "__main__":
    unittest.main()
