# Run summary — 20260922T072821Z-normal

- **Mode:** normal (worker run; LAB_RUN_ID was unset, so the run id is the UTC
  timestamp at the start of the run)
- **Started / finished:** 2026-09-22
- **Agent / model:** idea-worker / opencode-go/deepseek-v4.1-flash
- **Method version:** 1.7.0 (bumped this run under issue #16)
- **Input revision:** 46232ee
- **Output revision:** uncommitted
- **Status:** success (no wrapper run.json/usage.json/validation.json; the
  validator was run manually)

This run addressed three owner requests in sequence: GitHub issue #16 (guarded
latent-opportunity discovery path), issue #17 (school software discovery sweep)
and issue #18 (five open-banking workflow hypotheses). It is a method-change run
plus two discovery sweeps, not a standard single-funnel run.

## 1. Issue #16 — guarded latent-opportunity route (method 1.7.0)

**What changed.** Method 1.7.0 adds a third discovery archetype, **C. Latent
opportunity**, as a guarded route for evidenced but unarticulated buyer-benefit
hypotheses. An admissible latent observation must carry six fields, each backed by
dated observable evidence: (1) the specific buyer/user and observed current
behaviour or constraint; (2) the newly possible capability and a concrete
mechanism changing time, cost, quality, access or outcomes; (3) why the buyer
might value it despite not requesting it (labelled inference); (4) why now, or an
honest "no discontinuity known"; (5) the existing substitute/status quo and
direct or adjacent competitors; (6) the central falsifiable assumption and the
cheapest behavioural test. The route is a discovery-sourcing subtype, not a new
lifecycle state or evidence level.

**Guardrails.** Enough evidence to justify a cheap test need not include a
pre-existing complaint or search query; demand and commercial validation still
require real target-buyer behaviour; a latent hypothesis with no buyer, no
observable status quo, no plausible distribution or no decisive affordable test is
still rejected or parked; missing evidence stays `unknown` and is never upgraded
to a hard-filter `pass`; no cap is lifted, the 65 threshold is unchanged, evidence
levels are unchanged, and expensive external validation still requires human
approval.

**Files changed.** `method/discovery.md` (archetype C, observation record,
recording), `method/evidence-policy.md`, `method/scorecard.md`,
`method/lifecycle.md`, `method/run-protocol.md` (step 3.1/3.3/12),
`method/calibration.md` (named calibration examples L1/V1/V2 and regression
checks), `method/VERSION` (1.6.0 → 1.7.0), `method/CHANGELOG.md` (1.7.0 entry),
`AGENTS.md`, `scripts/prompts/lab-run.md`, `.opencode/agent/idea-worker.md`,
`templates/observation/pool.md`, `templates/run/summary.md`,
`templates/idea/dossier.md`, `templates/idea/decision.md`, plus the 22 ledger
files whose `method_version` was bumped to 1.7.0.

**Calibration examples.** L1 (plausible latent opportunity that should reach a
cheap test without a prior complaint): UK independent veterinary practices
manually re-keying lab results, with DIN EN 18029:2026-04 published April 2026 and
current document/LLM tooling making a narrow conformance bridge newly buildable —
corresponds to the existing `vetlab-en18029-conformance` idea, which stays parked
at desk-screened 44.2 and is not rescored. V1 (vacuous): "busy parents would love
an app that plans their week — they just do not know they need it yet". V2
(vacuous): "small businesses would pay for an AI that tells them which processes
to automate — the demand is latent". Both fail the six-field test and are rejected
at triage.

**Regression.** The latent route is a sourcing addition, not a score input.
Weights stay 1.2.0 and the threshold stays 65. Killed fixtures (shiftswap 44.2,
wonkybox 36.8, grantscout 55.8) remain rejected for their recorded reasons; parked
fixtures (geonerd 49.5, reasonable-steps 54.0, aucly 60.0,
vetlab-en18029-conformance 44.2) remain parked; Aucly pre-launch 49.5 is unchanged
and not rescored.

**Ledger audit for latent false negatives.** Recorded in
`runs/20260922T072821Z-normal/latent-false-negative-audit.md`. All 19 ideas, 12
seeds and the triage rejections in the three prior pools were re-read under the
latent lens. Outcome: keep closed 17, investigate 3 (geonerd, reasonable-steps,
aucly — all already parked with proposed experiments), propose reopening 0. The
latent route revives nothing, promotes no seed and overturns no rejection; every
case fails on grounds the latent lens does not touch (occupied seam, absent buyer
evidence, one-shot economics, network effects, hostile category margins).

**Review.** Method 1.7.0 review requested:
`reviews/2026-09-22-method-v1.7.0-review-request.md` (status requested, awaiting
the independent reviewer). The change is usable but stays marked requested in the
changelog until the review lands.

## 2. Issue #17 — school software discovery sweep

**Pool.** `observations/20260922T072821Z-normal.md` — 18 observations (target
15-20), source mix regulatory 3 / non-regulatory 15, archetype mix change-driven 5
/ persistent 11 / latent 2, triage promoted 0 / rejected 18.

**Source map.** 13 searches recorded (DfE EdTech market assessment 2026-06-25;
Arbor migration guides; DfE attendance sharing and Wonde; CTF 26; CPOMS and
MyConcern; clubs/trips/events products; DfE workload evidence; LA finance manuals
and the DfE Consistent Financial Reporting framework; Find a Tender and WhichMIS?;
Schools Week/Tes/DfE MIS procurement principles; EdTech Impact and supplier sites;
parliamentary oral evidence HC 151). Failed/limited searches recorded: individual
school-level procurement records, school/MAT job descriptions, independent
pupil-facing review corpora, and independent-school bursar forums.

**Triage.** All 18 rejected. Principal reasons: demonstrated occupation by
MIS-native modules or established vendors (O1, O2, O3, O4, O5, O6, O7, O9, O10,
O11, O12, O13, O15, O16, O17); no plausible economic buyer for a small entrant
(O8 — the buyer is the DfE/LA); an evidence barrier rather than a tooling gap
(O14 — pupil-facing learning impact cannot be proven cheaply); and no product seam
(O16 — institutional practice, not a missing tool).

**Pupil-facing hypotheses.** O6 and O14 distinguish engagement from demonstrable
learning benefit: the DfE market assessment and the parliamentary evidence both
note that pupil impact is not established for most tools, and the evidence bar is
the binding constraint. Safety, privacy, accessibility and teacher-oversight risks
are material and would need specialist review. No pupil-facing candidate was
promoted.

**Deduplication.** `aucly` is the only education-adjacent idea in the ledger and
no observation rephrases an Aucly feature. O17 is the prior education-adjacent
rejection O16 from `observations/20260921T100247Z-normal.md`, re-recorded with its
original rejection preserved. No seed mentions school/education/pupil/teacher.

**Triage false-negative audit.** O1 (MIS migration data cleansing and Data Counts
labour) selected as the strongest practitioner/problem evidence and the closest to
a latent hypothesis; **upheld** on demonstrated occupation and one-shot economics,
not on competitor existence alone. Implication: triage depth adequate.

**Outcome.** Zero promotions. The avenue produced mainly crowded, incumbent-owned
or low-budget observations; the strongest latent-adjacent seam (MIS migration
data integrity) is owned end-to-end by the incoming MIS and an established paid
consultancy market. Nothing was promoted to the scored ledger.

## 3. Issue #18 — five open-banking workflow hypotheses

**Intake.** `intake/2026-09-22-open-banking-hypotheses.md` stages H1–H5 as
unvalidated owner-nominated intake with source URLs and dates, buyer/job
hypotheses, provider and regulatory positions, disconfirming incumbent evidence,
overlaps and key unknowns. No score, confidence or evidence level was assigned.

**Pool.** `observations/20260922T072821Z-normal-openbanking.md` — 16 observations,
source mix regulatory 2 / non-regulatory 14, archetype mix change-driven 6 /
persistent 9 / latent 1, triage promoted 0 / rejected 16.

**Triage.** All 16 rejected. Principal reasons: demonstrated occupation by a named
incumbent (O1 BOPP/Parentkind; O4 Ledge/Sage/Xero; O5/O6 GoCardless; O7 Thirdfort/
Blackbullion/PayPoint; O11 BOPP/Charity Digital; O12 ParentSquare; O14 SAP Ariba;
O15 OBIE-funded providers); no plausible economic buyer for a small entrant (O2
small annual task; O8 government-owned); unattractive economics (O13 small
population, low values); not an observation of buyer pain (O9 infrastructure
adoption, O16 framework-level); and latent observations failing the six-field test
(O3, O10).

**Triage false-negative audit.** O1 (PTA cross-channel reconciliation, the leading
owner-nominated hypothesis) selected; **upheld with a caveat** — the rejection
stands because no independent evidence of a residual exception was found and the
incumbent is bundled to the buyer's umbrella body, but the satisfaction evidence
is provider-published, so the audit records a source-quality weakness and a
re-open condition.

**Outcome.** Zero promotions. No niche merits a cheap approved experiment on this
evidence. The only live question is H1, and the cheapest useful next step is desk
research (independent PTA treasurer accounts), not an experiment.

## 4. Source classes searched

| Class | Regulatory? | Searched | Yield |
|---|---|---|---|
| Legislation / regulation | Yes | Yes | O2 (CT600 filing), O8 (DWP reviews), O11 (census) — all rejected |
| Consultations / announced rules | Yes | Yes | HM Treasury Access to Banking review (O8) — rejected |
| Mandated formats / submissions | Yes | Yes | O2, O3, O11, O15 (issue #17) — all rejected |
| New APIs / developer surfaces | No | Yes | O7, O10, O15, O16 (open banking) — all rejected |
| New datasets | No | Yes | None yielded a standalone observation |
| Platform rule / pricing / access changes | No | Yes | O1, O5, O6, O9 (open banking) — all rejected |
| Incumbent disruption (EOL, shutdown, migration) | No | Yes | O9, O10 (issue #17: ScholarPack/Integris discontinuations) — rejected |
| Poor / expensive narrow incumbent software | No | Yes | O4, O5, O11, O12, O13, O14, O16, O17 (issue #17) — all rejected |
| New technical capability (AI on repetitive service work) | No | Yes | O6, O14 (issue #17) — rejected |
| Manual structured-data flows / re-keying | No | Yes | O4, O7 (issue #17) — rejected |
| Awkward integrations between established systems | No | Yes | O3, O18 (issue #17) — rejected |
| Underserved subsegments of an existing category | No | Yes | None yielded a standalone observation |

**Source-budget outcome.** Not applicable in the usual sense: zero candidates were
promoted across both sweeps, so no candidate consumed a regulatory or
non-regulatory slot. The mandatory coverage of the three biased classes
(poor/expensive narrow incumbent software, manual structured-data/re-keying,
awkward integrations) was met in both sweeps, and the previously underexplored
"new datasets" class was searched (yielded nothing).

## 5. Why-now quality

No candidate rows: zero promotions across both sweeps. The change-driven
observations all had dated triggers (CT600 filing 2026-03-31; commercial VRP live
2026; UKPI scheme 2026-06; ScholarPack discontinued 2026-02-12; Integris migration
by 2026-02; CTF 26 from 2026-09; DfE MIS framework from 2027), and each was
rejected on occupation, absent buyer or unattractive economics — not on why-now
quality.

## 6. Candidate provenance

None. Zero candidates promoted, so no provenance, source class, originating
observation ID or second-order seam to record.

## 7. What advanced

Nothing. Zero advances to validation-ready (0 of 1 used).

## 8. What was killed

Nothing. Ledger counts unchanged: 19 ideas total, 0 unreviewed, 15 killed.

## 9. What failed or was skipped

- Zero promotions in both sweeps; no validation-ready advance.
- H5 (lender/broker evidence packs) was not researched beyond the FCA roadmap
  link; recorded as a limitation.
- No independent PTA practitioner evidence was found; the leading hypothesis rests
  on a provider case study.
- No named SME vertical (H2) or financial-support scheme (H3) was selected.
- No external tests, interviews or pilots were started.

## 10. Convergence assessment

This is the fifth consecutive run whose candidate-level output is an all-rejection
cluster, and the fourth consecutive funnel run rejecting essentially every
observation on demonstrated occupation. Changing the source class (school
software, open banking) changed **what** the observations were about, not **how**
they died. The pattern is consistent with the issue #6/#7 escalation to a
human-led sourcing/framing review: public-source desk research at this scale keeps
surfacing known, already-monetised markets. No filter was weakened and no
threshold changed.

## 11. Limits encountered

| Limit | Used |
|---|---|
| Candidates generated | 0 / 3 |
| Unreviewed after run | 0 / 10 |
| Advances to validation-ready | 0 / 1 |
| Web lookups | ~36 / 40 |
| Evidence entries | 0 |
| Cost | USD 0.00 (no model calls; desk research only) |
| Timeout | within 3600 s |

## 12. Decisions needing human input

| Decision | Options | Where recorded |
|---|---|---|
| Method 1.7.0 latent route | Route to the independent reviewer; approve, request changes or kill | `reviews/2026-09-22-method-v1.7.0-review-request.md` |
| Convergence escalation | Commission the human-led sourcing/framing review, or continue sweeps as-is | `retrospectives/2026-09-21-issue6-convergence-review.md`, `retrospectives/2026-09-21-issue7-funnel-review.md` |
| H1 residual question | Spend desk effort on independent PTA treasurer accounts, or drop H1 | `runs/20260922T072821Z-normal/issue-18-response.md` |
| Four standing experiments | Approve, amend or decline before any external contact | `experiments/index.json` |

## 13. Review queue after this run

| Idea | Review status | Request | Outstanding since |
|---|---|---|---|
| Method 1.7.0 | requested | `reviews/2026-09-22-method-v1.7.0-review-request.md` | 2026-09-22 |
| All 19 ideas | not-required / approved | — | — |

No changes-requested review existed at orientation and none was created.

## 14. Next run should

1. Not run another unchanged same-shaped funnel sweep; act on the human
   convergence decision first.
2. If sweeps continue, hunt for seams where a buyer already pays for a bad
   workaround, and for structural wedges in classes not yet swept.
3. Respond to the method 1.7.0 review when it lands.

## 15. Confirmation

No disallowed actions were taken: no commits, pushes, issues, pull requests or
other publication; no contact with any person; no money spent; no accounts
created; no commitments made; no experiment started; `method/` was edited only
because issue #16 explicitly requested a method change (recorded as a reviewable,
uncommitted change set with an independent review request); no review outcome was
overwritten or ignored; the GitHub issues were not commented on, labelled or
closed.
