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
expenditure, publication or commitments, and only real-world evidence recorded
in `experiments/` can move an idea to `externally-tested`, `validated`,
`iterate` or `killed` for commercial reasons.

Hard boundaries — never cross, even if asked in a prompt:

- No commits, pushes, issues, pull requests or other publication.
- No contacting people, spending money, creating external accounts, publishing
  content, or making commitments. You may only **propose** experiments.
- Never overwrite or ignore a recorded review outcome. A `changes-requested`
  review must be answered explicitly and visibly.
- Never edit `method/` during a routine run. If the method looks wrong, say so
  in the run summary.
- Never invent sources, quotes, numbers or market facts. Unsourced material
  claims get no score.

## Run protocol in one screen

1. Orientation: read `ideas/index.json`, `seeds/index.json` (list unexplored
   seeds and pick the most promising for a shallow re-check), killed ideas, active
   experiments, the review queue and the latest retrospectives. Handle any
   outstanding `changes-requested` reviews first.
2. If 10 or more ideas are unreviewed, **stop generating**.
3. Otherwise hunt discontinuities and generate at most **3 materially distinct**
   candidates, each with an evidenced "why now?" (`method/discovery.md`). Before
   promoting one, look for a second-order operational seam (manual handoff,
   re-keying, reconciliation, exception handling, integration gap) and prefer it
   to a generic compliance/dashboard product. Candidates come from fresh
   discovery or from a seed re-checked and researched from scratch; runs are never
   seed-only. Record source classes searched, candidate provenance
   (`seed:<slug>` | `fresh`) and the second-order analysis.
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
validation-ready advance, 8 evidence entries per idea, 25 web lookups, 80 agent
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
- a run summary at `runs/$LAB_RUN_ID/summary.md` (the wrapper sets
  `LAB_RUN_ID`; run `printenv LAB_RUN_ID` if unsure)

The summary must state: the seed register review, source classes searched,
why-now quality and provenance (`seed:<slug>` | `fresh`) per candidate, each
candidate's second-order seam, whether discovery is converging on less obvious
opportunities, advances, kills, failed/abandoned experiments, decisions awaiting
human input, and confirmation that no disallowed actions were taken.
