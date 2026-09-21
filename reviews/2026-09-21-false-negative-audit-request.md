# Review request: false-negative audit of killed ideas (trigger 6)

- **Requested by:** worker
- **Date:** 2026-09-21
- **Run:** `20260921T065316Z-normal`
- **Requested from:** ChatGPT reviewer (human-mediated)
- **Trigger:** `method/review-policy.md` trigger 6 — every fifth killed idea, auditing the oldest un-audited kill.
- **Target idea:** `shiftswap` (kill #1; oldest un-audited)
- **Status:** requested

## Why this audit is triggered

`packproof` is the fifth killed idea recorded in `ideas/index.json`
(`shiftswap`, `wonkybox`, `grantscout`, `agentready`, `packproof`). Under
`method/review-policy.md` this triggers a false-negative audit of the oldest
un-audited killed idea, which is `shiftswap`. A worker self-audit has been
recorded in `ideas/shiftswap/decision.md`; this request asks the reviewer to
confirm or challenge the kill independently.

## What the reviewer is asked to decide

1. Was `shiftswap` correctly killed, or was it a false negative? The kill rested
   on hard-filter fails for `non_paid_distribution`, `defensible_wedge`,
   `no_network_effects_needed`, `plausible_margins` and `not_all_optimistic`.
2. If `wonkybox` or `grantscout` should be re-examined, should the next audit
   target them (they remain un-audited)?
3. Is the adjacent seed `grantscout-application-quality` the right way to carry
   forward the GrantScout observation, or should that idea be reconsidered?

## Evidence for the reviewer

- `ideas/shiftswap/decision.md`, `ideas/shiftswap/scorecard.json`, `ideas/shiftswap/dossier.md`
- `evidence/shiftswap/2026-09-20-uk-hospitality-labour-market.md`
- `evidence/shiftswap/2026-09-20-incumbent-rota-software.md`
- `ideas/index.json` (killed list), `seeds/grantscout-application-quality.md`

## Worker self-audit summary

- Verdict: kill upheld. The sourced evidence shows the core function (self-service
  shift swaps) is bundled at £0–£49/mo, so the idea fails the defensible-wedge and
  network-effects filters independent of the labour-market pain.
- Residual uncertainty: no direct buyer-side research was done on whether venues
  pay a premium specifically for cover. That is the only credible reopening path.

## Review outcome (to be completed by reviewer)

- Verdict:
- Reviewer:
- Date:
- Reasons:
