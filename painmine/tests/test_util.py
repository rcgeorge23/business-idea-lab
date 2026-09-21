import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine.util import (  # noqa: E402
    append_jsonl,
    domain_of,
    jaccard,
    normalize_text,
    parse_date,
    read_jsonl,
    sha1_hex,
    shingles,
    slugify,
    strip_html,
    tokenize,
    truncate,
    write_jsonl,
)


class TestNormalisation(unittest.TestCase):
    def test_strip_html_removes_tags_entities_and_markdown_links(self):
        text = "<p>Export&nbsp;the <b>CSV</b> [here](https://example.com/x)</p>"
        cleaned = strip_html(text)
        self.assertNotIn("<", cleaned)
        self.assertIn("Export", cleaned)
        self.assertIn("CSV", cleaned)
        self.assertIn("here", cleaned)
        self.assertNotIn("https://example.com", cleaned)

    def test_normalize_text_lowercases_and_strips_urls_punctuation(self):
        self.assertEqual(normalize_text("Export CSV to Xero, NOW! https://x.io/a"), "export csv to xero now")

    def test_tokenize_drops_stopwords_but_keeps_pain_words(self):
        tokens = tokenize("We still do this manually for the client")
        self.assertIn("manually", tokens)
        self.assertIn("still", tokens)
        self.assertIn("client", tokens)
        self.assertNotIn("the", tokens)
        self.assertNotIn("we", tokens)

    def test_shingles_short_and_long(self):
        self.assertEqual(shingles(["a", "b"], 5), {"a b"})
        self.assertEqual(len(shingles(["a", "b", "c", "d", "e"], 5)), 1)

    def test_jaccard(self):
        self.assertEqual(jaccard({"a", "b"}, {"a", "b"}), 1.0)
        self.assertEqual(jaccard({"a"}, {"b"}), 0.0)
        self.assertEqual(jaccard(set(), {"b"}), 0.0)

    def test_truncate_adds_ellipsis(self):
        out = truncate("abcdef", 4)
        self.assertEqual(len(out), 4)
        self.assertTrue(out.endswith("\u2026"))

    def test_slugify_and_sha1(self):
        self.assertEqual(slugify("Weekly Re-key (Xero)"), "weekly-re-key-xero")
        self.assertEqual(len(sha1_hex("abc", 16)), 16)
        self.assertEqual(sha1_hex("abc"), sha1_hex("abc"))

    def test_parse_date_iso_and_epoch(self):
        self.assertEqual(parse_date("2026-08-14T09:12:00Z"), "2026-08-14T09:12:00Z")
        self.assertEqual(parse_date("2026-08-14"), "2026-08-14T00:00:00Z")
        self.assertIsNone(parse_date(""))
        self.assertIsNone(parse_date("not a date"))
        self.assertIsNotNone(parse_date(1700000000))

    def test_domain_of(self):
        self.assertEqual(domain_of("https://www.reddit.com/r/x/comments/1/"), "reddit.com")
        self.assertEqual(domain_of("nonsense"), "")


class TestJsonHelpers(unittest.TestCase):
    def test_jsonl_roundtrip_and_append(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "rows.jsonl")
            write_jsonl(path, [{"a": 1}])
            append_jsonl(path, [{"a": 2}])
            self.assertEqual(read_jsonl(path), [{"a": 1}, {"a": 2}])
            self.assertEqual(read_jsonl(os.path.join(tmp, "missing.jsonl")), [])


if __name__ == "__main__":
    unittest.main()
