# Run summary: 20260920T210550Z-normal

- **Mode:** normal
- **Started / finished:** 2026-09-20T21:05:50Z / 2026-09-20T21:10:31Z
- **Agent / model:** idea-worker / opencode-go/deepseek-v4.1-flash
- **Method version:** 1.0.0
- **Input / output revision:** `uncommitted` / `uncommitted`
- **Status:** success

## What advanced

| Idea | From | To | Why |
|---|---|---|---|
| — | — | — | No idea was advanced this run. `geonerd` remains `validation-ready` with an open review request; no advance to `validation-ready` was proposed. |

## What was killed

| Idea | Reason | Preserved in |
|---|---|---|
| shiftswap | Hard filters failed (non-paid distribution, defensible wedge, network effects, margins, all-optimistic). Every low-cost UK rota tool already bundles self-service shift swaps. | `ideas/shiftswap/`, `ideas/shiftswap/decision.md`, `evidence/shiftswap/` |
| wonkybox | Hard filters failed (non-paid distribution, defensible wedge, margins, all-optimistic). Category leader Oddbox is loss-making at ~£27m revenue with operating losses widening 98.7% in FY2025. | `ideas/wonkybox/`, `ideas/wonkybox/decision.md`, `evidence/wonkybox/` |
| grantscout | Passed all hard filters at desk screen (the run's attractive control), then failed the adversarial pass: active veto on `defensible_wedge` — GovOwed already sells the exact flat-fee wedge (£29 one-time / £499-per-year), and GOV.UK "Find a grant" provides authoritative discovery for free. | `ideas/grantscout/`, `ideas/grantscout/decision.md`, `evidence/grantscout/` |

## What failed or was skipped

- No experiments were run; none were proposed this run (all three candidates were killed before an experiment was justified). The existing `geonerd-demand-spike` remains `proposed`, awaiting human approval.
- No `changes-requested` reviews existed at run start; there was nothing to answer under step 8.
- `method/` was not edited, per the worker boundary. `method/calibration.md` is now stale: it still lists the first normal run as "pending" although this run completes it and generates the required fixtures (2 weak ideas killed via the documented hard-filter path; 1 attractive control killed by adversarial veto). A human should update the status table in a method-calibration action.

## Limits encountered

- Candidates generated: 3 / 3
- Unreviewed after run: 0 / 10
- Advances to validation-ready: 0 / 1
- Web lookups: 6 / 25
- Cost: not yet recorded in this file (the wrapper writes `run.json` / `runs/index.jsonl` from `usage.json` at finalisation); well within the $1.00 default bound. Tokens: see `run.json`.

## Decisions needing human input

| Decision | Options | Deadline / trigger | Where recorded |
|---|---|---|---|
| GeoNerd independent review | Provide the ChatGPT critique; worker must then respond explicitly and never overwrite it | Before any further GeoNerd advance | `reviews/2026-09-20-geonerd-review-request.md`, `ideas/geonerd/scorecard.json#review` |
| Approve or decline the GeoNerd demand spike | Grant/decline `approval.granted` (£50, 20 human-hours, 7 days) | Before any contact, spend or publication | `experiments/index.json`, `experiments/geonerd-demand-spike/plan.md` |
| Update `method/calibration.md` status table | Mark first normal run complete; record fixtures generated | Anytime; worker may not edit `method/` | `method/calibration.md` (human edit) |
| Early false-negative audit of the attractive control (grantscout) | Optional early audit despite the 5-kill trigger not being reached | Optional | `ideas/grantscout/decision.md` |
| Reopen grantscout via a review request | Leave killed, or raise `killed` -> `requested` if the human disputes the veto | Optional | `ideas/grantscout/scorecard.json#review` |

## Review queue after this run

| Idea | Review status | Request | Outstanding since |
|---|---|---|---|
| geonerd | requested | `reviews/2026-09-20-geonerd-review-request.md` | 2026-09-20 |

No review was requested for the three killed ideas: each is a documented hard-filter rejection or a kill resting on a cited veto, which does not trigger review. No `changes-requested` review exists, so no review outcome was overwritten or ignored.

## Next run should

1. If the ChatGPT/independent review of GeoNerd has landed, respond to every point explicitly in a dated review-response file and update `scorecard.json#review.history`; if it is `changes-requested`, treat that as the first task.
2. If GeoNerd is approved and the human owner has recorded experiment results, process them mechanically against the pre-fixed decision rule; otherwise leave the idea untouched.
3. If GeoNerd is killed or iterated, generate up to 3 materially distinct new candidates, checking all fingerprints and the three existing killed ideas first.

## Disallowed actions

No commits, pushes, issues, pull requests or other publication; no contact with anyone; no spend; no accounts created; no content published; no commitments made. Only repository files were written. `python3 scripts/validate_repo.py` reports **PASS: 0 error(s), 0 warning(s)**.
