# GeoNerd — decision record

- Idea id: `geonerd`
- State: `adversarially-researched` (parked; previously `validation-ready`)
- Date: 2026-09-21
- Method version: 1.1.0
- Actor: worker (issue #2 recalibration), seeded by bootstrap (human owner, issue #1)

## What changed

Rescored under method 1.1.0 and the tightened rubric. The desk case no longer
reaches the `validation-ready` threshold: 65.3 → **49.5** (threshold unchanged at
65). State moves down from `validation-ready` to `adversarially-researched`. The
`geonerd-demand-spike` experiment remains proposed and is unaffected by the
state change (experiments are decoupled from `validation-ready` under 1.1.0).

Why the score fell, dimension by dimension:

| Dimension | 1.0.0 | 1.1.0 | Reason for change |
|---|---|---|---|
| problem_severity_frequency | 3 | 2 | Pain inferred by analogy; no buyer observed. Analogy cap. |
| buyer_budget_clarity | 3 | 3 | Held: buyer identified and incumbents already sell to them (weak budget-line evidence). |
| evidence_strength | 3 | 2 | All internal desk research; no buyer-derived or independent evidence. |
| distribution | 3 | 2 | Channels plausible, no prospects produced. Plausible-channels cap. |
| differentiation | 3 | 2 | TendorAI/SearchScore already contest the position. Direct-overlap cap. |
| validation_speed_cost | 4 | 4 | Held: 1-week, £50, pre-fixed decision rule. |
| feasibility | 4 | 3 | Manual scan feasible; collection pipeline unproven. |
| economics | 4 | 2 | Modelled only, no tested input. Modelled-economics cap, low confidence. |
| founder_fit | null | null | Still no evidence about the actual founder. |
| risk | 3 | 3 | Held: no regulated data; claims verifiable. |

## State and transition

- Previous state: `validation-ready`
- Current state: `adversarially-researched`
- Reason: weighted_total 49.5 < 65 and two gating dimensions below 3 under
  method 1.1.0; carrying the idea at `validation-ready` would be unsupported.
- Transition authority: worker (downward moves are permitted and recorded). The
  idea remains parked pending the proposed demand experiment; it can be
  re-proposed for `validation-ready` only with new evidence.

## Hard filters

| Filter | Status | Note | Evidence / resolve via |
|---|---|---|---|
| economic_buyer | pass | Practice owner/partner is the decision maker; £19.99/mo is small relative to one client | `evidence/geonerd/2026-09-20-wedge-strategy.md` |
| painful_frequent_or_budgeted | unknown | Assumed by analogy with search-visibility tracking; desk evidence only (A2) | Demand-spike interviews: whether practices raise the problem unprompted; commitment ≥£19/mo |
| non_paid_distribution | unknown | Directory outreach, communities, SEO, benchmark; unmeasured (A4) | Measure directory-outreach reply/scan rates and community yield in the spike |
| defensible_wedge | unknown | Vertical depth + honest measurement is describable, but TendorAI/SearchScore contest the position | Interview reaction to positioning/price versus those incumbents |
| no_network_effects_needed | pass | Market-level prompt set works for a single customer | `evidence/geonerd/2026-09-20-wedge-strategy.md` |
| plausible_margins | unknown | Contribution positive at d≥10 in the model; no real provider bill (A5) | Record actual provider bill and achieved density in the spike |
| acceptable_risk | pass | No regulated personal data; claims about AI answers verifiable | `evidence/geonerd/2026-09-20-competitive-teardown.md` |
| cheap_disconfirming_test | pass | £50 / 20h / 1-week demand spike with a pre-fixed decision rule | `evidence/geonerd/2026-09-20-demand-validation-plan.md` |
| not_all_optimistic | pass | Stop rules fire on 0/5 commitments; iterate path defined | `evidence/geonerd/2026-09-20-demand-validation-plan.md` |

Four filters are `unknown` (assumption-based), each with a named resolution in
the proposed experiment. They are not counted as positive evidence anywhere.

## Evidence considered

- `evidence/geonerd/2026-09-20-wedge-strategy.md`
- `evidence/geonerd/2026-09-20-demand-validation-plan.md`
- `evidence/geonerd/2026-09-20-spike-findings.md`
- `evidence/geonerd/2026-09-20-competitive-teardown.md`

All are internal desk research from `/home/richard/projects/geonerd` @
`327f02e`; none is independent market evidence. No new external evidence was
gathered for this rescore.

## Scores

Weighted total 49.5 (threshold 65), confidence **low**, 9 of 10 dimensions
scored, aggregate does not meet the threshold. `founder_fit` remains unscored.
See `scorecard.json` for per-dimension evidence links. Overall confidence is low
because the two gating dimensions with the weakest support
(`problem_severity_frequency`, `evidence_strength`) are low-confidence.

## Review

- Status: `requested`
- Requested from: independent reviewer (ChatGPT), via
  `reviews/2026-09-21-geonerd-review-request-v2.md` (the 2026-09-20 request is
  preserved at `reviews/2026-09-20-geonerd-review-request.md`)
- Trigger: revision change while the original request was still `requested`;
  the rescore and downward move are themselves reviewable
- Outcome: none yet. The worker must answer any `changes-requested` review in
  the next run and must never overwrite a recorded outcome.

## Reasons if killed

Not killed. The idea is parked at `adversarially-researched`; its unresolved
questions are exactly what the proposed experiment measures. A kill would
require evidence that the problem is not felt, that owners will not pay, or that
incumbents already satisfy them.

## False-negative audit

Not applicable (no kill). The GrantScout kill from 2026-09-20 produced the
adjacent seed `seeds/grantscout-application-quality.md`; no such seed was
warranted here.

## Decision log

| Date | Actor | Decision | Rationale |
|---|---|---|---|
| 2026-09-20 | bootstrap | Created at `validation-ready`, review requested, experiment proposed | See 2026-09-20 entry in the dossier |
| 2026-09-21 | worker | Rescored 65.3 → 49.5; state `validation-ready` → `adversarially-researched`; review re-requested (v2) | Tightened method 1.1.0 semantics; threshold unchanged; the demand spike remains the route back up |
