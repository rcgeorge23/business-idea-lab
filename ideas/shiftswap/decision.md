# Decision record: ShiftSwap: last-minute shift cover for UK hospitality

- **Idea:** `shiftswap`
- **Date:** 2026-09-20
- **Run:** `20260920T210550Z-normal`
- **Decision:** kill
- **State:** `discovered` -> `killed`
- **Actor:** worker

## What changed

Generated as a calibration fixture (a weak candidate expected to die on hard filters). Desk research confirmed the labour-market pain is real (ONS/UKHospitality: ~89,000 hospitality job losses since Oct 2024, elevated vacancies, labour costs ~35% of revenue) but found the proposed function to be a commodity: every surveyed low-cost UK rota product already bundles self-service shift swaps, several at £0–£10/mo. Killed before any experiment was justified.

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | pass | Venue owner/GM controls a small software budget. |
| painful_frequent_or_budgeted | pass | Uncovered shifts are frequent and operationally painful. |
| non_paid_distribution | fail | Two-sided (venue + staff) adoption; no non-paid route to critical mass. |
| defensible_wedge | fail | Incumbents bundle self-service swaps at low/no cost. |
| no_network_effects_needed | fail | Cover value depends on participating-staff density. |
| plausible_margins | fail | Advertised alternatives at £0/£9/£10/£49 per month. |
| acceptable_risk | pass | Standard workforce-data handling. |
| cheap_disconfirming_test | pass | A small concierge test is cheap. |
| not_all_optimistic | fail | Requires simultaneous venue and staff adoption plus low CAC. |

## Evidence considered

- `evidence/shiftswap/2026-09-20-uk-hospitality-labour-market.md` (supports the problem; credible secondary ONS-derived).
- `evidence/shiftswap/2026-09-20-incumbent-rota-software.md` (cuts against the idea; vendor pages showing feature parity and low prices).

## Scores

Weighted total **45.3** against threshold **65** (meets threshold: false). Details in `ideas/shiftswap/scorecard.json`. Gating dimensions: problem 3/5, buyer 2/5, evidence strength 3/5.

## Review

No review triggered or required: this is a hard-filter rejection with a scorecard far below threshold, which `method/review-policy.md` lists under "no review needed". Review status remains `not-required`.

## Reasons if killed

The distinction between "painful problem" and "sellable product" is the whole issue: uncovered shifts hurt, but the function is already given away inside tools venues may already own, and the value needs two-sided density no small entrant can bootstrap for free. What would have changed the decision: evidence that venues actively pay a premium above existing rota tools specifically for cover, or a distribution channel that reaches staff directly at zero cost.

## False-negative audit (killed ideas only)

- Audited: yes — worker self-audit on 2026-09-21, after `packproof` became the fifth killed idea and triggered `method/review-policy.md` trigger 6 (oldest un-audited kill). External confirmation requested in `reviews/2026-09-21-false-negative-audit-request.md`.
- Reviewer / date: worker, 2026-09-21 (external review pending).
- Verdict: kill upheld. The sourced evidence shows self-service shift swaps are bundled into low-cost rota products, so the idea fails `defensible_wedge`, `no_network_effects_needed` and `plausible_margins` independently of whether the labour-market pain is real.
- Residual uncertainty: no direct venue-side research was done on paying a premium specifically for cover.
- What new evidence would justify reopening: an independent survey showing venues pay extra for cover beyond their rota tool, or a novel non-paid staff-side channel.
