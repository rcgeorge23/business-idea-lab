# Seed: Ongoing AML monitoring of corporate property ownership for small conveyancers

- **Seed ID / slug:** corporate-property-aml-monitor
- **Origin idea:** propident
- **Recorded:** 2026-09-21
- **Status:** unexplored

## Observation

HM Land Registry is adding UPRN/INSPIRE identifiers to Price Paid Data (live
28 August 2026) and plans the same for UK Companies and Overseas Companies data
later in FY2026-27. Combined with Economic Crime Act beneficial-ownership
obligations, this could support ongoing monitoring of corporate property
ownership changes rather than a one-off title lookup.

## Why this is materially different

It is a monitoring/ongoing-compliance service for smaller conveyancing firms,
not a commodity data index. It depends on a future dataset release (the
companies identifier tables) and a specific AML job, and would be evaluated on
alerting and workflow rather than lookup price.

## Evidence

- `evidence/propident/2026-09-21-hmlr-identifiers-and-incumbents.md`

## Non-inheritance

This seed does not inherit propident's score, confidence or evidence level. Any
promotion requires its own research, dossier, evidence register and scorecard.

## Outcome (append-only)

| Date | Status | Note |
|---|---|---|
| 2026-09-21 | unexplored | Shallow re-check (run `20260921T081223Z-normal`): no evidence found that the Companies/Overseas identifier tables this seed depends on have shipped; the existing propident defeat (landregistry.company at £1.00/title, CCOD v2026.04, 3,814,226 titles, 98,412 overseas entities) still stands. Remains undeveloped and blocked on the dataset release. See `evidence/propident/2026-09-21-corporate-ownership-data-shallow-recheck.md`. |
| 2026-09-27 | unexplored | Fresh shallow re-check in run `20260927T064618Z-normal`: HMLR's Price Paid Data identifier milestone is confirmed (UPRN/INSPIRE IDs from 2026-08-28), but current broad GOV.UK searches did not resolve whether the UK-company/Overseas Companies identifier tables have shipped. This is not evidence that they have not shipped. No buyer workflow, willingness-to-pay or evidence of an underserved monitoring gap was found. Remains unexplored and inherits no score/evidence from `propident`; see `observations/20260927T064618Z-normal.md` O2. |
