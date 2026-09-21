# Decision record: WasteTrack: receiver-side digital waste tracking records

- **Idea:** `wastetrack`
- **Date:** 2026-09-21
- **Run:** `20260921T081223Z-normal`
- **Decision:** kill
- **State:** `discovered` -> `killed`
- **Actor:** worker

## What changed

A fresh discontinuity hunt in the legislation/regulation class found the Digital Waste
Tracking (England) Regulations 2026 (SI 2026/729, made 24 June 2026, in force 1 October
2026). This is a strong, dated mandate with a large captive population (12,000 permitted
sites; 300,000 carriers/brokers/dealers from October 2027). Running the
novelty/incumbent sanity check before deep research showed the market has already formed:
a Defra-approved software list exists, an independent comparison of 18 August 2026
catalogues 54 providers, a second comparison states "around 79 providers", at least two
offer free tiers, and weighbridge/waste-management systems bundle tracking. The
government also expects its spreadsheet fallback to remain until at least October 2027.
The candidate therefore fails `defensible_wedge` and is killed.

## Why now? (discovery gate)

- What changed / when: SI 2026/729 made 24 June 2026, in force 1 October 2026; GOV.UK
  service public beta from 28 April 2026; Phase 2 October 2027.
- Why it materially improves the opportunity: creates a mandatory recurring digital
  record and two-working-day submission duty with correction obligations.
- Strength: `strong`
- If `weak` or `absent`: n/a - the why-now gate passed; the idea was killed later by the
  hard filter.

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | pass | Operators of ~12,000 permitted waste facilities in England; a £26/year statutory operator fee is already mandated |
| painful_frequent_or_budgeted | pass | Per-load digital records must be submitted within two working days from 1 October 2026 |
| non_paid_distribution | unknown | Trade-body/search routes plausible but no prospects; moot given the wedge fail |
| defensible_wedge | fail | 54-79 approved providers (two comparisons), free tiers, bundled weighbridge/waste-management systems, and a free government spreadsheet fallback to at least Oct 2027 |
| no_network_effects_needed | pass | Single-site record-keeping tool |
| plausible_margins | unknown | Modelled price £15-£40/month/site against free incumbents; unproven |
| acceptable_risk | pass | No regulated activity beyond using an approved government API |
| cheap_disconfirming_test | pass | A receiver-demand test is cheap, though defeated by the wedge evidence before it ran |
| not_all_optimistic | unknown | Requires winning share against embedded/free incumbents |

Status values are `pass` | `unknown` | `fail`; see `method/scorecard.md`. `unknown`
entries name what would resolve them in the scorecard's `resolve_via`.

## Evidence considered

- `evidence/wastetrack/2026-09-21-digital-waste-tracking-mandate-and-crowding.md` -
  legislation, GOV.UK service design, Defra approved-provider list, and crowding
  evidence (BreakerHQ 18 Aug 2026; LoadSnap compare page; WasteTrace; IntelliWaste).
- Evidence cutting against the kill: the mandate is strong and dated; the population is
  large; the government spreadsheet fallback may be temporary; free tiers could be
  loss-leaders. None of this survives the 54-79-provider evidence.

## Scores

Weighted total 58.9 (threshold 65, not met), 9 of 10 dimensions scored, confidence
`medium`; killed by the `defensible_wedge` fail, not by the aggregate. See
`ideas/wastetrack/scorecard.json`.

## Review

- Review status: `not-required`. A review is not triggered: no advance to
  `validation-ready`, no method/weight change, no >20 human-hour / >£100 experiment, and
  this is not a 5th-kill false-negative trigger (it is the 9th killed idea; the next
  audit is due at the 10th).

## Reasons if killed

The receiver-side opportunity is already served by a populated, government-recognised
provider market that includes free options and bundled weighbridge/waste-management
systems. Evidence that would have changed the decision: a receiver segment still
unserved at the deadline (e.g. small permitted sites without software access) plus
willingness to pay a newcomer despite free alternatives - neither found. The deferred
cross-border green-list/DIWASS gap is preserved as a non-inheriting seed.

## False-negative audit (killed ideas only)

- Audited: no
- Reviewer / date: n/a
- Verdict: n/a
- What new evidence would justify reopening: evidence that approved providers leave a
  specific receiver segment unserved at the deadline, or that free tiers reprice
  materially after October 2026.
