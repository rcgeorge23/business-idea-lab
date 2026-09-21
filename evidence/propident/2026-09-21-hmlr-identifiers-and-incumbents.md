# Evidence register — HM Land Registry property-identifier lookup tables (new dataset)

- Idea: `propident`
- Run: `20260921T075410Z-normal`
- Date: 2026-09-21
- Register type: evidence + inference (append-only)

## Evidence (dated external sources)

| # | Source | Publisher | Date | URL | What it establishes |
|---|--------|-----------|------|-----|---------------------|
| E1 | "HM Land Registry to provide property identifiers for Price Paid Data from 28 August" | HM Land Registry / GOV.UK | 26 Aug 2026 | https://www.gov.uk/government/news/hm-land-registry-to-provide-property-identifiers-for-price-paid-data-from-28-august | From 28 Aug 2026, UPRNs and INSPIRE IDs are provided in separate lookup tables alongside monthly Price Paid Data; UK Companies data and Overseas Companies data are to get similar lookup tables later in the financial year. |
| E2 | landregistry.company — UK Corporate Land Registry Search | landregistry.company | accessed 21 Sep 2026; dataset refresh 3 Apr 2026 | https://landregistry.company/ | Existing commercial product: searchable index of HM Land Registry Commercial and Corporate Ownership Data (CCOD), 3,814,226 titles indexed, cross-referenced with Companies House director history; £1.00 per title, £3.00 premium search; CCOD listed under Open Government Licence. |

## Inference (conclusions citing the above)

- I1 (from E1): A genuine, dated dataset discontinuity exists — property transactions and (later) corporate ownership data gain stable identifiers, which lowers the cost of deterministic joins versus fuzzy address matching. (confidence: high)
- I2 (from E1, E2): The underlying data is published free under the Open Government Licence, and at least one commercial product already indexes CCOD with Companies House cross-references at low unit prices; enterprise property-data providers (Landmark, Search Acumen, Orbital Witness) serve the same market. There is no evidenced buyer urgency or defensible wedge. (confidence: medium)
- I3: This is an enabling change, not a mandated or painful one; no buyer has been shown to have a budget or deadline tied to it. (confidence: medium)

## Assumptions (falsifiable, not evidence)

- A1: A buyer would pay for pre-joined identifier tables rather than build the join themselves from the free OGL files. Falsified by five buyer interviews showing they already join the data in-house.
- A2: Conveyancers/lenders have an unmet need for corporate-property linkage. Unverified.

## Unresolved

- Whether the forthcoming Companies/Overseas Companies lookup tables will be joined to the Register of Overseas Entities in a way that creates a new AML verification job.
