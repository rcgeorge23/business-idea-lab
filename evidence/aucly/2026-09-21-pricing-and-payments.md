# Evidence: Aucly pricing and payment model

- **Idea / scope:** `aucly`
- **Register:** evidence
- **Source:** Aucly application repository, `/home/richard/projects/aucly-micronaut` @ `c6bf305b5` —
  `aucly/src/main/resources/db/changelog/insert-default-price-tiers.yaml`,
  `aucly/src/main/resources/views/pricing.html`,
  `aucly/src/main/java/.../service/PriceTierService.java`,
  `aucly/src/main/java/.../service/HostingEntitlementService.java`,
  `plans/done/FREE_TIER_LAUNCH_ENTITLEMENT_PLAN.md`
- **Accessed / dated:** 2026-09-21 (pricing tiers seeded 2025-08-21; public pricing page added 2025-08-20)
- **Credibility:** primary (the live product's own code and pricing page)

## Claim(s) supported

- Aucly charges a **one-off flat fee per paid auction**, with no commission on winning bids.
- Current tiers are Free (max 15 items, £0), Standard (max 50 items, £60) and Unlimited (no item cap, £120).
- Stripe fees are separate and paid directly by the organiser; offline / bank-transfer payments are supported.
- Free-tier auctions are technically entitled without setting `paymentCompleted`; the dashboard distinguishes "Free tier" from "Paid".
- Approximately 7 paid auctions to date (owner-supplied) is the only figure available for actual payments; no lifetime payment export was found in the workspace.

## Exact detail

Seed changelog `insert-default-price-tiers.yaml` (commit "Seed default pricing tiers", 2025-08-21) inserts
`price_tier` rows: Free `maxItems=15, price=0`; Standard `maxItems=50, price=60`; Unlimited `maxItems=null, price=120`.
`PriceTier` carries `priceTierType = PAY_PER_AUCTION`, `durationMonths`, `highlight`, and `status = CURRENT`.
`pricing.html` presents Free / Standard / Unlimited with Standard highlighted "Most Popular" and states there is
no commission on winning bids, no bidder tips, and that Stripe fees are separate.
`HostingEntitlementService` separates a FREE_TIER entitlement from a completed hosting payment (free-tier launch
does not set `paymentCompleted`).

## Why it is credible

These are the live product's own data and billing code, dated, and directly verifiable in the repository.
The owner's "approximately 7 paid auctions" statement is treated separately below because it is memory, not a ledger.

## What it does NOT show

- It does not show how many people paid, when, or how much revenue was recognised — the payment ledger itself
  was not available in this workspace, so the ~7 figure is unverified.
- It does not show whether any organiser has paid twice or renewed; there is no retention or repeat-purchase evidence.
- It does not show that £60/£120 is acceptable to buyers; the fee might be suppressing paid conversion (free tier exists).
- The flat fee is a pricing *choice*, not evidence of willingness to pay at that level.

## Links

- Used by: `ideas/aucly/scorecard.json#economics`, `ideas/aucly/scorecard.json#buyer_budget_clarity`,
  `ideas/aucly/decision.md`
