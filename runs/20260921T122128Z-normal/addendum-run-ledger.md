# Addendum — run ledger (issue #13) and bounded synthesis verification

Date: 2026-09-21 (same working session as `summary.md` and
`addendum-source-expansion.md`; this run directory is append-only).

## Why

The spike report's own audit found the PoC's accounting dishonest: `source_status`
labelled query attempts as "requests" (24 real HTTP requests vs 60 attempt rows),
counted item-cap and budget-prevented rows as failures, and could not separate
items returned from items accepted. Issue #13 requires distinct, reconcilable
counters across `report.json`, `run-meta.json`, Markdown and workflow summaries.

## What changed

- `painmine/budget.py`: new counters `http_responses` and `retries`, new
  `record_response()` / `record_retry()`, `fetch.max_retries_per_request`
  (default 1), and a stop when provider-reported LLM tokens exceed
  `llm.max_total_tokens_per_run`.
- `painmine/fetch.py`: bounded retries for 429/5xx and transport errors;
  per-attempt status carries `attempted`, `http_requests`, `http_responses`,
  `retries`, `items_returned`, `items_accepted` and a classified `error_kind`
  (`budget_prevented`, `per_source_item_cap`, `item_cap`, `http_error`,
  `timeout`, `transport_error`, `invalid_json`, `collector_missing`);
  `summarise_statuses()` now returns the per-source ledger and `build_ledger()`
  adds run totals plus a reconciliation against the `Budget` counters.
- `painmine/cli.py`: `run-meta.json` gains `run_ledger`; `report.json` gains
  `ledger`; `report.md` replaces the old source table with "Source ledger
  (attempted vs accepted)" and adds "Run ledger reconciliation". Old artefacts
  still render with their original counters and a "predates the run ledger"
  note.
- `painmine/limits.json`: `fetch.max_retries_per_request: 1`.
- Tests: `painmine/tests/test_ledger.py` (success, retry, timeout, non-retryable
  HTTP failure, budget prevention, per-source cap, total item cap, mid-run
  exhaustion, missing collector, totals reconciliation, offline pipeline,
  legacy report rendering); `test_budget.py` token-overrun stop; `test_llm.py`
  no-credential, credentials-file and no-spawn-when-unavailable paths.

## Verification

- `python3 -m unittest discover -s painmine/tests -t .` -> **142 tests, OK**.
- Offline fixture pipeline: `ledger.reconciliation` all true; totals
  `queries_attempted 1`, `http_requests_initiated 0`, `items_returned 18`,
  `items_accepted 18`, no cap or failure counters; `run-meta.run_ledger`
  matches `report.ledger`.
- Live local run at the 40-request cap (recorded in the session log): 85 raw
  items, 66 signals, 3 clusters, 40/40 requests, and `source_status` returned
  345 items while only 85 were accepted — the exact returned/accepted gap the
  new ledger now makes explicit.
- Bounded synthesis (owner-approved spend, model `opencode-go/deepseek-v4.1-flash`):
  two independent calls on the top cluster, both `ok`, USD 0.00581745 and
  USD 0.00572685 (total USD 0.011544 for the session), agreement on `pain`,
  disagreement recorded on `buyer` (token overlap 0.0) and `job` (0.22).

## Finding and recommendation

Provider-reported input tokens per agent call were ~36.6k (OpenCode agent
scaffolding dominates), far above the local `len // 4` estimate, so the
40,000-token per-run cap was silently exceeded at 73,330 tokens. The cap is now
enforced on provider-reported usage: further calls stop once the total is
exceeded. The verified two-call run still fits (the second call starts before
the total crosses 40k), but if dual synthesis is expected on every run the owner
should consider raising `llm.max_total_tokens_per_run` (e.g. to 120,000); the
USD 0.25 per-run cap remains the real economic bound.

**Update 2026-09-21 (owner-approved):** `llm.max_total_tokens_per_run` is now
150,000 so that dual synthesis of the top two clusters (four calls, roughly
USD 0.024 at observed rates) can complete in one run. The USD 0.25 per-run cap
and the six-call limit are unchanged.

## Boundaries

No commits, pushes, issues, pull requests, outreach, accounts or spend beyond
the owner-approved synthesis calls. No authentication bypass; Reddit remains
blocked and is reported as an access failure, not worked around.
