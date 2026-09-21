# Aucly: pre-launch reconstruction (calibration case)

- **Calibration case:** Aucly (owner's live business, evaluated for issue #3)
- **Reconstruction date / stage:** 2025-07-30, before the first application
  commit (`04566e4ea feat: Index page now rendering`), i.e. the decision
  "is this worth testing/building?"
- **Method version:** 1.2.0
- **Hindsight rule:** only evidence that could reasonably have been available
  on 2025-07-30 is used. Furzedown/Lingfield case studies, SEO/GSC/Cloudflare
  analytics, the paid-auction count, current pricing-page refinements and all
  post-2025 Aucly learning are excluded. Where a fact was re-verified later but
  was public before 2025 (e.g. incumbent commission models), it is labelled as
  an assumption or a public-category fact, not as Aucly traction evidence.

## What was known (or knowable) on 2025-07-30

- UK schools and PTAs run fundraising auctions regularly (annual/summer fairs,
  gala events); the buyer is the PTA chair/committee or a school/charity
  fundraiser with control of the event budget. *(Assumption, based on general
  public knowledge of the category; not surveyed.)*
- Established providers existed with different commercial models: commission
  models such as Jumblebee (beeClassic ~5% + VAT) and PTA Events (~5% of auction
  sales), GalaBid (free plan funded by bidder tips; Pro ~4.9%), and fully
  managed per-event providers for large galas (Givergy, Generosity Works).
  *(Public category fact re-verified 2026-09-15 in
  `evidence/aucly/2026-09-21-competitive-landscape.md`; vendor-authored source,
  weak secondary.)*
- No incumbent was widely known to offer a flat fee with no commission for a
  self-service school/PTA auction. *(Assumption from the same source; not
  independently verified at the time.)*
- Building an auction platform (scheduling, proxy bidding, post-sale payment
  tracking, email) was within the founder's technical capability. *(Inference
  from the founder starting the build; plausible.)*
- Nothing recorded in the Aucly repository addresses demand, willingness to
  pay, distribution or alternatives before the build started; the repository
  begins with code, not validation. *(Primary: repo history,
  `evidence/aucly/2026-09-21-build-and-operating-burden.md`.)*

## Assumptions genuinely unknown on 2025-07-30

- A1: that PTAs/schools feel enough pain with incumbents to switch.
- A2: that a flat fee is more attractive than a commission to this buyer.
- A3: that organisers can be reached without paid acquisition (SEO, direct
  outreach, school networks).
- A4: that an auction can be run by a volunteer organiser with low support
  burden.
- A5: that £60/£120 per auction yields a workable contribution after hosting,
  email and founder time.
- A6: repeat usage — that organisers return the following year.
- A7: market size — how many UK PTAs/schools/charities run auctions at all.

## Scorecard (simulated, method 1.2.0, only pre-launch evidence)

| Dimension (weight) | Score | Confidence | Evidence / rationale |
|---|---|---|---|
| problem_severity_frequency (15) | 2 | low | Category plausibly painful and recurring, but no evidence about this buyer's dissatisfaction; assumption only. A missing/unevidenced why-now caps this at 2 (method 1.2.0). |
| buyer_budget_clarity (15) | 3 | low | Buyer identifiable (PTA chair / school fundraiser, event budget); category incumbents charge commission, so money moves. No Aucly-specific willingness-to-pay evidence. |
| evidence_strength (15) | 2 | low | Public category facts only; no buyer-derived or independent evidence. |
| distribution (10) | 2 | low | Channels describable (SEO, school networks, direct outreach); no measured yield; plausible-only cap. |
| differentiation (10) | 2 | low | Flat fee vs commission is a positioning choice, not an evidenced wedge; free tiers at GalaBid and Jumblebee beeFree contest it. |
| validation_speed_cost (10) | 4 | medium | A recruit-and-run-a-real-auction test is cheap and fast; decision rule can be fixed in advance. |
| feasibility (5) | 3 | medium | Auction product is buildable by this founder, but no part of the pipeline was proven at this point. |
| economics (10) | 2 | low | £60/£120 modelled; hosting, email and support costs unknown; modelled-only cap. |
| founder_fit (5) | null | none | No recorded evidence of founder fit, domain access or unfair advantage at this date. |
| risk (5) | 3 | medium | No regulated data; payments via organisers' own channels; platform dependency and incumbent competition are the main risks. |

**Aggregate:** raw 47.0 / scored weight 95 → **weighted_total 49.5** (threshold
65, not met). Confidence **low**. No vetoes.

## Hard filters (simulated, method 1.2.0)

| Filter | Status | Note | Evidence / resolve_via |
|---|---|---|---|
| economic_buyer | pass | PTA chair / school fundraiser controls the event budget; incumbents in the category charge for the same job. | `evidence/aucly/2026-09-21-competitive-landscape.md` (public category fact, re-verified later; used only for what was publicly knowable) |
| painful_frequent_or_budgeted | unknown | Annual fundraising is plausibly painful, but no evidence about dissatisfaction with incumbents. | resolve via: recruit 3–5 PTAs and observe/ask what they use today and what it costs them in effort |
| non_paid_distribution | unknown | No measured route to organisers. | resolve via: the proposed concierge test measures reply and launch rates from unpaid outreach |
| defensible_wedge | unknown | Flat fee is contestable by free tiers and commission models may suit some buyers better. | resolve via: ask organiser reactions to flat fee vs commission in the same conversations |
| no_network_effects_needed | pass | A single organiser can run an auction with their own bidders; no marketplace density required. | `evidence/aucly/2026-09-21-live-auctions-and-customers.md` (mechanism is one-to-many by design) |
| plausible_margins | unknown | £60/£120 modelled with unknown costs. | resolve via: record hosting/email/support cost and time for the first real auctions |
| acceptable_risk | pass | No sensitive data beyond organiser/bidder emails; funds collected via organisers' own accounts, not held by Aucly. | `evidence/aucly/2026-09-21-pricing-and-payments.md` |
| cheap_disconfirming_test | pass | A concierge test can be run before building: recruit 3–5 PTAs, offer to run their auction manually, and measure whether they commit. | `experiments/aucly-channel-test/plan.md` (proposed) |
| not_all_optimistic | unknown | Viability depends on several untested assumptions (A3–A6) all holding. | resolve via: the concierge test and a follow-up retention check |

No `fail`, no veto.

## Cheapest decisive experiment the lab would have proposed

Recruit 3–5 UK PTAs/school organisers **before building**. Offer to run their
next auction with a concierge/manual process (or to set it up on an existing
platform while standing behind the flat-fee promise). Pre-fixed decision rule:
proceed to build only if at least 2 of 5 commit to run a real auction and at
least 2 more show concrete intent; stop if 0 commit. Cost bound: ~20 human
hours, ≤£50, 30 days. This is materially the same test as the proposed
`aucly-channel-test`, moved before the build instead of after launch.

## The decision the lab would have made

- **Not killed.** The buyer, budget and problem were plausible enough to test.
- **Not advanced to `validation-ready`.** At 49.5 the scorecard is below the
  threshold and most hard filters are `unknown`; under method 1.2.0 an advance
  would also require every unknown to be named in a proposed experiment.
- **Parked at `desk-screened` with a proposed cheap experiment**, and a strong
  recommendation to spend the ~20 hours before committing months of building.
- **What actually happened:** the build started on 2025-07-30 with no recorded
  screening artefact, the public pricing page landed 2025-08-20, and
  distribution/retention questions were addressed later (SEO investment,
  case studies, channel work) after launch. The calibration point is not that
  the idea was bad — it is that the lab's cheapest test (distribution and
  willingness to run an auction) was available in July 2025 and went unrun.

## Leakage controls

Excluded from the scores above: Furzedown and Lingfield case studies, live
auction slugs, GSC/Cloudflare/acquisition analytics, the ~7 paid-auction figure,
the 2026 pricing-page copy and comparison guide, and all repository features
built after 2025-07-30. The current-state assessment and the comparison with
what subsequently happened are recorded separately in
`ideas/aucly/decision.md`.
