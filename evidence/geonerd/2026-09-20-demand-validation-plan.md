# Evidence register — GeoNerd demand validation plan

- Idea: `geonerd`
- Register opened: 2026-09-20
- Method version: 1.0.0

## Source

- `/home/richard/projects/geonerd/docs/demand-validation-plan.md` @ `327f02e`
  (internal experimental design, desk-authored, 2026-09-20).

This document supplies the falsification design, not market evidence. It is
recorded so the scorecard's `validation_speed_cost` dimension and the proposed
experiment can be traced to a concrete plan.

## What the plan specifies

| Element | Value |
|---|---|
| One question | Will UK accountancy practices commit real money to a monthly AI-visibility digest at ≥£19/mo, and does the free scan get them there? |
| Cohort | 5 practices, owner/partner decision maker, 1–20 staff, contractor/IR35 or small-practice specialism |
| Network rule | ≥3 of 5 conversations must come from non-network sources; personal relationships excluded from the gate |
| Recruitment | Public directories (ICAEW/ACCA find-an-accountant, Google Maps), community posts, referrals |
| Funnel targets | 100 visits → 30 scans → ≥25% email capture → ≥5 calls held → ≥2 of 5 commitments at ≥£19/mo |
| Price test | Within-subject ladder: £9 / £19 / £29 per month, committed price recorded |
| Effort | 1 week; 12 prompts × 1 surface × 1 manual run per practice (~1 hour each) |
| Decision rule (proceed) | ≥2 of 5 commit at ≥£19/mo **and** ≥25% of scan completers submit email **and** ≥1 non-network channel produces a conversation |
| Iterate rule | ≥1 but <2 commitments, or consistent £9 choice, or email works but no calls |
| Stop rules | 0 of 5 commit at any price; or "interesting but wouldn't pay" persists; or buyers already satisfied by an incumbent |
| Instrumentation | 10 named events recorded from first visitor (landing_view → digest_open) |

## Evidential status

- The plan is executable and bounded: 1 week, ~£50, 20 human-hours.
- The decision rule is fixed in advance and mechanical, satisfying
  `method/experiment-rules.md`.
- It is a **plan, not a result**. No stage of the funnel has been observed.
- It does not validate the measurement pipeline, retention beyond the first
  digest, or CAC (stated in the plan itself, §10).

## Related

- `evidence/geonerd/2026-09-20-wedge-strategy.md` — the hypothesis under test
- `experiments/geonerd-demand-spike/plan.md` — the repository-registered form
