# Decision record: Corporate-property ownership intelligence on HMLR property identifiers

- **Idea:** propident
- **Date:** 2026-09-21
- **Run:** `20260921T075410Z-normal`
- **Decision:** Kill
- **State change:** discovered -> killed
- **Actor:** worker

## What changed

New candidate generated from the HM Land Registry property-identifier
discontinuity. Registered, scored and killed because the underlying data is
open-licensed and an existing commercial index plus enterprise vendors already
occupy the job.

## Why now? discovery gate

Strong but commercially weak. HMLR press release 2026-08-26; UPRN/INSPIRE lookup
tables live for Price Paid Data from 2026-08-28; UK and Overseas Companies data
to follow later in FY2026-27. A genuine dataset change, but an enabling one.

## Hard filters

| Filter | Status | Note |
| --- | --- | --- |
| economic_buyer | unknown | Conveyancing/AML teams identified but payment for a new entrant unproven. |
| painful_frequent_or_budgeted | unknown | Ownership questions occur, but frequency/budget unmeasured. |
| non_paid_distribution | unknown | Search-led acquisition untested in this niche. |
| defensible_wedge | fail | Open data + existing £1/title index + enterprise vendors. |
| no_network_effects_needed | pass | Single-sided data product. |
| plausible_margins | unknown | Commodity data pricing. |
| acceptable_risk | pass | Public data; no regulated activity. |
| cheap_disconfirming_test | pass | Hand-built paid pilot report for one conveyancing firm. |
| not_all_optimistic | unknown | Case requires buyers to switch from self-join/open data. |

`defensible_wedge` = fail, so the idea is killed.

## Evidence considered

`evidence/propident/2026-09-21-hmlr-identifiers-and-incumbents.md` (HMLR press
release 2026-08-26; landregistry.company CCOD index, £1.00/title, £3.00 premium
director-history search). Enterprise providers (Landmark, Search Acumen,
Orbital Witness) recorded as inference from market position, not cited here.

## Scores

Weighted total **49.0** vs threshold 65 - below threshold. Gating dimensions:
problem_severity_frequency 3, buyer_budget_clarity 2, evidence_strength 3 -
buyer_budget_clarity is below the gating minimum of 3.

## Review

No review requested. A false-negative audit will be due when the killed count
next reaches a multiple of five.

## Reasons if killed

`defensible_wedge` fail: the identifiers lower cost for everyone and create no
wedge; the CCOD index is already mirrored and sold at £1.00/title; the data is
Open Government Licence. Buyer clarity and willingness to pay are unproven. A
future AML monitoring job built on the forthcoming Companies/Overseas Companies
identifier tables remains speculative and enterprise-held.

## False-negative audit (killed ideas only)

Human owner may audit. Audit question: does the FY2026-27 Companies/Overseas
Companies identifier release plus Economic Crime Act obligations create a
small-firm AML monitoring job that no vendor serves? If so, this kill was a
false negative and should be revisited as a new, separately evidenced candidate.
