# Decision record — `bikpayroll`

- **Idea:** `bikpayroll`
- **Date:** 2026-09-21
- **Run:** `20260921T081223Z-normal` (method 1.3.0)
- **Decision:** hold (park)
- **State:** `discovered` → `desk-screened`
- **Actor:** worker (idea-worker)

## What changed

A fresh discontinuity hunt found a dated, primary-evidenced mandate — mandatory payrolling of benefits in kind from 6 April 2027 (HMRC policy paper 2026-07-13; SI 2026/189 made 2026-09-14) — and a candidate was created around its second-order operational seam: collecting, validating and reconciling third-party benefit data into each pay run. It was novelty-checked before deep research, then adversarially reviewed.

## Why now? (discovery gate)

Why-now strength: **strong**. Changed date 2026-06-24 (policy confirmation/update window; SI 2026-09-14). Primary sources dated and registered in `evidence/bikpayroll/2026-09-21-mandatory-bik-payrolling.md`. Provenance: **fresh**.

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | unknown | Buyer hypothesis (SME finance/payroll; bureau principal) is identifiable but no budget owner or comparable spend is evidenced. `resolve_via`: bureau/employer interviews in escalation experiment. |
| painful_frequent_or_budgeted | unknown | Obligation is evidenced and recurring (monthly payroll) but buyer-felt pain and willingness to pay are not. `resolve_via`: willingness-to-pay test (escalation). |
| non_paid_distribution | unknown | Bureau/accountant channels plausible; no prospects or channel tests. `resolve_via`: channel test after capability scan. |
| defensible_wedge | unknown | No cited incumbent supplies/absorbs provider BiK data, so a fail cannot be affirmed; but the seam is decade-old under voluntary payrolling and vendors are building adjacent RTI fields. `resolve_via`: `bikpayroll-incumbent-capability` scan. |
| no_network_effects_needed | pass | Single-sided tool; value does not require other users. Cites `evidence/bikpayroll/2026-09-21-mandatory-bik-payrolling.md`. |
| plausible_margins | unknown | Software margin only if provider ingestion is automated; services burden if manual. `resolve_via`: pilot/build estimate. |
| acceptable_risk | unknown | Handles payroll and medical-benefit personal data; DPIA/security needed. No regulated activity identified. `resolve_via`: DPIA before pilot. |
| cheap_disconfirming_test | pass | £0, ≤6h, ≤3d desk scan with pre-fixed kill thresholds. Cites `experiments/bikpayroll-incumbent-capability/plan.md` and evidence file. |
| not_all_optimistic | unknown | Viability currently rests on several unproven assumptions (providers do not self-supply; vendors do not bundle; buyers pay; channel works). `resolve_via`: capability scan then WTP test. |

No filter recorded `fail`.

## Evidence considered

- `evidence/bikpayroll/2026-09-21-mandatory-bik-payrolling.md` (HMRC, SI 2026/189, ATT, CIOT, ICAEW, Sage, ADP, Saffery).
- Adversarial pass by `idea-critic`, 2026-09-21 (kill recommendation; "do not advance"; wedge strictly `unknown` on cited evidence).

## Scores

`ideas/bikpayroll/scorecard.json`: 9 of 10 dimensions scored; aggregate **50.5** (scored_weight 95, raw 48.0), below the 65 threshold; gating dimensions problem (2) and buyer budget (2) below 3; overall confidence **low**. Not eligible for any advance beyond `desk-screened`.

## Review

Not triggered. Review status `not-required`. The idea is not proposed for `validation-ready`, does not rest on a high score, and no experiment exceeding 20 human-hours or £100 is proposed. (If later evidence raises the score and it is proposed for validation-ready, review-policy trigger 4 — privacy/trust risk from payroll and medical-benefit data — would apply.)

## Reasons if killed

Not killed. Parked because `defensible_wedge` is genuinely `unknown` on cited evidence; the record documents that the adversarial pass recommended kill and that no advance is permitted on current evidence.

## False-negative audit

Not applicable (idea not killed).
