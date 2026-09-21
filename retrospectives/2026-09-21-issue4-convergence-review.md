# Retrospective — issue #4 discovery refinement and convergence review

- **Date:** 2026-09-21
- **Method version:** 1.3.0
- **Run reviewed:** `20260921T081223Z-normal` (`runs/20260921T081223Z-normal/summary.md`)
- **Changes reviewed:** second-order effects, seed-aware discovery, candidate
  provenance and the convergence recording added for issue #4
  (`method/CHANGELOG.md` 1.3.0)

## What issue #4 asked for

After the first 1.2.0 run killed three reasonable candidates on
`defensible_wedge`, issue #4 asked the lab to look past the obvious first-order
"new mandate -> compliance tool" product; to review the seed register at run
start without letting seeds inherit their parent's scores; to keep fresh
discovery enabled and the limits unchanged; and to report whether discovery is
converging on less obvious, better-defended opportunities or merely getting
efficient at finding and rejecting regulatory SaaS. If another run produced
several reasonable candidates all killed on `defensible_wedge`, the issue asked
for that to be flagged for review rather than for the filter to be weakened.

## What the run did

- **Seed register reviewed** (2 shallow re-checks of 6 unexplored seeds):
  `uk-epr-small-producer-tooling` was **dropped** (fee low-burden, free GOV.UK
  reporting service, established compliance schemes; re-check evidence under
  `evidence/packproof/2026-09-21-uk-epr-small-producer-recheck.md`);
  `corporate-property-aml-monitor` was **kept `unexplored`** with the no-change
  reason appended; a new non-inheriting seed
  `cross-border-green-list-waste-bridge` was recorded from the `wastetrack`
  rejection.
- **Two candidates generated (limit 3), both `fresh`**:
  - `wastetrack` (Digital Waste Tracking, SI 2026/729) — why now `strong`, but
    killed on `defensible_wedge`: 54-79 Defra-approved providers, free tiers,
    bundled weighbridge systems and a government spreadsheet fallback to at
    least October 2027. Kill #9 (score 58.9).
  - `bikpayroll` (mandatory payrolling of BiK from 2027-04-06) — why now
    `strong`, framed around the second-order seam (collecting, validating and
    reconciling third-party benefit-provider data into each pay run). No filter
    `fail` (6 `unknown` with `resolve_via`), aggregate 50.5, parked at
    `desk-screened`; the adversarial pass recommended kill and that dissent is
    recorded in the decision record rather than being overwritten.
- **0 advances to `validation-ready`**; one desk-only experiment proposed
  (`bikpayroll-incumbent-capability`, £0 / 6 human-hours / 3 days, no external
  contact, approval not required for the desk scan).

## Did the refinement do what issue #4 intended?

- **Second-order guidance changed behaviour, and produced one honest negative.**
  For `wastetrack` the worker recorded that the *framed* product was itself
  first-order (record and submit) and that the second-order reconciliation seam
  was identified but not adopted — the run did not pretend a second-order idea
  existed where the evidence did not support one. For `bikpayroll` the seam was
  the reason to keep the idea alive at low score instead of killing it: the open
  question is narrowly testable (does any incumbent supply machine-readable
  per-period BiK data?) rather than a generic compliance pitch.
- **Seed-aware discovery worked as a register, not an inheritance channel.**
  The run reviewed seeds explicitly, recorded a drop and a no-change, and both
  candidates it generated were fresh. A seed-derived candidate did not occur in
  this run, so the no-inheritance path has not yet been exercised end to end;
  that remains untested.
- **Limits and falsification character preserved.** Weights and threshold are
  unchanged at 1.2.0 (method 1.3.0 is discovery-only), the validator passes, and
  no candidate was advanced or scored favourably to justify the new guidance.

## Convergence assessment (the issue's review question)

**Discovery is not converging yet — it is currently efficient at finding, and
rejecting, regulatory/compliance SaaS.** The `defensible_wedge` kill cluster now
spans `vetcma`, `prsregister`, `propident`, `packproof`, `agentready` and
`wastetrack`, plus the earlier `grantscout` veto. The run's own assessment says
the same, and this retrospective endorses it rather than treating the filter as
the problem.

Two things can be true at once, and both are recorded:

1. The cluster is partly a property of the source classes. Regulation is easy to
   search, discontinuities there are loud and dated, and the first-order product
   is obvious to everyone at once. The lab's sourcing still leans on it.
2. The filter is doing its job. Every kill cites a populated market or free
   authoritative alternative; weakening `defensible_wedge` now would produce
   candidates that compete with 54-79 free-or-cheap incumbents, which is not an
   opportunity.

Per issue #4, the pattern is therefore **flagged for review, not acted on by
changing the filter**. The question of whether the lab's sourcing can find
better-defended opportunities is an empirical one for the next runs, and the seed
register now holds candidates for it (`agent-checkout-offplatform`,
`grantscout-application-quality`, `vet-estimate-bridge`, `prs-listing-precheck`,
`corporate-property-aml-monitor`, `cross-border-green-list-waste-bridge`).

## What the next run should do (no method change proposed)

1. Run the `bikpayroll-incumbent-capability` desk scan (or record a human
   decision to skip it) — it is the cheapest route to a `fail` or a documented
   gap, and it tests whether a second-order seam survives contact with the
   incumbents.
2. Re-check at least one further unexplored seed, preferring
   `prs-listing-precheck` or `agent-checkout-offplatform`.
3. Search at least one non-regulatory, non-platform source class (new technical
   capability, platform rule change, poor narrow incumbent) as the previous
   retrospective also proposed; two consecutive runs have now missed this.
4. Avoid further "new mandate -> submission tool" candidates unless a
   second-order seam inside the mandate is evidenced as unserved.
5. If a third consecutive run produces reasonable candidates all killed on
   `defensible_wedge`, escalate the convergence question to the human owner /
   reviewer with this retrospective as evidence — do not adjust the filter.

## Calibration status after this review

- The 1.3.0 change is discovery-only; `method/CHANGELOG.md` records it as
  `requested` (`reviews/2026-09-21-method-v1.3.0-review-request.md`) and this run
  is its empirical check.
- The run cost USD 0.008245 (147,315 tokens) and passed validation with 0 errors.
- The false-negative audit is now due on the next kill (killed count 9).

## Follow-ups for the human owner

- Route the outstanding review requests (GeoNerd v2, shiftswap false-negative
  audit, method v1.1.0 / v1.2.0 / v1.3.0) — none has a recorded response yet.
- Decide whether to schedule the `bikpayroll-incumbent-capability` desk scan and
  whether the three proposed experiments (plus that scan) should be approved.
