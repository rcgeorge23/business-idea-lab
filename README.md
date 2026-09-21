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

The worker never commits, pushes, opens issues or PRs, contacts anyone, spends
money, publishes, creates accounts, or makes commitments. It may only propose
experiments. Review the diff when the run finishes and commit it yourself.

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
| `ideas/index.json` | Ledger: every idea, state, score, review and experiment link |
| `ideas/<slug>/` | Dossier, scorecard, decision record |
| `evidence/<slug>/` | Dated evidence registers (claims, sources, caveats) |
| `seeds/` | Adjacent-opportunity seeds from rejections (non-inheriting) |
| `experiments/` | Experiment index, plans, results |
| `reviews/` | Review requests and responses |
| `retrospectives/` | What the loop itself should learn |
| `runs/` | Per-run metadata, usage, validation, summaries, dry-run diffs |
| `templates/` | Templates for every artefact type |
| `scripts/` | Validator, runner, usage extraction, review-request builder |
| `.opencode/agent/` | `idea-worker` (primary) and `idea-critic` (read-only subagent) |

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
critiques (GeoNerd review request v2, method v1.1.0, v1.2.0 and v1.3.0
requests, and the shiftswap false-negative audit) are **still pending**, so the
loop's output must not yet be treated as trusted.

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
