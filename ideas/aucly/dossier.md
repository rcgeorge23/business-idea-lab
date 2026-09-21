# Aucly: flat-fee online auction platform for UK schools, PTAs and charities

- **Idea ID / slug:** `aucly`
- **State:** `adversarially-researched` (parked)
- **Evidence level:** `Commercial evidence` (early; roughly seven paid auctions, owner-supplied and unverified)
- **Calibration case:** evaluated for issue #3. The pre-launch reconstruction is a
  separate document: `ideas/aucly/pre-launch-assessment.md`.
- **Updated:** 2026-09-21 · **Method version:** 1.2.0

## One-sentence proposition

Aucly is a self-service online auction platform for UK schools, PTAs and small
charities, charging a flat fee per paid auction (£60/£120) with no commission on
winning bids, so organisers keep the full proceeds.

## Why now?

- **Strength:** absent — recorded honestly.
- **What changed:** nothing favourable changed. Fundraising auctions and
  auction platforms for schools/PTAs predate Aucly by years; the flat-fee model
  is a positioning choice, not a discontinuity.
- **When:** n/a (`changed_date` null).
- **Evidence:** `evidence/aucly/2026-09-21-competitive-landscape.md`,
  `evidence/aucly/2026-09-21-build-and-operating-burden.md`.
- **Why it matters:** with no why-now, the case has to rest on demonstrated
  execution and operating evidence rather than a category shift. Under method
  1.2.0 the missing why-now cap is lifted because the idea reached `Commercial
  evidence`, so the idea is judged on that evidence; pre-launch (Plausible) it
  would have capped `problem_severity_frequency` and `differentiation` at 2.
- **Competitors responded:** incumbents are entrenched (Jumblebee, PTA Events
  reporting £40m processed, GalaBid, Givergy, Generosity Works); none needed to
  respond to Aucly's entry.

## Buyer

PTA chairs and committees, school fundraisers/business managers, and small
charity organisers with control of an event budget. For a typical school
auction this is a volunteer or part-time organiser, not procurement. Pricing
evidence: Free (15 items), Standard £60 (50 items), Unlimited £120, one-off per
paid auction.

## Problem

Running a good fundraising auction is effortful — collecting lots, managing
bidding, collecting payments and chasing winners — and commission-based or
managed platforms either take a slice of proceeds or require budget. Organisers
of small/medium auctions plausibly want a self-service tool that keeps proceeds
intact. The problem is real for the recorded customers; dissatisfaction with
incumbents is not evidenced.

## Mechanism/wedge

Flat fee, no commission, no bidder tips; free tier to build confidence; Stripe
card links or offline payment tracking, direct to the organiser; proxy bidding
and post-sale winner management; case-study social proof.

## Novelty / incumbent sanity check

| Check | Answer | Notes |
|---|---|---|
| Exact product already exists? | Yes | Jumblebee, PTA Events, GalaBid and others run school/PTA auctions today |
| Multiple credible providers? | Yes | Six compared in Aucly's own guide; PTA Events reports £40m processed |
| Wedge is already a standard feature? | Partly | Free plans (GalaBid, beeFree) cover part of it; flat fee without commission is not universal |
| Authoritative free alternative adequate? | Unknown | Free tiers exist; whether they satisfy this buyer is untested |
| Well-capitalised company showed hostile economics? | Not demonstrated | No evidence found |
| Merely a feature of an established category? | Risk | PTA platform suites bundle auctions with events/ticketing/comms |
| Reason to continue | Real auctions with real amounts raised and named customers show the offer works for some organisers; the open question is repeatable unpaid acquisition |

## Distribution

Current evidence is negative: a sustained SEO effort (blog, landing pages)
produced 45 GSC clicks and 2,333 recorded visitors in the export window with
0 accounts, 0 auctions launched and £0 revenue, and most traffic is brand
queries. No unpaid channel has demonstrated it reaches organisers. Direct
outreach is untested and is the subject of the proposed experiment
(`experiments/aucly-channel-test/plan.md`).

## Economics

Flat one-off pricing caps revenue per organiser per event; there is no
commission tail. Roughly seven paid auctions are owner-supplied and unverified
(no lifetime export found). Hosting (Railway, Postgres/Redis), email (Brevo) and
a continuing founder maintenance burden are real costs; per-auction contribution
is not quantified. Modelled-only economics cap the score at 2.

## Founder fit

The founder built and continues to operate the product, shipping a broad feature
set and handling real customer workflows — evidenced execution fit. Domain
access, sales capacity and founder-time economics are not evidenced. Score 3.

## Strongest supporting case

Real organisers used the platform for real events: Furzedown Primary PTA
auctioned 44 lots to 63 unique bidders, taking 1,074 bids and raising £2,265,
and a Lingfield Foundation golf-day auction raised £2,500 with a positive
organiser quote. Active auctions appear in first-party analytics. The category
demonstrably moves money (competitors charge commission or fees; PTA Events
reports £40m processed). The build and payment plumbing are done, and the
£0/£60/£120 flat-fee offer is simple and priced below typical incumbents'
commission on a £2,000+ auction.

## Adversarial case (strongest case this is wrong)

Distribution is failing in the one channel that has been measured: after
substantial SEO work, a recorded window of 2,333 visitors produced zero
accounts, zero launches and zero revenue, and commercial queries have zero
clicks. The category is occupied by entrenched providers with network effects
and reputation, and free plans blunt the flat-fee wedge. The economics are
structurally small — one-off £60/£120 per event with no commission tail and a
heavy maintenance burden — and neither retention, market size nor founder-time
contribution is evidenced. On this evidence Aucly could be a technically
excellent, well-loved small project that never becomes a worthwhile business,
and the honest reading of the ~7 paid auctions is early evidence, not
validation.

## Unresolved assumptions

| Ref | Assumption | Status 2026-09-21 | Resolve via |
|---|---|---|---|
| A1 | Organisers feel enough pain with incumbents to switch | Unknown | win/loss questions in the channel test |
| A2 | Flat fee is more attractive than commission to this buyer | Unknown | price-model reaction in the channel test |
| A3 | Organisers can be reached without paid acquisition | Negative so far (0 accounts from 2,333 visitors) | aucly-channel-test |
| A4 | A volunteer can self-serve an auction with low support | Partially evidenced (Furzedown, Lingfield ran with limited help) | support load recorded per launch |
| A5 | £60/£120 per auction yields workable contribution | Unknown | hosting/email cost + founder hours per auction |
| A6 | Organisers return in a second year | Unknown | retention follow-up after experiment |
| A7 | Enough UK PTAs/schools/charities run auctions | Unknown | market sizing from public data; incumbent scale |

## Cheapest decisive experiment

`aucly-channel-test` (proposed, awaiting human approval): approach 20 UK PTAs
outside the founder's network through organisational contact addresses, with the
Furzedown case study and free setup help; proceed only if at least 2 launch a
real auction within 30 days at zero paid spend. Cost bound: ~20 human hours,
£0, 30 days. It tests the central assumption (unpaid distribution) and gives
win/loss input on the wedge.

## Decision log

| Date | Change | Reason | Actor |
|---|---|---|---|
| 2025-07-30 | Build started (outside the lab) | No recorded screening artefact; recorded here for calibration | founder (historical) |
| 2026-09-21 | Added to ledger as calibration case; scored 60.0; parked at `adversarially-researched`; experiment proposed | Issue #3: early commercial evidence but unproven sustainability; below threshold 65; remaining unknowns named in the proposed experiment | worker |
