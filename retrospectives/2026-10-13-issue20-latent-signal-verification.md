# Issue #20 verification: latent-signal pass operationalisation

- **Issue:** rcgeorge23/business-idea-lab#20, "Operationalize latent-opportunity
  discovery around shadow work and non-consumption" (opened 2026-09-25)
- **Verification date:** 2026-10-13
- **Method under test:** 1.8.2 (implemented in commit `344b01e`,
  "feat: operationalize latent-signal discovery", 2026-09-25)
- **Verified at:** `d1cbe57` (worker workspace HEAD; clean tree)
- **Verifier:** idea-worker (self-verification against the issue's acceptance criteria;
  independence is supplied only by the outstanding review, see "Remaining item")

This document checks the delivered method change against the issue's acceptance
criteria using committed artefacts. It does not change any score, evidence level or
lifecycle state, and it does not approve the method change.

## Acceptance criteria mapping

| # | Criterion | Status | Evidence |
|---|---|---|---|
| 1 | A normal run records at least one deliberate latent-signal search pass, including no-result | Met | All eight normal runs since 1.8.2 recorded a pass in both the pool file and the run summary; see the exercise log below. Three recorded blocked (CAPTCHA/HTTP 429) or no-result searches; none was reinterpreted as evidence. |
| 2 | Latent observations record the six fields with dated evidence and labels | Met (vacuous in practice) | `method/discovery.md` (bounded latent-signal search pass) and `templates/observation/pool.md` (latent six-field block) require the six fields and dated sources. No post-1.8.2 pass produced an admissible latent observation: every pool records 0 latent hits, so the field requirement has not yet bound a real case. The pre-1.8.2 calibration example O16 (CLCH payer-side invoices) remains rejected and shows the boundary in `observations/20260925T115959Z-normal.md`. |
| 3 | Novelty/inferred benefit alone cannot score, pass a filter, claim demand or promote | Met | No latent observation was promoted in any post-1.8.2 run; the only promotion in this window was O1 of `observations/20260922T090448Z-normal.md`, which predates the rule and was promoted on documented occupation of the exact seam by no vendor plus audited spend evidence, not novelty. The method text and templates state the prohibition. |
| 4 | Limits intact, no filler | Met | No signal, latent-observation or candidate quota was added; pools after 1.8.2 held 15–18 observations (no manufacturing); candidate maximum stays three and validation-ready maximum stays one; the source-class budget, lookup/step/cost/time limits and no-filler rule are unchanged. Payroll/step/lookup budgets were reported per run. |
| 5 | Calibration examples retain outcomes | Met | `method/calibration.md` 1.8.2 regression section keeps L1 admissible but unscored and parked at 44.2, and V1/V2 rejected; O16 remains a rejected hypothesis with its boundary recorded. The status table records the change as `requested`. |
| 6 | Method/prompt/templates/validator consistent, and the method change receives the required human review | Partially met - reviewer response outstanding | `method/discovery.md`, `method/run-protocol.md`, `templates/observation/pool.md`, `templates/run/summary.md`, `templates/idea/dossier.md`, `templates/idea/decision.md`, `AGENTS.md`, `.opencode/agent/idea-worker.md`, `scripts/prompts/lab-run.md`, `observations/README.md` and `method/CHANGELOG.md` all carry the 1.8.2 rule; validator passes (`validation: pass` in every post-1.8.2 run record). The independent review requested in `reviews/2026-09-25-method-v1.8.2-review-request.md` is still `requested`; only a human/reviewer can supply it, so this criterion cannot be closed by the worker. |

## Latent-signal pass exercise log (all normal runs since 1.8.2)

All eight runs recorded a completed pass in both `observations/<run-id>.md` and
`runs/<run-id>/summary.md`. Yield is stated exactly as the run recorded it.

| Run | Pool file | Pass recorded | Yield |
|---|---|---|---|
| 20260925T150347Z-normal | `observations/20260925T150347Z-normal.md` | yes | No admissible latent observation; job ads document work, not an unarticulated buyer benefit |
| 20260925T163230Z-normal | `observations/20260925T163230Z-normal.md` | yes | No usable latent observation; practitioner queries CAPTCHA-blocked |
| 20260925T190044Z-normal | `observations/20260925T190044Z-normal.md` | yes | Completed; no usable firsthand result |
| 20260925T210741Z-normal | `observations/20260925T210741Z-normal.md` | yes | No latent observation met the six-field test; no firsthand behavior evidence |
| 20260926T180413Z-normal | `observations/20260926T180413Z-normal.md` | yes | All three searches blocked (CAPTCHA) or irrelevant; no latent observation recorded |
| 20260927T051926Z-normal | `observations/20260927T051926Z-normal.md` | yes | Paid staffing for repeated work found; no dissatisfaction or unmet need; no latent opportunity |
| 20260927T064618Z-normal | `observations/20260927T064618Z-normal.md` | yes | Vendor/consultant content only; no directly accessible practitioner thread; none admitted |
| 20260927T101528Z-normal | `observations/20260927T101528Z-normal.md` | yes | Reddit query HTTP 429 blocked; no usable firsthand report; none promoted |

Since 1.8.2 every pass has returned no admissible latent observation. That is a valid
outcome under the method (there is no quota) but it also means the pass has not yet
demonstrated a positive latent case; the calibration examples (L1, V1/V2) remain the
only latent boundary tests, and O16 remains the retrospective example.

## Remaining item

The issue's final acceptance clause - "method change receives required human review" -
is outside the worker's authority. The request
`reviews/2026-09-25-method-v1.8.2-review-request.md` states `Status: requested`;
no response file exists, and no `changes-requested` outcome is outstanding, so the
worker has nothing to answer. This matches the earlier precedent where issue #16 was
closed with the method review still requested; the open request remains visible in
`method/calibration.md` and `reviews/`.

The worker therefore recommends closing issue #20 with this verification recorded and
leaving the independent review as the tracked follow-up. If the reviewer returns
`changes-requested`, the normal review-response rule applies and this verification
will be revisited.

## Files checked

- `method/discovery.md` (bounded latent-signal search pass, archetype C six fields)
- `method/run-protocol.md` (step 3.1 latent pass, limits)
- `method/calibration.md` (L1/V1/V2 and O16 boundaries, status table)
- `templates/observation/pool.md`, `templates/run/summary.md`,
  `templates/idea/dossier.md`, `templates/idea/decision.md`
- `AGENTS.md`, `.opencode/agent/idea-worker.md`, `scripts/prompts/lab-run.md`
- `observations/README.md` and the eight pool files listed above
- `runs/index.jsonl` and each run's `validation.json` status (`pass`)
