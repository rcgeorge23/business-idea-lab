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

- Audited: sampled for the kill-#15 trigger (every 5th kill, oldest unaudited)
  on 2026-09-21; external audit request raised at
  `reviews/2026-09-21-false-negative-audit-request-wonkybox.md`.
- Worker self-audit: **kill upheld**. The kill rests on the category leader's
  reported accounts (Oddbox ~£27m revenue, widening losses, churn), which are a
  natural experiment in the delivered-box model; no delivery-density argument
  improves a small entrant's economics relative to the leader. Residual
  uncertainty: the evidence covers delivered boxes only, not pickup-only or B2B
  surplus channels.
- Reviewer / date: **kill upheld** — ChatGPT / GPT-5.6 Sol, 2026-09-21, response
  at `reviews/2026-09-21-false-negative-audit-wonkybox-chatgpt.md`. The reviewer
  agreed the kill is correct on multiple independent grounds (occupied direct
  position, weakened low-CAC assumption, persistent category-leader losses,
  joint optimism) and that a pickup/community-hub model is a materially
  different mechanism whose economics the reviewed evidence does not establish.
  The reviewer also recorded one calibration lesson: category-leader losses are
  strong negative evidence, not a universal impossibility proof, so the
  decision wording above ("a small entrant will not either") is stronger than
  the evidence warrants. The kill stands regardless.
- Adjacent seed: **not created**. The reviewer advised against promoting a
  pickup/community/B2B pivot on the current evidence, since no affirmative
  indication of attractive economics or an underserved buyer exists. Such a
  model should be captured as a fresh observation with its own provenance if
  discovery independently surfaces evidence.
- What new evidence would justify reopening: independently verifiable evidence
  that a structurally different distribution model (pickup, B2B, community hub)
  reaches positive contribution per box at small scale, with credible repeat
  purchase/retention and a plausible low-paid-acquisition route — evaluated as a
  new proposition from scratch, not by changing this historical kill.
