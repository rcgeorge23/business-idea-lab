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

## Plausibility is not evidence

A coherent, well-written or quantitative account of why an idea should work is still not
evidence that it does. From v1.1.0:

- analogies to other markets, business-model models/spreadsheets, model output, vendor
  positioning and "a wedge can be described" are **plausibility**, not evidence;
- plausibility caps dimension scores at 2 (see `method/scorecard.md`), contributes
  nothing to the aggregate at 3+, and can never produce a hard-filter `pass`;
- when a hard filter is plausible but undemonstrated, the honest status is `unknown`
  with a `resolve_via` naming the cheap check that would settle it - not `pass`;
- modelled economics built on untested inputs are capped at 2 with `low` confidence
  regardless of how detailed the model is;
- the fact that a direct competitor already sells the proposed position is evidence
  *against* differentiation and must lower that dimension, not be ignored.

**Latent-opportunity hypotheses (v1.7.0).** A hypothesis that a buyer would value a
capability they have not asked for is admissible as an observation only when it names
the buyer and their observed current behaviour, the newly possible capability and its
mechanism, the inferred value (labelled as inference), the status quo and competitors,
and a falsifiable assumption with a cheap test (see `method/discovery.md`, archetype C).
Such a hypothesis:

- may justify a **cheap test** without a pre-existing complaint or search query;
- is **never** demand evidence, and never produces a hard-filter `pass` - missing
  evidence stays `unknown` with a `resolve_via`;
- does not lift any score cap, lower the threshold or redefine evidence levels;
- still requires real target-buyer behaviour (payment, pre-order, meaningful
  commitment, or an approved experiment with a pre-declared decision rule) before any
  demand or commercial claim.
- A search pass with no usable result, or no complaint found, does not establish that
  the behavior is absent and does not establish demand. Search yield is discovery
  coverage, not evidence of non-consumption or purchase intent.

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
