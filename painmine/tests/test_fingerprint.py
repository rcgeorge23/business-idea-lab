import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine import fingerprint  # noqa: E402


ORIGINAL = (
    "I spend three hours every week exporting invoices from Xero into CSV and "
    "re-keying them into Excel for the bookkeeping reconciliation."
)
MIRROR = (
    "I spend three hours every week exporting invoices from Xero into CSV and "
    "re-keying them into Excel for the bookkeeping reconciliation, and it is still painful."
)
UNRELATED = (
    "The warehouse team types Amazon orders into the inventory spreadsheet every "
    "morning before the courier arrives."
)


def signal(text, source_type="hn", source_id="1", author="alice"):
    return {
        "signal_id": f"{source_type}:{source_id}",
        "source_type": source_type,
        "source_id": source_id,
        "source_author": author,
        "pain_statement": text,
        "current_workaround": "",
        "task": "",
    }


class TestFingerprint(unittest.TestCase):
    def test_exact_match_is_independent_of_source_and_url(self):
        left = fingerprint.make_fingerprint(signal(ORIGINAL, "hn", "1", "alice"))
        right = fingerprint.make_fingerprint(signal(ORIGINAL, "reddit", "999", "bob"))
        self.assertEqual(left["exact"], right["exact"])
        self.assertEqual(fingerprint.compare(left, right), ("exact", 1.0))

    def test_exact_match_ignores_whitespace_and_url_noise(self):
        left = fingerprint.make_fingerprint(signal(ORIGINAL))
        noisy = ORIGINAL.replace(" ", "   ") + "  https://example.com/mirror"
        right = fingerprint.make_fingerprint(signal(noisy))
        self.assertEqual(left["exact"], right["exact"])

    def test_mirror_is_a_near_match(self):
        left = fingerprint.make_fingerprint(signal(ORIGINAL))
        right = fingerprint.make_fingerprint(signal(MIRROR))
        match_type, similarity = fingerprint.compare(left, right)
        self.assertEqual(match_type, "near")
        self.assertGreaterEqual(similarity, fingerprint.NEAR_DUPLICATE_THRESHOLD)

    def test_unrelated_text_is_not_a_match(self):
        left = fingerprint.make_fingerprint(signal(ORIGINAL))
        right = fingerprint.make_fingerprint(signal(UNRELATED))
        match_type, similarity = fingerprint.compare(left, right)
        self.assertIsNone(match_type)
        self.assertLess(similarity, fingerprint.NEAR_DUPLICATE_THRESHOLD)

    def test_signature_is_deterministic_and_order_independent(self):
        first = fingerprint.minhash_signature(ORIGINAL)
        second = fingerprint.minhash_signature(ORIGINAL)
        self.assertEqual(first, second)
        self.assertTrue(fingerprint.is_valid_signature(first))
        self.assertEqual(fingerprint.estimated_jaccard(first, second), 1.0)

    def test_empty_text_yields_valid_zero_signature(self):
        signature = fingerprint.minhash_signature("")
        self.assertTrue(fingerprint.is_valid_signature(signature))
        self.assertEqual(signature, [0] * fingerprint.PERMUTATIONS)
        self.assertEqual(fingerprint.band_keys(signature), [])

    def test_invalid_signature_is_rejected_without_crashing(self):
        self.assertFalse(fingerprint.is_valid_signature([1, 2, 3]))
        self.assertFalse(fingerprint.is_valid_signature("nope"))
        self.assertEqual(fingerprint.estimated_jaccard([1, 2, 3], [1, 2, 3]), 0.0)
        self.assertEqual(fingerprint.band_keys(None), [])

    def test_band_keys_are_bounded_and_stable(self):
        signature = fingerprint.minhash_signature(ORIGINAL)
        keys = fingerprint.band_keys(signature)
        self.assertEqual(len(keys), fingerprint.BANDS)
        self.assertEqual(keys, fingerprint.band_keys(signature))
        self.assertTrue(all(len(key) == fingerprint.ROWS_PER_BAND for key in keys))

    def test_signal_text_matches_dedupe_basis(self):
        record = signal(ORIGINAL)
        record["current_workaround"] = "copy and paste"
        record["task"] = "monthly reconciliation"
        text = fingerprint.signal_text(record)
        self.assertIn("copy and paste", text)
        self.assertIn("monthly reconciliation", text)


if __name__ == "__main__":
    unittest.main()
