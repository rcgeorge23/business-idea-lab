# Evidence: PRSRegister post-kill reassessment

- **Idea / scope:** `prsregister` — PRS Database registration/readiness for letting agents and landlords
- **Register:** evidence + inference (append-only reassessment; original kill preserved)
- **Source:** GOV.UK announcement; legislation.gov.uk draft regulations; Lettable product/pricing page
- **Accessed / dated:** 2026-09-26
- **Credibility:** primary (government) plus vendor claim (Lettable)

## Claim(s) supported

- The English Register Your Rental Property service is announced to start in the West Midlands on 2026-12-15 and roll out regionally; all active landlords are to register by 2027-11-14. Government describes the service as straightforward/simple and the announcement does not state a registration fee. [S1]
- The regulations page checked for this reassessment still presented draft regulations. Its text assigns landlords the registration duty, allows an agent/property manager to provide specified information/documents on the landlord’s behalf, and leaves the fee to the operator’s relevant costs; a confirmed public fee amount was not established. [S2]
- Lettable currently advertises a free readiness assessment, £19/month entry plan, higher £49 and £99/month plans and bespoke agency pricing, with portfolio/bulk capabilities. These are the supplier’s offered prices and feature claims. [S3]
- The self-managing-landlord seed was separately rechecked in `runs/20260925T190044Z-normal`; that consumer workflow did not establish a paid gap and is not treated here as evidence about letting-agent operations. [S4]

## Exact detail

- [S1] GOV.UK, 2026-09-09: https://www.gov.uk/government/news/stronger-protections-and-greater-confidence-for-renters — phased service launch, registration-by date and government description of the service.
- [S2] Draft Private Rented Sector Database Regulations 2026: https://www.legislation.gov.uk/ukdsi/2026/9780348286861 — draft status and provisions checked 2026-09-26. The official launch announcement does not confirm the eventual fee amount.
- [S3] Lettable: https://lettable.co/ — current first-party product and pricing offer. Claims such as council coverage, fines avoided, performance and testimonials are unverified marketing.
- [S4] `runs/20260925T190044Z-normal/summary.md` — fresh, non-inheriting consumer-landlord-seed result; not a letting-agent workflow study.
- Related earlier evidence: `evidence/prsregister/2026-09-21-prs-database-and-incumbents.md` and `evidence/prsregister/2026-09-21-prs-database-rollout-recheck.md`.

## Why it is credible

The timing and public-service description come from GOV.UK; the proposed legal provisions come from the legislation site and are explicitly labelled draft. Lettable’s own page is direct evidence that a product and advertised price exist, not evidence of sales or successful implementation.

## What it does NOT show

- It does not establish a final registration fee, actual implementation/API behaviour, agent-level bulk workflow, or whether landlords/agents will pay an independent supplier.
- It does not show Lettable adoption, customer retention, satisfaction or how many customers use portfolio functions.
- It does not establish that a separate readiness tool has a buyer budget or non-paid distribution route.

## Reassessment (inference)

- **Buyer:** landlords have the legal registration duty; agents may assist with specified submissions and have a marketing-related role. A distinct agent-controlled software budget is unproven.
- **Problem:** the phased deadline creates a real operational trigger, but government describes the core registration service as simple. The earlier assumption that a £65 fee is confirmed should not be carried forward; the current official announcement gives no amount.
- **Alternatives / wedge:** Lettable directly markets the readiness job with low-priced tiers and portfolio/agency offers; existing letting CRMs remain adjacent. The core service is government-run. `defensible_wedge` remains `fail` for generic readiness/pre-check tooling.
- **Distribution / economics:** agent access, willingness to buy outside existing CRM contracts, conversion and support economics remain unknown.
- **Risk / next evidence:** depend on final regulations, operator processes and rollout. Reopening would need evidence of a specific high-volume agent workflow that the final register interface and existing CRM/Lettable products do not cover, along with an evidenced separate budget and reachable channel. Not established here.

## Links

- Used by: `ideas/prsregister/decision.md` (2026-09-26 reassessment)
- Related prior evidence: the files listed above
