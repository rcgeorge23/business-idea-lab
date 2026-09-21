# Decision record: CMA veterinary price-transparency compliance for independent practices

- **Idea:** vetcma
- **Date:** 2026-09-21
- **Run:** `20260921T075410Z-normal`
- **Decision:** Kill
- **State change:** discovered -> killed
- **Actor:** worker

## What changed

New candidate generated from the CMA veterinary market investigation. The
candidate was screened, evidence-registered, scored, and then killed because the
wedge is already a standard feature of the incumbent category and free
alternatives exist.

## Why now? discovery gate

Strong and evidenced. CMA final report 2026-03-24; draft *Veterinary Services
Market Investigation Order 2026* published 2026-07-21; statutory deadline
2026-09-23; funded monitoring via the Funding Order in force 2026-08-21. The
discontinuity is real and dated.

## Hard filters

| Filter | Status | Note |
| --- | --- | --- |
| economic_buyer | pass | Independent practice owner/manager; ~2,382 independents (VetGuard). |
| painful_frequent_or_budgeted | pass | Mandatory duties with staged 2026-2027 deadlines and a funded regulator levy. |
| non_paid_distribution | unknown | Trade-body route unproven for a new entrant. |
| defensible_wedge | fail | Wedge is a standard feature of PMS/website vendors; >=4 providers, two free forever. |
| no_network_effects_needed | pass | Single-sided compliance tool. |
| plausible_margins | unknown | Free-forever anchor; conversion unproven. |
| acceptable_risk | pass | No regulated activity; dependencies on CMA/RCVS timetables. |
| cheap_disconfirming_test | pass | Landing page plus free price-list tool. |
| not_all_optimistic | unknown | Case depends on conversion against free incumbents. |

Any `fail` kills. `defensible_wedge` = fail, so the idea is killed.

## Evidence considered

`evidence/vetcma/2026-09-21-cma-order-and-incumbent-landscape.md` (CMA case
page; BVA; draft Order PDF; Cloud 9 Vets/GlobeNewswire; Funding Order; VetGuard;
pricebook.vet; vetcompliance.co.uk; Vetstoria; Provet; VetGuard practice stats).

## Scores

Weighted total **61.0** vs threshold 65 - below threshold. Gating dimensions:
problem_severity_frequency 3, buyer_budget_clarity 3, evidence_strength 4 - all
>= 3. The kill is driven by the hard-filter failure, not by the aggregate.

## Review

No review requested. Killed ideas do not trigger the validation-ready review.
A false-negative audit will be due when the killed count next reaches a multiple
of five.

## Reasons if killed

`defensible_wedge` fail: the CMA compliance job is already served by VetGuard
(£49/month, free price-list tool), pricebook.vet (free forever),
vetcompliance.co.uk (free scanner), Vetstoria and Provet. This is commodity
positioning with no wedge; free alternatives reset the price to zero. The only
unserved sub-job identified (estimate-to-bill bridge) is too small to carry a
business and is recorded as a seed (`vet-estimate-bridge`).

## False-negative audit (killed ideas only)

To be completed by the human owner if this kill is selected for audit. Audit
question: did we kill a real business because a free tool was mistaken for a
free *business*? A plausible audit path is to observe whether any of the free
entrants converts to paid at scale; if VetGuard or pricebook.vet converts well,
this kill was a false negative.
