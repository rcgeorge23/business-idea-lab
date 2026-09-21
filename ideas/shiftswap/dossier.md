# ShiftSwap: last-minute shift cover for UK hospitality

- **ID / slug:** `shiftswap`
- **State:** `killed`
- **Evidence level:** `Plausible`
- **Owner:** worker
- **Created:** 2026-09-20
- **Updated:** 2026-09-20
- **Source:** worker run `20260920T210550Z-normal` (calibration fixture: weak/rejected candidate expected to die on hard filters)

## One-sentence proposition

> UK hospitality venues lose shifts to last-minute absences; we provide a standalone last-minute shift-cover service at a low monthly fee.

## Buyer

- Who exactly pays: venue owner/GM of a small group (1–5 sites).
- Who uses it: duty managers and hourly staff.
- Evidence: `evidence/shiftswap/2026-09-20-incumbent-rota-software.md`

## Problem

- What is painful/frequent/expensive: uncovered shifts force managers to phone around and can mean closing sections; UK hospitality lost ~89,000 jobs since Oct 2024 and vacancies remain elevated (ONS/UKHospitality).
- Current alternatives and their weaknesses: existing rota tools already include self-service shift swaps; informal WhatsApp groups are free.
- Evidence: `evidence/shiftswap/2026-09-20-uk-hospitality-labour-market.md`

## Mechanism / wedge

- What we would actually do: a standalone app/marketplace where staff offer shifts and others claim them, with reminders and manager approval.
- Why it is defensible against the cheapest credible incumbent: **it is not** — RotaApp, RotaHub, RotaKeep, ClockRota, BatchStaff and others already bundle this, several at £0–£10/mo.
- Evidence: `evidence/shiftswap/2026-09-20-incumbent-rota-software.md`

## Distribution

- Route to the first 10 buyers without paid acquisition: none identified that reaches both venues and their staff at once.
- Evidence: `evidence/shiftswap/2026-09-20-incumbent-rota-software.md`

## Economics (assumptions labelled)

- Price hypothesis: £10–£29/mo per venue (Assumption).
- Cost drivers: support, notifications, two-sided onboarding.
- Contribution margin at realistic scale: implausible — advertised alternatives at £0/£9/£10/£49 per month leave no defensible price above acquisition cost.

## Founder fit

- Reach, skills, motivation: `null` — no evidence recorded.

## Adversarial case (strongest case this is wrong)

This is a commodity feature, not a product. Every low-cost UK rota tool already gives staff self-service swap; building a standalone marketplace asks venues to adopt a second system for a job their existing tool does, and asks staff to install yet another app for a benefit their rota app already provides. Worse, the value depends on density — enough staff at enough venues participating — so a launch in a thin market has no cover to offer and churns immediately. A contracting labour market (falling headcount, cut hours) reduces both the need for extra cover and the budget to pay for it.

## Strongest supporting case

The labour-market data are real and current: ONS-derived job losses, elevated vacancies and 35% labour-cost ratios mean unfilled shifts genuinely hurt. A concierge service in one dense city could create value quickly if it reached staff directly.

## Unresolved assumptions

| Assumption | How it could be falsified | Status |
|---|---|---|
| Venues would pay for cover on top of existing rota tools | Ask 10 venues to pay after a two-week free trial | Untested |
| Staff would adopt a second app | Measure repeat claims without manager nagging | Untested |
| A non-paid channel can reach both sides | Attempt to recruit 50 staff without paid marketing | Untested |
| Price above £10/mo is sustainable | Competitor pricing offers | Falsified at desk screen |

## Cheapest decisive experiment

- Assumption under test: venues will pay for standalone shift cover.
- Proposed test: not pursued — the idea was killed at hard-filter stage; no experiment is justified.
- Pre-fixed decision rule: n/a.
- Cost bound: n/a.
- Status: not proposed
- Link: n/a

## Decision log (append-only)

| Date | State change | Why | Link |
|---|---|---|---|
| 2026-09-20 | `discovered` -> `killed` | Hard filters failed on non-paid distribution, defensible wedge, network effects, margins and all-optimistic case; commodity incumbents bundle the feature. | `ideas/shiftswap/decision.md` |
