# GrantScout: matched UK grant digest for small businesses

- **ID / slug:** `grantscout`
- **State:** `killed`
- **Evidence level:** `Plausible`
- **Owner:** worker
- **Created:** 2026-09-20
- **Updated:** 2026-09-20
- **Source:** worker run `20260920T210550Z-normal` (calibration fixture: attractive control that should survive desk screening and fail adversarial review)

## One-sentence proposition

> UK SMEs miss grant funding because eligible schemes are hard to find and interpret; we provide a monthly matched grant digest at £19/mo.

## Buyer

- Who exactly pays: SME owner/director, or their accountant/adviser on their behalf.
- Who uses it: owner, finance lead or bookkeeper.
- Evidence: `evidence/grantscout/2026-09-20-incumbent-pricing-and-contingency.md`

## Problem

- What is painful/frequent/expensive: grant discovery and applications are time-consuming with long, competitive processes; missing funding is a direct, quantified loss (GOV.UK guidance).
- Current alternatives and their weaknesses: GOV.UK "Find a grant" is free and improving; success-fee consultancies win work only on award; GovOwed sells a £29 one-time report.
- Evidence: `evidence/grantscout/2026-09-20-free-government-grant-discovery.md`

## Mechanism / wedge

- What we would actually do: maintain a UK grant database, match by sector/size/region, and send a plain-language monthly digest with eligibility and deadlines.
- Why it is defensible against the cheapest credible incumbent: **it is not.** The free government service covers discovery (the stated pain), and GovOwed already sells the flat-fee report wedge at £29 one-time / £499 per year for accountants.
- Evidence: `evidence/grantscout/2026-09-20-incumbent-pricing-and-contingency.md`

## Distribution

- Route to the first 10 buyers without paid acquisition: accountant/adviser channel, small-business networks and communities, and SEO/benchmark content — plausible but unmeasured.
- Evidence: `evidence/grantscout/2026-09-20-free-government-grant-discovery.md`

## Economics (assumptions labelled)

- Price hypothesis: £15–£29/mo (Assumption).
- Cost drivers: content maintenance, matching quality, support.
- Contribution margin at realistic scale: plausible on paper (low content cost), but the price is anchored to £0 (government) and £29 one-time (GovOwed), and consultancy pricing is contingency-based.

## Founder fit

- Reach, skills, motivation: `null` — no evidence recorded.

## Adversarial case (strongest case this is wrong)

This was the run's attractive control, and it fails on the wedge. The one thing the idea proposes to sell — a searchable, matched list of grants — is already provided for free by the government ("Find a grant"), and GOV.UK is explicitly expanding it. The paid flat-fee version already exists at GovOwed for £29 one-time, including drafted applications and 12 months of re-runs, and £499/year for accountants — precisely the channel this idea would use for distribution. Advisers themselves price on success/contingency, so the customer's reference price for a *paid* service is "pay only if you win", which a £19/mo subscription contradicts. The value is not in discovery (free) but in application quality and win rate — a service business, not a digest. There is no defensible position between free government discovery and contingency-fee advisers.

## Strongest supporting case

The underlying need is real and expensive to miss, SMEs demonstrably seek grant help, and GovOwed's existence shows at least one operator believes a flat-fee model can work. A wedge around win-rate improvement (rather than discovery) could be materially distinct — but that is a different idea.

## Unresolved assumptions

| Assumption | How it could be falsified | Status |
|---|---|---|
| SMEs will pay for discovery the government gives away | Price test against the free service | Weakened at desk screen; vetoed |
| Accountants will resell a digest | Ask 10 accountants to commit | Untested |
| Matching quality beats free search | Blind comparison | Untested |
| The real pain is application quality, not discovery | Interviews | Open (points to a different idea) |

## Cheapest decisive experiment

- Assumption under test: SMEs will pay a subscription for grant matching.
- Proposed test: not pursued — the adversarially-identified veto (wedge already occupied; free authoritative alternative) makes the test redundant; a landing-page test would have been the cheapest check had the wedge survived.
- Pre-fixed decision rule: n/a.
- Cost bound: n/a.
- Status: not proposed
- Link: n/a

## Decision log (append-only)

| Date | State change | Why | Link |
|---|---|---|---|
| 2026-09-20 | `discovered` -> `desk-screened` | All nine hard filters passed and dated sources supported the problem; attractive control retained for adversarial review. | `ideas/grantscout/decision.md` |
| 2026-09-20 | `desk-screened` -> `killed` | Adversarial pass recorded an active veto on `defensible_wedge`: the flat-fee wedge is occupied by GovOwed and the authoritative discovery alternative (GOV.UK) is free. | `ideas/grantscout/decision.md` |
