# Retrospective: issue #2 delta review (method 1.1.0)

- **Date:** 2026-09-21
- **Scope:** method 1.0.0 -> 1.1.0 changes (discontinuity-first discovery, stricter
  evidence semantics, adjacent seeds, source-class recording) and the first
  post-change discovery run.
- **Run reviewed:** `runs/20260921T065316Z-normal/summary.md` (status success,
  cost USD 0.018569 against the USD 1.00 bound, validation pass, 3 candidates,
  2 kills, 0 advances).

## What the run produced

| Candidate | Why-now strength | Outcome | Reason |
|---|---|---|---|
| `agentready` | strong (ACP 2025-09-29 / UCP 2026) | killed | `defensible_wedge` fail: platforms bundle agent-mediated checkout readiness free |
| `packproof` | strong (PPWR applies 2026-08-12) | killed | `defensible_wedge` fail: multiple credible providers incl. a cheap UK tier |
| `reasonable-steps` | strong (Employment Rights Act 2025 commencement 2026-10-30) | parked at `adversarially-researched` | 54.0 < 65, 8 of 9 filters `unknown`; wedge and budget unproven |

The run recorded source classes searched, including honest gaps (new datasets,
incumbent disruption, poor narrow incumbents, manual structured-data flows not
searched). Kill #5 triggered the every-fifth-kill false-negative audit: a worker
self-audit of `shiftswap` plus `reviews/2026-09-21-false-negative-audit-request.md`
for independent confirmation.

## Assessment

1. **Why-now is now real.** All three candidates carry a dated structural change
   with a cited evidence file, and the competitive-response field did useful work:
   in both kills the discontinuity was genuine and the wedge was nonetheless
   already occupied or bundled. That is exactly the failure mode issue #2 wanted
   surfaced earlier.
2. **Source diversity worked but is incomplete.** Regulatory and platform classes
   dominated. The four unsearched classes are recorded as the largest gap and are
   the recommended focus of the next discovery pass; the run itself says so.
3. **Stricter semantics changed outcomes without killing the pipeline.**
   `reasonable-steps` reached `adversarially-researched` with 8 `unknown` filters and
   a low confidence score. That is the intended shape: an honest, cheaply
   falsifiable candidate with a proposed experiment, not an inflated
   `validation-ready`.
4. **Regression checks hold.** GeoNerd rescored 65.3 -> 49.5 and parked; the three
   calibration kills still fail for substantially the same reasons (44.2 / 36.8 /
   55.8). No goalpost was moved: the 65 threshold was left unchanged.
5. **The method comfortably returns no advance.** Two consecutive runs advanced
   nothing to `validation-ready`; this is treated as a valid outcome, not a
   failure.

## Method observations (proposed, not yet changed)

- `proposed`: consider requiring at least one non-regulatory, non-platform source
  class to be searched per discovery run once the current gap classes are covered,
  to prevent the lab drifting into a compliance-tool generator.
- `proposed`: the novelty/incumbent check is doing most of the killing
  (`defensible_wedge` twice). A future run could sample whether the check is
  rejecting genuinely viable niches or simply rejecting competition as such.
- No template or threshold change is proposed from this run. Method 1.1.0 is itself
  `requested` for reviewer sign-off; tuning should wait for that outcome.

## Calibration status after this run

- Fixtures: complete (GeoNerd seed + rescore; 2 weak kills; 1 control veto).
- False-negative audit: sampled and requested (trigger 6).
- Post-change discovery run: complete and reviewed here.
- Outstanding: independent ChatGPT critiques of GeoNerd v2 and method v1.1.0, then
  a worker response to them.
