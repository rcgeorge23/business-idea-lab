# Review request: <idea title>

- **Idea:** `<slug>`
- **Date:** YYYY-MM-DD
- **Trigger:** <which review trigger from method/review-policy.md>
- **Proposed transition:** `<from>` -> `<to>`
- **Reviewed revision:** `<git sha or 'uncommitted'>`
- **Requested from:** chatgpt (independent reviewer)

## What the reviewer must decide

<One paragraph: the single question the review answers.>

## Decision summary

<3-6 sentences a busy reviewer can act on.>

## State and scores

| Dimension | Weight | Score | Confidence | Evidence |
|---|---|---|---|---|

- Weighted total: X / 100 (threshold 65)
- Overall confidence:
- Hard filters: <pass/fail summary>
- Vetoes: <list or none>

## Strongest supporting case

## Strongest disconfirming case

## Unresolved assumptions

| Assumption | How it could be falsified | If it fails |
|---|---|---|

## Cheapest decisive experiment

- Test:
- Pre-fixed decision rule:
- Cost bound:
- Status:

## Machine-readable review block

<Copy of `scorecard.json#review` and `ideas/index.json` entry.>

## Instructions to the reviewer

1. Work only from the repository artefacts listed below.
2. Attack the weakest link: unsupported inference, convenience evidence, mis-scored
   dimension, premature advancement, missed risk.
3. State a verdict: `changes-requested`, `approved`, or `killed`.
4. For each verdict, list the condition that would change it.
5. Write the response as `reviews/<date>-<slug>-<reviewer>-<model>.md` using
   `templates/review/response.md`.
6. A second model is not market validation. Do not treat agreement as demand evidence.

## Artefacts for review

- `ideas/<slug>/dossier.md`
- `ideas/<slug>/scorecard.json`
- `ideas/<slug>/decision.md`
- `evidence/<slug>/...`
- `experiments/<id>/plan.md`
- `ideas/index.json`
