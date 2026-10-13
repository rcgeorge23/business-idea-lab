# Legacy re-triage

Method 1.9.0 changed both the discovery route (search-intent-first) and the
scorecard (schema v2, weights 1.3.0, 12 hard filters including three
self-service gates). Ideas recorded under schema v1 keep their original
method version, scores, decisions and review outcomes, permanently. This
document defines the **opt-in** procedure for re-assessing such an idea
under current criteria without rewriting any of that history.

A re-triage is a deliberate, owner-triggered action. It is never run
automatically over the ledger, and it must never be used to launder a new
score into an old card.

## Principles

1. **History is evidence, not a draft.** `ideas/<slug>/scorecard.json`,
   `decision.md`, the review history and any kill reasons are append-only.
   A re-triage does not edit them, does not change their `method_version`,
   `schema_version` or `weights_version`, and does not replace their scores.
2. **Additive memo.** The output of a re-triage is one new file,
   `ideas/<slug>/retriage-<YYYY-MM-DD>.md`, that states the original record
   (clearly labelled with its method/weights version) and the current
   assessment alongside it. Old and new assessments are never presented
   together without those labels, and no combined or blended score is
   produced.
3. **No numeric rescoring of the old card.** The v1 card is not recalculated
   under v2 weights. If the owner wants a v2 assessment, the route is a
   fresh candidate entry with its own slug, fingerprint, evidence register
   and schema v2 scorecard, linked from the memo; it does not inherit the
   old card's score, evidence level or review outcome.
4. **Same evidence standards.** A re-triage uses only recorded, cited
   evidence unless the run's lookup budget is explicitly spent on new
   research (in which case the new evidence is registered normally).
   Invented or remembered data cannot appear. Per-gate findings use
   `pass` | `unknown` | `fail` with the same semantics as
   `method/scorecard.md`: `pass` needs cited evidence, assumptions give
   `unknown` with a `resolve_via`, and a `fail` is disqualifying for the
   current owner constraints.
5. **No promotion by re-triage.** A re-triage cannot move an idea to
   `validation-ready`. Promotion still requires a full candidate treatment
   under the current method, including the normal hard filters and the
   review trigger.
6. **Recorded, not silent.** A re-triage performed in a run is listed in
   that run's summary (idea, outcome, conclusion) and, when it changes the
   method-level picture, in the calibration status table.

## Procedure

1. **Nomination.** The owner nominates the idea(s), typically in an intake
   note, a GitHub issue or a review response. The worker may also propose a
   re-triage in a run summary, but does not perform one until it is
   nominated or part of an instructed task.
2. **Review the record.** Read the existing dossier, decision, scorecard
   and evidence register. Note the recorded state, evidence level,
   aggregate score and method/weights version, plus any recorded
   contradictions.
3. **Assess against the current gates and filters.** Apply the 12 hard
   filters of the current method, calling out the three self-service gates
   (`seo_discoverable`, `self_serve_purchase`, `solo_operator_fit`)
   explicitly. Statuses are `pass` | `unknown` | `fail`, each with a cited
   basis or an explicit statement that no evidence is recorded.
4. **Choose one conclusion:**
   - **confirm parked** — the recorded decision still stands; no change;
   - **deprioritise** — the idea is not pursued under current owner
     constraints; the memo records why; the ledger is left untouched;
   - **fresh-candidate route** — a new schema v2 candidate is warranted;
     normal discovery, hard-filtering, evidence and review rules then
     apply to the new entry.
5. **Write the memo** at `ideas/<slug>/retriage-<YYYY-MM-DD>.md` with the
   original record, the per-gate findings, the conclusion and what would
   change it.
6. **Leave the ledger alone** unless step 4 chose the fresh-candidate
   route. In that case the new entry follows the normal `ideas/index.json`
   rules; the memo links both records.

## Boundaries

- No contact with buyers, no spend, no publication, no accounts and no
  commitments are made as part of a re-triage.
- A re-triage is not an experiment. Proposed experiments attached to the
  old idea stay exactly as recorded (status, approval, plan) until the
  owner changes them.
- Re-triage never lowers the evidence bar and never confers an evidence
  level, score or review outcome on any other idea.
