import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine.extract import EXTRACTOR_VERSION, extract_many, named_systems  # noqa: E402
from painmine.fetch import load_fixture_items  # noqa: E402
from painmine.schema import validate_signal  # noqa: E402
from painmine.util import read_json  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE = os.path.join(HERE, "fixtures", "raw_items.jsonl")
LIMITS = read_json(os.path.join(HERE, "..", "limits.json"))


def load():
    items = load_fixture_items(FIXTURE)
    signals, rejects = extract_many(items, LIMITS)
    return items, signals, rejects


class TestExtract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items, cls.signals, cls.rejects = load()
        cls.by_source = {s["source_id"]: s for s in cls.signals}

    def test_all_items_produce_signals_or_rejects(self):
        self.assertEqual(len(self.items), 18)
        self.assertEqual(len(self.signals) + len(self.rejects), 18)

    def test_expected_rejects_with_reasons(self):
        reasons = {r["source_id"]: r["reason"] for r in self.rejects}
        self.assertEqual(reasons.get("hn:4004"), "vendor_marketing_only")
        self.assertEqual(reasons.get("gh:empty/empty#1"), "empty_text")
        self.assertEqual(reasons.get("hn:4005"), "no_pain_cue")
        self.assertEqual(len(self.signals), 15)

    def test_accounting_signal_fields(self):
        signal = self.by_source["hn:4001"]
        self.assertEqual(signal["target_role"], "Accountant")
        self.assertIn("Xero", signal["named_systems"])
        self.assertIn("Excel", signal["named_systems"])
        self.assertIn("manual", signal["extraction_provenance"]["cue_groups"])
        self.assertIn("time_cost", signal["extraction_provenance"]["cue_groups"])
        self.assertGreaterEqual(signal["confidence"], 0.8)
        self.assertLessEqual(len(signal["raw_excerpt"]), 600)
        self.assertTrue(signal["current_workaround"])
        self.assertEqual(signal["extraction_provenance"]["version"], EXTRACTOR_VERSION)

    def test_every_signal_validates(self):
        for signal in self.signals:
            self.assertEqual(validate_signal(signal), [], msg=signal["signal_id"])

    def test_roles_and_systems_across_fixture(self):
        self.assertEqual(self.by_source["hn:4002"]["target_role"], "Accountant")
        self.assertEqual(self.by_source["se:9001:answer:1"]["target_role"], "Bookkeeper")
        self.assertEqual(self.by_source["hn:4006"]["target_role"], "Sole trader/freelancer")
        self.assertEqual(self.by_source["hn:4008"]["target_role"], "Practice manager (clinic/health)")
        self.assertEqual(self.by_source["hn:4009"]["target_role"], "Legal professional")
        self.assertIn("Shopify", self.by_source["se:9003:answer:3"]["named_systems"])
        self.assertIn("Google Sheets", self.by_source["se:9004:answer:4"]["named_systems"])

    def test_money_and_frequency_clues(self):
        self.assertTrue(self.by_source["se:9002:answer:2"]["money_cost_clue"])
        self.assertTrue(self.by_source["hn:4001"]["frequency_clue"])

    def test_low_confidence_extraction_is_lower_than_rich_one(self):
        self.assertLess(self.by_source["se:9001:answer:1"]["confidence"], self.by_source["hn:4001"]["confidence"])

    def test_named_systems_lexicon_is_bounded(self):
        self.assertEqual(named_systems("Nothing here"), [])
        self.assertIn("Xero", named_systems("we use Xero"))


if __name__ == "__main__":
    unittest.main()
