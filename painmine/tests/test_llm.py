import os
import sys
import unittest
from unittest import mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine.budget import Budget  # noqa: E402
from painmine.llm import (  # noqa: E402
    OpenCodeGo,
    collect_text,
    estimate_tokens,
    extract_json_blob,
    parse_event_stream,
    scan_usage,
)
from painmine.util import read_json  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
LIMITS = read_json(os.path.join(HERE, "..", "limits.json"))


class TestPureHelpers(unittest.TestCase):
    def test_estimate_tokens(self):
        self.assertGreaterEqual(estimate_tokens("abcd" * 10), 1)

    def test_scan_usage_finds_nested_max_values(self):
        acc = scan_usage({"usage": {"input_tokens": 10, "output_tokens": 4}, "total_cost": 0.02})
        self.assertEqual(acc["input"], 10)
        self.assertEqual(acc["output"], 4)
        self.assertGreaterEqual(acc["cost"], 0.0)

    def test_collect_text(self):
        self.assertEqual(collect_text({"message": {"content": "hello"}}), "hello")
        self.assertEqual(collect_text([{"text": "a"}, {"text": "b"}]), "a\nb")

    def test_extract_json_blob_from_prose(self):
        self.assertEqual(extract_json_blob('Here: {"a": 1} done'), {"a": 1})
        self.assertEqual(extract_json_blob("[1, 2]"), [1, 2])
        self.assertIsNone(extract_json_blob("no json"))
        self.assertIsNone(extract_json_blob('{"a": '))

    def test_parse_event_stream_skips_bad_lines(self):
        events = parse_event_stream('{"a":1}\nnot json\n{"b":2}')
        self.assertEqual(events, [{"a": 1}, {"b": 2}])


class TestOpenCodeGo(unittest.TestCase):
    def test_unavailable_when_llm_disabled(self):
        budget = Budget(LIMITS)
        llm = OpenCodeGo(LIMITS, budget)
        ok, reason = llm.available()
        self.assertFalse(ok)
        self.assertIn("disabled", reason)

    def test_unavailable_without_binary(self):
        limits = read_json(os.path.join(HERE, "..", "limits.json"))
        limits["llm"]["enabled"] = True
        budget = Budget(limits)
        with mock.patch.dict(os.environ, {"OPENCODE_BIN": "/definitely/not/a/binary", "OPENCODE_API_KEY": "test"}):
            llm = OpenCodeGo(limits, budget)
            ok, reason = llm.available()
        self.assertFalse(ok)
        self.assertIn("binary", reason)

    def test_auth_status_accepts_env_key(self):
        budget = Budget(LIMITS)
        llm = OpenCodeGo(LIMITS, budget)
        with mock.patch.dict(os.environ, {"OPENCODE_API_KEY": "test"}):
            ok, reason = llm.auth_status()
        self.assertTrue(ok)
        self.assertIn("env", reason)

    def test_run_fails_safely_when_unavailable(self):
        budget = Budget(LIMITS)
        llm = OpenCodeGo(LIMITS, budget)
        result = llm.run("hello")
        self.assertFalse(result["ok"])
        self.assertEqual(result["provider"], "opencode-go")
        self.assertEqual(result["model"], "opencode-go/deepseek-v4.1-flash")
        self.assertEqual(result["agent"], "painmine-extractor")
        self.assertIn("error", result)

    def test_no_fallback_provider_string_in_source(self):
        with open(os.path.join(HERE, "..", "llm.py"), encoding="utf-8") as handle:
            source = handle.read()
        for forbidden in ("github-models", "copilot", "azure-openai"):
            self.assertNotIn(forbidden, source.lower())


if __name__ == "__main__":
    unittest.main()
