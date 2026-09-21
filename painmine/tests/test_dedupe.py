import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine.dedupe import dedupe, independence_key, independent_count  # noqa: E402
from painmine.extract import extract_many  # noqa: E402
from painmine.fetch import load_fixture_items  # noqa: E402
from painmine.util import read_json  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE = os.path.join(HERE, "fixtures", "raw_items.jsonl")
LIMITS = read_json(os.path.join(HERE, "..", "limits.json"))


def fixture_signals():
    signals, _ = extract_many(load_fixture_items(FIXTURE), LIMITS)
    return signals


def simple_signal(sid, statement, author="a", source_type="hn_algolia"):
    return {
        "signal_id": sid,
        "source_type": source_type,
        "source_id": sid,
        "pain_statement": statement,
        "current_workaround": "",
        "task": statement,
        "confidence": 0.5,
        "source_author": author,
    }


class TestDedupe(unittest.TestCase):
    def test_repost_is_collapsed_and_not_counted_twice(self):
        signals = fixture_signals()
        result = dedupe(signals)
        self.assertEqual(result["stats"]["duplicates_removed"], 1)
        duplicate_ids = set(result["duplicate_of"])
        self.assertTrue({"hn:4001", "hn:4003"} & duplicate_ids or duplicate_ids)
        reps = [s for s in signals if s["source_id"] in ("hn:4001", "hn:4003")]
        self.assertEqual(len(reps), 2)
        self.assertEqual(sum(1 for s in reps if s.get("duplicate_of")), 1)
        self.assertEqual(result["stats"]["input_signals"] - result["stats"]["duplicates_removed"], len(result["canonicals"]))

    def test_identical_text_with_same_author_counts_once(self):
        a = simple_signal("s1", "We still copy the CSV by hand every week into Excel", author="same_person")
        b = simple_signal("s2", "We still copy the CSV by hand every week into Excel", author="same_person", source_type="stack_exchange")
        result = dedupe([a, b])
        self.assertEqual(result["stats"]["duplicates_removed"], 1)
        self.assertEqual(independent_count(result["canonicals"]), 1)

    def test_independence_key_uses_author(self):
        self.assertEqual(independence_key(simple_signal("s1", "x", author="Alice")), ("hn_algolia", "alice"))
        self.assertEqual(independence_key(simple_signal("s1", "x", author="")), ("hn_algolia", "s1"))

    def test_distinct_statements_are_not_merged(self):
        signals = [
            simple_signal("s1", "Manual export from Xero to Excel takes hours every week"),
            simple_signal("s2", "Our clinic types appointment reminders into the practice system by hand"),
        ]
        result = dedupe(signals)
        self.assertEqual(result["stats"]["duplicates_removed"], 0)
        self.assertEqual(len(result["canonicals"]), 2)

    def test_duplicate_ratio_reported(self):
        signals = fixture_signals()
        stats = dedupe(signals)["stats"]
        self.assertGreater(stats["duplicate_ratio"], 0)
        self.assertLess(stats["duplicate_ratio"], 0.5)


if __name__ == "__main__":
    unittest.main()
