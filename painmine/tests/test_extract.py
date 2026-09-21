import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine.extract import EXTRACTOR_VERSION, extract_many, extract_signal, named_systems  # noqa: E402
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

    def test_paid_workaround_is_a_strong_cue(self):
        """Spend evidence must extract even without a manual/time cue."""
        item = {
            "source_type": "hn",
            "source_id": "hn:paid-1",
            "url": "https://example.test/paid-1",
            "title": "Paying for data entry",
            "text": (
                "We pay a virtual assistant to keep our supplier records up to date "
                "and it costs us a fortune every single month."
            ),
            "author": "paid_pat",
            "published_at": "2026-09-01",
        }
        signal, reason = extract_signal(item, LIMITS)
        self.assertEqual(reason, "")
        self.assertIsNotNone(signal)
        self.assertIn("paid_workaround", signal["extraction_provenance"]["cue_groups"])

    def test_paid_workaround_does_not_rescue_vendor_marketing(self):
        item = {
            "source_type": "hn",
            "source_id": "hn:paid-2",
            "url": "https://example.test/paid-2",
            "title": "Our platform",
            "text": (
                "Our platform helps teams reconcile supplier records every week. "
                "Book a demo. Request a demo. We pay attention to detail and "
                "outsourced teams love us."
            ),
            "author": "vendor",
            "published_at": "2026-09-01",
        }
        signal, reason = extract_signal(item, LIMITS)
        self.assertIsNone(signal)
        self.assertEqual(reason, "vendor_marketing_only")

    def test_auto_generated_digest_post_is_rejected(self):
        """Digest/roundup posts are machine-written summaries, not buyer pain."""
        item = {
            "source_type": "github_issues",
            "source_id": "gh:agents-radar#1",
            "url": "https://example.test/agents-radar/1",
            "title": "AI CLI Tools Digest",
            "text": (
                "AI CLI Tools Digest\n"
                "Generated: 2026-09-20\n"
                "Tools covered: 12\n"
                "Hot Issues (Top 10 by Community Signal)\n"
                "Releases *No new releases in the last 24 hours*\n"
                "Developer Pain Points | Pain point | Frequency / impact | Typical workaround\n"
                "We manually copy and paste data between tools every week."
            ),
            "author": "agents-radar-bot",
            "published_at": "2026-09-20",
        }
        signal, reason = extract_signal(item, LIMITS)
        self.assertIsNone(signal)
        self.assertEqual(reason, "digest_post")

    def test_ordinary_post_is_not_treated_as_a_digest(self):
        item = {
            "source_type": "hn",
            "source_id": "hn:not-digest",
            "url": "https://example.test/not-digest",
            "title": "Weekly reconciliation",
            "text": (
                "Every week I manually export the bank transactions from Xero to CSV "
                "and re-key the reference numbers into Excel for the reconciliation."
            ),
            "author": "ledger_lucy",
            "published_at": "2026-09-01",
        }
        signal, reason = extract_signal(item, LIMITS)
        self.assertEqual(reason, "")
        self.assertIsNotNone(signal)


if __name__ == "__main__":
    unittest.main()
