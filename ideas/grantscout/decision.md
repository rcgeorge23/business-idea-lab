# Decision record: GrantScout: matched UK grant digest for small businesses

- **Idea:** `grantscout`
- **Date:** 2026-09-20
- **Run:** `20260920T210550Z-normal`
- **Decision:** kill
- **State:** `desk-screened` -> `killed`
- **Actor:** worker

## What changed

Generated as the run's attractive control: a plausible pain (SMEs missing grant funding), a clear buyer (owner/accountant), and a cheap subscription wedge. It passed all nine hard filters at desk screen and was advanced to adversarial review deliberately. The adversarial pass found the proposed wedge already occupied: GOV.UK's "Find a grant" provides free discovery and is actively expanding, while GovOwed sells the exact flat-fee match/report product at £29 one-time / £499 per year for accountants, and advisers price on success/contingency. An active veto was recorded and the idea killed.

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | pass | SME owner/accountant has budget and incentive. |
| painful_frequent_or_budgeted | pass | Grant discovery/application is time-consuming and competitive. |
| non_paid_distribution | pass | Accountant channel, networks, SEO (assumption, unmeasured). |
| defensible_wedge | pass | Looked usable at desk screen; contested and vetoed at adversarial pass. |
| no_network_effects_needed | pass | Single-customer database utility. |
| plausible_margins | pass | Modelled to cover low content costs (assumption). |
| acceptable_risk | pass | Public funding data; minimal personal data. |
| cheap_disconfirming_test | pass | Cheap landing-page/digest test available. |
| not_all_optimistic | pass | Stop rules defined. |

## Evidence considered

- `evidence/grantscout/2026-09-20-free-government-grant-discovery.md` (primary government source; discovery is free and improving).
- `evidence/grantscout/2026-09-20-incumbent-pricing-and-contingency.md` (vendor pages; the flat-fee wedge is occupied and the category is anchored to contingency pricing).
- Adversarial pass: recorded as an active veto in `ideas/grantscout/scorecard.json#vetoes`.

## Scores

Weighted total **62.1** against threshold **65** (meets threshold: false). Details in `ideas/grantscout/scorecard.json`. Gating dimensions: problem 4/5, buyer 3/5, evidence strength 3/5. Note the score is close to threshold, but the active veto independently bars advancement and requires killed or adversarially-researched.

## Review

No independent review triggered. The kill rests on a documented veto with cited sources, and review policy does not require a request for a killed idea unless the fifth-kill audit or another trigger applies. Review status remains `not-required`. If a human owner disputes the veto, the correct path is a new review request (`killed` -> `requested` is an allowed transition), which this worker has not initiated.

## Reasons if killed

Discovery — the thing the idea would sell — is free from the authoritative source, and the paid flat-fee version already exists with a strong accountant-channel incumbent. The customer's reference price for paid help is "no win, no fee", which a monthly subscription contradicts. The real value sits in application quality/win rate, which is a different (service) idea. What would have changed the decision: evidence that SMEs pay for discovery despite the free service, or that matching/interpretation quality — not application quality — is the binding bottleneck.

## False-negative audit (killed ideas only)

- Audited: no — kill #3 of the run; the fifth-kill audit trigger has not been reached. Given this was the attractive control, a human may reasonably want it audited early; recorded as a decision for human input in the run summary.
- Reviewer / date: n/a
- Verdict: n/a
- What new evidence would justify reopening: primary evidence that SMEs or accountants pay for grant *discovery/matching* rather than application support, or that the free government service is materially inadequate for a specific niche (e.g. a sector or region it does not cover).
