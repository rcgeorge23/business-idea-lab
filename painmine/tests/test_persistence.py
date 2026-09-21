import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine.cluster import cluster  # noqa: E402
from painmine.dedupe import dedupe  # noqa: E402
from painmine.extract import extract_many  # noqa: E402
from painmine.fetch import load_fixture_items  # noqa: E402
from painmine.persistence import (  # noqa: E402
    cluster_archetype,
    detect_archetype,
    mechanism_hypotheses,
    persistence_thesis,
)
from painmine.util import read_json  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE = os.path.join(HERE, "fixtures", "raw_items.jsonl")
LIMITS = read_json(os.path.join(HERE, "..", "limits.json"))


def prepared():
    signals, _ = extract_many(load_fixture_items(FIXTURE), LIMITS)
    dedupe(signals)
    clusters = cluster(signals, LIMITS)
    by_id = {s["signal_id"]: s for s in signals}
    by_source = {s["source_id"]: s for s in signals}
    return signals, clusters, by_id, by_source


class TestPersistence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.signals, cls.clusters, cls.by_id, cls.by_source = prepared()

    def test_change_cue_item_is_change_driven(self):
        result = detect_archetype(self.by_source["hn:4006"])
        self.assertEqual(result["archetype"], "change_driven")
        self.assertTrue(result["change_cue"])

    def test_ordinary_item_is_persistent(self):
        result = detect_archetype(self.by_source["hn:4001"])
        self.assertEqual(result["archetype"], "persistent")
        self.assertIsNone(result["change_cue"])

    def test_mechanism_hypotheses_need_two_independent_signals(self):
        # Use canonical (non-duplicate) members of the recurring accounting cluster.
        cl = [c for c in self.clusters if "Xero" in (c["named_systems"] or [])][0]
        members = [self.by_id[sid] for sid in cl["member_signal_ids"]]
        mechanisms = mechanism_hypotheses(members)
        integration = mechanisms["partial_or_manual_integration"]
        self.assertGreaterEqual(integration["evidence_count"], 2)
        self.assertTrue(integration["supported"])
        self.assertTrue(all(not m["supported"] or m["evidence_count"] >= 2 for m in mechanisms.values()))

    def test_accounting_cluster_persistence_thesis(self):
        cl = [c for c in self.clusters if "Xero" in (c["named_systems"] or [])][0]
        members = [self.by_id[sid] for sid in cl["member_signal_ids"]]
        thesis = persistence_thesis(cl, members)
        self.assertTrue(thesis["limb1_continued_pain_despite_alternatives"]["pass"])
        self.assertTrue(thesis["limb2_persistence_mechanism"]["pass"])
        self.assertIn(thesis["strength"], ("strong", "weak"))
        self.assertIn("not an assertion", thesis["disclaimer"].lower())

    def test_single_signal_has_no_persistence_thesis(self):
        signal = self.by_source["hn:4001"]
        cl = {
            "cluster_id": "c-solo",
            "member_signal_ids": [signal["signal_id"]],
            "independent_sources": 1,
        }
        thesis = persistence_thesis(cl, [signal])
        self.assertEqual(thesis["strength"], "absent")

    def test_cluster_archetype_majority_rule(self):
        accounting = [c for c in self.clusters if "Xero" in (c["named_systems"] or [])][0]
        members = [self.by_id[sid] for sid in accounting["member_signal_ids"]]
        result = cluster_archetype(members)
        self.assertEqual(result["archetype"], "persistent")
        self.assertIsNone(result["why_now"])

    def test_change_driven_cluster_records_unverified_why_now(self):
        result = cluster_archetype([self.by_source["hn:4006"]])
        self.assertEqual(result["archetype"], "change_driven")
        why_now = result["why_now"]
        self.assertTrue(why_now["changed"])
        self.assertIn("competitors_responded", why_now)
        self.assertEqual(why_now["competitors_responded"], "unknown")
        self.assertIn("UNVERIFIED HYPOTHESIS", why_now["why_it_matters"])


if __name__ == "__main__":
    unittest.main()
