# Owner-nominated intake: independent trades and small trade firms (issue #19)

- **Recorded:** 2026-09-22
- **Source:** GitHub issue #19, "Explore narrow software opportunities for independent trades and small trade firms" (opened 2026-09-22T08:12:09Z by the owner)
- **Status:** unvalidated discovery input. This is **not** a Method 1.6 observation pool, not a batch of scored ideas, and confers no score, evidence level, hard-filter result or exemption from the source-class budget. A mandate or an official workflow is evidence of a required task, not of willingness to pay.
- **Scope:** discovery only. No product implementation, no outreach, no customer-record access, no pilot, no spend and no publication without the owner's recorded approval under `method/experiment-rules.md`.

## Why this intake exists

Issue #19 asks whether a narrow, valuable software opportunity exists for independent UK
tradespeople and small trade firms. It nominates four unvalidated hypotheses and explicitly
warns that Tradify and ServiceM8 already cover ordinary quoting, scheduling and invoicing,
so those are not an open wedge. The hypotheses are staged here with dated evidence and
direct incumbent counterevidence, then investigated through a normal Method 1.6 observation
sweep (see `observations/20260922T081421Z-normal.md`).

## Buyer / user / payer distinction (applies to all hypotheses)

| Role | Who | Notes |
| --- | --- | --- |
| User | The tradesperson on site (sole trader or employee) | Does the work, captures the record, often the one who feels the friction |
| Economic buyer | Owner/principal of the firm (sole trader, or owner of a 2-10 person firm) | Chooses and pays for job-management software; budget is typically GBP 0-60/user/month |
| Payer | Same as economic buyer for micro-firms; for hypothesis 4 the payer may be a letting agent or property manager, not the trader | This is why hypothesis 4 is separated |
| Customer | The householder or business commissioning the work | Approves variations, receives certificates; not a software buyer |

## Hypothesis 1 - On-site variations (scope/price/timing changes)

**Buyer/job hypothesis.** A micro-firm loses margin when extra work is agreed verbally on
site and never invoiced. The job is to capture the variation at the moment it arises, get a
no-login customer acknowledgement, and carry it into the final invoice.

**Evidence the pain is real and quantified (practitioner/secondary).**
- Simply Business, "Unpaid tasks costing UK tradespeople" (simplybusiness.co.uk/knowledge/trades/unpaid-tasks-costing-uk-tradespeople, accessed 2026-09-22): 92% of UK tradespeople have been asked to take on extra work beyond the original booking; 62% say it happens regularly; nearly 1 in 5 say almost every job; average 1.8 hours/week on out-of-scope requests (~93.6 hours/year, ~GBP 2,600 lost earnings at a representative GBP 30/hour); 34% receive no payment at all; 19% say customers now expect extras as standard; 6% worry they may not be insured for out-of-scope work.
- Kingsbridge, "How to manage scope creep" (kingsbridge.co.uk/blog/trades/trades-life/how-to-manage-scope-creep-tradespeople, 2024-08-20): documents scope creep as a profit drain for tradespeople.

**Direct incumbent counterevidence (the seam is already served).**
- TradePlanr (tradeplanr.com/features/variations, accessed 2026-09-22) sells exactly this workflow: "Extra work, agreed in writing, paid in full. Scope creep kills margins. Record variations the moment they come up, get the customer's acknowledgement, and watch them flow onto the final invoice." Log extras/omissions in seconds, customer acknowledgement by signature on site or share link, auto-added to the final invoice, VO number per variation. Pricing free to start, then GBP 9.99/month or GBP 99.99/year Pro.
- KRBR (karbar.app/blog/change-orders-for-contractors, 2026-07-08) sells change-order discipline.
- TradeDraft (tradedraft.co.uk/handling-variations, 2026-07-25) sells variation handling.
- Buildxact (help.buildxact.com/en/articles/3038641-all-about-variations-change-orders, cited in the issue) offers variations/change orders.

**Key unknowns.** Whether micro-firms (1-2 people) find TradePlanr's workflow too heavy or
too expensive; whether the binding failure is capture, customer approval, or the discipline
to invoice; whether a GBP 9.99/month incumbent leaves any price or simplicity gap.

**Cheapest falsifying test (not run).** Ask a small number of micro-firms to show recent
jobs where extra work was done and not invoiced, then offer a manual (non-software) variation
approval workflow for two weeks and measure whether variations are captured and invoiced.
Predeclared rule: proceed only if a majority of participating firms capture at least one
previously-lost variation and say they would pay for it. Requires owner approval.

## Hypothesis 2 - Installation handover / certificate evidence

**Buyer/job hypothesis.** Certificate-heavy trades (electricians, heating engineers) must
produce certificates, warranties, product details and photos at handover. The job is to
produce and store that evidence with less effort and fewer omissions.

**Direct incumbent counterevidence (extremely crowded).**
- Electrical certificate software: Electrical Certificate App (electricalcertificateapp.co.uk, 5,000+ UK electricians, 24 certificate types, free 14-day trial); EDIS (electricalcertificates.co.uk, free electrical certificate software, BS 7671:2018+A2:2022); CertSync (certsync.co.uk, launching soon, 13 certificate types, GBP 15/month per company + GBP 5/user, BS 7671:2018+A4:2026 live circuit checking); SnapCert (snapcert.app, early-access waitlist, job -> certificate -> photos -> signature -> PDF + invoice, offline-first); Pro Certs (procertssoftware.com, Windows/iPad/Android, unlimited certificates, offline, cloud sync); Elec-Mate (elec-mate.com, from GBP 6.99/month, 1,600+ UK electricians, 16-19 certificate types, AI board scanner, defect code AI, 70+ calculators, RAMS generation); CertVault (certvault.co.uk, "Full EICRs in 12 minutes not 3 hours", AI consumer-unit board scan, 9 certificate types); ElecCerts (eleccerts.co.uk, free public beta, CertScan PDF extraction, 788 BS 7671 observation templates, RegScan, AutoQS, SnapEntry, remedial workflow).
- Job-management products with certificates: Powered Now (powerednow.com, UK-built, 4,000+ UK trade businesses, GBP 2.2B invoiced, 4.7/5 from 1,200+ reviews, 80+ trade forms and certificates signed on the customer's phone, Gas Safety to EICRs, GBP 28-40/user/month, CIS/DRC support); Jobivo (jobivo.co.uk, flat price for whole team, GPS+time-stamped photo evidence, EICR-heavy portfolios, Xero/QuickBooks sync, live verify link); Joblogic (joblogic.com, EICR & NICEIC, certificates stored, quote-to-invoice, Xero sync); ElectroPro/crmflow.io (EUR 19.99/month per crew).
- Official workflow (not demand): gov.uk/building-regulations-approval/use-a-competent-person-scheme establishes the competent-person scheme workflow.

**Key unknowns.** Whether any certificate-heavy trade lacks coverage (e.g. gas/oil, fire,
renewables, refrigeration) or whether the gap is only in a sub-step (e.g. warranty/product
registration, multi-trade handover packs). No evidence gathered of an unserved trade.

**Cheapest falsifying test (not run).** Count the certificate types and trades covered by
the named incumbents and look for a trade with no dedicated product; if one exists, check
whether practitioners in that trade complain about the gap. Desk-only, no approval needed.

## Hypothesis 3 - Heat-pump grant case completion

**Buyer/job hypothesis.** Heat-pump installers must assemble MCS documentation, obtain
customer declarations, meet BUS voucher deadlines and keep audit evidence. The job is to
complete the grant case with less paperwork and fewer rejected vouchers.

**Evidence the obligation is real (primary/official).**
- Ofgem, BUS installer guidance (ofgem.gov.uk/environmental-and-social-schemes/boiler-upgrade-scheme-bus/installers, updated 2026-09-18): installer-led scheme; installers must be MCS certified and a member of an approved consumer code; grants GBP 9,000 off air-to-water or ground source heat pumps in eligible off-gas grid properties until 31 March 2027 (from 21 July 2026), GBP 7,500 standard ASHP/GSHP/water source, GBP 5,000 biomass, GBP 2,500 air-to-air; voucher applications must be submitted by an authorised user from the BUS installer account; installers cannot use a temporary MCS certification number; if MCS certification expires or changes Ofgem withholds vouchers and redemption payments; Ofgem may reject applications or revoke vouchers; the new heat pump must be commissioned no more than 120 days before the voucher application is properly made; EPC number required if a valid EPC exists; vouchers valid 3 months (6 for ground source); installer must deduct the grant value from the quoted total (Regulation 14 amended by SI 2026/390) and must not request or accept payment of the difference (Regulation 17(1)(d)); BUS installer guidance V5.1 applies to applications properly made on or after 28 April 2026.
- MCS MIS 3005-D (Heat Pump Design Standard V3.0, 2025-12-05) and MIS 3005-I (Installation, Issue 1.0): the MCS Contractor must collate a comprehensive document handover pack including all commissioning forms/checklists, maintenance requirements, manufacturer manuals and warranty details, and any documentation required for incentive schemes; handover must include a signed declaration, client/site address, contractor details and MCS certification body/number, and list of key components; no later than 10 working days after commissioning the installation must be registered on the MCS Installation Database (MID) and an MCS Certificate generated and sent to the customer; a per-installation fee is levied. MCS Reference HANDOVER v1.0 issued 30/01/2025.

**Direct incumbent counterevidence (already served, including by a dedicated 2026 startup).**
- CompliancePack (compliancepack.co.uk, accessed 2026-09-22): "MCS documentation automation for UK renewable energy installers"; "Done in 5 minutes, not 2 hours"; "8 installs a month? That's 16 hours, two full working days, spent on post-installation documentation"; claims 2 hours average manual compliance docs per installation vs 5 minutes with the product; GBP 50,000+ typical cost of a failed MCS audit; generates customer declaration + MCS commissioning records + homeowner handover pack; all 17 MCS:2025 checklist items tick off automatically; manages BUS grant documentation for Ofgem voucher redemption; GBP 149/month single plan, 14-day free trial; launched 2026; ICO registration ZC159737.
- Payaca (payaca.com/uk/industries/heat-pump-installers): "MCS Documentation ... Customer declarations, commissioning certificates, and handover packs - all linked to the project"; "75% less time on MCS paperwork"; Heatpunk heat-loss integration; grant tracking; service plans; 2-4 weeks to go live; ISO 27001; trusted by OVO Solar and British Gas; 4.8/5 Google, 4.9/5 Capterra; full REST API + webhooks.
- Kizeo Forms (kizeo-forms.com/en/jobs/heat-pump-installer, 2026-06-11): "Generate your BUS Scheme files"; signed commissioning sheet; before/after photos; MCS certificate archived in one click; AI photo capture (OCR) pre-fills grant file fields; GBP 15/user/month annual; 120,000 daily users.
- VioTrade (viotrade.co.uk/trades/heat-pump-installer-software): MCS, BUS grants & quotes; attach MCS and grant paperwork to each job; free 14-day trial.
- Quickler (quickler.co.uk): CP12/heat-pump commissioning checklists via WhatsApp. Aireo App (aireo.app): heat loss calculation and compliance software for installers.

**Key unknowns.** Whether the addressable market (MCS-certified heat-pump installers) is
large enough for a new entrant at GBP 149/month against CompliancePack and Payaca; whether
the residual gap is audit defence rather than document generation.

**Cheapest falsifying test (not run).** Count MCS-certified heat-pump installers and the
number of shipping products serving the exact documentation workflow; if the product count
is already >= 4 and the installer population is small, reject on demonstrated occupation.
Desk-only, no approval needed.

## Hypothesis 4 - Safety-check / access coordination

**Buyer/job hypothesis.** Coordinating gas safety, EICR, EPC and alarm checks across a
property portfolio, including tenant access, is administratively costly. Note the buyer may
be a letting agent or property manager rather than a solo trader, so this track is separated.

**Direct incumbent counterevidence (already served).**
- Safe2 (nrla.org.uk/services/property-compliance/safe2): NRLA service covering EICR, Fire Risk Assessment, EPC, Gas Safety Certificate, Smoke Alarm Test, PAT, Gas Boiler Service; "We handle tenant and contractor coordination, making the process hassle-free for landlords and agents"; online portal to order/track/renew; Safe2Rent subscription.
- JRM Compliance (jrmcompliance.com): "Letting, landlord and contractor software"; document storage; automatic expiry reminders at 90/60/30/7 days; Contractor Centre (secure job link, request quotes, book work, receive finished certificate, no account needed for the contractor); Right to Rent checks; portfolio compliance score; Renters' Rights Act 2025 ready.
- Comprent (comprent.co.uk): built for letting agents managing every landlord; tracks every obligation per property/tenancy; Awaab's Law timers; deposit deadlines; certificate expiry; ombudsman registration; document generation; certificate vault (Gas Safety, EPC, EICR) with reminders at 60/30/7 days; AI compliance assistant; maintenance/Awaab's Law 5-working-day investigation deadline; tenant portal; PRS Database registration flagged as "Upcoming Dec 2026"; fines up to GBP 40,000 per property.
- ExpiryEdge (expiryedge.com/solutions/facilities-management): facilities compliance software tracking fire, lift, gas, EICR, legionella, asbestos, HVAC/TM44 across every building with 90-day lead alerts, per-building and per-portfolio rollup, insurance/lender/audit exports.
- Gas-elec (gas-elec.co.uk): one coordinated visit (CP12 + boiler service + appliance checks + CO alarm checks + electrical tests + digital reporting); dashboards for letting agents and housing providers. ADREM (adrem.co.uk): EICR/PAT/gas safety/plumbing for landlords, hospitality, healthcare, commercial. Manchester EICR (manchestereicr.com): bundled landlord compliance packages.
- Official obligations (not demand): NRLA compliance checklist - annual gas safety check producing a CP12, copy to tenants within 28 days and to new tenants at move-in, records kept at least 2 years; EICR at least every 5 years, provided to tenants before move-in, urgent remedial work within 28 days; smoke alarms each storey and CO alarms in rooms with fuel-burning appliances since 1 October 2022; EPC E or above; deposit protection and prescribed information; Legionella risk assessment; Right to Rent checks. Missed CP12 is a criminal offence; HSE can prosecute up to GBP 6,000 per appliance; no CP12 means no possession order on most grounds. Typical costs GBP 60-120 boiler-only, GBP 80-150 full house, GBP 200-300 combined gas+EICR+EPC compliance pack.

**Key unknowns.** Whether any portfolio size or property type is unserved; whether the
residual pain is contractor-side (getting paid, scheduling) rather than agent-side.

**Cheapest falsifying test (not run).** Identify a portfolio segment (e.g. self-managing
landlords with 1-3 properties, or small housing providers) and check whether the named
products serve it at a price it will pay. Desk-only, no approval needed.

## Hypothesis-adjacent finding - CIS changes from 6 April 2026

Not one of the four nominated hypotheses, but surfaced during the incumbent research and
recorded here because it is a dated change with a named buyer (contractors and their
accountants) and a concrete new task.

- inndex.co.uk, "Construction Industry Scheme changes 2026" (2026-09-19); gov.uk CIS 340 (updated 8 July 2026); smithbutler.co.uk (2026-08-28): the "should have known" anti-fraud standard lets HMRC pursue any contractor that knew or should have known a payment in their supply chain was connected to fraudulent or non-compliant CIS activity, potentially three tiers up; monthly CIS NIL returns are reinstated from 6 April 2026 (removed in 2015) with the full penalty regime (GBP 100 initial fixed penalty, further charges at six and twelve months); payments to local authorities and qualifying public sector bodies are removed from CIS scope (Regulation 24ZA); HMRC can make a tax determination, charge a penalty and immediately cancel gross payment status, with a five-year bar on reapplying; Autumn Budget 2025 costings used ~GBP 0.5bn annual labour fraud losses and expect the measure to raise GBP 205m in 2026/27; contractors must give a payment and deduction statement to each subcontractor within 14 days after the tax month end (normally by the 19th); CIS deduction rates 20% registered, 30% unregistered, 0% gross payment status; the VAT domestic reverse charge (since 1 March 2021) means VAT-registered subcontractors invoice VAT-registered contractors without VAT and must state "Reverse charge: customer to account for VAT to HMRC".
- Counterevidence: cloud accounting platforms (Xero, QuickBooks, Sage, FreeAgent) already handle CIS, reverse charge and MTD reasonably well; Trade PA (tradespa.co.uk) advertises CIS deductions and statements and Domestic Reverse Charge invoicing; Powered Now advertises CIS/DRC support.

**Status:** triaged in the observation pool as a change-driven observation; not promoted.

## Deduplication against existing ledger and prior intake

- **Aucly** (school/PTA/charity auctions) - no overlap with trades.
- **Issue #17** (school software) - no overlap.
- **Issue #18** (open banking) - no overlap; hypothesis 4's coordination pain is adjacent to property compliance, not payments.
- **Seeds** - no seed covers trades, variations, certificates, heat-pump grants or safety-check coordination.
- **Prior observations** - the 20260921T100247Z-normal pool rejected an independent-school finance/MIS observation; no trades observation exists in any prior pool.

## Boundaries

No source was accessed through authentication; no customer records, no outreach, no pilot,
no spend and no publication. This intake is a discovery input only. Any experiment arising
from it must be proposed under `method/experiment-rules.md` with a predeclared decision rule
and requires the owner's recorded approval before any external action.
