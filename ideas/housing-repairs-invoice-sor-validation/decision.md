# Decision: housing-repairs-invoice-sor-validation

- **Idea:** housing-repairs-invoice-sor-validation
- **Date:** 2026-09-22
- **Run:** 20260922T090448Z-normal
- **Decision:** advance (to desk-screened)
- **State:** (none) → discovered → desk-screened
- **Actor:** worker

## What changed

Observation O1 of run 20260922T090448Z-normal (money-already-moving sourcing frame, method 1.8.0) was rejected in shallow triage on the ground that the reconciliation step "is currently performed by employed staff rather than bought as software". The sampled triage false-negative audit re-checked it and **overturned** the rejection: "currently done by a person" is not a triage rejection ground under `method/discovery.md`, and the evidence does not show a credible vendor occupying the provider-side invoice-to-SOR validation seam. The observation was promoted and given full candidate treatment.

## Why now? (discovery gate)

- **Archetype:** persistent market failure (with a weak change-driven component)
- **What changed / when:** the cost of extracting structured line items from an unstructured invoice and matching them against a reference rate set has fallen sharply with current document/LLM tooling (2025–2026). Rentari.ai has already productised the mechanism for the US market.
- **Why it materially improves the opportunity:** the check is only economic if reading an invoice costs less than the human time it saves; that threshold has now been crossed.
- **Strength:** `weak`
- **Persistence thesis (archetype B):**
  - **Limb 1 — continued pain/workaround despite reachable alternatives:** `pass`. Providers still employ reconciliation staff (GBP 29,400–38,115) and their own policies mandate the manual check; council audits keep finding the control failing.
  - **Limb 2 — credible persistence mechanism:** `pass (moderate)`. The systems of record are workflow/compliance tools, not invoice validators; the SOR software market is contractor-side; the provider-side check has historically been cheaper to staff than to automate.
  - **Net thesis quality:** `weak` — both limbs supported by cited evidence, but limb 2 is an inference about vendor incentives and the capability shift is general. Strong enough to lift the missing-why-now cap, only just.
- **If weak or absent:** the candidate was generated because the money-already-moving frame surfaced proven spend and a documented control failure. It was kept because the UK provider-side SOR-specific seam is unoccupied and the buyer already pays for the work — but it is parked at desk-screened, not advanced further, because the central assumption (standalone product vs suite feature) is unresolved.

## Hard filters

| Filter | Status | Note |
| ------ | ------ | ---- |
| economic_buyer | pass | Buyer named in primary documents (Winchester CAB3557(H); NLM policy) |
| painful_frequent_or_budgeted | pass | Every invoice, monthly; GBP 29,400–38,115/year on staff; GBP 300,000 overcharge documented |
| non_paid_distribution | unknown | Channels plausible, no prospect produced; framework-bound procurement |
| defensible_wedge | unknown | UK provider-side SOR check unoccupied, but Rentari.ai has the mechanism and a suite vendor could add it |
| no_network_effects_needed | pass | Value to a single provider on its own invoices |
| plausible_margins | unknown | Modelled only; integration may be bespoke per customer |
| acceptable_risk | pass | No veto-level exposure; commercial risk only |
| cheap_disconfirming_test | pass | Desk-only vendor roadmap/release-note scan, GBP 0, pre-fixed stop rule |
| not_all_optimistic | unknown | Viability needs several optimistic assumptions to hold at once |

## Evidence considered

- `evidence/housing-repairs-invoice-sor-validation/2026-09-22-repairs-invoice-sor-evidence.md` — Winchester CAB3557(H) audit findings (2026-07-06); Brighton & Hove GBP 300,000 overcharge; NLM policy (2026-03); bridge-role job ads; Rentari.ai invoice check (competitor); Joblogic/Automio/Estimark contractor-side SOR software; Fixflo/Ingentive/Plentific surrounding workflow; SHAC tribunal analysis (weak secondary); Circle Housing Merton Priory (secondary).

## Scores

- **Weighted total:** 58.9 / 100 (threshold 65) — **below threshold**
- **Scored dimensions:** 9 of 10 (founder_fit null)
- **Gating dimensions:** problem_severity_frequency 4, buyer_budget_clarity 3, evidence_strength 3 — all ≥ 3
- **Overall confidence:** low
- **Link:** `ideas/housing-repairs-invoice-sor-validation/scorecard.json`

## Review

- **Review status:** not-required (no trigger applies: not proposed for validation-ready; no material method change; no high score on contradictory evidence; no material legal/regulatory/privacy/trust/safety/platform risk; the proposed experiment is GBP 0 and 4 hours, below the 20-hour/GBP 100 threshold; not a 5th-kill audit; owner did not ask)

## Reasons if killed

Not killed. Parked at desk-screened below threshold.

## False-negative audit (killed ideas only)

Not applicable — the idea is not killed.
