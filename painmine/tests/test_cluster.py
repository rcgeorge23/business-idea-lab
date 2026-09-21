import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine.cluster import cluster, role_family, roles_compatible  # noqa: E402
from painmine.dedupe import dedupe  # noqa: E402
from painmine.extract import extract_many  # noqa: E402
from painmine.fetch import load_fixture_items  # noqa: E402
from painmine.util import read_json  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE = os.path.join(HERE, "fixtures", "raw_items.jsonl")
LIMITS = read_json(os.path.join(HERE, "..", "limits.json"))


def clustered():
    signals, _ = extract_many(load_fixture_items(FIXTURE), LIMITS)
    dedupe(signals)
    return signals, cluster(signals, LIMITS)


class TestRoleCompatibility(unittest.TestCase):
    def test_same_family_and_micro_business_pairs(self):
        self.assertTrue(roles_compatible("Accountant", "Bookkeeper"))
        self.assertTrue(roles_compatible("Accountant", "Sole trader/freelancer"))
        self.assertTrue(roles_compatible(None, "Accountant"))

    def test_unrelated_families_do_not_merge(self):
        self.assertFalse(roles_compatible("Accountant", "E-commerce operator"))
        self.assertFalse(roles_compatible("Warehouse/logistics operator", "E-commerce operator"))

    def test_role_family_unknown_role_passthrough(self):
        self.assertEqual(role_family("Widget wrangler"), "widget wrangler")
        self.assertIsNone(role_family(None))


class TestCluster(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.signals, cls.clusters = clustered()
        cls.signals_by_id = {s["signal_id"]: s for s in cls.signals}

    def test_multiple_clusters_form(self):
        self.assertGreaterEqual(len(self.clusters), 2)

    def test_accounting_rekey_cluster_recurs(self):
        accounting = [c for c in self.clusters if "Xero" in (c["named_systems"] or [])]
        self.assertTrue(accounting, "expected a cluster naming Xero")
        top = accounting[0]
        self.assertGreaterEqual(top["independent_sources"], 3)
        self.assertEqual(top["role"], "Accountant")
        self.assertIn("Excel", top["named_systems"])

    def test_ecommerce_cluster_recurs(self):
        ecommerce = [
            c for c in self.clusters if set(c["named_systems"]) & {"Shopify", "WooCommerce"}
        ]
        self.assertTrue(ecommerce, "expected a cluster naming Shopify/WooCommerce")
        self.assertGreaterEqual(ecommerce[0]["independent_sources"], 3)

    def test_min_cluster_size_enforced(self):
        for cl in self.clusters:
            self.assertGreaterEqual(cl["member_count"], LIMITS["cluster"]["min_cluster_size"])

    def test_members_are_canonical_signals_only(self):
        seen = set()
        for cl in self.clusters:
            for sid in cl["member_signal_ids"]:
                self.assertNotIn(sid, seen)
                seen.add(sid)
                self.assertIsNone(self.signals_by_id[sid].get("duplicate_of"))

    def test_duplicate_travels_with_canonical(self):
        dup_clusters = [c for c in self.clusters if c["duplicate_count"]]
        self.assertTrue(dup_clusters, "expected the reposted signal to travel with its cluster")
        self.assertEqual(sum(c["duplicate_count"] for c in self.clusters), 1)

    def test_cluster_ids_are_stable(self):
        again = cluster(self.signals, LIMITS)
        self.assertEqual(
            sorted(c["cluster_id"] for c in self.clusters),
            sorted(c["cluster_id"] for c in again),
        )


class TestCrossRunRestatements(unittest.TestCase):
    """Restatements of prior-run evidence may hold a cluster together.

    They must never count towards independent sources (issue #10 semantics).
    """

    def _signal(self, signal_id, text, author, duplicate_of=None, scope=None):
        signal = {
            "signal_id": signal_id,
            "source_type": "hn",
            "source_id": signal_id,
            "source_url": f"https://example.test/{signal_id}",
            "retrieved_at": "2026-09-21T00:00:00Z",
            "published_at": "2026-09-01",
            "source_author": author,
            "target_role": "Bookkeeper",
            "pain_statement": text,
            "current_workaround": "copy and paste into Excel",
            "task": "reconcile the ledger",
            "named_systems": ["Xero", "Excel"],
            "confidence": 0.8,
        }
        if duplicate_of:
            signal["duplicate_of"] = duplicate_of
            signal["duplicate_scope"] = scope
        return signal

    def test_restatements_are_clusterable_but_not_independent(self):
        text = (
            "Every week I manually export the bank transactions from Xero to CSV "
            "and re-key the reference numbers into Excel for the reconciliation."
        )
        signals = [
            self._signal("s1", text, "alice"),
            self._signal("s2", text, "bob"),
            self._signal("s3", text, "carol"),
            # A restatement of a signal first seen in an earlier run.
            self._signal("s4", text, "dave", duplicate_of="prior-run-signal", scope="previous-run"),
        ]
        clusters = cluster(signals, LIMITS)
        self.assertEqual(len(clusters), 1)
        top = clusters[0]
        self.assertEqual(top["member_count"], 4)
        self.assertEqual(top["restated_count"], 1)
        self.assertEqual(top["independent_sources"], 3)

    def test_within_run_duplicates_still_travel_with_canonical(self):
        text = (
            "Every week I manually export the bank transactions from Xero to CSV "
            "and re-key the reference numbers into Excel for the reconciliation."
        )
        signals = [
            self._signal("s1", text, "alice"),
            self._signal("s2", text, "bob"),
            self._signal("s3", text, "carol"),
            self._signal("s4", text, "dave", duplicate_of="s1", scope="within-run"),
        ]
        clusters = cluster(signals, LIMITS)
        self.assertEqual(len(clusters), 1)
        self.assertEqual(clusters[0]["member_count"], 3)
        self.assertEqual(clusters[0]["duplicate_count"], 1)
        self.assertEqual(clusters[0]["restated_count"], 0)
        self.assertEqual(clusters[0]["independent_sources"], 3)


if __name__ == "__main__":
    unittest.main()
