# Decision record: VetLab Bridge

- **Idea:** `vetlab-bridge`
- **Date:** 2026-09-21
- **Run:** `20260921T091851Z-normal`
- **Decision:** kill
- **State:** `discovered` -> `desk-screened` -> `adversarially-researched` -> `killed`
- **Actor:** worker

## What changed

Promoted from observation `O17` (fresh discovery). Full desk research confirmed a
persistent, practitioner-evidenced semantic-interoperability gap in veterinary
diagnostics exchange, but also found that the connection/structural layers are already
contested by live vendors (DataHub Vet, ManuCare, Bitwerx, Covetrus Connect, PupPilot)
and that ManuCare already markets the proposed mechanism itself (universal lab-result
import, "zero copy-paste"). An independent adversarial review (idea-critic, read-only)
concluded that `defensible_wedge` is a hard-filter `fail`, not `unknown`. The idea is
therefore killed. Corrected score 47.4/100, below the 65 threshold.

## Why now? (discovery gate)

- What changed / when: DIN EN 18029:2026-04 (E), a European standard for electronic
  veterinary laboratory analysis data exchange, published April 2026.
- Why it materially improves the opportunity: a published format could lower the per-lab
  mapping burden (inference); the DIN record does not show that any vendor has
  implemented it, and it creates no buyer budget.
- Strength: `weak`
- If `weak` or `absent`: generated anyway because the underlying failure is persistent
  and the wedge question was worth resolving; the weak why-now contributed to the kill
  but the decisive filters were `defensible_wedge` and `not_all_optimistic`.

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | unknown | Independent labs are small and their willingness to fund a channel is undocumented; no lab is named. |
| painful_frequent_or_budgeted | pass | Manual re-entry/attachment of lab results is practitioner-evidenced (frequency and population unquantified). |
| non_paid_distribution | unknown | A small lab population makes unpaid outreach plausible but untested; no partner interest evidenced. |
| defensible_wedge | **fail** | ManuCare already markets universal lab-result import into the patient case ("zero copy-paste") and DataHub Vet already exposes a normalised data model into long-tail PIMS. Under `method/scorecard.md` a wedge that is a feature of an established category is a hard-filter failure, not a score reduction. |
| no_network_effects_needed | pass | A single lab plus a single practice receives value from one structured results channel. |
| plausible_margins | unknown | A low ACV must clear a documented $30–50/clinic/month access-fee floor; not modelled with a real price. |
| acceptable_risk | unknown | Processor obligations where owner personal data travels with results, and the contractual exposure of a local DB connector, were not assessed; legal view required. |
| cheap_disconfirming_test | pass | A desk capability check of ManuCare/DataHub Vet/IDEXX-Covetrus bundles is cheap and decisive. |
| not_all_optimistic | **fail** | Buyer, wedge and margin would all have to resolve favourably at once; the wedge is already contradicted. |

A `fail` kills (`method/scorecard.md`, `method/run-protocol.md`).

## Evidence considered

- `evidence/vetlab-bridge/2026-09-21-vet-interoperability-structural-gap.md` (supports; also a vendor-authored analysis)
- `evidence/vetlab-bridge/2026-09-21-pims-api-openness-and-fees.md` (cuts against: fees, gatekeeping, single unreplicated paper)
- `evidence/vetlab-bridge/2026-09-21-incumbent-bridges-and-lab-integrations.md` (kills: live direct competitors)
- `evidence/vetlab-bridge/2026-09-21-din-en-18029-standard.md` (why-now, weak)
- Observation pool `observations/20260921T091851Z-normal.md` (O17).
- Independent adversarial review: `idea-critic` subagent, 2026-09-21 (read-only; verdict kill).

## Scores

Weighted total 47.4/100 against a threshold of 65; 9 of 10 dimensions scored
(`founder_fit` is `null` — no source, no score); gating dimensions: problem 3, buyer 2,
evidence 2. Confidence `low`. See `ideas/vetlab-bridge/scorecard.json`.

## Review

No review was required at any point because no advance to `validation-ready` was
proposed; the idea was killed at the hard-filter stage. No recorded review outcome was
overwritten (none existed). If the reopening test ever passes, a review should be raised
before any advance.

## Reasons if killed

`defensible_wedge` fails: a named, live vendor (ManuCare) already markets universal
lab-result import, and DataHub Vet already normalises PIMS data, so the proposition is a
feature of an established category rather than a product with a wedge. `not_all_optimistic`
also fails: buyer, wedge and margin must all succeed simultaneously and none is
established. The why-now is weak (a standard, not a mandate) and the likely vertical
incumbent (IDEXX) can bundle the capability at no incremental fee.

## False-negative audit (killed ideas only)

- Audited: 2026-09-21
- Reviewer / date: idea-critic (read-only adversarial review), 2026-09-21
- Verdict: kill upheld. Every `unknown` was re-examined; `defensible_wedge` was found to
  be `fail` on the filed evidence, with `not_all_optimistic` a second fail.
- What new evidence would justify reopening: a documented desk capability check showing
  that **neither** ManuCare nor DataHub Vet nor any IDEXX/Covetrus bundle performs
  semantic lab-result delivery into long-tail PIMS **and** that ≥2 named independent
  UK/IE labs have no sanctioned structured import route. Failing either is a kill.
