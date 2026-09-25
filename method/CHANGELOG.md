# Method Changelog

Every material change to the method bumps `method/VERSION` and is listed here with its
review status. Review status values: `not-required` | `requested` | `changes-requested` |
`approved` | `killed`. See `method/review-policy.md` (section "Method changes").

## 1.8.1 - 2026-09-25

**Changed (repository operations):**

- The worker may commit and push repository changes to GitHub, and create or modify
  GitHub issues, when those actions are part of the task. They are not automatic steps
  of a standard or scheduled run; commits must include only task-related changes.
- Pull request creation/modification and external activities such as outreach, spending,
  and public-facing content publication remain outside the worker's authority.
- Updated `AGENTS.md`, `.opencode/agent/idea-worker.md`,
  `scripts/prompts/lab-run.md`, `README.md`, `method/lifecycle.md`,
  `method/discovery.md`, and `method/experiment-rules.md` to match.

**Review:** not-required - this operational permission change does not alter discovery,
scoring, evidence, or lifecycle rules.

## 1.8.0 - 2026-09-22

Motivated by the convergence escalation recorded across six consecutive funnel runs
(schools, open banking, trades, regulatory changes and the general sweep), all of which
produced zero promotions with demonstrated occupation as the dominant rejection reason.
The convergence reviews in `retrospectives/` (issue #6 and issue #7) escalated this to a
sourcing/framing problem rather than a filter problem: complaint forums are where
problems are discussed, not where budgets are spent, so the sweep was systematically
sampling seams that are already monetised.

**Changed (discovery sourcing only):**

- `method/discovery.md` gained the "Bias the sweep toward money already moving
  (v1.8.0)" section: every normal funnel run must aim a meaningful share of its search
  effort at sources where a buyer is already paying, hiring or procuring - job
  advertisements describing repetitive administrative work, service/agency pricing
  pages, public procurement and tender records, incumbent support forums and release
  notes, trade press reporting spend or staffing, and job descriptions for roles that
  exist only to bridge two systems. A run that cannot find money-already-moving
  evidence for a seam must record that as a finding rather than treating complaint-forum
  observations as equivalent.
- The non-regulatory source-class list in `method/discovery.md` now includes the
  money-already-moving classes.
- The Recording section requires the run summary to state which money-already-moving
  sources were searched and what they yielded, including unsuccessful searches.
- `method/run-protocol.md` step 3.1 states the money-already-moving bias.
- `AGENTS.md`, `scripts/prompts/lab-run.md` and `.opencode/agent/idea-worker.md` state
  the bias and its recording requirement.
- `templates/run/summary.md` source-class table gained six money-already-moving rows
  and a "Money-already-moving outcome (v1.8.0)" line.

**Regression:** this is a sourcing bias, not a scoring change. Weights stay 1.2.0,
threshold stays 65, no cap is lifted, no evidence level is redefined, and
`defensible_wedge` is unchanged. Killed fixtures (shiftswap 44.2, wonkybox 36.8,
grantscout 55.8) and parked fixtures (geonerd 49.5, reasonable-steps 54.0, aucly 60.0,
vetlab-en18029-conformance 44.2) are unaffected by construction because no score input
changed. The empirical check is the sourcing-frame run performed under this version.

**Review:** requested - see `reviews/2026-09-22-method-v1.8.0-review-request.md`.

## 1.7.0 - 2026-09-22

Motivated by issue #16 ("Add a guarded discovery path for latent, unarticulated
opportunities"). Method 1.6 is strong at articulated pain (complaints, manual
workarounds, spend, persistent market failures) but some worthwhile products change a
behaviour the buyer currently accepts as normal; the buyer may not discuss a "problem"
because they have not seen the alternative, so a sweep that only looks for articulated
pain can under-source or prematurely reject these hypotheses. This version adds a
**guarded** latent-opportunity route. It is explicitly **not** a relaxation of
validation standards: "customers do not know they need it yet" is never a blanket
defence for an unevidenced idea, and the route lifts no score cap, lowers no threshold,
redefines no evidence level and upgrades no hard filter.

Changed (discovery sourcing only):

- **`method/discovery.md`**: the archetype section is now "Three discovery archetypes"
  and adds **C. Latent opportunity (v1.7.0)** - a guarded route for evidenced but
  unarticulated buyer-benefit hypotheses. An observation is admissible as a latent
  hypothesis only if it names all six required fields, each backed by dated observable
  evidence: (1) the specific buyer/user and their observed current behaviour or
  constraint; (2) the newly possible capability and a concrete mechanism; (3) why the
  buyer might value the difference despite not requesting it (labelled as inference);
  (4) why now, or an honest "no discontinuity known"; (5) the existing substitute /
  status quo and direct or adjacent competitors; (6) the central falsifiable assumption
  and the cheapest behavioural test. The section also states the evidence and gate
  semantics: enough evidence to justify a cheap test need not include a pre-existing
  complaint or search query; demand/commercial validation still requires real
  target-buyer behaviour (payment, pre-order, meaningful commitment, or an approved
  experiment with a pre-declared decision rule) with interviews and model opinions
  insufficient; a latent hypothesis with no buyer, no observable status quo, no
  plausible distribution or no decisive affordable test is still rejected or parked;
  missing evidence stays `unknown` and is never upgraded to a hard-filter `pass`; and
  expensive external validation, outreach, publication and spend still require human
  approval. The observation-record and recording sections now include the latent
  archetype and require a run that exercises the route to report how many latent
  observations were found, triaged, promoted and rejected (zero promotions acceptable).
- **`method/evidence-policy.md`**: new "Latent-opportunity hypotheses (v1.7.0)"
  paragraph under "Plausibility is not evidence" - such a hypothesis may justify a cheap
  test without a pre-existing complaint, is never demand evidence, never produces a
  hard-filter `pass`, does not lift a cap or lower the threshold, and still requires
  real target-buyer behaviour before any demand or commercial claim.
- **`method/scorecard.md`**: new "Latent-opportunity hypotheses (v1.7.0)" note - a
  candidate promoted from a latent observation is scored under exactly the same rules;
  the route changes where observations come from, not how they are scored.
- **`method/lifecycle.md`**: the why-now section now covers latent-opportunity
  candidates - treated like persistent-market-failure candidates for the cap (no
  discontinuity required or invented; lifted only by an evidence-backed persistence
  thesis meeting both limbs), and the latent route is a discovery-sourcing subtype, not
  a new lifecycle state or evidence level.
- **`method/run-protocol.md`**: step 3.1 covers all three archetypes; step 3.3 notes a
  promoted latent candidate is treated the same way for the cap; step 12 and the
  summary requirements record the latent split and the latent-route counts.
- **`AGENTS.md`, `scripts/prompts/lab-run.md`, `.opencode/agent/idea-worker.md`**: state
  the latent route, its six admissibility fields and its non-relaxation.
- **Templates**: `templates/observation/pool.md` gains the latent archetype in the
  header and a six-field latent-observation block; `templates/run/summary.md` gains the
  latent split and latent-route counts; `templates/idea/dossier.md` and
  `templates/idea/decision.md` gain the latent archetype and the six admissibility
  fields.

Regression (issue #16): the change is a discovery-sourcing addition, not a score input,
so no score, evidence level or hard-filter outcome can move because of it. The killed
fixtures (shiftswap 44.2, wonkybox 36.8, grantscout 55.8) and the parked fixtures
(geonerd 49.5, reasonable-steps 54.0, aucly 60.0, vetlab-en18029-conformance 44.2) were
re-read against the new wording and nothing was revived: their failures remain unchanged
hard-filter failures/vetoes, and the latent route cannot rescue a candidate whose wedge
is occupied, whose distribution is paid, or whose margins are hostile. Aucly pre-launch
(the 1.2.0-simulated 49.5 parked at desk-screened) remains internally consistent - a
latent hypothesis is now recordable in place of a discontinuity but the limited
pre-launch evidence still leaves the score below threshold and the state unchanged; the
historical assessment file is not rescored. Named calibration examples were added to
`method/calibration.md` (one plausible latent opportunity that should reach a cheap test
without a prior complaint, and two attractive-but-vacuous "customers do not know they
need it" ideas that should fail/park). The route was exercised in one bounded normal
observation sweep (issue #17's school-software run) and the full ledger was audited for
latent-opportunity false negatives (issue #16), with every reconsidered idea's outcome
recorded.

Review: `requested` - request written to
`reviews/2026-09-22-method-v1.7.0-review-request.md`; awaiting the independent reviewer.
Until the review lands the change is usable but stays marked `requested`, and any idea
whose score depends on the new rules carries that fact in its review request.

## 1.6.0 - 2026-09-21

Motivated by issue #8, implementing the independent review findings on 1.5.0
(`reviews/2026-09-21-method-v1.5.0-chatgpt.md`, verdict `changes-requested`) before any
further normal discovery run. The 15-20 observation funnel is retained; the review found
two defects and one framing risk, and this version corrects them without touching
scoring, threshold 65, hard-filter semantics, `defensible_wedge`, evidence levels or
lifecycle gates.

Changed:

- **`method/discovery.md`, `method/scorecard.md`, `method/lifecycle.md`**: the
  missing/unevidenced why-now cap is now **archetype-aware (v1.6.0)**. Change-driven
  candidates keep the 1.2.0 behaviour unchanged. Persistent-market-failure candidates no
  longer need a fabricated discontinuity: the cap lifts only when an evidence-backed
  **persistence thesis** satisfies BOTH (a) continued buyer pain / cost / workaround
  despite available and reachable alternatives, and (b) a credible present-tense
  mechanism explaining why the market has not adequately resolved the problem for the
  specified segment. A weak, absent or speculative thesis leaves the cap in place; the
  thesis is not a scoring bonus and unsupported "evergreen pain" narratives do not
  bypass it.
- **`method/discovery.md`, `method/run-protocol.md`**: triage must not equate competitor
  existence with adequate occupation. The `defensible_wedge` filter is unchanged and
  still fails where credible incumbents demonstrably occupy the exact proposed seam for
  the defined buyer.
- **`method/discovery.md`, `method/run-protocol.md` (new step 3.4), templates and
  prompts**: every normal funnel run performs a cheap **sampled triage false-negative
  audit** - exactly one triage-rejected observation, favouring promising/high-ambiguity
  rejections (relatively strong practitioner/problem evidence rejected because an
  incumbent or free alternative appeared to occupy the seam), re-checked against five
  confusion tests: competitor existence vs adequate satisfaction; feature vs complete
  solution; enterprise availability vs niche accessibility; vendor claims vs
  demonstrated capability; one-shot service/migration vs recurring product economics.
  The record (observation selected, why, original reasoning, evidence checked,
  rejection upheld or overturned, implication for triage depth) goes in the run summary
  and the pool file. A single overturn does not change the method; repeated overturns
  trigger a later review of triage depth.
- **`templates/run/summary.md`**, **`templates/observation/pool.md`**,
  **`templates/idea/dossier.md`**, **`templates/idea/decision.md`**: record the triage
  audit, the candidate archetype and the persistence-thesis two-part result. The
  observation pool stays 15-20, retained provisionally pending several empirical runs.
- `AGENTS.md`, `scripts/prompts/lab-run.md` and `.opencode/agent/idea-worker.md` state
  the archetype-aware cap, the competitor-existence clarification and the audit.

Regression (issue #8): Aucly pre-launch, `shiftswap`, `wonkybox` and `grantscout` were
re-evaluated; see `retrospectives/2026-09-21-issue8-archetype-cap-regression.md`.
Nothing was revived. Aucly's persistence thesis is recognised without manufacturing a
discontinuity and without inflating its limited pre-launch evidence (49.5, still parked
at `desk-screened`); the three killed fixtures remain killed on unchanged filter
failures - the mechanism never rescues persistent pain where the wedge is occupied,
network effects are required or category margins are hostile. The v1.5 triage rejection
O14 (insurance broker submission re-keying) was re-checked as the first sampled audit;
the rejection was upheld on demonstrated incumbent occupation, not on mere competitor
existence.

Review: **`approved`** - response received 2026-09-21 in
`reviews/2026-09-21-method-v1.6.0-chatgpt.md` (ChatGPT/GPT-5.6 Sol): the two-part
persistence test is tight enough, one sampled audit per run is the right starting
cadence, the competitor-existence clarification does not weaken `defensible_wedge`, the
regressions are sufficient, and the funnel/pool size is retained. No changes requested;
the reviewer's monitor list for the next run is recorded in the response. This version
answers the `changes-requested` 1.5.0 review recorded below; the 1.4.0 review is recorded
as `approved` in its entry below.

## 1.5.0 - 2026-09-21

Motivated by issue #7: the source-class budget worked (the 1.4.0 run produced three
non-regulatory candidates) but candidate quality did not improve, so the next
experiment increases **breadth before depth** rather than weakening filters or
rerunning the same three-candidate process.

Changed (discovery shape only - scorecard weights, threshold 65, hard-filter
semantics, `defensible_wedge`, evidence-level definitions, lifecycle gates and the
candidate/advancement maxima are unchanged):

- **`method/discovery.md`**: new `## Opportunity-observation funnel` section. A run
  sweeps 15-20 materially distinct opportunity observations into
  `observations/<run-id>.md` before promoting at most 3 full candidates. Supports both
  change-driven opportunities (conventional evidenced why-now) and persistent market
  failures (answer "why does this problem still persist despite existing
  alternatives?"; never invent a discontinuity). Biases the sweep toward poor/expensive
  narrow incumbent software, manual structured-data/re-keying workflows and awkward
  integrations between established systems, seeking practitioner/community evidence.
  Defines the observation record, shallow triage with recorded negative evidence, and
  promotion criteria; observations carry no score, dossier or evidence level and
  surviving triage confers no inherited positive evidence. The 1.4.0 source-class budget
  is retained unchanged and applies at promotion.
- **`templates/observation/pool.md`** (new) and **`observations/README.md`** (new): the
  compact pool format and directory rules.
- **`method/run-protocol.md`**: step 3 is now the funnel (3.1 observation sweep, 3.2
  shallow triage, 3.3 promotion); step 12 and the limits table updated (web lookups
  25 -> 40, agent steps 80 -> 120); run metadata example now 1.5.0.
- **`templates/run/summary.md`**: new `## Opportunity observations` section (pool
  statistics, triage outcomes, promotions) and an Observation ID column in the
  candidate provenance table.
- `AGENTS.md`, `scripts/prompts/lab-run.md` and `.opencode/agent/idea-worker.md` state
  the funnel and its recording requirements; the worker agent iteration limit is 120.

Regression: the funnel changes where candidates come from and how much of the space is
inspected first; it is not a score input, so no score, evidence level or hard-filter
outcome can move because of it. Killed fixtures remain rejected for their recorded
reasons; parked ideas remain parked. The empirical check is the post-change run
required by issue #7, whose assessment is recorded in
`retrospectives/2026-09-21-issue7-funnel-review.md`.

Review: **`changes-requested`** - response received 2026-09-21 in
`reviews/2026-09-21-method-v1.5.0-chatgpt.md` (funnel retained; archetype-aware
missing-why-now cap and a sampled triage false-negative audit required; threshold 65,
`defensible_wedge` and evidence standards to stay unchanged). Answered by method 1.6.0,
which implements the requested changes; the response file is never superseded or
rewritten.

## 1.4.0 - 2026-09-21

Motivated by issue #6, implementing the non-regulatory source-budget proposal recorded
at the end of issue #5 and reinforced by the independent v1.3.0 review: the lab keeps
converging on easily searchable regulatory discontinuities, whose obvious first-order
products incumbents bundle away (`defensible_wedge` kill cluster: agentready, packproof,
vetcma, prsregister, propident, wastetrack, bikpayroll).

Changed (discovery constraint only - scoring, weights, threshold 65, hard filters,
evidence levels, lifecycle gates and the candidate/advancement maxima are unchanged):

- **`method/discovery.md`**: new `## Source-class budget` section. At least 2 of the
  maximum 3 candidate slots must originate from non-regulatory source classes; at most
  1 may primarily originate from legislation/regulation; at least one previously
  underexplored non-regulatory class must actually be searched. Lists the non-regulatory
  classes, requires the run summary to record classes searched (regulatory vs
  non-regulatory, successful and unsuccessful), candidate provenance, the class each
  candidate qualifies under and why, and the budget outcome. Forbids manufacturing
  filler: fewer than three candidates, all-kill runs and zero advances remain valid.
- **`method/run-protocol.md`**: step 3 applies the budget and records it; step 12
  requires the budget outcome in the run summary. Run metadata example now 1.4.0.
- **`templates/run/summary.md`**: source-class table marks each class regulatory or
  non-regulatory and adds a budget-outcome line; candidate provenance table adds the
  source class and why the candidate qualifies.
- `AGENTS.md`, `scripts/prompts/lab-run.md` and `.opencode/agent/idea-worker.md` state
  the budget and its recording requirements.

Regression: the budget is a sourcing constraint, not a score input, so no score,
evidence level or hard-filter outcome can move because of it. Killed fixtures remain
rejected for their recorded reasons; parked ideas remain parked. The empirical check is
the post-change run required by issue #6, whose convergence assessment is recorded in
`retrospectives/2026-09-21-issue6-convergence-review.md`.

Review: **`approved`** - independent response received 2026-09-21 in
`reviews/2026-09-21-method-v1.4.0-chatgpt.md` (budget retained as a discovery-only
experiment; no quota gaming found; do not tighten). Method 1.5.0 superseded this version;
the response to the 1.4.0 request arrived afterwards and approved it. The earlier note
here that the request had been superseded "before a response was received" was stale and
is corrected under issue #8; see the `## Resolution` block in
`reviews/2026-09-21-method-v1.4.0-review-request.md`.

## 1.3.0 - 2026-09-21

Motivated by issue #4, following the first normal run under method 1.2.0
(`20260921T075410Z-normal`), where all three candidates had strong dated discontinuities
but died on `defensible_wedge` because the obvious first-order product was already
served by incumbents or free alternatives.

Changed (discovery guidance only - scoring, weights, threshold, hard filters and
evidence semantics unchanged):

- **Second-order effects**: `method/discovery.md` now requires an explicit investigation
  of the operational seam a discontinuity creates (manual handoffs, re-keying,
  reconciliation, evidence collection, exception handling, status chasing, awkward
  imports/exports, mandated data transformations, integration gaps, poor incumbent
  workflow steps, newly automatable review, underserved subsegments) and prefers an
  awkward workflow/integration seam to a generic compliance/dashboard product.
- **Seed-aware discovery**: normal runs must review the seed register at orientation and
  shallowly re-check the most relevant seeds; a seed becomes a candidate only via full
  fresh research (own fingerprint, evidence, filters, scorecard) with no inheritance;
  runs remain explicitly not seed-only.
- **Provenance and convergence recording**: candidates record provenance
  (`seed:<slug>` or `fresh`) and their second-order seam; the run summary must assess
  whether discovery is converging on less obvious opportunities or repeating one class
  of rejection (and flag it for review rather than weakening a filter).
- Run protocol steps 1/3/12, AGENTS.md, the worker agent prompt, the lab-run prompt and
  the run summary template updated to match. Candidate/advance limits (3/1) unchanged.

Regression: weights version stays 1.2.0; no scoring rule, threshold, hard filter or
evidence level changed, so every existing scorecard keeps its scores. Killed fixtures
and parked ideas are unaffected by construction.

Review: `approved` (ChatGPT / GPT-5.6 Sol, 2026-09-21) - see
`reviews/2026-09-21-method-v1.3.0-chatgpt-gpt-5.6-sol.md`. Reviewer found the
second-order and seed-aware refinements appropriate and non-weakening, and noted
the empirical run did not force novelty; follow-up observation: the next
sourcing refinement must ensure meaningful effort reaches non-regulatory
classes (implemented as the issue #6 source budget, see 1.4.0), and the
recurring `defensible_wedge` failures are a sourcing/convergence signal rather
than grounds to weaken the filter.

## 1.2.0 - 2026-09-21

Motivated by issue #3 (Aucly calibration). One narrow, evidence-driven change; all other
candidate refinements were rejected as unnecessary (see `ideas/aucly/decision.md`).

Changed:

- **Why-now cap scoped (weights version 1.2.0)**: the "missing why-now caps
  `differentiation` and `problem_severity_frequency` at 2" rule now applies only while
  the idea's evidence level is `Plausible` or `Promising`. From `Demand evidence`
  upward the cap does not apply, because real payment evidence is stronger than a
  discontinuity claim. Aucly exposed the systematic error: an evergreen niche
  (school/charity fundraising, incumbents predating 2025) with paying customers was
  being penalised twice - once for having no discontinuity and again in the
  differentiation dimension - which would have understated a genuinely evidenced
  business.
- **No other scoring rules changed.** Small-market viability, bootstrapped vs
  venture-scale framing, founder fit, cheap build/testability, direct-competitor
  treatment and payment-vs-validation separation were all reviewed against Aucly and
  found already adequate.

Regression: existing fixtures are unaffected. The killed fixtures (ShiftSwap,
WonkyBox, GrantScout, AgentReady, PackProof) are all at evidence level `Plausible`, so
the scoped cap still applies to them, and their kills rest on `fail` hard filters or
vetoes, not on the cap. GeoNerd and Reasonable Steps are `Promising`: cap still applies.
The only score change is Aucly's own `problem_severity_frequency` 2 -> 3 (60.0 total).

Review: `approved` (ChatGPT / GPT-5.6 Sol, 2026-09-21) - see
`reviews/2026-09-21-method-v1.2.0-chatgpt-gpt-5.6-sol.md`. The scoping was found
justified, with no obvious loophole (escaping the cap requires reaching a
separately defined evidence level) and the regression fixtures still rejected.
Caveat recorded: the Aucly "2,333 visitors -> 0 accounts" figure must not be read
as a clean website conversion cohort; the supported conclusion is only that no
repeatable organic organiser-acquisition channel is demonstrated. The
distribution score is unchanged.

## 1.1.0 - 2026-09-21

Motivated by issue #2 and the first normal run (`runs/20260920T210550Z-normal`), which
showed (a) conventional candidates with no discontinuity behind them and (b) scores and
hard-filter passes resting on assumptions.

Changed:

- **New `method/discovery.md`**: discontinuity-first generation ("why now?" test),
  change-source classes, novelty/incumbent sanity check, duplicate detection, adjacent
  opportunity seeds.
- **`method/scorecard.md`** (weights version 1.1.0): "plausibility is not evidence"
  anchors; explicit caps (analogy-based problem <= 2, inferred budget <= 2,
  plausible-only distribution <= 2, direct incumbent overlap lowers differentiation to
  <= 2, modelled economics <= 2 with `low` confidence); hard filters now carry
  `status` (pass | unknown | fail) plus `note`, `evidence` and `resolve_via`; `pass`
  requires affirmative cited evidence; assumptions/analogies cannot pass; new threshold
  condition 8 (every unknown named in the proposed experiment). Threshold deliberately
  left at 65 despite the tightening.
- **`method/evidence-policy.md`**: "Plausibility is not evidence" section.
- **`method/lifecycle.md`**: transitions aligned to the new filter semantics; experiments
  decoupled from `validation-ready` so parked ideas can still reach a cheap test; "Why
  now?" requirement for new candidates.
- **`method/run-protocol.md`**: steps reordered around discontinuity hunting, novelty
  check, tightened filters, adjacent seeds, source-class recording.
- **`method/review-policy.md`**: method-change review handling; re-request after a
  revision change.
- **Templates**: dossier gains "Why now?" and "Novelty / incumbent sanity check";
  scorecard hard filters gain `evidence`/`resolve_via`; new `templates/seed/entry.md`;
  run summary gains source classes + why-now quality.
- **Ledger**: GeoNerd rescored 65.3 -> 49.5 and moved down to
  `adversarially-researched`; `why_now` backfilled for existing ideas; GrantScout
  adjacent seed recorded.
- **Validator**: new filter semantics enforced, `why_now` required, `seeds/index.json`
  checked, historical run method versions downgraded to a warning.

Review: `approved` (ChatGPT / GPT-5.6 Sol, 2026-09-21) - see
`reviews/2026-09-21-method-v1.1.0-chatgpt-gpt-5.6-sol.md`. Discontinuity-first
discovery, tightened evidence semantics, the retained 65 threshold, mandatory
`resolve_via` on `unknown` and non-inheriting seeds were all found sound, with no
regression fixture weakened. Observations recorded: monitor score coverage,
since the normalised aggregate over unscored dimensions is slightly awkward (do
not change on this review alone), and keep cheap-experiment eligibility separate
from `validation-ready`.

## 1.0.0 - 2026-09-20

Initial method, implemented under issue #1: lifecycle, evidence policy, scorecard,
experiment rules, run protocol, review policy, calibration procedure, templates and the
deterministic runner (`scripts/run.sh`).

Review: `not-required` (bootstrap; superseded by the first normal run and the 1.1.0
change).
