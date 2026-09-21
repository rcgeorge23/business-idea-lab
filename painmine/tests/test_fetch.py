"""Collector-level tests: GitHub token handling and safe failure semantics.

Uses mocked transport only; no network calls are made from the test suite.
"""
from __future__ import annotations

import os
import sys
import unittest
import urllib.parse
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from painmine.budget import Budget  # noqa: E402
from painmine.fetch import collect, fetch_github, fetch_reddit, fetch_stack_exchange  # noqa: E402
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


class TestStackExchangeSites(unittest.TestCase):
    """Config-driven site rotation across the Stack Exchange network."""

    def _capture(self, payload):
        captured: dict = {}

        def fake(url, budget, headers=None):
            captured["url"] = url
            return payload, {"ok": True, "url": url}

        return captured, fake

    def test_site_is_used_and_item_ids_include_it(self):
        captured, fake = self._capture(
            {
                "items": [
                    {
                        "question_id": 123,
                        "title": "Re-keying exports",
                        "body": "<p>I manually copy and paste every week.</p>",
                        "owner": {"display_name": "alice"},
                        "creation_date": 1750000000,
                        "score": 2,
                        "tags": ["google-sheets"],
                    }
                ]
            }
        )
        with mock.patch("painmine.fetch.http_get_json", fake):
            items, status = fetch_stack_exchange("copy paste", 10, Budget(LIMITS), site="webapps")
        self.assertIn("site=webapps", captured["url"])
        self.assertEqual(status["site"], "webapps")
        self.assertEqual(items[0]["source_id"], "se:webapps:123:question:123")
        self.assertEqual(items[0]["url"], "https://webapps.stackexchange.com/q/123")
        self.assertEqual(items[0]["extra"]["site"], "webapps")

    def test_default_site_is_stackoverflow(self):
        captured, fake = self._capture({"items": []})
        with mock.patch("painmine.fetch.http_get_json", fake):
            fetch_stack_exchange("copy paste", 10, Budget(LIMITS))
        self.assertIn("site=stackoverflow", captured["url"])

    def test_collect_rotates_sites_without_extra_requests(self):
        captured: dict = {"urls": []}

        def fake(url, budget, headers=None):
            captured["urls"].append(url)
            return {"items": []}, {"ok": True, "url": url}

        budget = Budget(LIMITS)
        with mock.patch("painmine.fetch.http_get_json", fake):
            items, statuses = collect(
                ["q1", "q2", "q3"],
                ["stack_exchange"],
                budget,
                source_options={"stack_exchange": {"sites": ["webapps", "money"]}},
            )
        self.assertEqual(items, [])
        self.assertEqual(len(captured["urls"]), 3)
        self.assertEqual(len(captured["urls"]), len(statuses))
        sites = [
            urllib.parse.parse_qs(urllib.parse.urlparse(url).query)["site"][0]
            for url in captured["urls"]
        ]
        self.assertEqual(sites, ["webapps", "money", "webapps"])
        self.assertTrue(all(status.get("ok") for status in statuses))
        self.assertEqual([status["site"] for status in statuses], ["webapps", "money", "webapps"])

    def test_collect_without_options_uses_default_site(self):
        captured: dict = {"urls": []}

        def fake(url, budget, headers=None):
            captured["urls"].append(url)
            return {"items": []}, {"ok": True, "url": url}

        with mock.patch("painmine.fetch.http_get_json", fake):
            collect(["q1"], ["stack_exchange"], Budget(LIMITS))
        self.assertIn("site=stackoverflow", captured["urls"][0])


if __name__ == "__main__":
    unittest.main()
