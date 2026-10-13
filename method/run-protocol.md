# Run Protocol

Method version: see `method/VERSION`. This is the exact procedure for one worker run.
The worker is the OpenCode `idea-worker` agent running DeepSeek. A normal run is
invoked manually and non-interactively via `scripts/run.sh`.

## Limits (hard)

| Limit | Value | Enforced by |
|---|---|---|
| Max new candidates per run | 3 | worker instructions; validator reports counts |
| Generation stops when unreviewed ideas reach | 10 (`state == discovered`) | worker instructions; validator warns at 8+ and fails at >10 |
| Max advances to `validation-ready` per run | 1 | worker instructions |
| Max new evidence entries per idea per run | 8 | worker instructions |
| Max web lookups (search + fetch) per run | 40 | worker instructions |
| Max agent steps | 120 | agent `steps` config |
| Max provider retries per run | 2 (3 attempts total) | `scripts/run.sh` |
| Max cost per run | USD 1.00 default (`--max-cost`) | `scripts/run.sh` post-run check + report |
| Default timeout | 3600 s (`--timeout`) | `scripts/run.sh` |

Cost and token usage are recorded per run. If a run finishes but exceeded the cost
bound, the run is marked `over-budget` and treated as failed: its ledger changes must
be reviewed by the human owner before keeping them.

## One run, in order

1. **Orientation.** Read `ideas/index.json`, `seeds/index.json` (list the `unexplored`
   and `exploring` seeds and identify the most relevant or promising ones for a shallow
   re-check), all active experiments (`experiments/index.json`), the review queue, the
   most recent retrospectives, the discovery log of recent runs (source classes already
   searched), the decision records of recently killed ideas, and the newest
   owner-nominated notes under `intake/` as unvalidated discovery leads. Intake notes
   must be verified and deduplicated before they are included in a normal sweep; they
   confer no score, evidence level, source-class-budget exemption or cap lift. Note any
   `changes-requested` reviews: these MUST be answered in this run (see step 9).
2. **Unreviewed check.** Count ideas with `state == discovered`. If >= 10, generate no
   new candidates this run and say so in the run summary.
3. **Run the search-intent discovery funnel (<= 3 candidates, only if step 2 allows).**
   Follow the v1.9.0 funnel in `method/discovery.md`:
   - **3.1 Hypothesis shortlist (v1.9.0).** Build a shortlist of 3-5 materially
     distinct qualified hypotheses - fewer when the evidence is weak, and an honest
     zero is valid; never manufacture filler to reach five. Each hypothesis starts from
     exact seed queries and follows the chain query -> job/task -> existing solutions ->
     neglected sub-niche -> paid self-service hypothesis, recording at minimum: the
     exact seed query/queries and intent cluster; the job/task behind the query; dated
     demand evidence (named sources; reported volumes only where credible, otherwise
     `unknown`); the live SERP landscape where checked (named pages/competitors with
     dates: organic, ads, forums, government, AI answers, marketplaces); the neglected
     sub-niche and why the wedge may be underserved, including negative evidence; the
     paid self-service hypothesis; source class and signal lens; archetype; and the
     triage outcome and reason. Record the shortlist in `observations/<run-id>.md`.
     Consider all four archetypes, but record only evidence-supported hypotheses; zero
     latent observations are valid. Change-driven (conventional evidenced why-now),
     persistent market failure (no forced discontinuity; answer "why does this problem
     still persist despite existing alternatives?" - never invent a discontinuity, and
     note that an evidence-backed persistence thesis, not the bare existence of
     competitors, is what allows scoring without the missing-why-now cap), latent
     opportunity (v1.7.0 - a guarded route for evidenced but unarticulated
     buyer-benefit hypotheses; admissible only with the six required fields in
     `method/discovery.md` archetype C, and never a substitute for a buyer, mechanism,
     distribution route or falsifiable test), and search-led (archetype D, v1.9.0 -
     intent-evidenced evergreen niche; `why_now.strength: not-required`, no contrived
     discontinuity; the search-led exemption removes the missing-why-now cap only and
     relaxes no evidence requirement). Never invent volumes, rankings, CPC, trends or
     difficulty - record `unknown` plus a low-cost next check.
     During this bounded sweep, conduct and log at least one deliberate latent-signal
     search pass per `method/discovery.md`: record the behavior lens (what), source
     class (where), focus/query, date and yield, including no-result or blocked
     searches. The pass can reuse sweep searches; it has no minimum latent-observation
     count or quota, and a missing complaint/search result is not evidence of
     non-consumption or demand.
     Deliberately search poor/expensive narrow incumbent software, manual
     structured-data/re-keying workflows and awkward integrations between established
     systems, and seek practitioner/community evidence where feasible. Aim a meaningful
     share of the search effort at **money-already-moving sources** (v1.8.0): job
     advertisements describing repetitive administrative work, service/agency pricing
     pages, public procurement and tender records, incumbent support forums and release
     notes, trade press reporting spend or staffing, and job descriptions showing a role
     that exists only to bridge two systems. These carry budget evidence that complaint
     forums do not; a run that cannot find money-already-moving evidence for a seam must
     record that as a finding rather than treating complaint-forum observations as
     equivalent. Observations are cheap: no scorecard, dossier or evidence level, and
     no 15-20 observation quota.
   - **3.2 Shallow triage.** Reject hypotheses cheaply where desk evidence already shows
     a standard incumbent feature of products the target buyer can readily adopt, an
     adequate free/authoritative alternative for the target buyer, credible vendors
     demonstrably and adequately occupying the exact proposed seam, no self-service
     purchase intent or reachable organic entry for the named queries with no neglected
     sub-niche evidenced, unattractive one-shot economics, no plausible buyer, a mere
     feature request or a network-effects dependency. Competitor existence is **not**
     wedge failure: named competitors, vendor claims, adjacent features or enterprise
     availability do not by themselves justify a rejection - the evidence must show the
     seam is genuinely well served for the defined buyer, or record why the gap is real.
     Record the negative evidence and reason for every rejection.
   - **3.3 Promotion.** Select at most 3 materially distinct hypotheses for full
     candidate treatment using the strongest combination of credible problem evidence,
     identifiable buyer, plausible payment route, a real gap left by alternatives,
     cheap falsification and fit for a small bootstrapped business; a search-led
     hypothesis additionally needs dated query/SERP evidence and a credible
     self-service path. Zero, one or two promotions are valid; never manufacture
     candidates to fill slots. Name each promotion's originating observation ID,
     archetype, source class and why, and, where a second-order seam exists, the seam.
     For a promoted persistent-market-failure candidate, apply the two-part persistence
     thesis from `method/discovery.md` (continued pain/workaround despite alternatives
     AND a credible persistence mechanism); a weak, absent or speculative thesis leaves
     the missing-why-now cap in place. The thesis is not a scoring bonus and never
     upgrades a hard filter. A promoted latent-opportunity candidate (archetype C) is
     treated the same way for the cap and is scored under the ordinary rules; the
     latent route confers no automatic score or validation status. A promoted
     search-led candidate (archetype D) records `why_now.strength: not-required`, which
     removes the missing-why-now cap only (not a score bonus; it relaxes no evidence
     requirement).
   - **3.4 Triage false-negative audit.** After triage, independently re-check **exactly
     one** triage-rejected hypothesis, favouring a promising/high-ambiguity rejection
     (relatively strong practitioner/problem or query/SERP evidence, rejected because an
     incumbent, free alternative or crowded field appeared to occupy the seam). Apply
     the five confusion tests in `method/discovery.md` (competitor existence vs
     adequate satisfaction; feature vs complete solution; enterprise availability vs
     niche accessibility; vendor claims vs demonstrated capability; one-shot service vs
     recurring product economics). Keep it cheap - roughly the cost of one observation,
     no full candidate research. Record in the pool file and run summary: hypothesis
     selected, why selected, original triage reasoning, additional evidence checked,
     rejection upheld or overturned, and the implication for triage depth. A single
     overturn does not automatically change the method. If triage rejected nothing,
     record that explicitly; there is then no rejection to sample.
   For each promoted candidate: run the discontinuity test where the why-now is
   change-driven ("This was not an attractive business three years ago, but it might be
   now because ___ changed."), apply the duplicate detection rules in
   `method/discovery.md` (slug/title collision; same buyer AND problem AND
   mechanism/keywords; variant of a killed idea that does not address the recorded kill
   reason; overlapping intent cluster for search-led candidates), investigate
   second-order effects and prefer an awkward workflow/integration seam to a generic
   compliance/dashboard product (if the first-order product is chosen, record why the
   second-order options were weaker), and apply the **source-class budget**
   (`method/discovery.md`): at least 2 of the 3 candidate slots must originate
   from non-regulatory source classes (search-led candidates sourced from query/SERP
   evidence qualify as non-regulatory), at most 1 may be primarily regulation-derived,
   and at least one previously underexplored non-regulatory class must actually be
   searched; never manufacture weak candidates to satisfy it. Candidates may come from
   fresh discovery (`fresh`) or from a shallow re-check of an existing seed that is then
   researched from scratch (`seed:<slug>`); a run is never seed-only. Record the source classes
   actually searched (regulatory vs non-regulatory, successful and unsuccessful), the
   shortlist statistics (shortlist size, source mix, archetype split including
   search-led, triage rejections and principal reasons, promotions and why), the
   candidates' provenance, the class each candidate qualifies under and why, the
   originating observation ID, and whether the budget was satisfied, for the run
   summary. Include the latent-signal search pass
   (behavior lenses, source classes, focus/query, date and yield, including no-result).
4. **Novelty / incumbent sanity check.** Before any deep research, run the screening
   checklist in `method/discovery.md` (exact product exists? multiple credible providers?
   wedge already a standard feature? adequate free/authoritative alternative? incumbent
   with hostile unit economics? merely a feature of a category?). Record the result in the
   dossier. This is a screening aid: it does not automatically kill, but it must be
   considered explicitly and a candidate that fails it needs a stated reason to continue.
5. **Hard filters before deep research.** Apply all twelve filters from
   `method/scorecard.md` to each new candidate: `economic_buyer`,
   `painful_frequent_or_budgeted`, `non_paid_distribution`, `defensible_wedge`,
   `no_network_effects_needed`, `plausible_margins`, `acceptable_risk`,
   `cheap_disconfirming_test`, `not_all_optimistic`, `seo_discoverable`,
   `self_serve_purchase`, `solo_operator_fit`. `pass` requires cited evidence; analogy
   and assumption produce `unknown`, not `pass`. Any `fail` => `killed` (preserve
   reason). `unknown` is parked at most but must name `resolve_via`. For each accepted
   candidate create `ideas/<slug>/{dossier.md,decision.md,scorecard.json}` and an entry
   in `ideas/index.json` with `state: discovered`, `why_now` populated, and the
   fingerprint fields.
6. **Desk screen survivors.** Gather dated evidence into `evidence/` (append-only), fill
   the scorecard dimensions that evidence supports (applying the caps in
   `method/scorecard.md`; new cards use schema v2 and include the required
   `seo_assessment` block), and move to
   `desk-screened` only if no filter `fail`.
7. **Adversarial pass.** For promising candidates, write the strongest possible case
   that the idea is wrong or worthless ("what would have to be true for this to fail"),
   then either kill the idea or record why it survives. Move to `adversarially-researched`.
   This pass must be genuinely aimed at killing; the sibling `idea-critic` agent can be
   used for a second adversarial opinion.
8. **Advance at most one idea.** Score the candidate(s) under weights version 1.3.0
   (scorecard schema v2). At most one idea per run may be proposed for
   `validation-ready`, and only if the threshold in `method/scorecard.md` and the
   review trigger in `method/review-policy.md` are satisfied: `weighted_total >= 65`;
   no hard filter `fail`; no active veto; the three gating dimensions
   (`problem_severity_frequency`, `buyer_budget_clarity`, `evidence_strength`) scored
   >= 3; at least 9 of 12 dimensions scored; overall confidence `medium` or `high`; and
   `review.status != not-required`. Legacy schema-v1 scorecards (weights version 1.2.0,
   method <= 1.8.2) remain valid under their historic rules and are never rewritten;
   new scorecards use schema v2 only. When triggered, set `review.status: requested`,
   write `reviews/<date>-<slug>-review-request.md` (generated with
   `scripts/build_review_request.py`), and stop advancing that idea. An idea that does
   not meet the threshold stays parked; it may still carry an experiment (see
   `method/lifecycle.md`).
9. **Answer outstanding reviews.** For every review with status `changes-requested`,
   address each point with new evidence or a documented concession; never overwrite the
   review or silently ignore it. For `approved`, require human-recorded experiment
   results before any state change above `validation-ready`. For `killed`, move the idea
   to `killed` (or record a well-argued disagreement as a new review request; the state
   stays put until the reviewer responds).
10. **Experiment step.** For the idea closest to `validation-ready`, ensure the cheapest
    decisive experiment is proposed in `experiments/<id>/plan.md` per
    `method/experiment-rules.md`. Never start it. Approval is the human owner's.
    Experiments whose cost exceeds 20 human-hours or GBP 100 require a review request
    before approval.
    For ideas whose buyer route is organic search, proposed experiments default to
    low-touch, no-cold-outreach options: a manual SERP audit, Search Console evidence,
    a free utility, an owner-approved public landing page, an opt-in waitlist, organic
    conversion tracking, or a paid self-service purchase test. Each proposal states
    whether it is desk research or behavioural evidence, names a feasible test horizon,
    and stays within the run limits; any public-facing or paid test requires explicit
    owner approval before execution. Interview- or outreach-based experiments are not
    the default and need a recorded rationale for why no desk option can settle the
    question.
11. **Adjacent seeds.** If a rejection surfaced an observation that could support a
    materially different proposition, record it under `seeds/` per `method/discovery.md`.
    A seed never inherits the killed idea's score or evidence level, and is never an idea
    until a later run researches it from scratch.
12. **Run summary.** Write `runs/<run-id>/summary.md`: what advanced, what was killed,
    what failed, what needs human input, limits hit, the hypothesis shortlist statistics
    (shortlist size, source mix, archetype split including search-led, number rejected
    in shallow triage with principal reasons, promotions and why, latent pass result
    including any no-result or blocked searches), the triage false-negative audit
    (selected hypothesis, why, original reasoning, evidence checked, upheld/overturned,
    implication for triage depth), the source classes searched
    (regulatory vs non-regulatory, successful and unsuccessful), the source-budget
    outcome (quota met or not, and why), the why-now quality of generated candidates
    (`strong` | `weak` | `absent` | `not-required`), each candidate's provenance
    (`seed:<slug>` or `fresh`), source class and
    second-order seam (and, for persistent-market-failure candidates, whether the
    persistence thesis is evidenced and which two-part test passed or failed), whether
    discovery is converging on less obvious opportunities or
    repeating one class of rejection, the review queue after the run, and confirmation
    that no manufactured observations or candidates were added. Report latent
    observations found, triaged, promoted and rejected, including zeros, and why; the
    required search pass does not require a latent observation.
    Update
    `ideas/index.json` counters and `experiments/index.json`. Commits, pushes to
    GitHub, and GitHub issue creation or modification are allowed when they are part
    of the task; they are not automatic steps of a standard run. Before committing,
    inspect `git status` and `git diff`, and stage only task-related files.

## Output contract

- All changed files are Markdown or JSON under the paths above. No app code, no database.
- Observation pools live at `observations/<run-id>.md`.
- `ideas/index.json`, every `scorecard.json`, `experiments/index.json` and
  `runs/index.jsonl` must remain valid and pass `scripts/validate_repo.py`. If the
  validator fails after your run, fix the offending files or (if the model cannot)
  leave the working tree as it was where possible and explain the failure in the run
  summary. Never leave the ledger malformed.
- Every score in a scorecard points at evidence; every state change is explained in the
  decision record.
- New scorecards under `ideas/<slug>/scorecard.json` follow schema v2 (method 1.9.0,
  weights version 1.3.0, `archetype` present, required `seo_assessment` block); legacy
  schema-v1 cards are preserved untouched and never rewritten or migrated in place.
- New evidence entries use `evidence/<idea>/<YYYY-MM-DD>-<slug>.md`.
- Run metadata is unchanged (`runs/<run-id>/run.json` plus one `runs/index.jsonl` line).

## Dry run

`scripts/run.sh --dry-run` copies the repository to a scratch directory, runs the worker
there, validates the copy, and discards the copy's ledger. Nothing in the live ledger
changes. The run report (`runs/<run-id>/dry-run.diff` plus `summary.md`) shows what the
worker would have changed. Use it to test prompt/agent changes and to audit before a
real run.

Ad-hoc or representative runs use the same recording rules and may be recorded with
mode `representative` in `runs/index.jsonl` (`scripts/finalize_run.py --mode
representative`); `scripts/validate_repo.py` accepts it.

## Failure handling

- Provider/transport failure with an unchanged working tree: the wrapper retries up to 2
  times, then fails with the provider error.
- Failure after the worker changed files: no automatic retry (avoid compounding partial
  writes). The run is marked failed with the change list and the exact commands to
  inspect or revert (`git status`, `git diff`, `git restore .`). Prior committed state is
  always recoverable.
- Validation failure: run marked `invalid-output`; changes are preserved for diagnosis;
  the human decides whether to fix or revert. The next run must explicitly handle the
  mess (see step 1) rather than ignore it.
- Do not commit or push automatically as a hidden side effect of a wrapper or scheduled
  run. When the task calls for it, commits, pushes and GitHub issue creation or
  modification are allowed. Do not open or modify pull requests.

## Run metadata

Every run writes `runs/<run-id>/run.json`:

```json
{
  "schema_version": 1,
  "run_id": "20260920T210000Z",
  "mode": "normal | dry-run | smoke | representative",
  "status": "success | failed | invalid-output | over-budget",
  "started_at": "ISO-8601",
  "finished_at": "ISO-8601",
  "agent": "idea-worker",
  "model": "opencode-go/deepseek-v4.1-flash",
  "method_version": "1.9.0",
  "input_revision": "git sha or 'none'",
  "output_revision": "git sha or 'none (uncommitted)'",
  "attempts": 1,
  "timeout_seconds": 3600,
  "max_cost_usd": 1.0,
  "cost_usd": 0.0,
  "tokens": {"input": 0, "output": 0, "total": 0},
  "changed_files": [],
  "validation": {"status": "pass", "errors": []},
  "summary_path": "runs/<run-id>/summary.md"
}
```

and appends one line to `runs/index.jsonl`. Token/cost data is parsed from
`opencode run --format json` events; `null` is recorded honestly when the provider does
not report usage.

## Determinism

The command is fixed, the model is pinned, the prompt is a versioned file
(`scripts/prompts/lab-run.md`), temperature is fixed in the agent config, and limits are
constants. Identical inputs will not produce byte-identical outputs (the model is
stochastic); "deterministic" means one command, no interactive choices, and a
reproducible boundary around the model's work.
