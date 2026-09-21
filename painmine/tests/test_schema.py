import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine.schema import SCHEMA_VERSION, make_signal, new_signal_id, validate_signal  # noqa: E402


def full_signal(**over):
    kwargs = dict(
        source_type="hn_algolia",
        source_id="hn:1",
        source_url="https://news.ycombinator.com/item?id=1",
        retrieved_at="2026-09-21T00:00:00Z",
        pain_statement="I still export the bank transactions to CSV and re-key them into Excel every month.",
        raw_excerpt="I still export the bank transactions to CSV and re-key them into Excel every month.",
        confidence=0.5,
    )
    kwargs.update(over)
    return make_signal(**kwargs)


class TestSchema(unittest.TestCase):
    def test_valid_signal_has_no_problems(self):
        self.assertEqual(validate_signal(full_signal()), [])

    def test_signal_id_is_deterministic(self):
        self.assertEqual(new_signal_id("hn", "1", "abc"), new_signal_id("hn", "1", "abc"))
        self.assertNotEqual(new_signal_id("hn", "1", "abc"), new_signal_id("hn", "2", "abc"))

    def test_missing_required_field_is_reported(self):
        signal = full_signal()
        signal["source_url"] = ""
        problems = validate_signal(signal)
        self.assertTrue(any("source_url" in p for p in problems))

    def test_confidence_range(self):
        self.assertTrue(any("confidence" in p for p in validate_signal(full_signal(confidence=2.0))))

    def test_named_systems_must_be_a_list_and_is_sorted_deduped(self):
        signal = full_signal(named_systems=["Xero", "Excel", "Xero"])
        self.assertEqual(signal["named_systems"], ["Excel", "Xero"])
        signal["named_systems"] = "Xero"
        self.assertTrue(any("named_systems" in p for p in validate_signal(signal)))

    def test_provenance_required_fields(self):
        signal = full_signal()
        signal["extraction_provenance"] = {"cue_groups": []}
        self.assertTrue(any("extraction_provenance" in p for p in validate_signal(signal)))

    def test_length_limits_enforced_by_construction_and_validation(self):
        signal = full_signal(pain_statement="x " * 500, raw_excerpt="y " * 500)
        self.assertLessEqual(len(signal["pain_statement"]), 400)
        self.assertLessEqual(len(signal["raw_excerpt"]), 600)

    def test_default_confidence_is_zero_and_schema_version_present(self):
        signal = make_signal(source_type="hn", source_id="1", pain_statement="x", raw_excerpt="x")
        self.assertEqual(signal["confidence"], 0.0)
        self.assertEqual(SCHEMA_VERSION, "0.1.0")


if __name__ == "__main__":
    unittest.main()
