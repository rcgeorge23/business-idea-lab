# Regression: method 1.6.0 archetype-aware cap and sampled triage audit (issue #8)

- **Date:** 2026-09-21
- **Issue:** [#8](https://github.com/rcgeorge23/business-idea-lab/issues/8) - address
  method 1.5.0 review findings before the next discovery run
- **Method under test:** 1.6.0 (archetype-aware missing-why-now cap; competitor
  existence is not wedge failure; sampled triage false-negative audit)
- **Run:** none - this is a calibration/regression pass, not a discovery cycle

## What was tested and why

The 1.5.0 review (`reviews/2026-09-21-method-v1.5.0-chatgpt.md`) required that the
archetype-aware cap and the competitor-existence clarification be regression-tested
against fixtures that must **not** be rescued by persistent pain alone. The rule
tested is the two-part persistence thesis in `method/discovery.md`:

> To lift the missing-why-now cap, an archetype-B candidate must affirmatively show
> BOTH (1) continued buyer pain / cost / workaround despite alternatives that exist
> and are reachable for the target segment, AND (2) a credible mechanism explaining
> why the market has not adequately resolved the problem for that segment.

A "regression" here would be any fixture that the new wording revives (kills
overturned, cap removed, score inflated, or generic/crowded propositions restored)
without new evidence. Historical files were re-read, not rewritten; no fixture was
rescored and no file was tuned to make a fixture pass.

## A. Aucly pre-launch - `ideas/aucly/pre-launch-assessment.md`

- **Archetype:** persistent market failure (school-fundraising auction category is
  evergreen; the named incumbents predate the 2025-07-30 evidence cut-off).
- **Before (as recorded under method 1.2.0):** 49.5, confidence low, no vetoes;
  `problem_severity_frequency` 2 with the rationale "A missing/unevidenced why-now
  caps this at 2 (method 1.2.0)"; `differentiation` 2; four hard filters `unknown`
  (`painful_frequent_or_budgeted`, `non_paid_distribution`, `defensible_wedge`,
  `plausible_margins`); parked at `desk-screened` with a cheap concierge experiment.
- **After (rule applied on paper):** the archetype is now explicitly recognised, so
  the assessment could record a persistence thesis instead of a forced discontinuity.
  At the cut-off, however, the recorded evidence does not affirmatively support both
  limbs: the competing products contest the same price points (weak limb 1), and no
  present-tense mechanism explains why the market has not resolved the problem for
  small PTAs specifically (limb 2 is an unresolved assumption, A1-A7). The cap
  therefore remains in force.
- **Verdict:** **no material change.** No discontinuity is manufactured - `why_now`
  keeps `strength: absent` with no invented `changed_date`. The score stays 49.5, the
  state stays `desk-screened`, and the file is not rescored. The rule was **not**
  tuned so that Aucly passes; the regression record is the interpretation, not a
  new score.

## B. ShiftSwap - `ideas/shiftswap/scorecard.json` (killed)

- **Archetype:** persistent (hospitality scheduling pain persists; ONS/UKHospitality
  labour-pressure evidence already recorded).
- **Failure reasons:** `non_paid_distribution` (two-sided adoption with no non-paid
  route), `defensible_wedge` (every low-cost UK rota product already bundles
  self-service shift swaps), `no_network_effects_needed`, `plausible_margins`
  (advertised £0/£9/£10/£49), `not_all_optimistic`. Score 44.2, review `approved`
  (false-negative audit upheld the kill).
- **Verdict:** **no material change.** The new cap rule can only affect the
  `differentiation` / `problem_severity_frequency` caps, never a hard filter. A
  persistence thesis cannot rescue a candidate whose distribution, wedge, network-
  effect and margin filters fail. Still killed.

## C. WonkyBox - `ideas/wonkybox/scorecard.json` (killed)

- **Archetype:** persistent (consumer food-waste concern and complaints persist).
- **Failure reasons:** `non_paid_distribution` (paid acquisition; revenue fell after
  the marketing cut), `defensible_wedge` (Oddbox, ~£30m raised, and Wonky Veg Boxes
  already serve the proposition), `plausible_margins` (category leader loss-making,
  ~£27m revenue, operating losses widening 98.7% FY2025), `not_all_optimistic`.
  Score 36.8.
- **Verdict:** **no material change.** Persisting complaints about waste do not
  constitute a persistence thesis that lifts anything, and especially not the
  hostile unit economics of the category leader. Still killed.

## D. GrantScout - `ideas/grantscout/scorecard.json` (killed)

- **Archetype:** persistent (grant discovery is a standing pain).
- **Failure reasons:** `defensible_wedge` **fail plus veto** - GovOwed sells the
  exact flat-fee wedge (£29 one-time / £499-per-year) and GOV.UK Find a grant is a
  free authoritative alternative; `non_paid_distribution`, `plausible_margins` and
  `not_all_optimistic` `unknown` with `resolve_via`. Score 55.8.
- **Verdict:** **no material change.** The persistence thesis requirement is
  explicitly evidence about alternatives *failing* the target segment; here the
  recorded evidence shows the opposite (a free authoritative service plus a
  like-for-like commercial product). Generic grant discovery stays killed.

## E. O14 triage rejection - first sampled triage false-negative audit

- **Observation:** O14, UK/Lloyd's insurance broker submission intake (risk data
  re-keyed into each carrier/portal; bordereaux still spreadsheets; Blueprint Two
  reset), recorded in `observations/20260921T091851Z-normal.md`.
- **Why selected:** it was the strongest high-ambiguity rejection in the v1.5 pool -
  practitioner *and* vendor evidence, persistent archetype, and rejected precisely
  for incumbent occupation ("A live vendor already occupies the exact seam; credible
  providers present"), which is the rejection class the 1.5.0 review asked to audit.
- **Original triage reasoning (before):** reject because a live vendor (Ergini)
  appeared already to occupy the exact seam, beside Acturis/Applied Epic, Open
  GI/Acturis connectivity and PathwayPort.
- **Additional evidence checked (cheap, 2026-09-21, 3 searches):**
  1. Applied Systems / Ivans 2026 Insurance Agency-Carrier Connectivity Trends survey
     (702 independent agents, fieldwork Apr-May 2026; released 2026-08-26/27): 74%
     of agents name re-keying risk data into carrier portals as a top workflow pain;
     90% have reduced business with a carrier over submission friction; commercial
     submission automation is the #1 wanted capability (79%).
  2. Multiple live vendors with demonstrated deployments in exactly this seam:
     CogniSure (carrier/broker/MGA workbench, rating-ready data no re-keying),
     Kalepa (brokers solution; named insurer deployments), Heron Data (UK MGA case
     study 2026-07-31: underwriting time halved, 25-40% more submissions/day; 130+
     customers), Unitary (AI virtual agents moving data between broker management
     systems and insurer portals), Insillion InFlow, Argonaut Platform, SubmitIQ,
     Broker Buddha + AgencyAssist, Agiliux.
  3. The originally named incumbent (Ergini) was **not** independently re-verified in
     this cheap check - a targeted search returned unrelated companies. This is
     recorded honestly; the wider vendor field was verified instead.
- **Five confusion tests:** (1) existence vs satisfaction - deployments show real
  usage, so no overturn; (2) feature vs complete solution - vendors ship complete
  intake-to-portal flows, not features; (3) enterprise vs niche - UK MGA/broker
  deployments show mid-market accessibility; (4) vendor claims vs demonstrated
  capability - Heron/NBS measured outcomes and named Kalepa/CogniSure customers;
  (5) one-shot vs recurring - the need is recurring and is served, so no rescue.
- **Verdict: rejection UPHELD.** This is not "a competitor exists": evidence shows
  demonstrated capability and genuine occupation of the seam. The pain persists
  because of carrier-side fragmentation, not because a tool is missing - so a new
  entrant would need a sub-seam the incumbent deployments do not cover.
- **Implication for triage depth:** the shallow triage reason was sound and the
  competitor-existence clarification does not force promotion where occupation is
  evidenced. No repeat-pattern signal, so triage depth stays as-is.

## Regression outcomes

| Fixture | Archetype | Before | After | Changed? |
|---|---|---|---|---|
| Aucly pre-launch | persistent | 49.5, parked `desk-screened`, cap rationale recorded | thesis opportunity noted; both limbs not evidenced at cut-off; cap and state unchanged; not rescored | no |
| ShiftSwap | persistent | killed, 44.2, five hard-filter fails | unchanged | no |
| WonkyBox | persistent | killed, 36.8, four hard-filter fails | unchanged | no |
| GrantScout | persistent | killed, 55.8, `defensible_wedge` fail + veto | unchanged | no |
| O14 (triage) | persistent | rejected: incumbent occupation | rejection upheld on demonstrated occupation | no |

No fixture was revived, no score inflated, and no generic or crowded proposition
restored. The persistent archetype is now explicitly admitted where permitted
(Aucly) without weakening `defensible_wedge` or any hard filter.

## Method status

Method 1.6.0 carries these changes with review `requested`
(`reviews/2026-09-21-method-v1.6.0-review-request.md`); it answers the 1.5.0
`changes-requested` review and records 1.4.0 as approved. The funnel and its 15-20
pool are retained provisionally. `defensible_wedge`, threshold 65, evidence levels and
lifecycle gates are unchanged.
