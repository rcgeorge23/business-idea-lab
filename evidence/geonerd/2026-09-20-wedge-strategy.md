# Evidence register — GeoNerd wedge strategy

- Idea: `geonerd`
- Register opened: 2026-09-20
- Method version: 1.0.0

## Sources

| ID | Source | Type | Date captured | Location |
|---|---|---|---|---|
| S1 | GeoNerd wedge strategy (issue #7 research deliverable) | internal desk research | 2026-09-20 | `/home/richard/projects/geonerd/docs/wedge-strategy.md` @ `327f02e` |
| S2 | GeoNerd spike findings (issue #1) | internal desk research | 2026-09-20 | `/home/richard/projects/geonerd/docs/spike-findings.md` @ `327f02e` |
| S3 | GeoNerd competitive teardown | internal desk research | 2026-09-20 | `/home/richard/projects/geonerd/docs/competitive-teardown.md` @ `327f02e` |
| S4 | GeoNerd collection cost model | internal desk research | 2026-09-20 | `/home/richard/projects/geonerd/docs/ui-scraping-cost-model.md` @ `327f02e` |
| S5 | GeoNerd demand validation plan (issue #8) | internal experimental design | 2026-09-20 | `/home/richard/projects/geonerd/docs/demand-validation-plan.md` @ `327f02e` |

All GeoNerd documents are desk research produced by the same project that would
build the product. They are **not** independent market evidence and carry no
buyer-action credibility. Vendor pricing and adoption figures cited inside them
are secondary sources with the dates recorded in those documents.

## Claims and what supports them

| Claim | Value | Source | Confidence | Notes |
|---|---|---|---|---|
| UK accountancy practices are a dense market with shared AI buying questions | ~35,921 actively trading firms (Firmbase 2026); 55,377 on register (justregistered, Sep 2026) | S1 §2–3 | medium | Counts are third-party estimates; order of magnitude only |
| Target buyer is identifiable | UK accountancy practices, 1–20 staff, owner/partner decision maker; first niche contractor/IR35 specialists | S1 §1–2 | medium | Buyer hypothesis, not yet observed |
| One accountancy client is worth £hundreds–£thousands/yr in fees | stated in S1 §2 | S1 | low-medium | No primary source in S1; used only to argue £19.99 is a rounding error |
| AI visibility tooling at the low end is crowded and cheap | 50+ tools; Otterly $29/mo, SearchScore from $25/mo; free checkers inside Ahrefs/Semrush/HubSpot | S1 §2, S3 | medium | Vendor pages change; needs re-check before launch |
| Accountancy-specific incumbents exist | TendorAI (ICAEW/ACCA multi-surface scans), Tramwai (£299/mo retainer + free audit), AireStream (GEO programme), SearchScore (1,038 UK accountancy firms audited) | S1 §2, S3 | medium | Contested wedge is the main risk to differentiation |
| Measurement is genuinely noisy | UI vs API brand overlap 6–24% in published studies | S2, S1 §2 | medium | The honest-measurement positioning follows from this |
| Shared-question density lowers collection cost | 30 prompts × 2 surfaces × 3 samples/week ≈ 780 calls/market/month → £60–95/market/month UI-equivalent | S1 §6, S4 | low-medium | Cost model has not been tested against a real provider bill |
| Price hypothesis | £19.99/mo launch; £29.99 multi-partner; £9.99 modelled and rejected | S1 §6 | low | Pure desk hypothesis; demand test pending |
| Minimum viable density | ≥10 customers/market at £19.99/mo | S1 §6 | low-medium | Depends on cost model above |
| Non-paid distribution channels plausibly exist | AccountingWEB, ICAEW/ACCA/AAT communities, directory/SEO landscape | S1 §7 | low-medium | Channel yield untested |
| A decisive external test is cheap and specified | 1-week spike, 5 buyer conversations, £50 / 20 human-hours bound | S5 | high (as a design) | Whether it disconfirms is the point of running it |

## Explicitly unsupported / assumptions register

- No observed buyer behaviour of any kind exists yet — no scan users, no emails,
  no conversations, no payments.
- The value of an accountancy client (§2) has no primary citation; it should not
  be used in any scored dimension beyond directional reasoning.
- Traffic/visit targets (100 visits etc.) are design choices, not evidence.
- Any claim that "accountants will pay £19.99" is an **assumption**, resolvable
  only by the demand-validation experiment.
