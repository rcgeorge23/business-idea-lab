# WasteTrack: receiver-side digital waste tracking records

- **ID / slug:** `wastetrack`
- **State:** `killed`
- **Evidence level:** `Plausible`
- **Owner:** worker
- **Created:** 2026-09-21
- **Updated:** 2026-09-21
- **Source:** worker run `20260921T081223Z-normal` (fresh discontinuity hunt; legislation/regulation class)

## One-sentence proposition

> Permitted waste facility operators (and later waste carriers, brokers and dealers)
> must keep and submit digital waste records within two working days from 1 October 2026;
> we provide a low-cost receiver-side record-keeping and submission tool at a monthly
> subscription.

## Why now?

> This was not an attractive business three years ago, but it might be now because the
> Digital Waste Tracking (England) Regulations 2026 were made on 24 June 2026 and come
> into force on 1 October 2026, creating a mandatory, dated record-keeping duty.

- What changed: SI 2026/729 was made and the GOV.UK digital waste tracking service moved
  to public beta; digital records and two-working-day submission become mandatory.
- When it changed (or is due to change): made 24 June 2026; in force 1 October 2026
  (England); Phase 2 for carriers/brokers/dealers October 2027.
- Evidence (dated source), and why the change is real rather than a trend: primary
  legislation and a GOV.UK service with a published Defra-approved-provider list
  (`evidence/wastetrack/2026-09-21-digital-waste-tracking-mandate-and-crowding.md`).
- Why this materially improves the opportunity now: it creates a compliance deadline
  that did not exist three years ago, with a captive population of permitted sites.
- Have competitors already responded? Yes, decisively: 54-79 approved providers are
  already listed/compared, several with free or near-free tiers, including a weighbridge
  vendor and a "companion, not a replacement" carrier tool.
- Strength: `strong`

## Buyer

- Who exactly pays (role, company size, segment): operators of permitted waste
  facilities (approx. 12,000) in England; later waste carriers, brokers and dealers
  (approx. 300,000 registered).
- Who uses it: weighbridge/yard staff and site administrators.
- Evidence: GOV.UK service guidance and Defra provider list (see evidence register).

## Problem

- What is painful/frequent/expensive: a mandatory, recurring (per-load) record and
  two-working-day submission duty with a £26/year operator fee and correction duties.
- Current alternatives and their weaknesses: a large approved-provider market plus a
  spreadsheet fallback the government expects to remain until at least October 2027;
  weighbridge and waste-management incumbents bundle tracking into existing systems.
- Evidence: see evidence register.

## Mechanism / wedge

- What we would actually do: a receiver-side digital waste record tool integrating the
  report-receipt-of-waste API, with approval-test compliance, at a low monthly price.
- Why it is defensible against the cheapest credible incumbent: it is not. The
  approved-provider list already contains 54-79 providers, free tiers exist, and
  weighbridge/waste-management vendors bundle the function. This is the kill reason.
- Evidence: see evidence register.

## Novelty / incumbent sanity check

| Check | Answer | Evidence |
|---|---|---|
| Does this exact product already exist? | Yes | BreakerHQ provider comparison (18 Aug 2026); Defra approved-software list |
| Are there multiple credible providers? | Yes - 54 to ~79 | `evidence/wastetrack/2026-09-21-digital-waste-tracking-mandate-and-crowding.md` |
| Is the wedge already a standard feature? | Yes - bundled with weighbridge/waste-management systems | Same |
| Is a free/authoritative alternative already adequate? | Yes - free tiers (IntelliWaste, Simple Digital Waste Tracking) and a government spreadsheet fallback to at least Oct 2027 | Same |
| Has a well-capitalised company shown hostile unit economics? | Not shown | - |
| Is this merely a feature of an established category? | Yes - waste-management/weighbridge software | Same |

If any check fails, state the reason to continue anyway: none - the checks fail
decisively, so the idea is killed on `defensible_wedge`. The only residual interest is
the deferred UK/EU cross-border (green-list/DIWASS) gap, recorded as a non-inheriting
seed.

## Distribution

- Route to the first 10 buyers without paid acquisition: trade bodies (CIWM), waste
  sector search, weighbridge-installer partnerships - plausible but unproven for a new
  entrant against embedded incumbents.
- Evidence: none gathered; left unresolved because the wedge fail kills the idea first.

## Economics (assumptions labelled)

- Price hypothesis: £15-£40/month per site (assumption, not evidenced).
- Cost drivers: API integration, Defra approval testing, support, ongoing regulatory
  change.
- Contribution margin at realistic scale: modelled only; incumbents' free tiers and the
  £26/year statutory fee anchor pricing downward. Capped at 2.

## Founder fit

- Reach, skills, motivation (evidence only; `null` if unknown):
  `null` - no evidence about the founder's reach into waste-management operations.

## Adversarial case (strongest case this is wrong)

The mandate is real and dated, but the market has already formed around it. A new
entrant would have to displace 54-79 approved providers, at least two of which are free,
and compete with weighbridge and waste-management systems that bundle tracking into a
system the operator already runs. The government's own spreadsheet fallback remains
valid until at least October 2027, further suppressing urgency to buy. There is no
plausible wedge for a newcomer on the receiver side, and the surviving question
(cross-border green-list movements) is a different regime, buyer and product.

## Strongest supporting case

The discontinuity is genuinely strong and the population is large (12,000 permitted
sites; 300,000 carriers/brokers/dealers from October 2027), and the two-working-day
submission duty with correction duties creates recurring workflow, not a one-off filing.
A very low-cost, opinionated receiver tool could still win share on usability if the
incumbents' free tiers prove loss-leaders that reprice - but that is speculation, not
evidence.

## Unresolved assumptions

| Assumption | How it could be falsified | Status |
|---|---|---|
| A newcomer can win share against 54-79 incumbents including free tiers | Test demand with receivers; observe incumbent repricing | Untested; killed before test because the wedge check failed |

## Cheapest decisive experiment

- Assumption under test: not reached - killed at the novelty/incumbent check.
- Proposed test: none (no experiment proposed for a killed idea).
- Pre-fixed decision rule: n/a
- Cost bound: n/a
- Status: none
- Link: n/a

## Decision log (append-only)

| Date | State change | Why | Link |
|---|---|---|---|
| 2026-09-21 | created -> killed | `defensible_wedge` fail: 54-79 approved providers, free tiers, bundled weighbridge/waste-management incumbents, free spreadsheet fallback until at least Oct 2027 | `ideas/wastetrack/decision.md` |
