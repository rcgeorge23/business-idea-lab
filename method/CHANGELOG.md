# Method Changelog

Every material change to the method bumps `method/VERSION` and is listed here with its
review status. Review status values: `not-required` | `requested` | `changes-requested` |
`approved` | `killed`. See `method/review-policy.md` (section "Method changes").

## 1.2.0 - 2026-09-21

Motivated by issue #3 (Aucly calibration). One narrow, evidence-driven change; all other
candidate refinements were rejected as unnecessary (see `ideas/aucly/decision.md`).

Changed:

- **Why-now cap scoped (weights version 1.2.0)**: the "missing why-now caps
  `differentiation` and `problem_severity_frequency` at 2" rule now applies only while
  the idea's evidence level is `Plausible` or `Promising`. From `Demand evidence`
  upward the cap does not apply, because real payment evidence is stronger than a
  discontinuity claim. Aucly exposed the systematic error: an evergreen niche
  (school/charity fundraising, incumbents predating 2025) with paying customers was
  being penalised twice - once for having no discontinuity and again in the
  differentiation dimension - which would have understated a genuinely evidenced
  business.
- **No other scoring rules changed.** Small-market viability, bootstrapped vs
  venture-scale framing, founder fit, cheap build/testability, direct-competitor
  treatment and payment-vs-validation separation were all reviewed against Aucly and
  found already adequate.

Regression: existing fixtures are unaffected. The killed fixtures (ShiftSwap,
WonkyBox, GrantScout, AgentReady, PackProof) are all at evidence level `Plausible`, so
the scoped cap still applies to them, and their kills rest on `fail` hard filters or
vetoes, not on the cap. GeoNerd and Reasonable Steps are `Promising`: cap still applies.
The only score change is Aucly's own `problem_severity_frequency` 2 -> 3 (60.0 total).

Review: `requested` - see `reviews/2026-09-21-method-v1.2.0-review-request.md`.
This changelog entry must be updated with the outcome when the review lands; the worker
must then answer it explicitly in the next run.

## 1.1.0 - 2026-09-21

Motivated by issue #2 and the first normal run (`runs/20260920T210550Z-normal`), which
showed (a) conventional candidates with no discontinuity behind them and (b) scores and
hard-filter passes resting on assumptions.

Changed:

- **New `method/discovery.md`**: discontinuity-first generation ("why now?" test),
  change-source classes, novelty/incumbent sanity check, duplicate detection, adjacent
  opportunity seeds.
- **`method/scorecard.md`** (weights version 1.1.0): "plausibility is not evidence"
  anchors; explicit caps (analogy-based problem <= 2, inferred budget <= 2,
  plausible-only distribution <= 2, direct incumbent overlap lowers differentiation to
  <= 2, modelled economics <= 2 with `low` confidence); hard filters now carry
  `status` (pass | unknown | fail) plus `note`, `evidence` and `resolve_via`; `pass`
  requires affirmative cited evidence; assumptions/analogies cannot pass; new threshold
  condition 8 (every unknown named in the proposed experiment). Threshold deliberately
  left at 65 despite the tightening.
- **`method/evidence-policy.md`**: "Plausibility is not evidence" section.
- **`method/lifecycle.md`**: transitions aligned to the new filter semantics; experiments
  decoupled from `validation-ready` so parked ideas can still reach a cheap test; "Why
  now?" requirement for new candidates.
- **`method/run-protocol.md`**: steps reordered around discontinuity hunting, novelty
  check, tightened filters, adjacent seeds, source-class recording.
- **`method/review-policy.md`**: method-change review handling; re-request after a
  revision change.
- **Templates**: dossier gains "Why now?" and "Novelty / incumbent sanity check";
  scorecard hard filters gain `evidence`/`resolve_via`; new `templates/seed/entry.md`;
  run summary gains source classes + why-now quality.
- **Ledger**: GeoNerd rescored 65.3 -> 49.5 and moved down to
  `adversarially-researched`; `why_now` backfilled for existing ideas; GrantScout
  adjacent seed recorded.
- **Validator**: new filter semantics enforced, `why_now` required, `seeds/index.json`
  checked, historical run method versions downgraded to a warning.

Review: `requested` - see `reviews/2026-09-21-method-v1.1.0-review-request.md`.
This changelog entry must be updated with the outcome when the review lands; the worker
must then answer it explicitly in the next run.

## 1.0.0 - 2026-09-20

Initial method, implemented under issue #1: lifecycle, evidence policy, scorecard,
experiment rules, run protocol, review policy, calibration procedure, templates and the
deterministic runner (`scripts/run.sh`).

Review: `not-required` (bootstrap; superseded by the first normal run and the 1.1.0
change).
