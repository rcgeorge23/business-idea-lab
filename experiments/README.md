# experiments/ — proposed, approved, running and completed experiments

Every idea's decisive test is registered in `experiments/index.json` and has a
plan at `experiments/<experiment-id>/plan.md`, following
`templates/experiment/plan.md`.

Statuses: `proposed -> awaiting-approval -> approved -> running -> completed`
(or `abandoned`). Rules in `method/experiment-rules.md`.

- A worker may only **propose** an experiment. The human owner approves and runs
  it, and records approval in `experiments/index.json`
  (`approval.granted: true`, `granted_by`, `granted_date`).
- Anything over 20 human-hours or £100 needs a review request before approval.
- Results are recorded by the human owner (or transcribed from material the
  owner supplies) in `experiments/<experiment-id>/results.md`, following
  `templates/experiment/results.md`.
- The recorded decision rule is applied mechanically; do not reinterpret a
  threshold after seeing the data. An ambiguous result is recorded as
  ambiguous.
- Only real-world results recorded here can move an idea beyond
  `validation-ready`.
