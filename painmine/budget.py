"""Hard per-run budget enforcement (issue #9 Part 8).

Design rule: stop with partial results rather than exceed a limit. Every
external action (HTTP request, model call) goes through this object.
"""
from __future__ import annotations

import time
from typing import Any

from .util import utcnow


class BudgetExceeded(RuntimeError):
    """Raised when an action would exceed a hard limit."""


class Budget:
    def __init__(self, limits: dict, started: float | None = None) -> None:
        self.limits = limits or {}
        fetch = self.limits.get("fetch", {})
        llm = self.limits.get("llm", {})
        runtime = self.limits.get("runtime", {})
        self.max_requests = int(fetch.get("max_requests_per_run", 0))
        self.max_items_total = int(fetch.get("max_items_total", 0))
        self.max_items_per_source = int(fetch.get("max_items_per_source", 0))
        self.request_timeout = int(fetch.get("request_timeout_seconds", 20))
        self.min_gap = float(fetch.get("min_seconds_between_requests", 1.0))
        self.max_retries = int(fetch.get("max_retries_per_request", 0))
        self.max_llm_calls = int(llm.get("max_calls_per_run", 0))
        self.max_llm_total_tokens = int(llm.get("max_total_tokens_per_run", 0))
        self.max_usd = float(llm.get("max_usd_per_run", 0.0))
        self.llm_enabled = bool(llm.get("enabled", False))
        self.max_wall = int(runtime.get("max_wall_seconds", 420))
        self.started = started if started is not None else time.monotonic()
        self.requests = 0
        self.http_responses = 0
        self.retries = 0
        self.items = 0
        self.llm_calls = 0
        self.llm_input_tokens = 0
        self.llm_output_tokens = 0
        self.usd = 0.0
        self.stop_reason: str | None = None
        self._last_request_at = 0.0

    # ---------------------------------------------------------------- time
    def elapsed(self) -> float:
        return time.monotonic() - self.started

    def remaining_runtime(self) -> float:
        return max(0.0, self.max_wall - self.elapsed())

    def runtime_exceeded(self) -> bool:
        if self.elapsed() >= self.max_wall:
            self.stop(f"wall-clock runtime limit ({self.max_wall}s) reached")
            return True
        return False

    def sleep_between_requests(self) -> None:
        gap = time.monotonic() - self._last_request_at
        if self._last_request_at and gap < self.min_gap:
            time.sleep(self.min_gap - gap)

    # --------------------------------------------------------------- fetch
    def can_fetch(self, n: int = 1) -> bool:
        if self.stop_reason:
            return False
        if self.remaining_runtime() <= 1.0:
            self.stop("wall-clock runtime nearly exhausted")
            return False
        if self.requests + n > self.max_requests:
            self.stop(f"request limit ({self.max_requests}) reached")
            return False
        return True

    def record_request(self) -> None:
        if self.requests + 1 > self.max_requests:
            raise BudgetExceeded(f"request budget exceeded ({self.max_requests})")
        self.requests += 1
        self._last_request_at = time.monotonic()

    def record_response(self) -> None:
        """An HTTP response was received (including an HTTP error response)."""
        self.http_responses += 1

    def record_retry(self) -> None:
        self.retries += 1

    def can_take_items(self, source_count: int, n: int = 1) -> bool:
        if self.items + n > self.max_items_total:
            self.stop(f"item limit ({self.max_items_total}) reached")
            return False
        return source_count + n <= self.max_items_per_source

    def record_items(self, n: int) -> None:
        self.items += max(0, n)

    # ----------------------------------------------------------------- llm
    def can_llm(self, est_input_tokens: int, est_output_tokens: int) -> tuple[bool, str]:
        if not self.llm_enabled:
            return False, "llm disabled by limits.json (owner approval required to enable spend)"
        if self.stop_reason:
            return False, self.stop_reason
        if self.llm_calls + 1 > self.max_llm_calls:
            return False, f"model call limit ({self.max_llm_calls}) reached"
        if self.llm_input_tokens + self.llm_output_tokens + est_input_tokens + est_output_tokens > self.max_llm_total_tokens:
            return False, f"model token limit ({self.max_llm_total_tokens}) reached"
        if self.max_usd <= 0:
            return False, "model USD limit is zero"
        if self.remaining_runtime() <= 5.0:
            return False, "wall-clock runtime nearly exhausted"
        return True, ""

    def record_llm(self, cost_usd: float, input_tokens: int, output_tokens: int) -> None:
        self.llm_calls += 1
        self.llm_input_tokens += max(0, int(input_tokens))
        self.llm_output_tokens += max(0, int(output_tokens))
        self.usd += max(0.0, float(cost_usd))
        if self.llm_input_tokens + self.llm_output_tokens > self.max_llm_total_tokens:
            self.stop(
                f"model token limit ({self.max_llm_total_tokens}) exceeded by provider-reported usage"
            )
        if self.usd > self.max_usd:
            self.stop(f"USD limit (${self.max_usd:.2f}) exceeded by provider-reported cost")

    # ---------------------------------------------------------------- stop
    def stop(self, reason: str) -> None:
        if not self.stop_reason:
            self.stop_reason = reason

    @property
    def stopped(self) -> bool:
        return self.stop_reason is not None

    def summary(self) -> dict[str, Any]:
        return {
            "requests_used": self.requests,
            "requests_limit": self.max_requests,
            "http_responses_received": self.http_responses,
            "retries_used": self.retries,
            "retries_limit_per_request": self.max_retries,
            "items_collected": self.items,
            "items_limit": self.max_items_total,
            "llm_enabled": self.llm_enabled,
            "llm_calls": self.llm_calls,
            "llm_calls_limit": self.max_llm_calls,
            "llm_input_tokens": self.llm_input_tokens,
            "llm_output_tokens": self.llm_output_tokens,
            "llm_tokens_limit": self.max_llm_total_tokens,
            "llm_usd": round(self.usd, 6),
            "llm_usd_limit": self.max_usd,
            "elapsed_seconds": round(self.elapsed(), 2),
            "wall_limit_seconds": self.max_wall,
            "stopped": self.stopped,
            "stop_reason": self.stop_reason,
            "recorded_at": utcnow().isoformat().replace("+00:00", "Z"),
        }
