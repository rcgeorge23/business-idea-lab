# Review request: false-negative audit of killed ideas (trigger 6, kill #10)

- **Requested by:** worker
- **Date:** 2026-09-21
- **Run:** `bikpayroll-incumbent-capability` scan (issue #5)
- **Requested from:** ChatGPT reviewer (human-mediated)
- **Trigger:** `method/review-policy.md` trigger 6 — every fifth killed idea. The tenth killed idea is `bikpayroll`.
- **Target idea:** `bikpayroll` (kill #10; oldest un-audited kill)
- **Status:** requested

## Why this audit is triggered

The killed-idea count reached ten when the precommitted
`bikpayroll-incumbent-capability` rule fired KILL on 2026-09-21
(`shiftswap` 1, `wonkybox` 2, `grantscout` 3, `agentready` 4, `packproof` 5,
`vetcma` 6, `prsregister` 7, `propident` 8, `wastetrack` 9, `bikpayroll` 10).
The shiftswap audit raised at kill #5
(`reviews/2026-09-21-false-negative-audit-request.md`) is still unanswered; this
request records the next obligation rather than replacing it.

Note: the review-policy wording says "sample the oldest un-audited one". At kill
#5 the oldest un-audited kill was shiftswap and it was sampled, so bikpayroll
(kill #10) is the natural target for this cycle. If the reviewer prefers to
treat the outstanding shiftswap audit as covering this trigger, that judgement
should be recorded here.

## What the reviewer is asked to decide

1. Was `bikpayroll` correctly killed, or was it a false negative? The kill
   rested on `defensible_wedge = fail` under a rule pre-committed in the
   experiment plan.
2. Was applying that pre-committed rule faithful, or did the scan over-read
   vendor marketing? Specifically: Zhoosh Benefits' page (2026-08-04) and Zest's
   integration claims are vendor-published; only IRIS's managed service and The
   Electric Car Scheme's API/SFTP mechanics are described concretely. Is the
   threshold "≥2 platforms already ingest provider BiK data" met on that
   evidence?
3. Should the segment gap (SME employers with no benefits platform) be recorded
   as a non-inheriting seed, or is it too close to the killed parent?
4. Does the recurring `defensible_wedge` cluster (now seven kills) indicate a
   discovery bias that should change sourcing (see the issue #5 sourcing
   proposal in `retrospectives/2026-09-21-issue5-backlog-and-next-run.md`),
   rather than a filter that should be relaxed?

## Evidence for the reviewer

- `ideas/bikpayroll/decision.md`, `ideas/bikpayroll/scorecard.json`, `ideas/bikpayroll/dossier.md`
- `experiments/bikpayroll-incumbent-capability/plan.md` (pre-committed rule and population)
- `experiments/bikpayroll-incumbent-capability/results.md`
- `evidence/bikpayroll/2026-09-21-incumbent-capability-scan.md`
- `evidence/bikpayroll/2026-09-21-mandatory-bik-payrolling.md`
- `ideas/index.json` (killed list)

## Worker self-audit summary

- Verdict: kill upheld. The rule fired mechanically against dated, public
  evidence and the thresholds were fixed before searching. The strongest
  counter-case (payroll software still requires manual cash-equivalent entry;
  some insurers do not do true monthly reconciliation) describes an execution
  gap already being absorbed by adjacent platforms.
- Residual uncertainty: whether Zhoosh/Zest capability is shipped at scale or
  aspirational marketing. If the reviewer judges the platform evidence too weak,
  the KILL branch would not be met and the correct action is a PARK with the
  seam kept `unknown` — not an advance.
- Dissent preserved: the adversarial pass had already recommended kill on
  inference before the scan; the scan is evidence, not merely agreement.

## Review outcome (to be completed by reviewer)

- Verdict:
- Reviewer:
- Date:
- Reasons:

## Resolution

- **Status:** answered — kill upheld
- **Response:** `reviews/2026-09-21-bikpayroll-chatgpt-gpt-5.6-sol.md`
- **Recorded:** 2026-09-21
- **Note:** Reviewer approved the BiK kill; the precommitted falsification threshold was met and no seed was created for the small-employer segment. Reopening condition recorded in the response file.
