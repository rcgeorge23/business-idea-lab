# Lifecycle

Method version: see `method/VERSION`. This file defines the only legal states for an
idea, who may move it, and what each transition requires.

## States

| State | Meaning | Set by |
|---|---|---|
| `discovered` | Candidate recorded with a buyer/problem hypothesis; not yet screened | worker |
| `desk-screened` | Hard rejection filters applied; first pass of evidence recorded | worker |
| `adversarially-researched` | Explicit kill attempt documented; strongest disconfirming case stated | worker |
| `validation-ready` | Narrow proposition plus a cheap, decisive external test with a pre-fixed decision rule | worker, subject to the review rules in `method/review-policy.md` |
| `externally-tested` | At least one approved external test has run and its results are recorded under `experiments/` | state recorded by worker from results supplied by the human owner |
| `validated` / `iterate` / `killed` | Outcomes after external evidence | human owner decides; worker records |

`killed` is reachable from any state. Killed ideas are never deleted; they are preserved
with their reason (including false-negative audits).

## Who may advance what

- The worker (OpenCode + DeepSeek) may set `discovered`, `desk-screened`,
  `adversarially-researched`, and `validation-ready` (subject to the review trigger),
  and may record `killed` with a reason.
- The worker MUST NOT set `externally-tested`, `validated` or `iterate` without
  human-recorded real-world evidence. It may only propose these transitions.
- The human owner approves all external tests, outreach, expenditure, publication,
  external account creation, and commitments. Approval is recorded in the experiment
  record (`approval.granted`) before anything external happens.
- A second model (e.g. ChatGPT) is a reviewer, not a validator. Its opinion is never
  market evidence and never advances an idea on its own; it can block or require
  changes to a proposed transition.

## Allowed transitions

| From | To | Requires |
|---|---|---|
| `discovered` | `desk-screened` | No hard filter `fail` (an `unknown` with `resolve_via` is allowed); at least one dated source for the problem; decision record written |
| `discovered` / `desk-screened` | `killed` | A failed hard filter or a documented disconfirming finding; reason preserved |
| `desk-screened` | `adversarially-researched` | Adversarial pass recorded: strongest disconfirming case, and why the idea survives it (or the idea is killed) |
| `adversarially-researched` | `validation-ready` | Scorecard meets the threshold in `method/scorecard.md`; no hard filter `fail`; no active veto; every `unknown` filter is named in the proposed experiment; review triggered (`review.status != not-required`) |
| `validation-ready` | `externally-tested` | `review.status == approved` AND human owner approved the experiment AND results are recorded |
| `externally-tested` | `validated` / `iterate` / `killed` | Human owner decision recorded in the decision record |
| any | `killed` | Reason recorded; prior state kept in history |

Downward moves (e.g. `validation-ready` -> `adversarially-researched` after a
`changes-requested` review or a tightened rescore) are legal and must be recorded as a
transition, never edited away.

### Experiments while parked

The threshold for `validation-ready` is deliberately strict, but the **experiment is not
gated on it**. A parked idea (`adversarially-researched`, or lower) may carry a proposed
experiment under `experiments/`, and the human owner may approve and run it. External
results recorded against a parked idea are the normal route back up: they raise the
evidence level and allow the idea to be re-scored and re-proposed. This lets promising
ideas reach a cheap decisive test without inflating their desk evidence.

### Why now

Every candidate discovered under method >= 1.1.0 records an evidenced `why_now` in
`ideas/index.json` and a "Why now?" section in its dossier (see `method/discovery.md`).
A missing or unevidenced "why now?" does not by itself kill an idea, but it caps
`differentiation` and `problem_severity_frequency` at 2 and is a strong reason to reject
a generic or crowded candidate at screening.

## Evidence levels

Evidence level is recorded per idea; it caps the safe state.

| Level | Definition | Highest state it supports |
|---|---|---|
| Plausible | Coherent problem + buyer hypothesis, no external evidence yet | `desk-screened` |
| Promising | Credible secondary evidence, no fatal desk objection | `adversarially-researched` |
| Validation-ready | Narrow proposition + cheap decisive external test with a pre-fixed decision rule | `validation-ready` |
| Demand evidence | Target buyers take meaningful action (time, data, introductions, real usage), not just expressed interest | `externally-tested` |
| Commercial evidence | >=2 unrelated target customers pay, pre-order, or commit a scarce resource | `externally-tested` / `validated` |
| Repeatability evidence | Acquisition and delivery repeat at workable economics | `validated` |

## Where state lives

- `ideas/index.json` carries `state` for every idea (machine-readable).
- The idea's `scorecard.json` carries the same `state` plus the `review` block and
  `review.history` (append-only).

These must never disagree; `scripts/validate_repo.py` fails the repository if they do.
