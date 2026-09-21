import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine.cluster import cluster  # noqa: E402
from painmine.dedupe import dedupe  # noqa: E402
from painmine.extract import extract_many  # noqa: E402
from painmine.fetch import load_fixture_items  # noqa: E402
from painmine.rank import rank_cluster, rank_clusters  # noqa: E402
from painmine.util import read_json, utcnow_iso  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE = os.path.join(HERE, "fixtures", "raw_items.jsonl")
LIMITS = read_json(os.path.join(HERE, "..", "limits.json"))


def ranked_fixture():
    signals, _ = extract_many(load_fixture_items(FIXTURE), LIMITS)
    dedupe(signals)
    clusters = rank_clusters(cluster(signals, LIMITS), signals, LIMITS)
    return {s["signal_id"]: s for s in signals}, clusters


def consumer_cluster():
    cluster_dict = {
        "cluster_id": "c-consumer",
        "role": None,
        "role_family": None,
        "named_systems": [],
        "source_types": ["reddit_public_json"],
        "member_signal_ids": ["s1"],
        "independent_sources": 1,
        "duplicate_count": 0,
        "last_seen": utcnow_iso(),
    }
    signal = {
        "signal_id": "s1",
        "source_type": "reddit_public_json",
        "pain_statement": "I wish my personal budget app on my iPhone worked with my bank without ads",
        "extraction_provenance": {"cue_groups": []},
    }
    return cluster_dict, {"s1": signal}


class TestRank(unittest.TestCase):
    def test_scores_are_bounded_and_explained(self):
        _, clusters = ranked_fixture()
        self.assertTrue(clusters)
        for cl in clusters:
            priority = cl["priority"]
            self.assertGreaterEqual(priority["score"], 0)
            self.assertLessEqual(priority["score"], 100)
            self.assertIn(priority["band"], ("A", "B", "C"))
            self.assertIn("not a business score", priority["disclaimer"].lower())
            self.assertIn("positive_signals", priority)
            self.assertIn("penalties", priority)

    def test_recurring_accounting_cluster_scores_higher_than_consumer_noise(self):
        _, clusters = ranked_fixture()
        accounting = [c for c in clusters if "Xero" in (c["named_systems"] or [])][0]
        self.assertGreaterEqual(accounting["priority"]["score"], 50)
        self.assertEqual(
            accounting["priority"]["positive_signals"]["recurrence"],
            min(30.0, 10.0 * accounting["independent_sources"]),
        )

    def test_consumer_only_cluster_is_penalised(self):
        cluster_dict, signals = consumer_cluster()
        priority = rank_cluster(cluster_dict, signals, LIMITS)
        self.assertIn("consumer_only", priority["penalties"])
        self.assertIn("no_identifiable_economic_buyer", priority["penalties"])
        self.assertEqual(priority["band"], "C")
        self.assertLessEqual(priority["score"], 25)

    def test_ranking_is_separate_from_method_business_score(self):
        _, clusters = ranked_fixture()
        for cl in clusters:
            self.assertNotIn("business_score", cl["priority"])
            self.assertIn("priority", cl)

    def test_vendor_led_risk_defaults_low_for_user_sources(self):
        _, clusters = ranked_fixture()
        accounting = [c for c in clusters if "Xero" in (c["named_systems"] or [])][0]
        self.assertEqual(accounting["priority"]["vendor_led_risk"], "low")


if __name__ == "__main__":
    unittest.main()
