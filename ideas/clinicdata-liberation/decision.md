# Decision record: ClinicData Liberation

- **Idea:** `clinicdata-liberation`
- **Date:** 2026-09-21
- **Run:** `20260921T091851Z-normal`
- **Decision:** kill
- **State:** `discovered` -> `desk-screened` -> `adversarially-researched` -> `killed`
- **Actor:** worker

## What changed

Promoted from observation `O25` (fresh discovery). Research confirmed a dated 2026
end-of-life cluster and a documented no-export reality, but found that ValueStreamAI
already sells the exact UI-level extraction method, that receiving vendors (Nookal,
Upheal) ship guided migration and give it away in onboarding, and that the buyer-behaviour
evidence is a competitor's published list bands rather than realised prices. An
independent adversarial review (idea-critic, read-only) concluded that `defensible_wedge`
is a hard-filter `fail`, not `unknown`. The idea is therefore killed. Corrected score
49.5/100, below the 65 threshold.

## Why now? (discovery gate)

- What changed / when: a 2026 end-of-life set — BP Allied switch-off 31 July 2026,
  Cherwell Service Management end-of-life 31 December 2026, on-premise RoboVet
  end-of-life with a UK practice migrating in June 2026.
- Why it materially improves the opportunity: a fixed switch-off forces an action that
  would otherwise be deferred.
- Strength: `strong` (the dates are real), but competitors have already responded and the
  events are heterogeneous; why-now strength does not rescue a failed wedge.
- If `weak` or `absent`: n/a.

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | unknown | "Documented" fees are one vendor's published list bands (inferred budget), and the receiving vendor gives the substitute away free. |
| painful_frequent_or_budgeted | pass | Forced-action end-of-life dates and documented migration workload (weeks of overlap; PDF-only, disconnected charts); the event is one-shot rather than frequent. |
| non_paid_distribution | unknown | SEO and receiving-vendor referral are plausible but the receiving vendor is also a competitor for the switch. |
| defensible_wedge | **fail** | ValueStreamAI already sells the exact UI-level extraction method at published bands, receiving vendors give guided migration away in onboarding, and data migration is an established category. Under `method/scorecard.md` this is a hard-filter failure, not a score reduction. |
| no_network_effects_needed | pass | One clinic's migration delivers value without other participants. |
| plausible_margins | unknown | Fixed fee against variable hours; margin depends on recipe amortisation and there is no retention. |
| acceptable_risk | unknown | Licence-term and UK data-protection exposure of UI-level extraction of clinical records is unresolved. |
| cheap_disconfirming_test | pass | A desk check of named systems plus 3 switcher interviews is cheap and decisive. |
| not_all_optimistic | **fail** | Buyer, wedge, margin and legal risk would all have to resolve favourably; the wedge is already contradicted. |

A `fail` kills (`method/scorecard.md`, `method/run-protocol.md`).

## Evidence considered

- `evidence/clinicdata-liberation/2026-09-21-eol-cluster-2026.md` (supports why-now; heterogeneous events)
- `evidence/clinicdata-liberation/2026-09-21-no-export-extraction-and-pricing.md` (kills: live vendor sells the exact method; vendor list bands)
- `evidence/clinicdata-liberation/2026-09-21-migration-pain-and-tooling.md` (kills: receiving vendors give migration away)
- `evidence/clinicdata-liberation/2026-09-21-enterprise-archive-crowding.md` (cuts against: established, well-capitalised category)
- Observation pool `observations/20260921T091851Z-normal.md` (O25).
- Independent adversarial review: `idea-critic` subagent, 2026-09-21 (read-only; verdict kill).

## Scores

Weighted total 49.5/100 against a threshold of 65; 9 of 10 dimensions scored
(`founder_fit` is `null` — no source, no score); gating dimensions: problem 3, buyer 2,
evidence 3. Confidence `low`. See `ideas/clinicdata-liberation/scorecard.json`.

## Review

No review was required because no advance to `validation-ready` was proposed; the idea was
killed at the hard-filter stage. No recorded review outcome was overwritten (none existed).
The adversarial review noted that if this idea were ever carried forward, the unresolved
UK data-protection/licence exposure over extracting clinical records is a **review-policy
trigger 4** matter (material privacy/legal risk) and a review must be raised before any
advance. Recorded here so the trigger is not silently bypassed.

## Reasons if killed

`defensible_wedge` fails: a named live vendor (ValueStreamAI) already sells the exact
UI-level extraction method and receiving vendors give an adequate substitute away free in
onboarding, so the proposition is a feature of an established services category.
`not_all_optimistic` also fails. The buyer-behaviour evidence is a competitor's published
list bands (inferred budget, capped at 2), and there is a documented database-backup
alternative for at least one EOL system.

## False-negative audit (killed ideas only)

- Audited: 2026-09-21
- Reviewer / date: idea-critic (read-only adversarial review), 2026-09-21
- Verdict: kill upheld. `defensible_wedge` was found to be `fail` on the filed evidence,
  with `not_all_optimistic` a second fail and `economic_buyer` downgraded from `pass` to
  `unknown`.
- What new evidence would justify reopening: a documented desk check showing ≥3 named UK
  clinical systems with genuinely no export path other than UI automation **and** ≥2 of 3
  recent UK switchers paid a third party rather than accept the receiving vendor's free
  guided migration, **plus** a clean legal view on licence terms and UK data-protection
  for UI-level extraction. Failing any of these is a kill.
