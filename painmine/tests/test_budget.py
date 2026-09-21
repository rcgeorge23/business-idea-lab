import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine.budget import Budget, BudgetExceeded  # noqa: E402


def make_limits(max_requests=2, max_items_total=3, max_items_per_source=2, llm_enabled=False):
    return {
        "fetch": {
            "max_requests_per_run": max_requests,
            "max_items_total": max_items_total,
            "max_items_per_source": max_items_per_source,
            "request_timeout_seconds": 5,
            "min_seconds_between_requests": 0.0,
        },
        "llm": {
            "enabled": llm_enabled,
            "max_calls_per_run": 1,
            "max_total_tokens_per_run": 100,
            "max_usd_per_run": 0.5,
        },
        "runtime": {"max_wall_seconds": 600},
    }


class TestBudget(unittest.TestCase):
    def test_request_limit_is_hard(self):
        budget = Budget(make_limits(max_requests=1))
        self.assertTrue(budget.can_fetch())
        budget.record_request()
        self.assertFalse(budget.can_fetch())
        self.assertTrue(budget.stopped)
        self.assertIn("request limit", budget.stop_reason)
        with self.assertRaises(BudgetExceeded):
            budget.record_request()

    def test_per_source_item_cap(self):
        budget = Budget(make_limits(max_items_total=10, max_items_per_source=2))
        self.assertTrue(budget.can_take_items(1, 1))
        self.assertFalse(budget.can_take_items(2, 1))

    def test_total_item_cap_sets_stop_reason(self):
        budget = Budget(make_limits(max_items_total=2))
        budget.record_items(2)
        self.assertFalse(budget.can_take_items(0, 1))
        self.assertIn("item limit", budget.stop_reason)

    def test_llm_disabled_by_default(self):
        budget = Budget(make_limits(llm_enabled=False))
        allowed, reason = budget.can_llm(10, 10)
        self.assertFalse(allowed)
        self.assertIn("disabled", reason)

    def test_llm_call_and_usd_limits(self):
        budget = Budget(make_limits(llm_enabled=True))
        allowed, _ = budget.can_llm(10, 10)
        self.assertTrue(allowed)
        budget.record_llm(0.1, 10, 10)
        allowed, reason = budget.can_llm(10, 10)
        self.assertFalse(allowed)
        self.assertIn("call limit", reason)
        budget.record_llm(1.0, 10, 10)
        self.assertIn("USD limit", budget.stop_reason)

    def test_provider_reported_token_overrun_stops_further_calls(self):
        budget = Budget(make_limits(llm_enabled=True))
        budget.record_llm(0.1, 60, 60)
        self.assertIn("token limit", budget.stop_reason)
        allowed, reason = budget.can_llm(1, 1)
        self.assertFalse(allowed)
        self.assertIn("token limit", reason)

    def test_summary_shape(self):
        budget = Budget(make_limits())
        summary = budget.summary()
        for key in ("requests_used", "requests_limit", "elapsed_seconds", "stopped", "llm_usd"):
            self.assertIn(key, summary)


if __name__ == "__main__":
    unittest.main()
