# Decision record: WonkyBox: local surplus-produce subscription

- **Idea:** `wonkybox`
- **Date:** 2026-09-20
- **Run:** `20260920T210550Z-normal`
- **Decision:** kill
- **State:** `discovered` -> `killed`
- **Actor:** worker

## What changed

Generated as a calibration fixture (weak candidate expected to die on hard filters). Desk research found a funded incumbent (Oddbox) that has raised ~£30m and is still loss-making at ~£27m revenue, with operating losses widening 98.7% in FY2025 and publicly cited churn. The category's unit economics and the presence of a second operator (Wonky Veg Boxes) killed the idea before any experiment.

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | pass | Consumers pay directly; frequent purchase. |
| painful_frequent_or_budgeted | pass | Weekly grocery is frequent; food-waste reduction is a preference. |
| non_paid_distribution | fail | DTC grocery depends on paid acquisition. |
| defensible_wedge | fail | Oddbox and Wonky Veg Boxes occupy the position. |
| no_network_effects_needed | pass | Single-customer value. |
| plausible_margins | fail | Category leader loss-making at scale. |
| acceptable_risk | pass | Standard food-handling/packaging. |
| cheap_disconfirming_test | pass | Single-city test is cheap to start. |
| not_all_optimistic | fail | Requires favourible CAC, retention and delivery density together. |

## Evidence considered

- `evidence/wonkybox/2026-09-20-oddbox-financials.md` (decisive against; credible secondary, four years of reported accounts).
- `evidence/wonkybox/2026-09-20-incumbent-box-schemes.md` (cuts against; incumbent pricing and a second operator).

## Scores

Weighted total **36.8** against threshold **65** (meets threshold: false). Details in `ideas/wonkybox/scorecard.json`. Gating dimensions: problem 2/5, buyer 2/5, evidence strength 3/5.

## Review

No review triggered or required: hard-filter rejection, scorecard well below threshold. Review status remains `not-required`.

## Reasons if killed

The incumbent's filings function as a natural experiment: if a well-capitalised leader with £27m of revenue cannot make surplus-produce delivery profitable, a small entrant will not either, and delivery density ("local") makes economics worse rather than better. What would have changed the decision: evidence of a structurally different model — e.g. pickup-only B2B or community-hub distribution with demonstrated positive contribution per box.

## False-negative audit (killed ideas only)

- Audited: no — kill #2 of the run; the fifth-kill audit trigger has not been reached.
- Reviewer / date: n/a
- Verdict: n/a
- What new evidence would justify reopening: audited unit economics showing a non-delivery model reaches positive contribution per box at small scale.
