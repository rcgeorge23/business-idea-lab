# Decision record: Aucly

- **Idea:** `aucly` — flat-fee online auction platform for UK schools, PTAs and charities
- **Date:** 2026-09-21
- **Actor:** worker (issue #3 calibration case)
- **Method version:** 1.2.0
- **State after:** `adversarially-researched` (parked) · **Evidence level:** `Commercial evidence` (early)
- **Related documents:** `ideas/aucly/dossier.md`,
  `ideas/aucly/pre-launch-assessment.md`, `ideas/aucly/scorecard.json`

## What changed

- The idea was added to the ledger as an explicit calibration/reference case with
  two deliberately separate assessments: pre-launch (no hindsight) and today.
- Current-state score: **60.0** (threshold 65, not met); confidence medium;
  hard filters: 3 `pass`, 4 `unknown`, 0 `fail`; no vetoes.
- State: parked at `adversarially-researched`. The worker does not advance it to
  `validation-ready` (below threshold; distribution and economics unproven) and
  cannot, by design, advance it further on historical operating evidence.
- Experiment proposed: `aucly-channel-test` (awaiting human approval).

## Why now? (discovery gate)

Recorded as **absent** and not disguised: nothing favourable changed recently.
Fundraising auctions and their platforms predate Aucly; the flat-fee model is a
positioning choice. Under method 1.2.0 the missing why-now cap does not apply at
`Commercial evidence` (it applies only at `Plausible`/`Promising`), so the idea
is judged on operating evidence rather than penalised for being evergreen.
Evidence: `evidence/aucly/2026-09-21-competitive-landscape.md`,
`evidence/aucly/2026-09-21-build-and-operating-burden.md`.

## Hard filters

| Filter | Status | Note | Evidence / resolve via |
|---|---|---|---|
| economic_buyer | pass | Organisers control an event budget; category pricing exists; Aucly tiers £60/£120. | `evidence/aucly/2026-09-21-pricing-and-payments.md`, `...-competitive-landscape.md` |
| painful_frequent_or_budgeted | pass | Recurring annual fundraising job; real engaged auctions (63 bidders, 1,074 bids, £2,265). | `evidence/aucly/2026-09-21-live-auctions-and-customers.md` |
| non_paid_distribution | unknown | 2,333 recorded visitors → 0 accounts; no unpaid channel demonstrated. | resolve via: `aucly-channel-test` (20 contacts, ≥2 launches in 30 days, no spend) |
| defensible_wedge | unknown | Flat fee contested by free plans and a scaled incumbent. | resolve via: win/loss questions in the channel test |
| no_network_effects_needed | pass | One organiser + their own community suffices. | `evidence/aucly/2026-09-21-live-auctions-and-customers.md` |
| plausible_margins | unknown | £60/£120 vs hosting/email/founder time unquantified. | resolve via: record cost and hours per auction; check second-year return |
| acceptable_risk | pass | No regulated data; payments via organiser's own channels; no funds held. | `evidence/aucly/2026-09-21-pricing-and-payments.md`, `...-build-and-operating-burden.md` |
| cheap_disconfirming_test | pass | 20 contacts, fixed kill rule, ~20h, £0, 30 days. | `experiments/aucly-channel-test/plan.md` |
| not_all_optimistic | unknown | Acquisition, retention, market size and founder-time economics all still open. | resolve via: channel test + retention/pricing follow-up |

No `fail`, no veto.

## Evidence considered

- `evidence/aucly/2026-09-21-pricing-and-payments.md` — flat fee, no commission;
  tiers seeded 2025-08-21; ~7 paid auctions owner-supplied and unverified (no
  lifetime export found; the issue asked for verification, and verification was
  not possible from the available first-party data).
- `evidence/aucly/2026-09-21-live-auctions-and-customers.md` — Furzedown and
  Lingfield outcomes, live auctions, named customers.
- `evidence/aucly/2026-09-21-seo-and-acquisition.md` — GSC/Cloudflare/export
  metrics including the zero-conversion export window.
- `evidence/aucly/2026-09-21-competitive-landscape.md` — six platforms, four
  pricing models; vendor-authored, weak secondary.
- `evidence/aucly/2026-09-21-build-and-operating-burden.md` — repo history,
  feature breadth, Railway hosting, no pre-build validation artefact.
- `ideas/aucly/pre-launch-assessment.md` — simulated 2025-07-30 assessment.

## Scores

| Dimension (weight) | Pre-launch | Today | Confidence |
|---|---|---|---|
| problem_severity_frequency (15) | 2 | 3 | medium |
| buyer_budget_clarity (15) | 3 | 3 | medium |
| evidence_strength (15) | 2 | 4 | medium |
| distribution (10) | 2 | 2 | high |
| differentiation (10) | 2 | 2 | medium |
| validation_speed_cost (10) | 4 | 4 | medium |
| feasibility (5) | 3 | 4 | high |
| economics (10) | 2 | 2 | medium |
| founder_fit (5) | null | 3 | medium |
| risk (5) | 3 | 3 | medium |
| **Weighted total** | **49.5** | **60.0** | medium |

Threshold 65 is not met today. Confidence medium; 9 of 10 dimensions scored.

## Review

`not-required` for the parked idea. Note for the human owner: the recorded
operating history is substantial external activity, but it was not run as a lab
experiment, so this record does not treat it as `externally-tested` evidence.
If the owner wants the idea moved to `externally-tested`, that transition needs
a recorded human decision and, per the review policy, a review outcome; the
worker may propose it but not perform it.

## Calibration findings (issue #3)

### A. Pre-launch Aucly (2025-07-30, no hindsight)

- **Evidence available at the time:** public category facts (PTAs run auctions;
  incumbents charge commission or fees; a flat-fee self-service offer was not
  prominent), the founder's build capability, and nothing else.
- **Genuinely unknown assumptions:** A1–A7 in the dossier.
- **Score and filters:** 49.5, below threshold; no `fail`, no veto; four
  `unknown` filters (distribution, wedge, margins, all-optimistic).
- **Decision the lab would have made:** not killed; not advanced; parked at
  `desk-screened` with a proposed ~20-hour concierge test — recruit 3–5 PTAs and
  only build if at least 2 commit to a real auction.
- **What actually happened:** build began 2025-07-30 with no recorded screening;
  launch and SEO followed; today there are real auctions and a small number of
  paying organisers, but no demonstrated unpaid acquisition channel.

### B. Aucly today

- **Positive:** real auctions with meaningful engagement; two publishable
  customer outcomes; production platform; some organisers pay.
- **Negative:** 0 accounts/launches/payments from the recorded 2,333 visitors;
  brand-only search demand; ~7 paid auctions unverified; retention, market size
  and founder-time economics unquantified; heavy maintenance.
- **Score and filters:** 60.0; three `pass` filters, four `unknown`, no `fail`.

### Key calibration questions

1. **Would the lab have considered pre-launch Aucly worth a cheap test?** Yes.
   Identifiable buyer, plausible budget, and a cheap falsifiable test.
2. **If not, why not?** N/A — it would have been parked for testing, not killed.
3. **Sensible or a false negative?** Neither: the lab would have demanded the
   very test that later failure suggests was missing. The outcome (real use,
   weak distribution) is consistent with parking-then-testing, so no false
   negative is indicated.
4. **How does Aucly score today?** 60.0, below 65, parked; `Commercial evidence`
   (early), confidence medium.
5. **Which dimensions changed most?** `evidence_strength` 2→4,
   `problem_severity_frequency` 2→3, `feasibility` 3→4, `founder_fit` null→3;
   total 49.5→60.0. Crucially, `distribution` did not move (2) despite launch.
6. **Did real-world evidence validate originally unknown assumptions?**
   Partially — A4 (self-service works with light help) and weakly A1 (some
   organisers will use and pay). A2 (flat fee preference), A3 (unpaid
   acquisition), A5 (economics), A6 (retention) and A7 (market size) remain
   unvalidated, and A3 currently has negative evidence.
7. **Which assumptions were wrong or weaker?** Discovery/SEO as an acquisition
   route; the flat fee as a decisive differentiator against free plans; and the
   sequencing assumption that building first and selling later was safe.
8. **Does the lab overweight novelty/defensibility for a small bootstrapped
   niche?** Not after v1.2.0. v1.1.0 did systematically double-penalise evergreen
   niches by applying the missing-why-now cap even when real payment evidence
   existed; that was fixed by scoping the cap to `Plausible`/`Promising`.
   Differentiation still scores Aucly 2, correctly, because the wedge is
   contested — that is not overweighting, it is the honest reading.
9. **Does it underweight ease/cost of building and testing?** No:
   validation_speed_cost and feasibility both score 4 here; the scorecard
   rewards cheap falsifiability. Pre-launch it was the founder's sequencing, not
   the scorecard, that skipped the cheap test.
10. **Distinguishes viable small business from venture-scale?** Yes. No
    dimension requires venture scale; small size shows up in economics,
    distribution, differentiation and risk without auto-killing, and the
    threshold tests evidence quality, not ambition.
11. **Does it recognise payment behaviour without over-reading ~7 purchases?**
    Yes: `evidence_strength` rose to 4 and `buyer_budget_clarity` stayed at 3,
    while `distribution` (2), `economics` (2) and `differentiation` (2) were not
    inflated. A handful of payments cannot lift retention, market size or
    channel scores, because none of those are evidenced.
12. **Dimensions where current evidence still does not justify a strong
    score?** distribution (negative evidence), differentiation (contested),
    economics (unquantified), buyer (payment count unverified), founder_fit
    (time economics unknown), problem (no incumbent-dissatisfaction evidence).

### Comparison with existing fixtures

| Idea | State | Score | Evidence level | Why this outcome |
|---|---|---|---|---|
| Aucly | parked | 60.0 | Commercial (early) | Real payments and real auctions, but unpaid distribution, retention and economics unproven; below threshold and no fail |
| GrantScout | killed | 55.8 | Plausible | No real-world evidence; veto on `defensible_wedge` (free GOV.UK discovery + GovOwed) |
| GeoNerd | parked | 49.5 | Promising | Genuine category discontinuity but all desk research; wedge contested by incumbents |
| ShiftSwap | killed | 44.2 | Plausible | Fails distribution, network-effect and margin filters; commodity feature bundled in rota software |
| WonkyBox | killed | 36.8 | Plausible | Oddbox loss-making at scale; paid acquisition required; margins fail |

The ordering is sensible: demonstrated payment behaviour (Aucly) outranks new-
category desk research (GeoNerd), which outranks ideas killed on hard filters or
hostile economics. Aucly is not advanced merely for having launched: it remains
below the threshold exactly because launch revealed distribution weakness rather
than validating it. GrantScout scoring above GeoNerd while being killed is also
consistent — its kill is a hard-filter veto, not an aggregate score.

### Apparent false positive / negative or scoring anomaly

- **Pre-launch false negative:** none — the lab would have tested, not killed.
- **False positive:** none — the lab would not have advanced it to
  `validation-ready` (49.5), so it never claimed more than a hypothesis.
- **Scoring anomaly found (systematic):** the v1.1.0 missing-why-now cap applied
  at every evidence level, double-penalising evergreen businesses once real
  commercial evidence existed (Aucly's `problem_severity_frequency` was capped at
  2, worth ~3 points of total). Fixed in v1.2.0 by scoping the cap to
  `Plausible`/`Promising`.
- **No change needed** for: hard-filter pass/unknown/fail semantics; treatment
  of direct competitors; treatment of small/niche markets; weighting of cheap
  build/testability; founder fit; evidence strength; willingness-to-pay
  evidence; retention handling; distribution difficulty; bootstrapped vs
  venture-scale distinction.

## Method refinement (v1.2.0)

- **Specific result exposing the problem:** Aucly today scored
  `problem_severity_frequency` 2 under the v1.1.0 cap (total 57.0) despite real
  auctions, real bidders and paying organisers.
- **Why the old rule was systematically wrong:** "no recent discontinuity" was
  being treated as evidence of weak demand. Evidence levels already distinguish
  pre-demand from demand/commercial evidence, so the cap should bind only where
  no demand evidence exists.
- **Change:** the missing/unevidenced why-now cap now applies only to ideas at
  `Plausible` or `Promising`; at `Demand evidence` or better the idea is judged
  on its operating evidence.
- **Regression check:** the killed fixtures (ShiftSwap, WonkyBox, GrantScout) are
  all `Plausible`, so the cap still applies and their kills rest on `fail`
  filters/vetoes; GeoNerd and Reasonable Steps (`Promising`) are unaffected;
  Aucly's change is a single dimension, 2→3.
- **Falsification preserved:** threshold unchanged at 65; hard filters
  unchanged; no weak idea becomes a pass.
- **Review:** method 1.2.0 change is `requested` —
  `reviews/2026-09-21-method-v1.2.0-review-request.md`; outcome to be recorded in
  `method/CHANGELOG.md` and answered next run.

## Reasons if killed

Not killed. A kill would require evidence that organisers will not switch or pay
(for example 0 of 20 launches in the channel test with incumbent-satisfaction
objections). A killed variant would keep this record and could produce a
non-inheriting seed (e.g. purpose-built tools for volunteer-run charity auctions
in other verticals).

## False-negative audit

Not applicable — Aucly has never been killed.

## 2026-09-22 — Locale expansion assessment (owner-directed, run `20260922T100404Z-normal`)

- **Question assessed:** the business value of expanding Aucly into another locale
  — Ireland, the US, Australia or New Zealand — including cost, benefit, different
  market conditions and different regulation.
- **Decision:** **hold — do not expand now.** State unchanged
  (`adversarially-researched`, parked). **Scores unchanged (60.0).** Recorded hard
  filters unchanged (3 `pass`, 4 `unknown`, 0 `fail`). No new candidate was created:
  a locale variant is the same buyer, problem and mechanism, so per
  `method/discovery.md` duplicate rules it updates this idea rather than adding a
  ledger entry.
- **Why:** the binding constraint is unpaid demand, still unsolved at home (2,333
  visitors → 0 accounts, 0 auctions, £0). Every locale examined already has a free
  or low-cost incumbent serving the same buyer (Toko free for NZ schools;
  Fundraising Solutions zero platform fee in IE; GalaBid free-with-tips in AU/NZ;
  Auctria free tier in the US), and no locale-specific evidence of organiser
  dissatisfaction was found. Expansion resets distribution to zero and adds
  regulation/tax cost without addressing the known failure. Ireland ranks first if
  expansion is ever pursued (cheapest discriminating probe), then Australia, then
  New Zealand, then the US.
- **Assessment document:** `ideas/aucly/expansion-assessment.md`.
- **Evidence added this run:**
  `evidence/aucly/2026-09-22-locale-market-and-incumbents.md`,
  `evidence/aucly/2026-09-22-locale-regulation-and-tax.md`.
- **Observation pool:** `observations/20260922T100404Z-normal.md` (20 observations,
  10 regulatory / 10 non-regulatory, 0 promoted; false-negative audit upheld O20).
- **Experiment proposed:** `aucly-ireland-demand` (awaiting human approval;
  informative only in combination with `aucly-channel-test`, which remains the
  cheapest decisive test for the idea's central assumption).
- **No overwrite:** this section appends to, and does not replace, the 2026-09-21
  record above.

## 2026-09-22 — Post-run correction: acquisition traffic is largely non-human (run `20260922T100404Z-normal`)

- **Correction:** the owner states (2026-09-22) that the 2,333 visitors in the
  acquisition export are **mainly bots**. Recorded append-only in
  `evidence/aucly/2026-09-22-acquisition-bot-correction.md` (register:
  assumption, owner-supplied and unverified). Corroborating first-party detail:
  the same source file records Cloudflare **130 visits** versus the application
  export's **2,333 visitors** over near-identical windows (~18x), and GSC shows
  only 45 clicks / 921 impressions, so the export cannot reflect 2,333 humans.
- **Effect:** the earlier characterisation "negative primary evidence" is too
  strong; the accurate reading is "human reach is unmeasured; the channel is
  effectively untested". The recorded outcomes (0 accounts, 0 auctions launched,
  **£0 revenue**) are unchanged, and **no unpaid channel has been demonstrated**.
- **Scores/state:** **unchanged** — weighted total **60.0**; state
  `adversarially-researched` (parked). Only `distribution.confidence` changed,
  **high → medium** (score stays **2**); the
  `non_paid_distribution` hard filter stays **unknown** (not `fail`).
- **Statements superseded by this correction** (left in place, not silently
  rewritten): the 2026-09-21 non_paid_distribution table row ("2,333 recorded
  visitors → 0 accounts"); the calibration section's "- **Negative:** 0
  accounts/launches/payments from the recorded 2,333 visitors"; and the
  2026-09-22 locale-expansion bullet beginning "- **Why:** the binding
  constraint is unpaid demand, still unsolved at home (2,333 visitors → 0
  accounts...)". Each should now be read as "0 accounts/launches/revenue against
  an unmeasured human base".
- **Consequence for any channel work:** the application-level acquisition
  endpoint counts bots and needs a bot filter (Cloudflare bot score, user-agent
  or served-request exclusion, or a server-side filter) before it can adjudicate
  any acquisition channel. The recommendation **not to expand locales** is
  unchanged, because there is still no demonstrated UK channel to replicate.
- **No overwrite:** this section appends to, and does not replace, the records
  above.

## Decision log

| Date | Change | Reason | Actor |
|---|---|---|---|
| 2026-09-21 | Added; scored 60.0; parked at `adversarially-researched`; experiment `aucly-channel-test` proposed | Issue #3 calibration: recognise early commercial evidence without over-claiming; name remaining unknowns in a cheap pre-fixed test | worker |
| 2026-09-22 | Held (no expansion); scores and filters unchanged; locale-expansion assessment recorded; evidence added; `aucly-ireland-demand` proposed | Owner asked for an expansion cost/benefit/regulation assessment; evidence shows free low-cost incumbents in every locale plus an unsolved home channel, so expansion is unsupported now | worker |
| 2026-09-22 | Post-run correction: acquisition traffic largely bots; `distribution` confidence high→medium (score stays 2); filter stays `unknown`; state/score unchanged (60.0) | Owner supplied the bot correction; evidence register corrected append-only per the evidence policy; no silent overwrite | worker |
