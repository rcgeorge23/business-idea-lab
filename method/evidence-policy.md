# Evidence Policy

Method version: see `method/VERSION`.

## The three registers

Every material statement in a dossier, scorecard or decision record belongs to exactly
one register, and is labelled in the text:

| Register | Meaning | Example | What it can support |
|---|---|---|---|
| **Evidence** | An externally checkable fact with a dated source | "SearchScore lists 1,038 audited UK accountancy firms (searchscore site, accessed 2026-09-20)" | Scores, transitions, kill decisions |
| **Assumption** | Something we believe but have not verified; must be falsifiable | "We assume owners read a monthly email" | The design of an experiment; never a score by itself |
| **Inference** | A conclusion drawn from evidence, with the reasoning shown | "Density makes per-customer collection cost fall, so £19.99 is viable at d>=10" | Lower-confidence scores; must cite the evidence it rests on |

An unlabelled material statement is treated as an inference at best. If it has no source
and no reasoning, it is noise and must be removed or marked as an assumption.

## Sources

- Every material claim in `evidence/` carries: source name, URL or file path, access
  date, and a one-line note on why it is credible.
- `ideas/**/scorecard.json` entries point at evidence register files (paths under
  `evidence/`) or external URLs with an access date.
- Dates are `YYYY-MM-DD`.
- Self-reported vendor claims, listicles, and AI-generated summaries are usable only as
  weak secondary evidence and must be labelled as such. Vendor claims never establish
  demand.
- Desk research, search volume, survey interest, and model opinion are **not** demand
  evidence. Only target buyers doing something costly counts.

## Scoring rule

**No source, no score.** A dimension with no evidence scores `null` (not 0) and is
excluded from the weighted aggregate; the exclusion is counted and reported. An idea
scored on fewer than 8 of the 10 dimensions is never `validation-ready`.

Scores are integers 0-5 and confidence is recorded separately per dimension:

- `high` - primary evidence, current (<=6 months) and directly about this buyer/market
- `medium` - credible secondary evidence or older primary evidence
- `low` - analogy, inference, or a single weak source

## Evidence levels

The per-idea evidence level (`Plausible`, `Promising`, `Validation-ready`, `Demand
evidence`, `Commercial evidence`, `Repeatability evidence`) is defined in
`method/lifecycle.md` and is derived from the strongest evidence present, not from the
number of sources.

## External evidence

Real-world results (experiments, conversations, commitments) are recorded by the human
owner, or by the worker transcribing results the owner supplies, under `experiments/`
and linked from the idea dossier. The worker may never fabricate, extrapolate or
"clean up" external results. Contradictory results must be recorded, not reconciled
away.

## Preservation

- `evidence/` entries are append-only once cited. Corrections are new entries that
  reference the old one, or explicit annotations marked `CORRECTION`.
- Rejected and killed ideas keep their evidence and reasons in place.
- Nothing in the ledger is silently overwritten; history is added.
