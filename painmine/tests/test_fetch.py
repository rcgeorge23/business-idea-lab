"""Collector-level tests: GitHub token handling and safe failure semantics.

Uses mocked transport only; no network calls are made from the test suite.
"""
from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from painmine.budget import Budget  # noqa: E402
from painmine.fetch import fetch_github, fetch_reddit  # noqa: E402
from painmine.util import read_json  # noqa: E402

LIMITS = read_json(ROOT / "painmine" / "limits.json")


class TestGithubAuth(unittest.TestCase):
    def _run(self, env):
        captured: dict = {}

        def fake(url, budget, headers=None):
            captured["url"] = url
            captured["headers"] = headers or {}
            return None, {"ok": False, "error": "test-double"}

        budget = Budget(LIMITS)
        with mock.patch("painmine.fetch.http_get_json", fake):
            with mock.patch.dict(os.environ, env):
                fetch_github("manual export", 10, budget)
        return captured

    def test_token_added_when_present(self):
        captured = self._run({"GITHUB_TOKEN": "tok-123", "GH_TOKEN": ""})
        self.assertEqual(captured["headers"].get("Authorization"), "Bearer tok-123")

    def test_gh_token_used_as_fallback(self):
        captured = self._run({"GITHUB_TOKEN": "", "GH_TOKEN": "alt-456"})
        self.assertEqual(captured["headers"].get("Authorization"), "Bearer alt-456")

    def test_no_token_no_authorization_header(self):
        captured = self._run({"GITHUB_TOKEN": "", "GH_TOKEN": ""})
        self.assertNotIn("Authorization", captured["headers"])


class TestSafeFailure(unittest.TestCase):
    def test_reddit_failure_returns_no_items_with_status(self):
        def fake(url, budget, headers=None):
            return None, {"ok": False, "status": 403, "error": "HTTP 403"}

        with mock.patch("painmine.fetch.http_get_json", fake):
            items, status = fetch_reddit("we still do this manually", 10, Budget(LIMITS))
        self.assertEqual(items, [])
        self.assertFalse(status["ok"])
        self.assertEqual(status["source_id"], "reddit_public_json")


if __name__ == "__main__":
    unittest.main()
