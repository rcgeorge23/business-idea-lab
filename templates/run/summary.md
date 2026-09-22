# Run summary: <run-id>

- **Mode:** normal | dry-run | smoke
- **Started / finished:** ISO-8601
- **Agent / model:** idea-worker / opencode-go/deepseek-v4.1-flash
- **Method version:** 1.7.0
- **Input / output revision:** `<sha>` / `<sha or 'uncommitted'>`
- **Status:** success | failed | invalid-output | over-budget

## Seed register review

| Seed | Shallow re-check result | Action (candidate / stays seed / status change) |
|---|---|---|

## Opportunity observations

| Metric | Value |
|---|---|
| Observations in pool | n (target 15–20) |
| Source-class distribution | ... |
| Change-driven / persistent market failure / latent opportunity | n / n / n |
| Rejected in shallow triage | n |
| Principal triage rejection reasons | ... |
| Promoted to full candidates | n (≤ 3) |
| Promoted observations and why | O1 → candidate-x: ... |
| Latent observations found / triaged / promoted / rejected | n / n / n / n (zero promotions acceptable) |

**Pool file:** `observations/<run-id>.md`. Observations carry no score,
confidence or evidence level, and triage survival confers no inherited
positive evidence on a promoted candidate.

## Triage false-negative audit

Exactly one triage-rejected observation is re-checked each normal funnel run,
preferring promising/high-ambiguity rejections (relatively strong practitioner or
problem evidence, rejected because an incumbent/free alternative appeared to occupy
the seam). Keep it cheap - roughly the cost of one observation - and record:

| Field | Value |
|---|---|
| Observation selected | |
| Why selected (vs other rejections) | |
| Original triage reasoning | |
| Additional evidence checked | |
| Confusion tests: existence vs satisfaction / feature vs solution / enterprise vs niche / claims vs capability / one-shot vs recurring | |
| Outcome | upheld / overturned |
| Implication for triage depth | |

A single overturn changes nothing; repeated overturns are a trigger to review triage
depth. The audit is also recorded in the pool file.

## Source classes searched

Record every class attempted, including unsuccessful searches. Mark each
`regulatory` or `non-regulatory`; the source-class budget needs at least 2 of 3
candidate slots from non-regulatory classes, at most 1 regulation-derived, and
at least one previously underexplored non-regulatory class actually searched.

| Source class | Regulatory? | Searched? | What it yielded (or why nothing) |
|---|---|---|---|
| Legislation / regulation | yes | | |
| Consultations / announced rules | yes | | |
| Mandated formats / submissions | yes | | |
| New APIs / developer surfaces | no | | |
| New datasets | no | | |
| Platform rule / pricing / access changes | no | | |
| Incumbent disruption (EOL, shutdown, migration) | no | | |
| Poor / expensive narrow incumbent software | no | | |
| New technical capability (esp. AI on repetitive service work) | no | | |
| Manual structured-data flows / re-keying | no | | |
| Awkward integrations between established systems | no | | |
| Underserved subsegments of an existing category | no | | |

**Source-budget outcome:** [met / not met — of N candidates, X non-regulatory,
Y regulation-derived; previously underexplored class searched: ...; if not met,
why, and why no filler candidates were manufactured]

## Why-now quality

For every promoted persistent-market-failure candidate, state whether the two-part
persistence thesis is evidenced (`strong` | `weak` | `absent`) and which limb of the
test passed or failed (see `method/discovery.md`).

| Candidate | Archetype | Why now (one line) | Strength | Persistence thesis | Competitors responded |
|---|---|---|---|---|---|

## Candidate provenance

| Candidate | Observation ID | Provenance (seed:<slug> or fresh) | Source class (regulatory?) | Why it qualifies for that class | Second-order seam | Why not the obvious first-order product |
|---|---|---|---|---|---|---|

## What advanced

| Idea | From | To | Why |
|---|---|---|---|

## What was killed

| Idea | Reason | Preserved in |
|---|---|---|

## What failed or was skipped

## Convergence assessment

<Is discovery converging on less obvious, better-defended opportunities, or repeating a
single class of candidate (e.g. "new mandate -> compliance SaaS") that keeps failing the
same hard filter? Flag it for method review; do not weaken a filter.>

## Limits encountered

- Candidates generated: n / 3
- Unreviewed after run: n / 10
- Advances to validation-ready: n / 1
- Web lookups: n / 40
- Cost: $x / $1.00 (tokens: n)

## Decisions needing human input

| Decision | Options | Deadline / trigger | Where recorded |
|---|---|---|---|

## Review queue after this run

| Idea | Review status | Request | Outstanding since |
|---|---|---|---|

## Next run should

<Two or three concrete priorities.>
