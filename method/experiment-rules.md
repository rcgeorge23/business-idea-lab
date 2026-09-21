# Experiment Rules

Method version: see `method/VERSION`.

An experiment is the only way an idea moves past `validation-ready`. Desk research can
rank ideas; it cannot validate them.

## Rules for proposing an experiment

1. **One central assumption.** State the single assumption whose failure kills the
   idea. Everything else is secondary.
2. **Pre-fixed decision rule.** The proceed / iterate / stop rule, including numbers and
   a timebox, must be written before the experiment starts and must not change
   mid-experiment. If the rule is wrong, record a new experiment; do not edit the old
   one.
3. **Cheapest decisive test.** Prefer the smallest test that can produce disconfirming
   evidence. Cost bound is recorded (`cost_bound`: money, human hours, calendar days).
4. **Kill condition.** Every experiment states what result means "stop". An experiment
   with no possible failing outcome is not an experiment.
5. **Human approval first.** The worker may only propose. The human owner decides
   whether the experiment runs, and performs or authorises all outreach, spend,
   publication and commitments. `approval.granted` must be `true` before any external
   action.
6. **Benchmark effort threshold.** A proposed experiment whose projected effort exceeds
   `20 human-hours` or `GBP 100` requires an independent review request (see
   `method/review-policy.md`) before human approval.

## Lifecycle of an experiment

```
proposed -> awaiting-approval -> approved -> running -> completed | abandoned
```

- `proposed`: worker created `experiments/<id>/plan.md` and the index entry.
- `awaiting-approval`: plan is complete and ready for the human owner.
- `approved`: human owner recorded approval (`approval.granted = true`, date, name).
- `running`: external activity has started (only after approval).
- `completed`: results recorded in `experiments/<id>/results.md` and summarised in the
  dossier.
- `abandoned`: stopped before completion; reason recorded.

## Recording results

- Results are recorded by the human owner or transcribed verbatim by the worker from
  material the owner supplies. Direct quotes are labelled as quotes.
- `results.md` must include: dates, what actually happened, the numbers the decision
  rule needs, anything that contradicted expectations, and raw artefacts (transcripts,
  spreadsheets) or links to them.
- The decision rule is then applied mechanically in a `Verdict` section. If evidence is
  insufficient to apply the rule, the verdict is "insufficient evidence", not
  "proceed".
- The worker then updates: the experiment status, the idea dossier, the decision record,
  the scorecard evidence links, and `ideas/index.json`. The human owner decides the
  resulting state (`validated`, `iterate`, `killed`).
- Negative and messy results are first-class: they are recorded with the same care as
  positive ones. A well-run experiment that produces a stop decision is a success.

## Guardrails

- Never contact a real person, create an account, publish anything, or spend money
  without explicit recorded approval.
- Never fabricate or extrapolate results. Missing data is reported as missing.
- Do not run a second experiment on the same assumption to "confirm" a favourable first
  result; run the pre-fixed decision rule instead.
- Survey interest, search volume, and model opinion are not demand. Actions with cost
  (time, data, introductions, money) are.
