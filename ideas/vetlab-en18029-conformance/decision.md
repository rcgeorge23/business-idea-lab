# Decision record — VetLab EN 18029 Conformance

- **Idea:** `vetlab-en18029-conformance`
- **Originating observation:** O5 (DIN EN 18029 / VetXML veterinary lab–prescriber exchange), from pool `observations/20260921T100247Z-normal.md`
- **Provenance:** `seed:vetlab-standard-conformance` (parent idea `vetlab-bridge`, killed 2026-09-21 on `defensible_wedge`; this candidate does not inherit the parent's score or evidence)
- **Actor:** worker (idea-worker)
- **Date:** 2026-09-21
- **Method version:** 1.6.0
- **State before:** new candidate (promoted from observation O5)
- **State after:** `desk-screened`

## What changed

The opportunity-observation funnel promoted observation O5 to a full candidate. The prior idea `vetlab-bridge` was killed because the lab-to-long-tail-PIMS **results-delivery** mechanism was already sold by ManuCare and DataHub Vet. Re-reading the same research surfaced a different job with a different buyer: DIN EN 18029:2026-04 (E) was published in April 2026 as a European standard for veterinary laboratory data exchange (request, result and acknowledgement files plus a data dictionary), and it **explicitly excludes the code lists** required for unambiguous exchange. VetXML publishes free schemas and a hub, but no shipping conformance, test-fixture or reference-list product was found. This candidate therefore sells conformance and mapping-validation tooling to the implementers of the standard (PIMS/LIMS and laboratory software vendors, and labs attesting conformance) rather than operating a delivery channel.

## Why now? (discovery gate)

- **Archetype:** change-driven (a new European standard published 2026-04) with a persistent-underinvestment overlay.
- **Why-now strength:** `weak`. A standard is not a mandate; no vendor implementation, adoption or buyer budget is evidenced. The archetype-aware missing-why-now cap is applied, capping `differentiation` and `problem_severity_frequency` at 2. No persistence-thesis lift is claimed: the two-part thesis is not evidenced (`absent`), so the cap is not lifted.
- **Evidence:** `evidence/vetlab-en18029-conformance/2026-09-21-en18029-standard-scope.md`.

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | unknown | Buyer set nameable; no named buyer/budget. `resolve_via`: interviews. |
| painful_frequent_or_budgeted | unknown | Recurring structurally; not evidenced as budgeted pain. `resolve_via`: interviews. |
| non_paid_distribution | unknown | Public VetXML member list plausible; untested. `resolve_via`: direct approaches. |
| defensible_wedge | unknown | No shipping product occupies the exact seam, but wedge unproven and standard voluntary. `resolve_via`: desk check + willingness to pay. |
| no_network_effects_needed | pass | A single lab + single vendor pair gets value. |
| plausible_margins | unknown | No pricing evidence; economics capped at 2. `resolve_via`: willingness-to-pay test. |
| acceptable_risk | unknown | No legal/platform risk; demand risk unassessed. `resolve_via`: proposed experiment. |
| cheap_disconfirming_test | pass | Zero-money desk check + small interview set with pre-fixed rule. |
| not_all_optimistic | unknown | Central assumptions unevidenced. `resolve_via`: proposed experiment. |

No `fail`, so the idea may be recorded at `desk-screened`. Four unresolved assumptions are carried into the proposed experiment; they are not treated as passes.

## Evidence considered

- `evidence/vetlab-en18029-conformance/2026-09-21-en18029-standard-scope.md`
- `evidence/vetlab-en18029-conformance/2026-09-21-vet-interoperability-and-incumbents.md`
- `evidence/vetlab-en18029-conformance/2026-09-21-vetlab-market-and-buyer-economics.md`

## Scores

Weighted total **44.2 / 100** (threshold 65; not met). Confidence `low`. Nine of ten dimensions scored (`founder_fit` null). Gating dimensions `problem_severity_frequency`, `buyer_budget_clarity` and `evidence_strength` are all 2 (below the validation-ready minimum of 3). This is a Plausible-level candidate only.

## Review

`review.status = not-required`. The idea is not proposed for validation-ready, so no review trigger applies.

## Reasons if killed

Not killed. If the proposed buyer-wedge experiment shows no funded need among five named labs/PIMS vendors before a mandate, the idea should be killed on `defensible_wedge` and `economic_buyer`.

## False-negative audit

Not applicable to a promoted candidate. The run's single triage false-negative audit re-checked observation O11 (funeral management software) and upheld the rejection; see the pool file.
