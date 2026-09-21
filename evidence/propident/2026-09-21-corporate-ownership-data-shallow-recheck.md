# Evidence: corporate ownership data - shallow seed re-check

- **Idea / scope:** seed `corporate-property-aml-monitor` (origin idea `propident`)
- **Register:** evidence
- **Source:** landregistry.company, GOV.UK Register of Overseas Entities collection, HMLR annual report and main estimate, Hansard, Practice Guide 78
- **Accessed / dated:** 2026-09-21
- **Credibility:** primary (GOV.UK/HMLR/Hansard) plus credible secondary (commercial mirror)

## Claim(s) supported

- HM Land Registry's Commercial and Corporate Ownership Data (CCOD) is commercially
  mirrored by landregistry.company (IntelTree Ltd) at £1.00 per title, with a £3.00
  premium director-history search; dataset v2026.04, last refresh 3 April 2026,
  3,814,226 titles indexed, 98,412 overseas entities.
- The Register of Overseas Entities (ECTEA 2022) amendment regulations on Protection and
  Trusts / LLPs were laid 1 June 2026 and debated 1 July 2026; HMLR Practice Guide 78 was
  updated 1 June 2026 and again around 20 August 2026.
- HMLR's Annual Report 2025-26 (HC 390, printed 13 July 2026) and Main Estimate 2026-27
  restate a multi-year plan to develop a geospatial land register combining geographic
  and ownership information; no release date is given for extending the companies
  identifier tables.
- No evidence was found that the specific "Companies/Overseas identifier tables" release
  the seed depends on has shipped.

## Exact detail

- landregistry.company home/data-source copy: "We mirror HM Land Registry's Commercial
  and Corporate Ownership Data (CCOD), refreshed monthly"; "v2026.04"; "3,814,226 titles
  indexed"; "98,412 overseas entities"; "£1.00 per title"; "£3.00 - premium director
  history". https://landregistry.company/
- GOV.UK Register of Overseas Entities collection (last updated 4 March 2025; guidance
  items dated 1 February 2026 and 9 July 2026):
  https://www.gov.uk/government/collections/register-of-overseas-entities
- Hansard, Draft Register of Overseas Entities (Protection and Trusts) and LLPs
  (Amendment) Regulations 2026, debated 1 July 2026:
  https://hansard.parliament.uk/commons/2026-07-01/debates/ef42b85e-2bb9-4b30-adcc-abde63f071b0/...
- HMLR Annual Report 2025-26 (HC 390, printed 13 July 2026):
  https://assets.publishing.service.gov.uk/media/6a6b7711862aaf18d9c62a77/HMLR_ARAC_2026_1307_WEB_2.pdf
- HMLR Main Estimate 2026-27 (multi-year geospatial land register plan):
  https://committees.parliament.uk/publications/52904/documents/295140/default

## Why it is credible

Primary government and parliamentary sources for the register and HMLR plans; the
commercial mirror is vendor-stated but its dataset version, refresh date and counts are
specific and checkable.

## What it does NOT show

- It does not show that identifier tables for UK/Overseas Companies data have been
  released, nor when they will be.
- It does not establish that small conveyancers would pay for ongoing AML monitoring on
  top of the existing £1/title lookup and free public registers.

## Links

- Used by: `seeds/corporate-property-aml-monitor.md` (Outcome row, 2026-09-21)
- Used by: `ideas/propident/scorecard.json` (prior run defeat remains in force)
