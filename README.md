# business-idea-lab

A durable, evidence-driven loop for discovering and validating business ideas,
run ad hoc with [OpenCode](https://opencode.ai) + DeepSeek. It exists to find
ideas worth testing and to kill weak ones cheaply — not to generate volume. A
run that advances nothing is a valid run.

- Method (authoritative): `method/` — lifecycle, evidence policy, scorecard,
  experiment rules, review policy, run protocol, calibration.
- Worker instructions: `AGENTS.md`.
- Ledger: `ideas/index.json` and `ideas/<slug>/`.
- Everything else: `evidence/`, `experiments/`, `reviews/`, `retrospectives/`,
  `runs/`, `templates/`, `scripts/`.

## Setup

1. Install OpenCode (`>= 1.18.30` recommended) and start it once in this
   repository. Run `/connect`, choose the opencode-go provider, and complete
   authentication. The pinned model is
   `opencode-go/deepseek-v4.1-flash` (`opencode.jsonc`).
2. If you prefer the native DeepSeek provider instead of the gateway, export
   `DEEPSEEK_API_KEY` in your shell (see `.env.example`). Never commit it —
   `.env*` is gitignored.
3. Verify plumbing without touching the ledger:

   ```bash
   scripts/run.sh --smoke
   ```

4. Run offline validation at any time:

   ```bash
   python3 scripts/validate_repo.py          # human-readable
   python3 scripts/validate_repo.py --json   # machine-readable
   python3 scripts/validate_repo.py --queue  # review queue + counters
   ```

## Running the loop

One deterministic, non-interactive command runs the complete protocol:

```bash
scripts/run.sh                 # normal run against the live ledger
scripts/run.sh --dry-run       # worker runs in a throwaway copy; live ledger untouched
```

Useful flags: `--timeout SECONDS` (default 3600), `--max-cost USD` (default
1.00), `--max-attempts N` (default 3), `--model provider/model`, `--agent NAME`,
`--allow-dirty` (only when you deliberately accept an unclean tree).

What a run does (see `method/run-protocol.md` for the full protocol and
limits):

1. Handles any outstanding `changes-requested` review first.
2. Stops generating if 10 or more ideas are unreviewed.
3. Hunts discontinuities ("why now?") per `method/discovery.md`, generates at
   most 3 materially distinct candidates, each with an evidenced `why_now`, and
   records which source classes were searched.
4. Runs the novelty/incumbent sanity check, then applies the 9 hard rejection
   filters before deep research (`pass` needs cited evidence; assumptions and
   analogies give `unknown` with a `resolve_via`; any `fail` kills).
5. Researches survivors, runs an explicit adversarial review aimed at killing
   them, and updates the ledger, evidence registers, scorecards and decision
   records.
6. Advances at most 1 idea to `validation-ready` per run, only if the scorecard
   threshold and review policy are satisfied. Parked ideas may still carry
   experiments.
7. Records adjacent-opportunity seeds under `seeds/` (they never inherit the
   parent's score or evidence level).
8. Proposes the cheapest experiment that could disprove the central assumption.
9. Writes the run summary to `runs/$LAB_RUN_ID/summary.md`.

Cost and retry bounds are documented in `method/run-protocol.md` and enforced
where practical by `scripts/run.sh` (wall-clock timeout, post-run cost check,
retry only when the tree is unchanged). Every run records timestamp, mode,
agent, model, method version, input/output revision, attempts and cost in
`runs/<id>/run.json` plus one line in `runs/index.jsonl`.

After finalising the run, `scripts/run.sh` regenerates `dashboard.html`, a
single self-contained HTML summary of the whole ledger (portfolio statistics,
score distribution against the 65 threshold, every idea's dimensions, hard
filters, why-now, review and experiment, plus experiments, seeds and run
history). Ideas are grouped by industry, using the controlled vocabulary
recorded on each idea as `industry` in `ideas/index.json` (see
`INDUSTRIES` in `scripts/validate_repo.py`). Open it in any browser — it needs
no server, network or JavaScript dependencies. Regenerate it on demand with:

```bash
python3 scripts/build_dashboard.py            # writes dashboard.html at the repo root
python3 scripts/build_dashboard.py --out /tmp/ledger.html
```

When a normal run is performed ad hoc without `scripts/run.sh`, the worker must
run `python3 scripts/build_dashboard.py` after finalizing the run metadata and
include the generated `dashboard.html` in the final diff. The dashboard is a
generated, read-only view and must not be edited by hand. Dry-runs leave the live
dashboard unchanged.

The dashboard also surfaces the discovery trail that never became a scored idea,
so early rejections stay visible: an **Intake** section listing each
owner-nominated note and its hypotheses, and an **Observation pools** section
listing every funnel run's observations with their triage decision and reason,
promotions and the sampled triage false-negative audit. Both are parsed from the
Markdown under `intake/` and `observations/` with a small tolerant parser; a file
that does not match the expected shape is listed with a note rather than guessed
at. The experiments table and each idea's experiment block also show the
experiment hypothesis text.

Every row in the **Score distribution** section is expandable: click a row to see
that idea's proposed next step, if one has been defined. A row with a next step
carries a small `next step` badge. The panel shows the linked experiment's status,
central assumption, decision rule, kill condition, cost bound and approval state
(so an experiment that is `proposed` and `awaiting owner approval` is obvious at a
glance), plus any outstanding review status and an explicit `next_step` field on
the idea entry if present. An idea with nothing defined shows `No next step
defined.`

The dashboard renders only what the machine-readable ledgers contain and shows
`unknown` / `not recorded` honestly; it is a read-only view and never changes
the ledger. It is skipped during `--dry-run`.

The worker may commit and push repository changes to GitHub, and create or modify
GitHub issues, when those actions are part of the task; no separate owner approval is
required. Before committing, it inspects the worktree and stages only task-related
files. It does not open or modify pull requests, contact anyone, spend money, create
external accounts, publish public-facing content outside repository maintenance, or
make commitments; it may only propose experiments. Review the diff when the run
finishes.

## Reviewing a candidate

Independent review is repository-mediated: the reviewer works only from the
files in this repository.

1. Build a request package:

   ```bash
   python3 scripts/build_review_request.py --slug <slug> \
       --trigger "proposed for validation-ready" \
       --transition "adversarially-researched -> validation-ready"
   ```

   This writes `reviews/<date>-<slug>-review-request.md` containing the state,
   scores, hard filters, strongest supporting and disconfirming cases,
   unresolved assumptions, the decisive experiment and a machine-readable review
   block.

2. Give that file (and the artefact list inside it) to the reviewer. The
   reviewer writes `reviews/<date>-<slug>-<reviewer>-<model>.md` following
   `templates/review/response.md`, with a verdict of `changes-requested`,
   `approved` or `killed`.

3. Record the outcome in `ideas/<slug>/scorecard.json` under `review` and
   `review.history`. History is append-only and transitions are validated
   (`not-required -> requested -> changes-requested | approved | killed`).

4. The next worker run must answer a `changes-requested` review explicitly and
   visibly; it may not silently overwrite any outcome.

Review triggers and the false-negative audit rule (every fifth killed idea) are
in `method/review-policy.md`. A second model is not market validation.

## Recording external experiment results

The human owner runs experiments; results go into the repository:

1. Approve the experiment in `experiments/index.json`
   (`approval.granted: true`, `granted_by`, `granted_date`) — anything above 20
   human-hours or £100 needs a review request first.
2. Run it. Record raw outcomes in
   `experiments/<experiment-id>/results.md` following
   `templates/experiment/results.md` (what happened, verbatim quotes, numbers,
   deviations from the plan).
3. Apply the decision rule that was fixed in the plan **mechanically**. If the
   outcome is ambiguous, record it as ambiguous — do not move the threshold.
4. Update the ledger: if real-world demand or commercial evidence exists, the
   idea may move to `externally-tested`, `validated`, `iterate` or `killed`
   (human owner decision), and the scorecard, dossier and decision record are
   updated with the new evidence.

## Layout

| Path | Purpose |
|---|---|
| `AGENTS.md` | Worker role, boundaries, protocol in one screen |
| `method/` | Authoritative method documents + `VERSION` |
| `ideas/index.json` | Ledger: every idea, state, industry, score, review and experiment link |
| `ideas/<slug>/` | Dossier, scorecard, decision record |
| `evidence/<slug>/` | Dated evidence registers (claims, sources, caveats) |
| `seeds/` | Adjacent-opportunity seeds from rejections (non-inheriting) |
| `experiments/` | Experiment index, plans, results |
| `reviews/` | Review requests and responses |
| `retrospectives/` | What the loop itself should learn |
| `runs/` | Per-run metadata, usage, validation, summaries, dry-run diffs |
| `templates/` | Templates for every artefact type |
| `scripts/` | Validator, runner, usage extraction, review-request builder, dashboard builder |
| `dashboard.html` | Generated browsable HTML summary of the ledger (regenerated by every run) |
| `painmine/` | Issue #9 spike: bounded public pain-signal mining, dedupe, clustering, discovery-priority ranking and Method 1.6 observation export (see `painmine/SPIKE-REPORT.md`) |
| `.github/workflows/` | Optional scheduled painmine collectors (daily collect + weekly cluster/all); no commits, no secrets in repo |
| `.opencode/agent/` | `idea-worker` (primary), `idea-critic` (read-only subagent), `painmine-extractor` (strict-JSON extraction, deny-all tools) |

## Calibration

Calibration compares the loop against known fixtures before its output is
trusted: GeoNerd (seeded), two weak/rejected ideas and one attractive-looking
control produced by the first worker run, plus Aucly as an explicit
calibration/reference case (issue #3), and an independent critique of at least
one DeepSeek result. Status and exit criteria: `method/calibration.md`.
The fixture-generation steps are **done**: the first normal run
(`runs/20260920T210550Z-normal`) produced two weak ideas killed through the
documented hard-filter path (`shiftswap`, `wonkybox`) and one attractive
control killed by adversarial veto (`grantscout`). Under method 1.1.0 GeoNerd
was rescored honestly (65.3 -> 49.5) and parked at `adversarially-researched`.
The Aucly calibration keeps a no-hindsight pre-launch reconstruction
(`ideas/aucly/pre-launch-assessment.md`; 49.5, parked, cheap test proposed) and
a current-state assessment on real operating evidence (`ideas/aucly/dossier.md`;
60.0, parked, early commercial evidence only). The independent ChatGPT
critiques were received and reconciled in issue #6: GeoNerd v2, the ShiftSwap
audit, the BiK audit and method v1.1.0/v1.2.0/v1.3.0 are all `approved` with
caveats preserved, and the falsification-first character of the method was
endorsed. The method **1.4.0** request was answered **`approved`**
(`reviews/2026-09-21-method-v1.4.0-chatgpt.md`) and the method **1.5.0** request was
answered **`changes-requested`** (`reviews/2026-09-21-method-v1.5.0-chatgpt.md`);
method 1.6.0 implements those changes and was itself answered **`approved`**
(`reviews/2026-09-21-method-v1.6.0-chatgpt.md`, no changes requested). The only
outstanding item is the `wonkybox` kill-#15 false-negative audit. The full backlog and
what closed each item is recorded in `reviews/2026-09-21-review-queue-reconciliation.md`.

## Status

- Method version 1.2.0 (2026-09-21): builds on 1.1.0 (discontinuity-first
  discovery with an evidenced `why now?` on every candidate, strict
  `pass`/`unknown`/`fail` hard-filter semantics, plausibility score caps,
  non-inheriting adjacent seeds, early novelty/incumbent sanity check). 1.2.0
  scopes the missing-why-now cap to `Plausible`/`Promising` ideas, so an
  evergreen niche with real payment evidence is judged on that evidence; no
  other rule changed. The `validation-ready` threshold (65) was deliberately
  **not** lowered; honest desk-only ideas typically land in the 45-60 range and
  stay parked, and parked ideas may still carry a proposed experiment. Method
  review requests are open for v1.1.0 and v1.2.0
  (`reviews/2026-09-21-method-v1.1.0-review-request.md`,
  `reviews/2026-09-21-method-v1.2.0-review-request.md`).
- Method 1.3.0 (2026-09-21) is **discovery-only**: candidates must investigate
  second-order operational effects and prefer an awkward workflow/integration
  seam over a generic compliance product; the seed register is reviewed at run
  start and seeds never inherit their parent's scores or evidence; each
  candidate's provenance (`seed:<slug>` or `fresh`) and second-order analysis
  are recorded, and the summary carries a convergence assessment. Scoring
  weights, threshold and hard-filter semantics are unchanged at 1.2.0. Review
  request: `reviews/2026-09-21-method-v1.3.0-review-request.md`.
- Latest run `20260921T081223Z-normal` (USD 0.008245): seed register reviewed
  (one seed dropped, one kept with reasons, one new non-inheriting seed), two
  fresh candidates, `wastetrack` killed (#9) on `defensible_wedge` and
  `bikpayroll` parked at `desk-screened` (50.5) with a desk-only incumbent
  capability scan proposed; **0 advances**. The convergence review
  (`retrospectives/2026-09-21-issue4-convergence-review.md`) finds discovery is
  **not yet converging**: the `defensible_wedge` cluster now spans six
  candidates. It is flagged for review rather than the filter being weakened,
  and the next run is directed to search at least one non-regulatory source
  class and to re-check further seeds.
- Issue #5 (2026-09-21) resolved the BiK payroll seam instead of generating
  more ideas: the pre-committed desk scan
  (`experiments/bikpayroll-incumbent-capability/results.md`) hit its KILL
  branch — Zhoosh Benefits and The Electric Car Scheme (with Zest and
  Zellis/Benefex) already ingest provider benefit data into per-period payroll —
  so `bikpayroll` is killed (#10) with dated evidence. The review backlog is
  reconciled honestly in `reviews/2026-09-21-review-queue-reconciliation.md`
  (nothing answered or superseded; a cumulative 1.0.0 -> 1.3.0 method review is
  offered as a routing option), and `experiments/queue.md` recommends: run
  `reasonable-steps-willingness` first, `aucly-channel-test` second, defer
  `geonerd-demand-spike` until GeoNerd review v2 is routed. The next discovery
  run is recommended only after the backlog is routed and with a
  **non-regulatory sourcing budget** (at least two of three candidate slots from
  non-regulatory classes; at most one mandate-derived candidate; at least one
  previously unsearched class attempted). That sourcing rule is proposed for
  review before adoption (`retrospectives/2026-09-21-issue5-backlog-and-next-run.md`);
  no scoring rule changes.
- Issue #6 (2026-09-21) reconciled the six independent ChatGPT responses (one
  `approved` per review, caveats preserved; the original GeoNerd v1 request is
  historical provenance superseded by v2; no idea was advanced on approval
  alone, and no approval is market validation). The issue #5 sourcing proposal
  became method **1.4.0** as a discovery-only **source-class budget**: at least
  2 of 3 candidate slots from non-regulatory classes, at most 1
  regulation-derived, at least one previously underexplored non-regulatory class
  actually searched, and no filler candidates. The post-change run
  `20260921T085149Z-normal` (USD 0.015021) met the budget with 3 of 3
  non-regulatory candidates - `apispend` (40.0), `ewsregister` (44.6) and
  `agent-checkout-offplatform` (49.2, a seed promoted and researched from
  scratch) - and **killed all three on `defensible_wedge`**; 0 advances. Two
  source searches failed (HTTP 429) and are recorded as unsuccessful. The
  convergence review
  (`retrospectives/2026-09-21-issue6-convergence-review.md`) retains the budget,
  reports that changing the source class changed the candidate subject matter
  but not the rejection reason, and escalates the third consecutive
  `defensible_wedge` cluster to a human-led review of discovery sourcing and
  framing. The filter is explicitly **not** weakened. The 1.4.0 review request was
  answered **`approved`** on receipt of `reviews/2026-09-21-method-v1.4.0-chatgpt.md`
  and was then superseded by 1.5.0; `reasonable-steps-willingness` remains deferred
  with no outreach.
- Method 1.5.0 (2026-09-21, issue #7) is **discovery-shape only**: every normal
  run now sweeps a pool of 15-20 materially distinct **opportunity
  observations** (`observations/<run-id>.md`) covering both change-driven
  opportunities and persistent market failures, shallow-triages all of them with
  recorded negative evidence, and promotes at most 3 to full candidates through
  the unchanged evaluation machinery. Persistent-market-failure observations
  answer "why does this problem still persist despite existing alternatives?"
  instead of a forced why-now, and the sweep must cover poor/expensive narrow
  incumbent software, manual re-keying workflows and awkward integrations, with
  practitioner/community evidence where feasible. Scoring, threshold,
  hard-filter semantics and lifecycle gates are unchanged; funnel limits are 40
  web lookups / 120 agent steps. Review request:
  `reviews/2026-09-21-method-v1.5.0-review-request.md`.
- Latest run `20260921T091851Z-normal` (USD 0.016822, method 1.5.0): 20
  observations across 12 source classes (5 change-driven / 15 persistent), 18
  rejected in shallow triage with cited reasons, 2 promoted - `vetlab-bridge`
  (47.4) and `clinicdata-liberation` (49.5) - and **both killed on
  `defensible_wedge`**; 0 advances. The source-class budget was met with 2 of 2
  promotions non-regulatory. The funnel retrospective
  (`retrospectives/2026-09-21-issue7-funnel-review.md`) **retains the funnel
  unchanged**: breadth widened the search cheaply but did not raise candidate
  quality on this run, so the third consecutive `defensible_wedge` cluster is
  escalated to a human-led sourcing/framing review rather than a filter change.
  The kill-#15 audit was raised for `wonkybox`
  (`reviews/2026-09-21-false-negative-audit-request-wonkybox.md`).
- Method 1.6.0 (2026-09-21, issue #8) answers the `changes-requested` 1.5.0 review:
  the missing-why-now cap is now **archetype-aware** (change-driven unchanged;
  persistent-market-failure candidates may lift it only with an evidence-backed
  persistence thesis showing BOTH continued pain/workaround despite reachable
  alternatives AND a credible mechanism why the market has not resolved the problem for
  the target segment - unsupported "evergreen pain" narratives do not bypass the cap),
  every normal funnel run performs a cheap **sampled triage false-negative audit** of
  exactly one promising/high-ambiguity rejection, and triage must not treat competitor
  existence as adequate occupation. The funnel and the 15-20 pool are retained; scoring,
  threshold 65, `defensible_wedge`, evidence levels and lifecycle gates are unchanged.
  Regression re-reads (Aucly pre-launch, `shiftswap`, `wonkybox`, `grantscout`) revived
  nothing, and the first sampled audit (O14 broker submission re-keying) upheld its
  triage rejection on demonstrated incumbent occupation. Review request
  `reviews/2026-09-21-method-v1.6.0-review-request.md`, answered **`approved`**
  (`reviews/2026-09-21-method-v1.6.0-chatgpt.md`), no changes requested; the reviewer
  asked that the next run be judged on the monitor list in that response (persistence
  test on real evidence, audit outcome, incumbent-captured promotions, pool padding,
  budget pressure, candidate strength).
- Issue #9 (2026-09-21) spike **painmine v0.1.0**: a bounded, cheap front-end
  that mines public practitioner pain signals, extracts them into an auditable
  schema, deduplicates, clusters, applies a **discovery-priority ranking
  explicitly separate from business scoring**, computes the two-limb
  persistence thesis and renders the strongest clusters into the Method 1.6
  observation format. One live PoC run collected 150 raw items from three
  source classes (Hacker News Algolia, Stack Exchange, GitHub issues; Reddit
  public JSON returned HTTP 403 and was recorded, not bypassed) in 43.84 s of a
  420 s cap and 24/24 requests with **USD 0.00** model spend, producing 139
  signals, 18 duplicates removed, 11 extraction rejects, 6 clusters and 1
  band-A observation; all 139 signals validate against the schema. Part 10
  evaluation (`painmine/SPIKE-REPORT.md`) recommends **ITERATE**: the
  mechanics, budgets, audit trail and retention controls work, but recurrence
  is currently inflated by shared vocabulary (the band-A cluster counted
  commentary as independent pain), so the next step is a job/seam-level
  recurrence gate plus a bounded, owner-approved DeepSeek/OpenCode Go
  extraction pass - not a production crawler. Method 1.6 scoring, thresholds,
  evidence levels, lifecycle gates and the funnel are unchanged; DeepSeek via
  OpenCode Go remains the only permitted inference provider, with no fallback.
  Scheduled GitHub Actions workflows (daily collect + weekly all-family) are
  prepared and locally validated but have not been executed on GitHub.
- GeoNerd is parked at `adversarially-researched` with score 49.5 (down from
  65.3 under the looser 1.0.0 semantics), an independent review requested
  (`reviews/2026-09-21-geonerd-review-request-v2.md`) and a proposed
  demand-validation experiment awaiting human approval. It has **no demand
  evidence**; 49.5 is below the threshold and is not a signal to invest.
- Aucly is recorded as a calibration case, not a candidate for investment:
  pre-launch 49.5 and today 60.0, both below the 65 threshold and parked. Its
  real auctions and small number of paying organisers count as early
  `Commercial evidence`; the recorded 2,333 visitors with zero accounts keep
  distribution at 2. Proposed next step is the cheap unpaid-channel test
  (`experiments/aucly-channel-test/plan.md`), awaiting human approval. Full
  reasoning: `ideas/aucly/decision.md`.
- `scripts/run.sh` has completed smoke, dry and normal runs end-to-end (cost
  well under the USD 1.00 bound; validator passing).
- Scheduling of recurring runs is deliberately out of scope. Every run is
  manual.
