# Decision record: PRS Database registration and marketing-readiness for letting agents and landlords

- **Idea:** prsregister
- **Date:** 2026-09-21
- **Run:** `20260921T075410Z-normal`
- **Decision:** Kill
- **State change:** discovered -> killed
- **Actor:** worker

## What changed

New candidate generated from the PRS Database regulations. Registered, scored
and killed because the readiness job is a commodity feature of letting software
and the core register is a free government service.

## Why now? discovery gate

Strong and evidenced. Renters' Rights Act 2025 Royal Assent 2025-10-27; Part 1
in force 2026-05-01; draft PRS Database Regulations 2026 laid 2026-09; rollout
from 2026-12-15 (West Midlands) to 2027-11-14; agents barred from marketing
without registration numbers.

## Hard filters

| Filter | Status | Note |
| --- | --- | --- |
| economic_buyer | pass | Letting agents and self-managing landlords in England. |
| painful_frequent_or_budgeted | pass | Mandatory entries, per-property fee, marketing prohibition. |
| non_paid_distribution | unknown | NRLA/Propertymark route unproven for a new entrant. |
| defensible_wedge | fail | Readiness is standard letting-software functionality; free register exists. |
| no_network_effects_needed | pass | Single-sided tool. |
| plausible_margins | unknown | £19/month anchor against free core register. |
| acceptable_risk | pass | No regulated activity. |
| cheap_disconfirming_test | pass | Pre-check tool for small agents in the first rollout region. |
| not_all_optimistic | unknown | Depends on paid conversion where a free register exists. |

`defensible_wedge` = fail, so the idea is killed.

## Evidence considered

`evidence/prsregister/2026-09-21-prs-database-and-incumbents.md` (draft PRS
Database Regulations 2026; Renters' Rights Act 2025; Lettable; Homelet /
Property Week / Independent Landlord / LandlordZONE / Ultralets; agent software
incumbents; EveryGuard).

## Scores

Weighted total **59.0** vs threshold 65 - below threshold. Gating dimensions:
problem_severity_frequency 3, buyer_budget_clarity 3, evidence_strength 4 - all
>= 3. The kill is driven by the hard-filter failure.

## Review

No review requested. A false-negative audit will be due when the killed count
next reaches a multiple of five.

## Reasons if killed

`defensible_wedge` fail: commodity readiness feature; the register itself is
free via GOV.UK; Lettable already sells readiness at £19/month; Goodlord,
Fixflo, OpenRent, Landlord Vision and Homelet own the agent workflow. The one
gap (no bulk upload/API at launch) is a feature incumbents can add, recorded as
a seed (`prs-listing-precheck`).

## False-negative audit (killed ideas only)

Human owner may audit. Audit question: did we underestimate a per-property,
high-volume compliance burden for large agents? If rollout exposes agent-level
penalties and no incumbent ships a bulk path, this kill could be a false
negative.

## Post-kill reassessment (2026-09-26; current-score rank among killed ideas: 2/5)

Fresh evidence is registered at
`evidence/prsregister/2026-09-26-killed-idea-reassessment.md`. The official
announcement schedules a phased service launch from 2026-12-15 and states that
all active landlords must register by 2027-11-14; it describes the core service
as straightforward and does not confirm a fee. The checked regulations page is
still a draft, with the operator’s fee set by relevant costs. Lettable currently
advertises £19/£49/£99 monthly tiers and portfolio/bespoke agency features.

The original generic readiness/pre-check product remains **killed**:
`defensible_wedge` remains fail because the public register is free and an
incumbent offers low-priced readiness and portfolio functions. The separately
rechecked self-managing-landlord seed is not treated as evidence about agent-side
operations. Historical score 59.0 and prior outcomes are unchanged; no rescore
or state transition is made. Reopening would require a specific high-volume
agent workflow missing from the final service and contracted CRM alternatives,
with an evidenced separate budget and reachable channel.
