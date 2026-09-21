# Evidence register: BiK incumbent-capability scan

- **Idea:** `bikpayroll`
- **Register:** evidence
- **Scope:** public desk scan of the incumbent/provider capability that the
  `bikpayroll-incumbent-capability` experiment set out to test; supports the
  experiment results and the kill decision
- **Experiment:** `experiments/bikpayroll-incumbent-capability/`
- **Collected:** 2026-09-21
- **Method:** public sources only (vendor sites, help centres, blogs,
  government publications, one broker interview). No accounts, trials, demos,
  contact or spend. Vendor marketing claims are labelled as such and are not
  treated as proof of shipped capability.

## Claims supported

1. Mandatory real-time BiK reporting is confirmed and phased from 6 April 2027
   (Phase 1: company cars and fuel, vans and fuel, employer-provided medical
   benefits; Phase 2 from April 2028; loans and accommodation excluded).
2. Named benefits platforms already ingest provider benefit data and emit
   per-period taxable values for payroll — the exact seam the idea targeted.
3. Several medical insurers already do true monthly reconciliation, with two
   offering downloadable monthly bills in employer zones.
4. Major payroll software still requires manual cash-equivalent entry, so
   payroll-vendor software is behind — but the gap is being absorbed by the
   benefits-platform category rather than left open.
5. Car-benefit calculation is commoditised via public APIs.

## Scan table

| Source (dated) | Row | Capability claim | Frequency | Fee | Evidence quality |
|---|---|---|---|---|---|
| HMRC, "Mandatory reporting of benefits in kind in Real Time Information (RTI) from April 2027", gov.uk publication, 2026-07-23 | Regime | Mandatory RTI reporting of in-scope BiKs; phased from 6 Apr 2027, remaining benefits 2028; loans/accommodation excluded | Per pay period | N/A | Primary, official |
| HMRC, interim guidance and draft legislation, gov.uk, first published 2025-11-26, updated 2026-09-04 | Regime | Draft guidance/legislation to aid preparation; reporting requirements and "getting ready" detail | Per pay period | N/A | Primary, official |
| HMRC technical note, 2025-04-28 | Regime | Mandatory payrolling moved from April 2026 to April 2027 after stakeholder feedback | N/A | N/A | Primary, official |
| Zhoosh Benefits, "Make real-time P11D benefit reporting feel simple", zhooshbenefits.co.uk/p11d-reporting/, 2026-08-04 | Benefits platform | Records benefit changes (join/leave/cover change/premium change) with effective dates; calculates correct taxable value for the payroll period; "Payroll receives an employee-by-employee report that includes taxable values, a benefit breakdown, and a clear record of what has changed"; monthly report; works "without waiting for insurer invoices or rebuilding the numbers in spreadsheets" | Monthly | Not stated | Vendor product page (marketing), but describes the exact mechanism and data flow |
| The Electric Car Scheme, "Salary sacrifice car scheme integrations", electriccarscheme.com/tech-and-integrations (undated, retrieved 2026-09-21) | Benefits platform / provider | "We integrate directly with your payroll via API or SFTP, providing clear monthly inputs with no manual processing required"; monthly payroll inputs generated automatically; works with all major payroll providers and benefits platforms | Monthly | Not stated (embedded in salary-sacrifice scheme) | Vendor product page (marketing), specific integration mechanics claimed |
| Zest, zestbenefits.com (undated, retrieved 2026-09-21; site-level citation) | Benefits platform | "Zest seamlessly connects with your HR and payroll systems"; "connects with the benefits providers and HR and payroll systems you use, updating information automatically"; SFTP and complex transformations | Ongoing / per period | Not stated | Vendor product page (marketing) |
| Zellis, zellis.com (undated, retrieved 2026-09-21; site-level citation) | Payroll/benefits platform | ZellisONE payroll with "continuous recalculation of pensions, salary sacrifice and benefits in kind"; Pensions and P11D modules; Benefex–Zellis MyView integration | Per pay run | Not stated | Vendor product page (marketing) |
| IRIS, "Mandatory payrolling of benefits in kind (BiK) from 2027", iris.co.uk blog, 2026-03-10 | Payroll vendor | "Our managed benefits in kind service handles the end-to-end process on your behalf, from calculating and updating benefit values each pay period to reporting income tax and Class 1A NICs via RTI – it's all processed as part of your regular pay run, with no separate system or manual workarounds required" | Each pay period | Managed service (priced) | Vendor blog (marketing) describing a shipped service |
| IRIS, "Mandatory payrolling of BiK now phased from April 2027", iris.co.uk blog, 2026-06-23 | Payroll vendor | "IRIS will see to it that the products it supplies to customers are legislatively compliant both by April 2027 and by April 2028" | Roadmap commitment | N/A | Vendor roadmap statement |
| Sage, payroll KB (2026-06-23) | Payroll vendor | Manual route: "Calculate the P11D values or cash equivalent manually, then you enter them into Sage 50 Payroll" | Manual | Included | Vendor help documentation — evidence payroll software does not ingest provider data |
| BrightPay, product documentation (undated, retrieved 2026-09-21) | Payroll vendor | Manual entry of car details in Expenses & Benefits; software then calculates the cash equivalent, distributes across remaining pay periods and reports FPS car fields | Manual entry, automatic calculation | Included | Vendor documentation |
| IRIS Cascade, help documentation (undated, retrieved 2026-09-21; site-level citation) | Payroll vendor | Cascade does not calculate cash equivalents of BiKs | N/A | N/A | Vendor help documentation |
| Xero, QuickBooks (retrieved 2026-09-21) | Payroll vendors | No BiK-specific per-period ingestion material found in searches; recorded as "no material found", not as absence of capability | N/A | N/A | Negative finding (search-level) |
| Hooray Health & Protection, "Are You Ready For Monthly Benefits In Kind Reporting?", hoorayinsurance.co.uk/monthly-benefits-in-kind-reporting/, 2026-04-13, quoting broker "Mike" | Medical insurers | "In private medical insurance some providers don't offer true monthly reconciliation... Many just divide the annual premium by twelve... Those providers that are ahead of the game currently and do true monthly reconciliation are Bupa, Vitality and AXA"; "Bupa and Vitality have good online employer zones that allow advisors and clients to view and download monthly bills" | Monthly | No separate fee stated | Secondary (broker interview) — names three insurers; format not specified |
| Lex Autolease, fleet administration services page and driver Tax Calculator (undated, retrieved 2026-09-21; site-level citation) | Fleet/leasing | Fixed-fee fleet administration including vehicle taxation admin; driver portal BIK tax calculator | Ongoing | Fixed monthly fee (services) | Vendor page (marketing) |
| QV Systems knowledge base (undated, retrieved 2026-09-21; site-level citation) | Fleet/leasing | Lex Autolease CSV ratebook mappings (CAP code, CO2, P11D column, rentals) consumed by fleet software | On ratebook update | N/A | Integration documentation — shows CSV exports exist, for fleet quoting rather than payroll BiK |
| Ayvens, myAyvens portal (undated, retrieved 2026-09-21; site-level citation) | Fleet/leasing | 50+ standardised reports in XLS/PDF/CSV covering vehicles, contracted services, operating costs, invoices | Regular | Included | Vendor portal documentation |
| Comcar API, api.comcar.co.uk; DriveSmart API, api.drivesmart.uk/Get_CarBenefit.aspx (retrieved 2026-09-21) | Calculation APIs | Public APIs returning company-car benefit/P11D value, CO2 and employer NIC | On request | API pricing | Public API docs — commoditised calculation |
| KPMG, article on company-car BiK readiness, 2025-04-16 (site-level citation) | Practitioner | "Engage your fleet provider... Establishing that real-time data feed into your payroll system will be crucial"; wheels/vehicle changes and multiple cars per employee are operationally challenging | Per pay period | N/A | Advisory commentary (secondary) |
| payrollexplained.uk, "Payrolling benefits from April 2027: predicting the spec HMRC hasn't published yet", 2026-08-14 | Practitioner | "Data-intake plumbing - fleet and insurer imports, bureau client cut-offs, estimate chase-ups. The tax calculation is honestly the easy bit; getting a medical premium into the system before cut-off is the product problem." | Per pay period | N/A | Independent practitioner analysis — articulates the seam publicly |

## Why it is credible

- The regime facts come from primary government publications with dates.
- The decisive platform capability (Zhoosh) is a live product page describing a
  concrete mechanism: recorded benefit changes with effective dates, per-period
  taxable values, an employee-by-employee report to payroll, and mid-year
  premium handling. The Electric Car Scheme adds a second named platform with
  API/SFTP payroll inputs, and Zest a third claiming provider integrations.
- Negative evidence (Sage manual entry, BrightPay manual entry, IRIS Cascade not
  calculating cash equivalents) is recorded with the same effort and is what
  kept the idea alive until the platform evidence was found.

## What it does NOT show

- Revenue, customer counts or market share for Zhoosh, Zest, Zellis or The
  Electric Car Scheme; marketing copy is not proof of shipped capability at
  scale.
- Whether Zhoosh's product is priced separately, and how it compares with the
  hypothesised bridge on cost.
- Machine-readable formats for insurer monthly bills (only that downloads
  exist).
- Whether payroll-vendor software (as opposed to managed services) will close
  the ingestion gap before April 2027.
- Any evidence of employer willingness to pay for a third-party bridge.

## Links / paths

- Register: `evidence/bikpayroll/2026-09-21-incumbent-capability-scan.md`
- Prior register: `evidence/bikpayroll/2026-09-21-mandatory-bik-payrolling.md`
- Results: `experiments/bikpayroll-incumbent-capability/results.md`
- Plan: `experiments/bikpayroll-incumbent-capability/plan.md`
