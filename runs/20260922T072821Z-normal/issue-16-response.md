# Issue #16 response — guarded discovery path for latent, unarticulated opportunities

- **Issue:** rcgeorge23/business-idea-lab#16, "Add a guarded discovery path for
  latent, unarticulated opportunities"
- **Run:** 20260922T072821Z-normal (method 1.7.0)
- **Written:** 2026-09-22
- **Boundary note:** I cannot comment on, label or close the GitHub issue. This is
  the local response of record; the owner decides what to post.

## What was done

Method 1.7.0 adds a third discovery archetype, **C. Latent opportunity**, as a
guarded route inside the existing funnel. It is a discovery-sourcing subtype, not
a new lifecycle state or evidence level, and it changes nothing about scoring,
the 65 threshold, hard-filter semantics, evidence levels or lifecycle gates.

An admissible latent observation must carry six fields, each backed by dated
observable evidence:

1. the specific buyer/user and observed current behaviour or constraint;
2. the newly possible capability and a concrete mechanism changing time, cost,
   quality, access or outcomes;
3. why the buyer might value it despite not requesting it (labelled inference,
   reasoning shown);
4. why now, or an honest "no discontinuity known";
5. the existing substitute/status quo and direct or adjacent competitors;
6. the central falsifiable assumption and the cheapest behavioural test.

## Acceptance criteria mapping

| Criterion | Status | Where |
|---|---|---|
| Explicit path exists for evidenced but unarticulated buyer-benefit hypotheses within the existing funnel | Met | `method/discovery.md` archetype C; `method/run-protocol.md` step 3.1/3.3/12 |
| Observation records distinguish observed behaviour, inference about value, and untested demand | Met | `templates/observation/pool.md` latent section (six-field table); `method/evidence-policy.md` latent paragraph |
| Normal candidate limits, source-class budget and lifecycle gates remain intact | Met | No limit, budget, threshold or gate changed; `method/scorecard.md` latent note |
| Cheap behavioural tests have predeclared pass/fail thresholds and none are run without approval | Met | Six-field requirement (field 6); `method/experiment-rules.md` unchanged; no test run |
| "Customers do not know they need it" is not accepted as a substitute for a buyer, mechanism, distribution route or falsifiable test | Met | `method/discovery.md` archetype C; `method/evidence-policy.md`; `method/scorecard.md`; AGENTS.md; lab-run prompt; worker agent prompt |
| Calibration and existing-fixture regression results are documented including false-positive checks | Met | `method/calibration.md` named examples L1/V1/V2 and regression checks under 1.7.0; `method/CHANGELOG.md` 1.7.0 regression paragraph |
| All existing documented ideas including killed and parked ideas, seeds and earlier triage rejections are audited for latent-opportunity false negatives with a dated reasoned outcome per potentially affected case | Met | `runs/20260922T072821Z-normal/latent-false-negative-audit.md` (19 ideas, 12 seeds, prior triage rejections; keep closed 17, investigate 3, propose reopening 0) |
| Any proposed reopening preserves the original decision/evidence, documents new evidence and follows ordinary review and lifecycle gates with no idea progressed merely because the new lens makes it sound plausible | Met | Audit preserves every original decision and citation; no reopening proposed; no score or state changed |
| Method docs, worker instructions and templates agree and independent review is recorded | Partly met | Docs, instructions and templates agree; the independent review is **requested** (`reviews/2026-09-22-method-v1.7.0-review-request.md`) and not yet recorded — the change stays marked requested until the reviewer responds |

## Calibration examples

- **L1 (plausible latent opportunity that should reach a cheap test without a
  prior complaint):** UK independent veterinary practices manually re-keying lab
  results; DIN EN 18029:2026-04 published April 2026 plus current document/LLM
  tooling makes a narrow conformance bridge newly buildable. All six fields
  present. Corresponds to the existing `vetlab-en18029-conformance` idea, which
  stays parked at desk-screened 44.2 and is not rescored.
- **V1 (vacuous):** "busy parents would love an app that plans their week — they
  just do not know they need it yet." No specific buyer, no mechanism, no status
  quo analysis, no falsifiable assumption, no cheap test. Rejected at triage.
- **V2 (vacuous):** "small businesses would pay for an AI that tells them which
  processes to automate — the demand is latent." Generic buyer, no observed
  behaviour, unspecified mechanism, assertion requiring the demand evidence it
  avoids. Rejected at triage.

## Regression

The latent route is a sourcing addition, not a score input. Weights stay 1.2.0
and the threshold stays 65. Killed fixtures (shiftswap 44.2, wonkybox 36.8,
grantscout 55.8) remain rejected for their recorded reasons; parked fixtures
(geonerd 49.5, reasonable-steps 54.0, aucly 60.0, vetlab-en18029-conformance
44.2) remain parked; Aucly pre-launch 49.5 is unchanged and not rescored.

## Bounded sweep exercise

The route was exercised in the issue #17 school-software sweep
(`observations/20260922T072821Z-normal.md`): 2 latent observations found (O18 MIS
migration reconciliation; and the latent framing of the migration seam), 2
triaged, 0 promoted, 2 rejected — both failing the six-field test on the
availability of a cheap behavioural test. Zero promotions is acceptable and no
filler was manufactured.

## Boundaries

No commits, pushes, issues, pull requests or publication; no contact, spend,
accounts or commitments; no experiment started; no review outcome overwritten.
`method/` was edited because this issue explicitly requested a method change, and
the change is left uncommitted with an independent review request.
