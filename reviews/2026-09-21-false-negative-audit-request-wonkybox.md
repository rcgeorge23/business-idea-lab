# False-negative audit request: WonkyBox (kill #15 trigger)

- **Requested by:** worker
- **Date:** 2026-09-21
- **Run:** `20260921T091851Z-normal` (method 1.5.0 funnel run; kill count reached 15)
- **Requested from:** ChatGPT (independent reviewer)
- **Trigger:** review-policy false-negative audit - every 5th killed idea, sampling the oldest un-audited one
- **Target idea:** `wonkybox` (killed 2026-09-20, kill #2; unaudited)
- **Status:** `answered` — kill upheld by ChatGPT / GPT-5.6 Sol on 2026-09-21
  (`reviews/2026-09-21-false-negative-audit-wonkybox-chatgpt.md`); no adjacent
  seed created; calibration lesson recorded in `ideas/wonkybox/decision.md`.

## Why this audit is being raised

`ideas/index.json` now records 15 killed ideas. The audits raised at kills #5
(`shiftswap`) and #10 (`bikpayroll`) have both been answered and approved. The
oldest kill that has never been audited is `wonkybox`, so it is the sample for
the kill-#15 trigger. This request records that obligation; it does not ask for
a second review of `shiftswap` or `bikpayroll`.

## What the reviewer must decide

1. Was the `wonkybox` kill correct on the evidence available at the time
   (Oddbox loss-making at ~£27m revenue with widening losses; paid-acquisition
   dependency; two incumbents in the position)?
2. Is the decision robust to the obvious alternative reading - that Oddbox's
   economics reflect its delivery model rather than the category, leaving room
   for a pickup-only or community-hub model the lab never tested?
3. If the kill is upheld, what new evidence would justify reopening (the
   decision record already names a non-delivery model reaching positive
   contribution per box at small scale)?
4. Does the existing `grantscout-application-quality`-style seed route apply
   here, or is an adjacent `wonkybox` seed warranted?

## Evidence for the reviewer

- `ideas/wonkybox/dossier.md`
- `ideas/wonkybox/decision.md`
- `ideas/wonkybox/scorecard.json` (36.8/100; `non_paid_distribution`,
  `defensible_wedge`, `plausible_margins`, `not_all_optimistic` all `fail`)
- `evidence/wonkybox/2026-09-20-oddbox-financials.md`
- `evidence/wonkybox/2026-09-20-incumbent-box-schemes.md`

## Worker self-audit summary

- Verdict proposed by the worker: **kill upheld**.
- The kill does not rest on novelty or taste: it rests on the category leader's
  reported accounts, which are a natural experiment in the model the idea would
  have to run. No delivery-density argument makes a small entrant's unit
  economics better than the leader's.
- Residual uncertainty recorded honestly: the evidence speaks to delivered
  boxes, not to pickup-only or B2B surplus channels; the kill is correct for the
  idea as scoped, not a claim that no surplus-produce business can work.
- Reopening condition: independently verifiable evidence of a structurally
  different distribution model (pickup/B2B/community hub) reaching positive
  contribution per box at small scale.

## Review outcome

- **Verdict:**
- **Reviewer:**
- **Date:**
- **Reasons / conditions:**
