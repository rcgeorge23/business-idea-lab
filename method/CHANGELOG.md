# Method Changelog

Every material change to the method bumps `method/VERSION` and is listed here with its
review status. Review status values: `not-required` | `requested` | `changes-requested` |
`approved` | `killed`. See `method/review-policy.md` (section "Method changes").

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
