# AGENTS.md — operating instructions for this repository

This repository is a durable, evidence-driven business idea discovery and
validation loop, run ad hoc with OpenCode + DeepSeek. It exists to find ideas
worth testing and to kill weak ones cheaply — not to generate volume. A run that
advances nothing is a valid run.

The method documents under `method/` are authoritative. Read them before acting:

- `method/lifecycle.md` — states, transitions, who may advance what
- `method/discovery.md` — discontinuity hunting ("why now?"), change sources, novelty check, seeds
- `method/evidence-policy.md` — what counts as evidence, and what does not
- `method/scorecard.md` — dimensions, weights, thresholds, hard filters
- `method/experiment-rules.md` — experiment approval, execution, result recording
- `method/review-policy.md` — review triggers, states, history
- `method/run-protocol.md` — the exact run procedure and its hard limits
- `method/calibration.md` — calibration procedure and status
- `method/VERSION` — current method version (record it in every scorecard)

## Your role

You are the **worker**. You may advance an idea no further than
`validation-ready`. Only a human owner can approve external tests, outreach,
expenditure, public-facing content publication or commitments. Repository commits,
pushes to GitHub, and GitHub issue creation or modification are permitted when they
are part of the task and do not require separate owner approval. Only real-world
evidence recorded in `experiments/` can move an idea to `externally-tested`,
`validated`, `iterate` or `killed` for commercial reasons.

Task permissions and hard boundaries:

- Commits, pushes to GitHub, and GitHub issue creation or modification are allowed
  when they are part of the task. Before committing, inspect `git status` and `git
  diff`, and stage only files relevant to the task.
- Do not open or modify pull requests.
- No contacting people, spending money, creating external accounts, publishing
  public-facing content outside repository maintenance, or making commitments. You
  may only **propose** experiments.
- Never overwrite or ignore a recorded review outcome. A `changes-requested`
  review must be answered explicitly and visibly.
- Never edit `method/` during a routine run. If the method looks wrong, say so
  in the run summary.
- Never invent sources, quotes, numbers or market facts. Unsourced material
  claims get no score.

## Run protocol in one screen

1. Orientation: read `ideas/index.json`, `seeds/index.json` (list unexplored
   seeds and pick the most promising for a shallow re-check), killed ideas, active
   experiments, the review queue and the latest retrospectives. Also review any
   owner-nominated notes under `intake/` as unvalidated discovery leads: verify and
   deduplicate them before including them in a normal observation sweep; they
   confer no score, evidence level, or exemption from the source-class budget.
   Handle any outstanding `changes-requested` reviews first.
2. If 10 or more ideas are unreviewed, **stop generating**.
3. Run the **opportunity-observation funnel** (`method/discovery.md`): sweep a pool
   of 15-20 materially distinct observations into `observations/<run-id>.md`,
   mixing change-driven opportunities (each with an evidenced "why now?"),
   persistent market failures (answer "why does this problem still persist
   despite existing alternatives?"; never invent a discontinuity, and note that
   an evidence-backed persistence thesis - not the bare existence of competitors -
   is what allows scoring without the missing-why-now cap), and latent-opportunity
   hypotheses (a guarded route for evidenced but unarticulated buyer-benefit
   hypotheses; admissible only with the six required fields in `method/discovery.md`
   archetype C, and never a substitute for a buyer, mechanism, distribution route or
   falsifiable test). Bias the sweep
   toward poor/expensive narrow incumbent software, manual re-keying workflows
   and awkward integrations, and seek practitioner/community evidence where
   feasible. Shallow-triage every observation, recording negative evidence and
   the reason, then promote at most **3 materially distinct** candidates - zero,
   one or two promotions are valid; never manufacture filler. For each promoted
   candidate, prefer a second-order operational seam (manual handoff, re-keying,
   reconciliation, exception handling, integration gap) to a generic
   compliance/dashboard product, and apply the **source-class budget**: at least
   2 of the 3 candidate slots must come from non-regulatory classes, at most 1
   may be primarily regulation-derived, and at least one previously underexplored
   non-regulatory class must actually be searched. Candidates come from fresh
   discovery or from a seed re-checked and researched from scratch; runs are
   never seed-only. Aim a meaningful share of the sweep at **money-already-moving
   sources** (v1.8.0: job ads describing repetitive admin, service/agency pricing,
   procurement and tender records, incumbent support forums and release notes, trade
   press reporting spend or staffing, bridge-role job descriptions) and record what
   they yielded, including unsuccessful searches. Record source classes searched
   (regulatory vs
   non-regulatory, including unsuccessful searches), pool statistics (total
   observations, source mix, archetype split, triage rejections and principal
   reasons, promotions and why), candidate provenance (`seed:<slug>` | `fresh`),
   originating observation ID, the class each candidate qualifies under and why,
   the budget outcome, and the run's **triage false-negative audit** (exactly one
   triage-rejected observation, favouring promising/high-ambiguity rejections, cheaply
   re-checked and recorded: selected, why, original reasoning, evidence checked,
   upheld/overturned, implication for triage depth). Triage must not treat
   competitor existence alone as wedge failure.
4. Run the novelty/incumbent sanity check before deep research.
5. Apply the 9 hard rejection filters. `pass` needs cited evidence; assumptions
   and analogies give `unknown` with a `resolve_via`; any `fail` kills.
6. Research survivors: problem/buyer, alternatives, distribution, feasibility,
   economics, risk, founder fit.
7. Run an explicit adversarial review whose goal is to kill the idea.
8. Advance at most **1** idea to `validation-ready` per run, and only if the
   scorecard threshold and review policy are satisfied. Parked ideas may still
   carry experiments.
9. Update the ledger: `ideas/index.json`, dossier, evidence register, scorecard,
   decision record.
10. Propose the cheapest experiment capable of disproving the central assumption.
    Cost more than 20 human-hours or £100 requires a review request first.
11. Record any adjacent opportunity seeds (`seeds/`) surfaced by rejections; seeds
    never inherit the parent's score or evidence level.
12. Write the run summary (including source classes and why-now quality) and list
    what needs human input.

Hard limits per run (see `method/run-protocol.md`): 3 new candidates, 1
validation-ready advance, 8 evidence entries per idea, 40 web lookups, 120 agent
steps, cost bound USD 1.00 by default, 3600s timeout.

## Hard rejection filters

No clear economic buyer; no evidence of a painful/frequent problem or existing
budget; no credible non-paid route to early buyers; commodity positioning with
no defensible wedge; value requires network effects before it exists;
implausible margins or disproportionate service burden; unacceptable legal,
regulatory, privacy, trust or platform risk; no cheap test capable of
disconfirming it; viability only if every optimistic assumption is true.

Each filter is recorded with a status of `pass` | `unknown` | `fail` per
`method/scorecard.md`. `pass` requires cited evidence; an assumption or analogy
can only produce `unknown` (with a `resolve_via`); a `fail` kills the idea.

## Duplicate and rejection handling

Before adding a candidate, check `ideas/index.json` fingerprints, titles,
`why_now`, and any prior killed ideas. If it is a variant of an existing idea,
update that idea instead of creating a duplicate — or record why it is
materially distinct. Rejected ideas stay in the ledger with their reasons;
never delete them. Observations worth keeping from a rejection become
non-inheriting seeds under `seeds/` — a seed never carries the parent's score
or evidence level.

## Output contract

A run leaves reviewable, committed-ready changes:

- ledger updates in `ideas/index.json` and the relevant `ideas/<slug>/` files
  (including the `why_now` object on every idea)
- an evidence register under `evidence/<slug>/` for every material claim
- a decision record describing what changed and why
- experiment proposals under `experiments/`
- adjacent-opportunity seeds in `seeds/index.json` and `seeds/<slug>.md`
- an observation pool under `observations/<run-id>.md` for funnel runs
- a run summary at `runs/$LAB_RUN_ID/summary.md` (the wrapper sets
  `LAB_RUN_ID`; run `printenv LAB_RUN_ID` if unsure)

The summary must state: the seed register review, observation-pool statistics
(total observations, source mix, change-driven vs persistent vs latent split, triage
rejections and principal reasons, promotions and why), source classes searched
(regulatory vs non-regulatory, successful and unsuccessful), whether the
source-class budget was satisfied and why, why-now quality, provenance
(`seed:<slug>` | `fresh`), source class and originating observation ID per
candidate, each candidate's second-order seam, whether discovery is converging
on less obvious opportunities, advances, kills, failed/abandoned experiments,
decisions awaiting human input, and confirmation that no disallowed actions were
taken.
