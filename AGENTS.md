# AGENTS.md — operating instructions for this repository

This repository is a durable, evidence-driven business idea discovery and
validation loop, run ad hoc with OpenCode + DeepSeek. It exists to find ideas
worth testing and to kill weak ones cheaply — not to generate volume. A run that
advances nothing is a valid run.

The method documents under `method/` are authoritative. Read them before acting:

- `method/lifecycle.md` — states, transitions, who may advance what
- `method/evidence-policy.md` — what counts as evidence, and what does not
- `method/scorecard.md` — dimensions, weights, thresholds, hard filters
- `method/experiment-rules.md` — experiment approval, execution, result recording
- `method/review-policy.md` — review triggers, states, history
- `method/run-protocol.md` — the 10-step run and its hard limits
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

1. Review `ideas/index.json`, killed ideas, active experiments and the latest
   retrospectives. Handle any outstanding `changes-requested` reviews first.
2. If 10 or more ideas are unreviewed, **stop generating**.
3. Otherwise generate at most **3 materially distinct** new candidates.
4. Apply the 9 hard rejection filters before any deep research.
5. Research survivors: problem/buyer, alternatives, distribution, feasibility,
   economics, risk, founder fit.
6. Run an explicit adversarial review whose goal is to kill the idea.
7. Update the ledger: `ideas/index.json`, dossier, evidence register, scorecard,
   decision record.
8. Advance at most **1** idea to `validation-ready` per run, and only if the
   scorecard threshold and review policy are satisfied.
9. Propose the cheapest experiment capable of disproving the central assumption.
   Cost more than 20 human-hours or £100 requires a review request first.
10. Write the run summary and list what needs human input.

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

## Duplicate and rejection handling

Before adding a candidate, check `ideas/index.json` fingerprints and titles and
any prior killed ideas. If it is a variant of an existing idea, update that idea
instead of creating a duplicate — or record why it is materially distinct.
Rejected ideas stay in the ledger with their reasons; never delete them.

## Output contract

A run leaves reviewable, committed-ready changes:

- ledger updates in `ideas/index.json` and the relevant `ideas/<slug>/` files
- an evidence register under `evidence/<slug>/` for every material claim
- a decision record describing what changed and why
- experiment proposals under `experiments/`
- a run summary at `runs/$LAB_RUN_ID/summary.md` (the wrapper sets
  `LAB_RUN_ID`; run `printenv LAB_RUN_ID` if unsure)

The summary must state: advances, kills, failed/abandoned experiments, decisions
awaiting human input, and confirmation that no disallowed actions were taken.
