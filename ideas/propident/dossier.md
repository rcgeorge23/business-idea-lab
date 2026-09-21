# Corporate-property ownership intelligence on HMLR property identifiers

- **ID / slug:** propident
- **State:** killed
- **Evidence level:** Plausible
- **Owner:** worker
- **Created:** 2026-09-21
- **Updated:** 2026-09-21
- **Source run:** `20260921T075410Z-normal`

## One-sentence proposition

> HM Land Registry began publishing UPRN and INSPIRE lookup tables alongside
> Price Paid Data in August 2026 and will extend them to UK and Overseas
> Companies data later in the financial year, which makes corporate-property
> ownership analysis easier - but the data is open-licensed and an
> already-commercial index plus enterprise data providers occupy the job.

## Why now?

- **What changed:** HM Land Registry started shipping property identifiers as
  separate lookup tables with its monthly Price Paid Data, with UK Companies and
  Overseas Companies data to follow later in FY2026-27.
- **Changed date:** 2026-08-26 (announcement); 2026-08-28 (in effect for Price
  Paid Data).
- **Evidence:** `evidence/propident/2026-09-21-hmlr-identifiers-and-incumbents.md`
  (HMLR press release; landregistry.company CCOD index).
- **Why it materially improves the opportunity:** reliable UPRN linkage removes
  matching pain for anyone analysing property ownership or corporate holdings.
- **Did competitors respond?** Yes. landregistry.company already mirrors HMLR's
  Commercial and Corporate Ownership Data, cross-references Companies House
  directors, and sells title lookups at £1.00 (plus a £3.00 director-history
  search); enterprise providers (Landmark, Search Acumen, Orbital Witness) sit
  in the same space.
- **Strength:** strong (a genuine dataset change) but of weak commercial
  relevance.

## Novelty / incumbent sanity check

| Question | Evidence | Reason to continue / stop |
| --- | --- | --- |
| Does an exact product already exist? | landregistry.company sells CCOD + Companies House cross-reference | Stop |
| Are there multiple credible providers? | landregistry.company plus enterprise property-data vendors | Stop |
| Is the wedge already a standard feature? | Programme/analytics vendors routinely join HMLR and Companies House data | Stop |
| Is there an adequate free/authoritative alternative? | The underlying data is Open Government Licence and free | Stop |
| Has a well-capitalised company shown hostile unit economics? | Commodity data resale with a £1/title anchor | Stop |
| Is it merely a feature of an established category? | Yes - a feature of property-data and AML/KYC platforms | Stop |

**Outcome:** Fails the novelty check. The identifiers are an enabling change
that lowers cost for everyone, not a wedge. Recorded adjacent observation as a
seed candidate rather than pursued.

## Buyer

Conveyancing due-diligence teams, AML/KYC compliance functions, lenders and
property analysts. Buyer clarity is weak: much of the need is met by existing
subscriptions or by joining open data in-house.

## Problem

Linking corporate proprietors to titles and then to beneficial ownership is
genuinely hard, but it is already solved commercially and the marginal
improvement from UPRN linkage accrues to incumbents.

## Mechanism / wedge

Envisaged mechanism: a searchable index of corporate-owned titles with
Companies House and Overseas Entities cross-reference and monitoring alerts.
No defensible wedge: the same index already exists at commodity prices, and
open licensing invites substitution.

## Distribution

Search-driven and via professional software; dominated by established data
vendors and existing conveyancing toolchains.

## Economics (assumptions labelled)

- *Assumption:* buyers would pay a subscription rather than self-join open data
  or use a £1/title search.
- *Evidence:* landregistry.company charges £1.00/title and £3.00 for a premium
  director-history search; underlying data is OGL.
- *Inference:* commodity pricing with no evidence of willingness to pay for a
  new entrant. Economics unsupported.

## Founder fit

Not assessed in depth (killed at novelty/filter stage).

## Adversarial case (strongest case this is wrong)

The strongest case is that the forthcoming UK and Overseas Companies identifier
tables could enable an AML monitoring product for corporate property ownership
that is not yet packaged for smaller conveyancers. But that job is speculative,
enterprise vendors are positioned for it, and no buyer evidence was found that
they are under-served.

## Strongest supporting case

A fresh, dated, official dataset enhancement with a clear analytical use - but
one that commoditises rather than differentiates.

## Unresolved assumptions

| Assumption | How it could be falsified | Status |
| --- | --- | --- |
| Buyers will pay a new entrant rather than self-join open data | Test pricing against the £1/title incumbent | Unresolved |
| A company-property ownership linkage job is unmet | Interview conveyancers about current tooling | Unresolved |

## Cheapest decisive experiment

None proposed. Killed on `defensible_wedge` (open data, existing commercial
index, commodity pricing). If revisited, the cheapest decisive test is a paid
pilot with a hand-built corporate-property report for one conveyancing firm.

## Decision log (append-only)

| Date | State change | Why | Link |
| --- | --- | --- | --- |
| 2026-09-21 | (new) -> discovered | Candidate from HMLR property-identifier discontinuity | this file |
| 2026-09-21 | discovered -> killed | `defensible_wedge` fail: open-licensed data plus an existing £1/title index and enterprise vendors | `decision.md` |
