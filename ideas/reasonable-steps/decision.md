# Decision record: "All reasonable steps" harassment-prevention evidence for UK SMEs

- **Idea:** `reasonable-steps`
- **Date:** 2026-09-21
- **Run:** `20260921T065316Z-normal`
- **Decision:** hold
- **State:** `discovered` -> `adversarially-researched`
- **Actor:** worker

## What changed

Generated from the Employment Rights Act 2025 (c.36) harassment reforms: from 30 October 2026 the preventive duty becomes "all reasonable steps" and a new third-party harassment duty applies, with liability unless all reasonable steps were taken. The statute contemplates recordable steps (risk assessments, incident monitoring, policy, training, complaint handling) — the basis for an evidence-of-compliance product. This is the only candidate this run not killed by a hard filter.

## Why now? discovery gate

- **Changed:** the standard becomes "all reasonable steps" and third-party harassment becomes actionable against employers from 30 October 2026.
- **Changed date:** 2026-10-30
- **Evidence:** `evidence/reasonable-steps/2026-09-21-harassment-duty-and-incumbents.md`
- **Strength:** strong for the legal change.
- **Competitors responded:** partially — free Acas/EHRC guidance and paid generic training exist; no dedicated low-cost SME evidence tool was surfaced. The novelty check did not fail, but the "adequate free/authoritative alternative" line is the central threat and is carried into the experiment.

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | unknown | SME owner/office manager identifiable; budget inferred only. |
| painful_frequent_or_budgeted | unknown | Duty evidenced; felt urgency/dedicated budget not. |
| non_paid_distribution | unknown | Referral/outreach routes plausible only. |
| defensible_wedge | unknown | No dedicated tool surfaced, but free official content and HR platforms are close substitutes. |
| no_network_effects_needed | unknown | Likely per-customer; not explicitly tested. |
| plausible_margins | unknown | No cost/conversion evidence; free content constrains price. |
| acceptable_risk | unknown | Sensitive data and advice-boundary risk; needs scoping. |
| cheap_disconfirming_test | pass | Proposed 10-interview commitment test is cheap and has a pre-fixed decision rule and kill condition. |
| not_all_optimistic | unknown | Requires owners to pay for something adjacent to free guidance. |

## Evidence considered

- `evidence/reasonable-steps/2026-09-21-harassment-duty-and-incumbents.md` (primary legislation and official Acas/gov.uk material; no demand-side evidence).

## Scores

Weighted total **54.0** against threshold **65** (meets threshold: false). Details in `ideas/reasonable-steps/scorecard.json`. Gating dimensions: problem 3/5, buyer 2/5, evidence strength 3/5. Below the bar for `validation-ready`, so the idea is parked at `adversarially-researched` and carries a proposed experiment instead.

## Review

No review triggered for this idea: it is not being advanced to `validation-ready` and the proposed experiment is £20 / 10 hours (below the >£100 / >20h thresholds in `method/experiment-rules.md`). However, review policy trigger 4 (material legal/regulatory/trust risk) should be assessed by the human owner before any external testing, because the product touches harassment records and legal-adjacent advice. Review status `not-required`.

## Reasons if parked (not advanced)

The dated duty and the explicit "evidence of steps" requirement are genuine, but the decisive uncertainty is commercial: free authoritative templates and existing HR software may already cover the job, and SME willingness to pay is inferred, not evidenced. Advancing to `validation-ready` would require buyer-budget evidence that does not yet exist. The cheapest way to get that evidence is the proposed experiment.

## Adjacent notes

No adjacent seed was created from this candidate (it was not rejected). The audit of earlier kills is recorded separately.
