# Method Changelog

Every material change to the method bumps `method/VERSION` and is listed here with its
review status. Review status values: `not-required` | `requested` | `changes-requested` |
`approved` | `killed`. See `method/review-policy.md` (section "Method changes").

## 1.4.0 - 2026-09-21

Motivated by issue #6, implementing the non-regulatory source-budget proposal recorded
at the end of issue #5 and reinforced by the independent v1.3.0 review: the lab keeps
converging on easily searchable regulatory discontinuities, whose obvious first-order
products incumbents bundle away (`defensible_wedge` kill cluster: agentready, packproof,
vetcma, prsregister, propident, wastetrack, bikpayroll).

Changed (discovery constraint only - scoring, weights, threshold 65, hard filters,
evidence levels, lifecycle gates and the candidate/advancement maxima are unchanged):

- **`method/discovery.md`**: new `## Source-class budget` section. At least 2 of the
  maximum 3 candidate slots must originate from non-regulatory source classes; at most
  1 may primarily originate from legislation/regulation; at least one previously
  underexplored non-regulatory class must actually be searched. Lists the non-regulatory
  classes, requires the run summary to record classes searched (regulatory vs
  non-regulatory, successful and unsuccessful), candidate provenance, the class each
  candidate qualifies under and why, and the budget outcome. Forbids manufacturing
  filler: fewer than three candidates, all-kill runs and zero advances remain valid.
- **`method/run-protocol.md`**: step 3 applies the budget and records it; step 12
  requires the budget outcome in the run summary. Run metadata example now 1.4.0.
- **`templates/run/summary.md`**: source-class table marks each class regulatory or
  non-regulatory and adds a budget-outcome line; candidate provenance table adds the
  source class and why the candidate qualifies.
- `AGENTS.md`, `scripts/prompts/lab-run.md` and `.opencode/agent/idea-worker.md` state
  the budget and its recording requirements.

Regression: the budget is a sourcing constraint, not a score input, so no score,
evidence level or hard-filter outcome can move because of it. Killed fixtures remain
rejected for their recorded reasons; parked ideas remain parked. The empirical check is
the post-change run required by issue #6, whose convergence assessment is recorded in
`retrospectives/2026-09-21-issue6-convergence-review.md`.

Review: `requested` - see `reviews/2026-09-21-method-v1.4.0-review-request.md`. This
entry must be updated with the outcome when the review lands; there are no other
outstanding review requests.

## 1.3.0 - 2026-09-21

Motivated by issue #4, following the first normal run under method 1.2.0
(`20260921T075410Z-normal`), where all three candidates had strong dated discontinuities
but died on `defensible_wedge` because the obvious first-order product was already
served by incumbents or free alternatives.

Changed (discovery guidance only - scoring, weights, threshold, hard filters and
evidence semantics unchanged):

- **Second-order effects**: `method/discovery.md` now requires an explicit investigation
  of the operational seam a discontinuity creates (manual handoffs, re-keying,
  reconciliation, evidence collection, exception handling, status chasing, awkward
  imports/exports, mandated data transformations, integration gaps, poor incumbent
  workflow steps, newly automatable review, underserved subsegments) and prefers an
  awkward workflow/integration seam to a generic compliance/dashboard product.
- **Seed-aware discovery**: normal runs must review the seed register at orientation and
  shallowly re-check the most relevant seeds; a seed becomes a candidate only via full
  fresh research (own fingerprint, evidence, filters, scorecard) with no inheritance;
  runs remain explicitly not seed-only.
- **Provenance and convergence recording**: candidates record provenance
  (`seed:<slug>` or `fresh`) and their second-order seam; the run summary must assess
  whether discovery is converging on less obvious opportunities or repeating one class
  of rejection (and flag it for review rather than weakening a filter).
- Run protocol steps 1/3/12, AGENTS.md, the worker agent prompt, the lab-run prompt and
  the run summary template updated to match. Candidate/advance limits (3/1) unchanged.

Regression: weights version stays 1.2.0; no scoring rule, threshold, hard filter or
evidence level changed, so every existing scorecard keeps its scores. Killed fixtures
and parked ideas are unaffected by construction.

Review: `approved` (ChatGPT / GPT-5.6 Sol, 2026-09-21) - see
`reviews/2026-09-21-method-v1.3.0-chatgpt-gpt-5.6-sol.md`. Reviewer found the
second-order and seed-aware refinements appropriate and non-weakening, and noted
the empirical run did not force novelty; follow-up observation: the next
sourcing refinement must ensure meaningful effort reaches non-regulatory
classes (implemented as the issue #6 source budget, see 1.4.0), and the
recurring `defensible_wedge` failures are a sourcing/convergence signal rather
than grounds to weaken the filter.

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

Review: `approved` (ChatGPT / GPT-5.6 Sol, 2026-09-21) - see
`reviews/2026-09-21-method-v1.2.0-chatgpt-gpt-5.6-sol.md`. The scoping was found
justified, with no obvious loophole (escaping the cap requires reaching a
separately defined evidence level) and the regression fixtures still rejected.
Caveat recorded: the Aucly "2,333 visitors -> 0 accounts" figure must not be read
as a clean website conversion cohort; the supported conclusion is only that no
repeatable organic organiser-acquisition channel is demonstrated. The
distribution score is unchanged.

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

Review: `approved` (ChatGPT / GPT-5.6 Sol, 2026-09-21) - see
`reviews/2026-09-21-method-v1.1.0-chatgpt-gpt-5.6-sol.md`. Discontinuity-first
discovery, tightened evidence semantics, the retained 65 threshold, mandatory
`resolve_via` on `unknown` and non-inheriting seeds were all found sound, with no
regression fixture weakened. Observations recorded: monitor score coverage,
since the normalised aggregate over unscored dimensions is slightly awkward (do
not change on this review alone), and keep cheap-experiment eligibility separate
from `validation-ready`.

## 1.0.0 - 2026-09-20

Initial method, implemented under issue #1: lifecycle, evidence policy, scorecard,
experiment rules, run protocol, review policy, calibration procedure, templates and the
deterministic runner (`scripts/run.sh`).

Review: `not-required` (bootstrap; superseded by the first normal run and the 1.1.0
change).
