# PRS Database registration and marketing-readiness for letting agents and landlords

- **ID / slug:** prsregister
- **State:** killed
- **Evidence level:** Plausible
- **Owner:** worker
- **Created:** 2026-09-21
- **Updated:** 2026-09-21
- **Source run:** `20260921T075410Z-normal`

## One-sentence proposition

> The England PRS Database begins regional rollout on 15 December 2026 and from
> that point agents may not market a rental without active Landlord and
> Property Registration Numbers, so readiness tooling for agents and landlords
> could be sold - but the government provides the register itself and cheap
> (£19/month) and incumbent readiness products already exist.

## Why now?

- **What changed:** The Private Rented Sector Database Regulations 2026 were
  laid in draft, operationalising the register created by the Renters' Rights
  Act 2025, with a region-by-region rollout and an agent marketing prohibition.
- **Changed date:** 2025-10-27 (Royal Assent); 2026-05-01 (Part 1 in force);
  rollout from 2026-12-15.
- **Evidence:** `evidence/prsregister/2026-09-21-prs-database-and-incumbents.md`
  (draft regulations, RRA 2025, Lettable, Homelet/Property Week/Independent
  Landlord/LandlordZONE/Ultralets, agent software set).
- **Why it materially improves the opportunity:** a dated, mandatory
  registration and pre-marketing check with penalties, and an annual per-property
  fee, create urgency for every landlord and agent in England.
- **Did competitors respond?** Yes. Lettable markets "the compliance operating
  system for letting in 2026" with a PRS Database readiness assessment at
  £19/month; Goodlord, Fixflo, OpenRent, Landlord Vision, Arthur, Homelet and
  NRLA all sit in the same workflow; EveryGuard builds the same pattern for
  care homes, nurseries, hotels and letting agents.
- **Strength:** strong.

## Novelty / incumbent sanity check

| Question | Evidence | Reason to continue / stop |
| --- | --- | --- |
| Does an exact product already exist? | Lettable PRS Database readiness; incumbents' compliance suites | Stop |
| Are there multiple credible providers? | Lettable plus Goodlord/Fixflo/OpenRent/Homelet/Landlord Vision | Stop |
| Is the wedge already a standard feature? | Readiness/checklist features are standard in letting software | Stop |
| Is there an adequate free/authoritative alternative? | The GOV.UK register itself (with a paper route) plus free guidance | Stop |
| Has a well-capitalised company shown hostile unit economics? | £19/month anchor against a free core register | Stop |
| Is it merely a feature of an established category? | Yes - a feature of letting-agent CRM/compliance suites | Stop |

**Outcome:** Fails the novelty check. The one evidenced gap - no bulk
upload/API for agents at launch - is a feature an incumbent can add, not a
company. Recorded as a seed (`prs-listing-precheck`) rather than pursued.

## Buyer

Letting agents (especially small/independent) and self-managing landlords in
England, beginning with the West Midlands rollout region.

## Problem

Landlords must create and maintain mandatory database entries; agents cannot
market a property without current registration numbers. Real but low-complexity
and close to the government's own service.

## Mechanism / wedge

Envisaged mechanism: assemble and store registration numbers and certificate
evidence, chase landlords, and pre-check listings before marketing. All of these
are already standard features of letting software or trivially added to them.

## Distribution

Trade bodies (NRLA, Propertymark), regional agent networks and portals - routes
already used by incumbents, and the register itself is self-serve.

## Economics (assumptions labelled)

- *Assumption:* agents/landlords will pay a subscription rather than use the
  free register and a spreadsheet.
- *Evidence:* Lettable prices readiness at £19/month; the register fee
  (~£65/property/year) flows to the operator, not a tool vendor.
- *Inference:* thin, commoditised subscription with no defensible margin.

## Founder fit

Not assessed in depth (killed at novelty/filter stage).

## Adversarial case (strongest case this is wrong)

The strongest case is the pre-marketing prohibition: agents face real risk if a
listing goes live without a valid number, and the absence of a bulk/API path
means work per property. But incumbents already own agent workflows and the
government service is free; the incremental value of a standalone tool is too
small to displace them.

## Strongest supporting case

A precise, dated, mandatory English property regulation with a named buyer and
a phased rollout - a strong "why now?" that nevertheless lands in an already
well-served market.

## Unresolved assumptions

| Assumption | How it could be falsified | Status |
| --- | --- | --- |
| Agents/landlords will pay for readiness tooling | Landing-page test against the free register; Lettable's pricing already anchors low | Unresolved |
| No bulk/API route will appear at launch | Watch the operator's launch guidance for a bulk/API path | Unresolved |

## Cheapest decisive experiment

None proposed. Killed on `defensible_wedge` (commodity positioning; free
authoritative alternative; multiple providers). If revisited, the cheapest
decisive test is a listing pre-check offered to small agents in the first
rollout region, measured against incumbents.

## Decision log (append-only)

| Date | State change | Why | Link |
| --- | --- | --- | --- |
| 2026-09-21 | (new) -> discovered | Candidate from PRS Database regulations | this file |
| 2026-09-21 | discovered -> killed | `defensible_wedge` fail: commodity readiness feature; free government register; incumbents priced at £19/month | `decision.md` |
