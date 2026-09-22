# Opportunity observation pool — 20260922T072821Z-normal (open-banking sweep)

- **Run:** 20260922T072821Z-normal
- **Date:** 2026-09-22
- **Method version:** 1.7.0
- **Pool size (target 15-20):** 16
- **Archetype mix:** change-driven 6 / persistent market failure 9 / latent opportunity 1
- **Source mix:** regulatory 2 / non-regulatory 14
- **Triage:** promoted 0 / rejected 16

An observation is not an idea. Each row records an evidenced problem, workflow,
dissatisfaction, market failure or change without a product proposition. Rows are
not scored, carry no evidence level, and confer no inherited positive evidence on
any candidate later promoted from them.

This pool is the issue #18 open-banking sweep. It stages the five owner-nominated
hypotheses (H1–H5 in `intake/2026-09-22-open-banking-hypotheses.md`) as
observations alongside other current open-banking and adjacent workflow evidence,
and deduplicates against `aucly`, issue #17's school-software pool and the prior
reconciliation rejection O19.

## Source map (searches run, and what they yielded)

| # | Source / search | Result |
|---|---|---|
| S1 | Open Banking Limited case study: Parentkind and BOPP (2022-07-20) | Useful. Documents PTA payment links, QR codes and a reconciliation dashboard; PTAs average 20 payments/month at GBP 7.48. |
| S2 | BOPP pricing and partners pages (bopp.io) | Useful. 5p–50p per transaction; partners include Parentkind (PTAs), MyT (small businesses), Charity Digital (charities). |
| S3 | Parentkind blog on HMRC CT600 filing change (2026-06-03) | Useful. HMRC closed free CT600 filing 31 March 2026; PTAs must use commercial software; penalties may apply even for nil returns. |
| S4 | GoCardless Recurring Pay by Bank (2026-08-25) and UKPI blog (2026-06-02) | Useful. Recurring Pay by Bank live; 100% UK bank coverage claim; sector maximums; 100,000+ businesses. |
| S5 | GoCardless Direct Debit failure data (guides/posts/why-payments-fail) | Useful. ~2.9% average failure rate; insufficient funds >80% of failures; ~30% involuntary churn; retry success >75%. |
| S6 | Fintech Times (2026-04-11) and Open Banking Expo (2026-04-02) on GoCardless "Revolutionising Recurring Revenue" | Useful. 489 UK leaders surveyed; legacy rails cost 3.5% of monthly revenue; 9 in 10 see commercial VRPs as the way forward. |
| S7 | QuickBooks Community threads (2026-02-23, 2026-03-06, 2020-11-18) | Useful. Practitioner pain on bulk deposits, lump sums, over/underpayments and credit memos that cannot be matched to a net deposit. |
| S8 | Ledge automated invoice reconciliation (ledge.co) | Useful. Already sells partial/batched/inconsistently-referenced payment matching with exception resolution. |
| S9 | Sage Intacct partial matching docs; SAP Ariba invoice exception taxonomy | Useful. Partial matching and exception workflows are standard ERP features. |
| S10 | Thirdfort open-banking statement retrieval (help.thirdfort.com, updated 2026-07-14) | Useful. Existing consented-data evidence product for 3/6/12 months of read-only statements. |
| S11 | Open Banking Limited written evidence to the Financial Inclusion Strategy committee (Dec 2025); OBIE written evidence CAF0055 | Useful. Consent-based framework; Nationwide GBP 3m "Open Banking for Good"; debt charities automating affordability assessments. |
| S12 | HM Treasury "Access to Banking Services Review: Call for Evidence" (8 June – 20 July 2026); DWP Pension Credit case reviews (Daily Record 2026-08-24) | Useful. Bank-statement evidence collection is a live, growing administrative burden. |
| S13 | FCA open-banking pages (open-banking-fca; AIS/PIS perimeter) and open-finance roadmap | Useful. 16m+ UK users, payments +53% in 2025; AIS/PIS are regulated activities; SME lending and mortgages are roadmap priorities. |
| S14 | Failed/limited searches | See below. |

## Failed and limited searches

- **H5 (lender/broker evidence packs):** no dedicated search was run this session
  beyond the FCA roadmap link in the issue. Recorded as a limitation; H5 remains
  the least-researched hypothesis.
- **PTA treasurer first-hand accounts:** no independent PTA forum or community
  thread was retrieved; the Parentkind/BOPP case study is a provider-published
  case study, not independent practitioner evidence. Recorded as a limitation.
- **Named SME vertical for H2:** no single vertical was selected or evidenced this
  run; the QuickBooks threads are generic accounting-software users, not a named
  vertical. Recorded as a limitation.
- **Named financial-support scheme for H3:** no single scheme was selected; the
  evidence is framework-level (Open Banking Limited, OBIE, HM Treasury, DWP).
  Recorded as a limitation.

## Observations

| ID | Observation (problem / workflow) | Buyer | Source class | Reg? | Archetype | Evidence (source, date) | Type | Incumbent / free-alternative check | Triage | Triage reason |
|---|---|---|---|---|---|---|---|---|---|---|
| O1 | A PTA treasurer collecting money across several channels at one event must match the proceeds to the event and report to a committee; BOPP's dashboard already lets a PTA "see all the payments it's received … reconcile events, and see who paid how much and for what event". | PTA treasurer (user); PTA committee (payer) | Platform rule/pricing/access changes | No | Persistent | Open Banking Limited Parentkind/BOPP case study (2022-07-20); BOPP pricing and partners pages | Vendor (provider case study) | BOPP, bundled exclusively and at a discount to Parentkind members, already provides payment links, QR codes and a reconciliation dashboard. | Reject | Demonstrated occupation: the exact reconciliation job is described as solved by the incumbent bundled to the buyer's umbrella body; no evidenced residual exception. |
| O2 | PTAs that are Gift Aid-registered and receive an HMRC notice must now file Corporation Tax returns using commercial software because HMRC closed its free CT600 filing service on 31 March 2026; penalties may apply even for nil returns. | PTA treasurer (user); PTA committee (payer) | Legislation/regulation | Yes | Change-driven | Parentkind blog (2026-06-03) | Practitioner (umbrella body) | Commercial CT600 filing software exists; the change is a new cost and complexity, not a missing product category. | Reject | No plausible standalone buyer: the affected population is small, the task is annual and low-value, and commercial filing software already exists. |
| O3 | A PTA or community group collecting cash, auction proceeds and a second fundraising platform alongside BOPP payments may still have a cross-channel close-out step BOPP's dashboard does not cover. | PTA treasurer (user); PTA committee (payer) | Awkward integrations between established systems | No | Latent | Open Banking Limited Parentkind/BOPP case study (2022-07-20); BOPP partners page (MyT, Parentkind, Charity Digital) | Vendor | BOPP covers card/bank payments; cash and auction proceeds are outside it; no evidence was found that a treasurer currently pays for a cross-channel close-out tool. | Reject | Latent observation fails the six-field test on field 1 and field 6: no dated observable evidence of the buyer's current cross-channel behaviour, and no cheap behavioural test without contacting treasurers. Rejected, not parked. |
| O4 | An SME receiving lump-sum deposits from a payment provider covering many orders, or over/underpayments and credit memos that cannot be matched to a single net deposit, must resolve the exceptions by hand. | SME bookkeeper / owner (user and payer) | Manual structured-data flows / re-keying | No | Persistent | QuickBooks Community threads (2026-02-23, 2026-03-06, 2020-11-18) | Practitioner | Ledge already sells partial/batched/inconsistently-referenced payment matching with exception resolution; Sage Intacct and SAP Ariba ship partial matching and exception workflows; Xero/QuickBooks ship bank feeds and rules. | Reject | Demonstrated occupation: the described exception job is already productised by Ledge and shipped as a standard feature by the accounting systems the buyer already owns. |
| O5 | A biller in a niche with variable or seasonal amounts loses money to Direct Debit failures and involuntary churn; UK Direct Debit failure rate averages ~2.9%, insufficient funds is >80% of failures, and ~30% of churn is involuntary. | Biller finance/collections lead (user and payer) | Platform rule/pricing/access changes | No | Change-driven | GoCardless Direct Debit failure data (guides/posts/why-payments-fail); GoCardless Recurring Pay by Bank (2026-08-25) | Vendor | GoCardless already sells recurring Pay by Bank with intelligent routing, balance checks and automatic retries at scale (100,000+ businesses). | Reject | Demonstrated occupation: the incumbent already sells the described capability at scale, and the failure data is the incumbent's own marketing case for its own product. |
| O6 | Commercial variable recurring payments (VRP) went live via the UK Payments Initiative in 2026, with per-sector maximums (financial services GBP 450, insurance GBP 85, energy/utilities GBP 200, telecoms GBP 120) and the first recurring open-banking transaction completed in March 2026. | Biller / merchant (buyer) | Platform rule/pricing/access changes | No | Change-driven | GoCardless blog (2026-06-02); GoCardless Recurring Pay by Bank (2026-08-25) | Vendor | GoCardless, the incumbent, is the primary commercial VRP provider and is already live. | Reject | Demonstrated occupation: the scheme's launch is being commercialised by the incumbent provider, not left open. |
| O7 | A financial-support provider must review applicants' bank statements to assess eligibility or affordability; consented-data products already retrieve 3/6/12 months of read-only statements for verification. | Scheme caseworker (user); scheme (payer) | New APIs/developer surfaces | No | Persistent | Thirdfort (help.thirdfort.com, updated 2026-07-14); Open Banking Limited written evidence (Dec 2025); OBIE written evidence CAF0055 | Vendor + primary | Thirdfort already sells consented statement retrieval; Blackbullion supports student funding; PayPoint/AperiData supports Citizens Advice debt assessments; "Open Banking for Good" paired fintechs with debt charities. | Reject | Demonstrated occupation: multiple existing consented-data products already serve the described evidence-collection job. |
| O8 | DWP has started Pension Credit case reviews asking selected claimants for recent bank statements, and HM Treasury ran an Access to Banking Services Review call for evidence (8 June – 20 July 2026). | DWP / scheme (buyer); claimant (user) | Legislation/regulation | Yes | Change-driven | Daily Record (2026-08-24); HM Treasury call for evidence (2026) | Secondary (journalism) + primary | The buyer is a government department; the evidence-collection process is government-owned. | Reject | No plausible economic buyer for a small entrant: the buyer is a government department and the process is government-owned. |
| O9 | Open banking has >16 million UK active users and payments grew 53% in 2025, but adoption of the infrastructure is not evidence of an underserved buyer. | n/a | Platform rule/pricing/access changes | No | Change-driven | FCA open-banking page (open-banking-fca) | Primary (regulator) | Infrastructure adoption is broad; the question is whether a specific buyer's workflow remains painful. | Reject | Not an observation of buyer pain: infrastructure adoption is context, not an evidenced problem. |
| O10 | A specialist SME lender or mortgage broker may need borrower-specific bank-data evidence that existing consented-data products leave as a manual gap; the FCA open-finance roadmap prioritises SME lending and mortgages. | Lender / broker (buyer) | New APIs/developer surfaces | No | Latent | FCA open-finance roadmap | Primary (regulator) | Not researched this run; the roadmap is a statement of intent, not proof of a gap. | Reject | Latent observation fails the six-field test on fields 1, 2, 5 and 6: no dated observable evidence of the buyer's current behaviour, no concrete mechanism, no named substitute analysis and no cheap test. Rejected, not parked. |
| O11 | Charity and community-group payment collection is served by BOPP via Charity Digital, including GiftAid capture, replacing cash donations. | Charity treasurer (user); charity (payer) | Poor/expensive narrow incumbent software | No | Persistent | BOPP partners page (bopp.io) | Vendor | BOPP/Charity Digital already serve charities; Wonderful also offers charity bank payments. | Reject | Demonstrated occupation: the charity collection job is already served by named providers. |
| O12 | Cross-school payment visibility is a recognised product category: ParentSquare launched centralised reporting for district-wide payment visibility in the US (2026-08-04). | School district / MAT (buyer) | Poor/expensive narrow incumbent software | No | Persistent | ParentSquare announcement (2026-08-04) | Vendor | ParentSquare and comparable platforms already productise cross-school payment reporting. | Reject | Demonstrated occupation: the category is recognised and being productised by an established vendor. |
| O13 | A PTA treasurer's reporting to a committee is an annual/event-level administrative task with a small affected population and low transaction values (average GBP 7.48 per payment). | PTA treasurer (user); PTA committee (payer) | Poor/expensive narrow incumbent software | No | Persistent | Open Banking Limited Parentkind/BOPP case study (2022-07-20) | Vendor | Parentkind bundles a discounted service; the population is small and the values low. | Reject | Unattractive economics: small population, low transaction values and an umbrella body already bundling a discounted service. |
| O14 | Invoice exception handling is a documented, standardised workflow in enterprise procurement (unmatched invoice, PO variance, partial invoicing, receiving, tax, payment terms) with escalation to supervisors. | Enterprise AP team (user); enterprise (payer) | Poor/expensive narrow incumbent software | No | Persistent | SAP Ariba documentation | Vendor | SAP Ariba, Sage Intacct and Ledge already ship exception workflows and partial matching. | Reject | Demonstrated occupation: exception handling is a standard ERP feature, not an unserved seam. |
| O15 | Debt advice charities automate affordability assessments using open banking, funded by Nationwide's GBP 3m "Open Banking for Good" programme pairing fintechs with debt and money charities. | Debt advice charity (user); funder (payer) | New APIs/developer surfaces | No | Persistent | OBIE written evidence CAF0055 | Primary | The programme already paired fintechs with charities; PayPoint/AperiData already serves Citizens Advice. | Reject | Demonstrated occupation: the job is already served by funded, named providers. |
| O16 | Open banking is a consent-based framework; providers design services for people with variable incomes and thin credit files, and for SMEs improved visibility leads to better access to lending. | Variable-income consumer / SME (user) | New APIs/developer surfaces | No | Persistent | Open Banking Limited written evidence (Dec 2025) | Primary | Framework-level statement; no specific buyer workflow or incumbent gap identified. | Reject | Not an observation of a specific buyer's workflow: framework-level evidence with no named buyer, task or incumbent gap. |

### Latent-opportunity observations (archetype C)

| Observation ID | Buyer/user and observed current behaviour or constraint | Newly possible capability and concrete mechanism | Why the buyer might value it despite not requesting it (inference) | Why now, or "no discontinuity known" | Existing substitute / status quo and competitors | Central falsifiable assumption and cheapest behavioural test |
|---|---|---|---|---|---|---|
| O3 | A PTA treasurer collects cash, auction proceeds and a second fundraising platform alongside BOPP card/bank payments and must close out the event for the committee. | A cross-channel close-out tool that consolidates all collection channels into one event report. | The treasurer may value a single report, but no evidence shows they currently pay for one or that BOPP's dashboard leaves a gap. | No discontinuity known; BOPP's dashboard already covers the card/bank channel. | BOPP dashboard (bundled to Parentkind members); manual spreadsheet close-out. | Assumption: a treasurer would pay for cross-channel close-out. Cheapest test: ask treasurers to describe their last close-out — but that requires contacting people, which is not authorised. **Rejected.** |
| O10 | A specialist lender or broker may need borrower-specific bank-data evidence. | A case-specific consented evidence pack. | Inferred only; no observed behaviour. | FCA roadmap prioritises SME lending and mortgages, but that is intent, not a change. | Not researched; existing consented-data products (Thirdfort and others) may already cover it. | Assumption: an existing product leaves a manual gap. Cheapest test: read one lender's published evidence requirements — not yet done. **Rejected.** |

## Promoted observations

| ID | Promoted to candidate | Why it was promoted |
|---|---|---|
| — | — | None. Zero promotions this run. |

## Triage false-negative audit

| Field | Record |
|---|---|
| Observation selected | O1 — PTA cross-channel event reconciliation (the highest-priority owner-nominated hypothesis) |
| Why selected (vs other rejections) | It is the leading hypothesis in the issue, it has the strongest (if provider-published) evidence in the pool, and it was rejected on "demonstrated occupation" — exactly the competitor-existence-vs-adequate-occupation confusion the audit exists to test. |
| Original triage reasoning | "Demonstrated occupation: the exact reconciliation job is described as solved by the incumbent bundled to the buyer's umbrella body; no evidenced residual exception." |
| Additional evidence checked | BOPP pricing and partners pages confirm the offering and its bundling to Parentkind members; the Parentkind blog confirms Parentkind actively bundles services to members; ParentSquare confirms cross-school payment reporting is a recognised category. No independent PTA practitioner account was found. |
| Confusion tests | Existence vs satisfaction: the case study describes the dashboard as solving the reconciliation job, but it is provider-published, so satisfaction is asserted rather than independently evidenced. Feature vs solution: the dashboard is presented as a complete reconciliation view, not a feature. Enterprise vs niche: the service is sold to individual PTAs, not only large groups. Claims vs capability: the claim is a provider case study, not independent verification. One-shot vs recurring: the need recurs per event. |
| Outcome | **Upheld, with a caveat.** The rejection stands because no independent evidence of a residual exception was found and the incumbent is bundled to the buyer's umbrella body. The caveat is that the satisfaction evidence is provider-published; if independent PTA accounts later show a cross-channel gap, this observation should be re-opened. |
| Implication for triage depth | Triage depth was adequate, but the audit exposes a source-quality weakness: the leading hypothesis rests on a provider case study. Future sweeps of this kind should seek independent practitioner evidence before treating occupation as settled. |

## Notes

- **Evidence type meanings:** primary = official documents, first-party data;
  practitioner = forums, communities, support threads, job ads, service pricing;
  vendor = vendor marketing, release notes; secondary = journalism, analyst
  summaries.
- A rejected observation with an adjacent insight becomes a seed under `seeds/`,
  never a candidate.
- **Deduplication:** `aucly` is the closest ledger entry to H1; issue #17's
  school-software pool is the closest recent sweep; O19 in
  observations/20260922T060326Z-normal.md (reconciliation tooling quality gap) is
  the closest prior rejection to H2. No seed or idea covers H3, H4 or H5.
- **Regulatory note:** AIS and PIS are regulated activities; no product in this
  pool has been checked against a specific regulatory perimeter beyond the general
  position. Any survivor would need that check before promotion.
- **Boundaries:** no bank data was accessed, no consent flow was run, no prospect
  was contacted, no pilot was started, no money was spent and no public claim was
  made.
