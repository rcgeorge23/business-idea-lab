"""Run-ledger tests (issue #13): honest, reconcilable counters.

All transport is mocked; no network calls are made from the test suite.
"""
from __future__ import annotations

import copy
import io
import json
import os
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from painmine import cli  # noqa: E402
from painmine.budget import Budget  # noqa: E402
from painmine.fetch import build_ledger, collect, http_get_json, summarise_statuses  # noqa: E402
from painmine.util import read_json  # noqa: E402

LIMITS = read_json(ROOT / "painmine" / "limits.json")
FIXTURE = str(ROOT / "painmine" / "tests" / "fixtures" / "raw_items.jsonl")


def fast_limits(**fetch_overrides):
    """A limits copy with no inter-request sleep, for deterministic tests."""
    limits = copy.deepcopy(LIMITS)
    limits["fetch"]["min_seconds_between_requests"] = 0.0
    limits["fetch"].update(fetch_overrides)
    return limits


class FakeResponse:
    def __init__(self, payload, status=200):
        self._payload = payload.encode("utf-8") if isinstance(payload, str) else payload
        self.status = status

    def read(self):
        return self._payload

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def reconciliation_checks(recon):
    """The boolean reconciliation checks (the dict also carries counters)."""
    return {key: value for key, value in recon.items() if isinstance(value, bool)}


def http_error(code):
    return urllib.error.HTTPError(
        "https://example.test/api", code, "err", {}, io.BytesIO(b"error body")
    )


class TestHttpLedger(unittest.TestCase):
    def test_success_counts_one_request_and_one_response(self):
        budget = Budget(fast_limits())
        with mock.patch(
            "painmine.fetch.urllib.request.urlopen", return_value=FakeResponse('{"ok": true}')
        ):
            data, status = http_get_json("https://example.test/api", budget)
        self.assertEqual(data, {"ok": True})
        self.assertTrue(status["ok"])
        self.assertIsNone(status["error_kind"])
        self.assertTrue(status["attempted"])
        self.assertEqual(status["http_requests"], 1)
        self.assertEqual(status["http_responses"], 1)
        self.assertEqual(status["retries"], 0)
        self.assertEqual(budget.requests, 1)
        self.assertEqual(budget.http_responses, 1)
        self.assertEqual(budget.retries, 0)

    def test_retryable_http_error_is_retried_then_succeeds(self):
        budget = Budget(fast_limits())
        with mock.patch(
            "painmine.fetch.urllib.request.urlopen",
            side_effect=[http_error(503), FakeResponse('{"ok": true}')],
        ):
            data, status = http_get_json("https://example.test/api", budget)
        self.assertEqual(data, {"ok": True})
        self.assertTrue(status["ok"])
        self.assertEqual(status["retries"], 1)
        self.assertEqual(budget.requests, 2)
        self.assertEqual(budget.http_responses, 2)
        self.assertEqual(budget.retries, 1)

    def test_timeout_is_retried_then_fails_safely(self):
        budget = Budget(fast_limits())
        with mock.patch(
            "painmine.fetch.urllib.request.urlopen", side_effect=TimeoutError("timed out")
        ):
            data, status = http_get_json("https://example.test/api", budget)
        self.assertIsNone(data)
        self.assertFalse(status["ok"])
        self.assertEqual(status["error_kind"], "timeout")
        self.assertTrue(status["attempted"])
        self.assertEqual(status["retries"], 1)
        self.assertEqual(budget.requests, 2)
        self.assertEqual(budget.http_responses, 0)

    def test_non_retryable_http_failure_is_not_retried(self):
        budget = Budget(fast_limits())
        with mock.patch(
            "painmine.fetch.urllib.request.urlopen", side_effect=[http_error(404)]
        ):
            data, status = http_get_json("https://example.test/api", budget)
        self.assertIsNone(data)
        self.assertFalse(status["ok"])
        self.assertEqual(status["error_kind"], "http_error")
        self.assertEqual(status["http_status"], 404)
        self.assertEqual(status["retries"], 0)
        self.assertEqual(budget.requests, 1)
        self.assertEqual(budget.http_responses, 1)

    def test_budget_exhaustion_prevents_the_request(self):
        budget = Budget(fast_limits(max_requests_per_run=1))
        budget.record_request()
        with mock.patch("painmine.fetch.urllib.request.urlopen") as urlopen:
            data, status = http_get_json("https://example.test/api", budget)
        urlopen.assert_not_called()
        self.assertIsNone(data)
        self.assertFalse(status["ok"])
        self.assertEqual(status["error_kind"], "budget_prevented")
        self.assertFalse(status["attempted"])
        self.assertEqual(budget.requests, 1)


def fake_collector(items_per_call=1, record_request=True):
    """A deterministic stand-in collector used to exercise collect()."""

    def collector(query, cap, budget):
        if record_request and not budget.can_fetch():
            return [], {
                "ok": False,
                "error": f"budget stopped: {budget.stop_reason}",
                "error_kind": "budget_prevented",
                "attempted": False,
            }
        if record_request:
            budget.record_request()
        count = min(cap, items_per_call)
        items = [
            {
                "source_type": "hn",
                "source_id": f"hn:{query}:{index}",
                "url": f"https://example.test/{query}/{index}",
                "text": "manual re-keying pain",
            }
            for index in range(count)
        ]
        return items, {
            "ok": True,
            "items": len(items),
            "attempted": True,
            "http_requests": 1,
            "http_responses": 1,
            "retries": 0,
        }

    return collector


class TestCollectLedger(unittest.TestCase):
    def test_per_source_item_cap_is_recorded_not_a_failure(self):
        limits = fast_limits(max_items_per_source=2, max_items_total=100)
        budget = Budget(limits)
        with mock.patch.dict(
            "painmine.fetch.COLLECTORS", {"test_source": fake_collector(items_per_call=2)}
        ):
            items, statuses = collect(
                ["a", "b", "c"], ["test_source"], budget, per_source_cap=2
            )
        self.assertEqual(len(items), 2)
        summary = summarise_statuses(statuses)["test_source"]
        self.assertEqual(summary["queries_attempted"], 1)
        self.assertEqual(summary["per_source_item_cap_reached"], 2)
        self.assertEqual(summary["source_access_failures"], 0)
        self.assertEqual(summary["items_accepted"], 2)
        self.assertEqual(summary["http_requests_initiated"], 1)
        self.assertEqual(budget.items, 2)

    def test_total_item_cap_is_recorded_not_a_failure(self):
        limits = fast_limits(max_items_total=1, max_items_per_source=50)
        budget = Budget(limits)
        with mock.patch.dict(
            "painmine.fetch.COLLECTORS", {"test_source": fake_collector(items_per_call=2)}
        ):
            items, statuses = collect(["a", "b"], ["test_source"], budget, per_source_cap=50)
        self.assertEqual(len(items), 1)
        self.assertEqual(budget.items, 1)
        summary = summarise_statuses(statuses)["test_source"]
        self.assertEqual(summary["total_item_cap_reached"], 1)
        self.assertEqual(summary["source_access_failures"], 0)
        self.assertEqual(summary["items_accepted"], 1)

    def test_mid_run_budget_exhaustion_is_prevented_not_failed(self):
        limits = fast_limits(max_requests_per_run=1)
        budget = Budget(limits)
        with mock.patch.dict(
            "painmine.fetch.COLLECTORS", {"test_source": fake_collector(items_per_call=1)}
        ):
            items, statuses = collect(["a", "b"], ["test_source"], budget, per_source_cap=50)
        self.assertEqual(len(items), 1)
        summary = summarise_statuses(statuses)["test_source"]
        self.assertEqual(summary["queries_attempted"], 1)
        self.assertEqual(summary["queries_skipped"], 1)
        self.assertEqual(summary["requests_prevented_budget"], 1)
        self.assertEqual(summary["source_access_failures"], 0)
        self.assertEqual(summary["http_requests_initiated"], 1)

    def test_missing_collector_is_a_source_access_failure(self):
        budget = Budget(fast_limits())
        items, statuses = collect(["a"], ["not_implemented"], budget)
        self.assertEqual(items, [])
        summary = summarise_statuses(statuses)["not_implemented"]
        self.assertEqual(summary["source_access_failures"], 1)
        self.assertEqual(summary["queries_attempted"], 0)

    def test_ledger_totals_reconcile_with_budget(self):
        statuses = [
            {
                "source_id": "a",
                "ok": True,
                "attempted": True,
                "http_requests": 2,
                "http_responses": 2,
                "retries": 1,
                "items_returned": 5,
                "items_accepted": 3,
            },
            {
                "source_id": "a",
                "ok": False,
                "attempted": False,
                "error_kind": "budget_prevented",
                "http_requests": 0,
                "http_responses": 0,
                "retries": 0,
                "items_returned": 0,
                "items_accepted": 0,
            },
            {
                "source_id": "b",
                "ok": False,
                "attempted": True,
                "error_kind": "http_error",
                "http_requests": 1,
                "http_responses": 1,
                "retries": 0,
                "items_returned": 0,
                "items_accepted": 0,
            },
            {
                "source_id": "c",
                "ok": False,
                "attempted": True,
                "error_kind": "per_source_item_cap",
                "http_requests": 0,
                "http_responses": 0,
                "retries": 0,
                "items_returned": 0,
                "items_accepted": 0,
            },
        ]
        budget = Budget(LIMITS)
        budget.requests = 3
        budget.http_responses = 3
        budget.retries = 1
        budget.items = 3
        ledger = build_ledger(statuses, budget)
        totals = ledger["totals"]
        self.assertEqual(totals["queries_attempted"], 3)
        self.assertEqual(totals["queries_skipped"], 1)
        self.assertEqual(totals["http_requests_initiated"], 3)
        self.assertEqual(totals["http_responses_received"], 3)
        self.assertEqual(totals["retries"], 1)
        self.assertEqual(totals["items_returned"], 5)
        self.assertEqual(totals["items_accepted"], 3)
        self.assertEqual(totals["per_source_item_cap_reached"], 1)
        self.assertEqual(totals["requests_prevented_budget"], 1)
        self.assertEqual(totals["source_access_failures"], 1)
        self.assertTrue(all(reconciliation_checks(ledger["reconciliation"]).values()))


class TestPipelineLedger(unittest.TestCase):
    def test_offline_fixture_report_reconciles(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "run")
            rc = cli.main(
                [
                    "pipeline",
                    "--offline-fixture",
                    FIXTURE,
                    "--out",
                    out,
                    "--run-id",
                    "pm-ledger-offline",
                ]
            )
            self.assertEqual(rc, 0)
            with open(os.path.join(out, "report.json"), "r", encoding="utf-8") as handle:
                report = json.load(handle)
            ledger = report["ledger"]
            self.assertTrue(all(reconciliation_checks(ledger["reconciliation"]).values()))
            self.assertEqual(ledger["reconciliation"]["budget_requests_used"], 0)
            self.assertEqual(ledger["reconciliation"]["budget_items_collected"], 18)
            self.assertEqual(ledger["totals"]["http_requests_initiated"], 0)
            self.assertEqual(ledger["totals"]["items_accepted"], 18)
            fixture = report["source_status"]["fixture"]
            self.assertEqual(fixture["items_returned"], 18)
            self.assertEqual(fixture["items_accepted"], 18)
            self.assertEqual(fixture["source_access_failures"], 0)
            with open(os.path.join(out, "run-meta.json"), "r", encoding="utf-8") as handle:
                meta = json.load(handle)
            self.assertTrue(all(reconciliation_checks(meta["run_ledger"]["reconciliation"]).values()))
            self.assertEqual(meta["source_status"], report["source_status"])
            with open(os.path.join(out, "report.md"), "r", encoding="utf-8") as handle:
                markdown = handle.read()
            self.assertIn("## Source ledger (attempted vs accepted)", markdown)
            self.assertIn("## Run ledger reconciliation", markdown)

    def test_legacy_report_still_renders(self):
        legacy = {
            "meta": {},
            "budget": {},
            "volumes": {},
            "source_status": {
                "hn_algolia": {
                    "requests": 15,
                    "ok_requests": 15,
                    "failed_requests": 0,
                    "items": 98,
                    "errors": [],
                }
            },
            "top_clusters": [],
            "quality_checks": {},
            "preliminary_recommendation": {"recommendation": "ITERATE", "note": ""},
        }
        markdown = cli.render_report_markdown(legacy)
        self.assertIn("hn_algolia", markdown)
        self.assertIn("predates the run ledger", markdown)


if __name__ == "__main__":
    unittest.main()
