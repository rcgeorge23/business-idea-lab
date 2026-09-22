# Issue #15 response: bounded UK legislative-change opportunity sweep

- **Issue:** rcgeorge23/business-idea-lab#15 — "Run a bounded UK legislative-change
  opportunity sweep through Method 1.6"
- **Run that did the work:** `20260922T060326Z-normal` (status success, method 1.6.0,
  cost USD 0.033194, 225,024 tokens, validation pass)
- **Written:** 2026-09-22
- **Status:** the sweep itself is complete and recorded in
  `runs/20260922T060326Z-normal/summary.md` and
  `observations/20260922T060326Z-normal.md`. This file supplies the three artefacts
  the issue's acceptance criteria require that the run did not emit as separate
  files — a dated official-source watchlist, an explicit intake disposition table,
  and a legal-source retrospective with a monitoring recommendation — and corrects
  one stale row in the run summary.

> **Boundary note.** I cannot comment on, label or close the GitHub issue (no
> commits, pushes, issues, PRs or other publication). This file is the local
> response; the owner decides what, if anything, to post back to the issue.

---

## 1. Dated official-source watchlist

Every row records the legal state, jurisdiction, confirmed vs provisional dates and
the uncertainty that would need re-checking. "Access date" is the date the cited
source was read during the run (2026-09-22 unless stated). Legal state uses the
issue's vocabulary: **consultation** / **Bill** / **enacted-not-commenced** /
**in force**.

| # | Change | Jurisdiction | Legal state | Effective date (confirmed / provisional) | Source (URL) | Access date | Uncertainty to re-check |
| - | ------ | ------------ | ----------- | ---------------------------------------- | ------------ | ----------- | ----------------------- |
| W1 | NHS dental contract reform: Unscheduled Care band, denture restructure, three Complex Care Pathways with monthly sequential FP17/FP17PR submissions | England | In force (contract variation) | 2026-04-01 (confirmed) | NHSBSA certified dental PMS list (updated 2026-07-09); NHS England dental contract reform guidance | 2026-09-22 | Whether further pathway phases are added in 2026-27; whether NHSBSA changes the certified-software list |
| W2 | DfE funded-hours operational guidance: itemised invoices separating funded and paid hours | England | In force (guidance) | 2026-01 (confirmed) | GOV.UK DfE early-years funding operational guidance | 2026-09-22 | Whether the guidance is revised for the 2027-28 funding year; local-authority rate schedules change annually |
| W3 | Pharmacy First independent prescribing pathways; single approved prescribing IT solution (Cleo Systems EPS Community) | England | In force (service launch) | 2026-10 (confirmed) | pharmacymagazine.co.uk 2026-09-17; Community Pharmacy England; NHS England statement | 2026-09-22 | Whether NHS England widens the supplier list; whether the MYS API is delivered; whether the £525/month infrastructure payment changes |
| W4 | German B2B e-invoicing: receive obligation live; issue obligation for turnover > €800,000 then all businesses | Germany | In force (receive) / enacted-not-commenced (issue) | Receive 2025-01-01 (confirmed); issue 2027-01-01 and 2028-01-01 (confirmed in statute) | EC digital-building-blocks 2026-03-06; vatupdate.com 2026-09-17; Avalara 2026-09-14 | 2026-09-22 | Whether the turnover threshold is amended; whether a central clearance portal is introduced (currently none) |
| W5 | Companies House identity verification under ECCTA 2023: personal ID code linked to each directorship and PSC role, separate submission windows | England & Wales / UK | In force (phased) | Director at confirmation-statement date; non-director PSC in first 14 days of birth month (confirmed, phased) | ICAEW 2026-02-12; AccountingWEB 2026-01-26; Companies House MI 30 Jul 2026 (via acenteus-cca.com 2026-08-31); Pinsent Masons 2026-09-10 | 2026-09-22 | Whether the remaining unverified population triggers an enforcement step; whether transitional easements are extended |
| W6 | HM Land Registry contractual control agreements: prescribed information to HMLR within 60 days of grant/assignment/variation, digitally via a regulated conveyancer; HMLR must publish a dataset | England & Wales | Enacted-not-commenced | Duty from 2027-04-06; dataset after 2028-04-06 (confirmed in SI) | GOV.UK guidance 2026-03-09 and news 2026-06-12; SI 2026/615; legislation.gov.uk; Simmons & Simmons 2026-03-24 | 2026-09-22 | Whether the HMLR digital service ships before 2027-04-06; whether commencement is deferred; the exact prescribed-information schema |
| W7 | Employment Rights Act 2025 guaranteed-hours, reasonable notice of shifts and short-notice payments | Great Britain | Enacted-not-commenced | 2027 (provisional, subject to consultation) | Employment Rights Act 2025 (c.36); implementation roadmap subject to consultation | 2026-09-22 | The consultation outcome and the actual commencement date; whether the duty is phased by employer size |
| W8 | Making Tax Digital for Income Tax: thresholds extended downward | UK | In force (phased) | > £50,000 from 2026-04-06 (in force); > £30,000 from 2027-04-06; > £20,000 from 2028-04-06 (confirmed) | HMRC MTD guidance; owner intake `intake/2026-09-22-owner-nominated-opportunities.md` | 2026-09-22 | Whether the £20,000 tranche is deferred; whether HMRC changes the recognised-software list |
| W9 | Smart Data / Data (Use and Access) Act 2025: powers to mandate sector smart-data schemes; Smart Data 2035 strategy | UK | Enacted-not-commenced (enabling powers) | Framework only; Open Banking consultation early 2026; energy regulations 2027-28; Guidebook early 2027 (provisional) | GOV.UK Smart Data Strategy 2026-03-26; GOV.UK digital-markets call-for-evidence response 2026-05-12; Freshfields 2025-07-02 | 2026-09-22 | Which sectors are actually designated; whether any scheme reaches commencement; nearly all detail is left to secondary legislation |
| W10 | Procurement Act 2023 and SI 2026/360: central platform and framework transparency | UK | In force | 2025-02-24 (confirmed); SI 2026/360 in force | Procurement Act 2023; SI 2026/360; dprte.co.uk 2026-08-26 | 2026-09-22 | Whether the central platform reduces portal fragmentation further; whether framework data is published in a machine-readable form |
| W11 | Enterprise software end-of-life wave: Dynamics GP, TrackWise on-prem, IBM Maximo 7.6→MAS, Siemens PCS7 v7→v9, higher-ed SIS/ERP | Global / vendor-driven | In force (vendor lifecycle) | Dynamics GP new subscriptions ended 2026-04-01, mainstream support to 2029-12-31; others 2026-2029 (vendor-published) | erpsoftwareblog.com 2026-07-24; sikich.com 2026-09-18; maximo-users.net 2026-06-25; vanguard-systems.ch 2026-05-01 | 2026-09-22 | Vendor dates shift; this is a vendor lifecycle, not legislation, and is listed for completeness |

**Legal-state discipline applied.** W1-W5 and W8 are in force or phased-in-force;
W6 and W7 are enacted-not-commenced; W9 is an enabling framework with no
commencement; W10 is in force; W11 is a vendor lifecycle, not law. No row treats a
consultation or an announcement as a mandate. W7's 2027 date is explicitly
provisional and subject to consultation, which is why O18 was rejected on timing.

---

## 2. Intake disposition table (I1-I4)

The owner intake `intake/2026-09-22-owner-nominated-opportunities.md` requires each
item to be checked against: verified/changed/disproved source status, legal state,
jurisdiction, affected buyer, mandatory task, existing public/free solution, named
incumbents, evidence of current workaround or spend, distribution route, and a cheap
falsifying test. The run folded I1-I4 into observations O20, O13, O18 and O10
respectively; this table makes the disposition explicit.

| Intake | Observation | Source status | Legal state / jurisdiction | Affected buyer | Mandatory task | Existing public/free solution | Named incumbents | Evidence of current workaround or spend | Distribution route | Cheap falsifying test | Disposition |
| ------ | ----------- | ------------- | -------------------------- | -------------- | -------------- | ----------------------------- | ---------------- | --------------------------------------- | ------------------ | --------------------- | ----------- |
| I1 Business Idea Lab as a validation service | O20 | Verified as stated (non-regulatory) | N/A | Founders and SME innovators | None (voluntary purchase) | None checked | WhyHire, EVIDR, Finsight, StartupValidation (named in the intake) | **None gathered this run** — no independent practitioner evidence of recurring paid pain | Not established | A tightly specified paid pilot offered to a small number of unrelated target buyers (no outreach authorised) | **Rejected** — absent evidenced problem and absent persistence thesis; the intake's persistence claim is an assertion and does not lift the missing-why-now cap |
| I2 Making Tax Digital transition for a narrow landlord/sole-trader cohort | O13 | Verified (thresholds confirmed) | In force (phased); UK | UK accountancy/bookkeeping practices (1-20 staff) and their self-employed/landlord clients | Digital record-keeping and quarterly updates above the threshold | HMRC directs users to compatible and bridging software | HMRC-recognised MTD software, bridging tools, IRIS Elements, TaxCalc, FirmFlow, FigsFlow, Layer3, Dext, Hubdoc | Practitioner evidence of manual intake (12-18 steps across 4-6 systems) but the filing seam is served | Accountancy practice channel | Count HMRC-recognised MTD products and bridging tools serving the £20k-£50k cohort | **Rejected** — recognised software and bridging tools demonstrably occupy the seam; deduplicates the prior pool's MTD observation |
| I3 Guaranteed-hours and shift-notice workflow | O18 | Verified as enacted; timing provisional | Enacted-not-commenced; Great Britain | UK SME employers in shift-based sectors (hospitality, retail, care) | Guaranteed hours, reasonable notice, short-notice payment | Free Acas guidance covers the duty | Rota and HR/payroll platforms already own the shift, contract and pay data | No live duty and no budget evidence; no dedicated tool surfaced | Rota/HR platform channel | Re-check the consultation outcome and commencement date | **Rejected** — timing not fixed (2027, subject to consultation) so no dated forcing event; the data sits inside rota/HR suites; deduplicated against `reasonable-steps` (same Act) |
| I4 Contractual control agreements reporting handoff | O10 | Verified (SI 2026/615) | Enacted-not-commenced; England & Wales | Conveyancers, developers, promoters and landowners | Send prescribed information to HMLR within 60 days, digitally via a regulated conveyancer | HMLR is building the submission service itself | No third-party product surfaced | **No evidenced buyer pain or budget yet** — the duty is pre-launch | Conveyancing channel (not yet reachable) | Re-check whether the HMLR digital service ships before 2027-04-06 and whether practitioners report a recurring handoff pain | **Deferred/rejected** — rejected on absent evidenced buyer/problem, not on incumbent occupation; the intake's own gate ("do not promote until buyer-side evidence shows the handoff is frequent and underserved") is not met. Adjacent seed `land-control-data-intelligence` recorded for the post-2028 dataset |

**Deduplication against prior art.** `wastetrack` (killed on defensible_wedge) and
`uk-epr-small-producer-tooling` (dropped seed) were not revived; `prsregister`,
`propident` and `reasonable-steps` were used as prior-art checks; I3 was explicitly
deduplicated against `reasonable-steps` (same Act). No new angle revives a killed
idea under a new title.

---

## 3. Legal-source retrospective and monitoring recommendation

**Which legal sources supplied useful signals.** The most useful were
**legislation.gov.uk and commencement instruments** (they let W6 be classified
enacted-not-commenced with a confirmed date rather than a vague "coming soon") and
**regulator/arm's-length-body operational guidance** (NHSBSA certified-software
lists, HMRC MTD guidance, HMLR guidance) because they name the concrete task and the
existing tooling. **Impact assessments and official statistics** were useful for
population and cost clues (e.g. the Companies House MI percentages) but, as the
issue warns, population is not addressable demand.

**Which sources were misleading.** **Announcement and consultation coverage** was
the main trap: several changes read as imminent in secondary coverage while the
legal state was consultation or an enabling power (W9 Smart Data is the clearest
case — a 2035 strategy with almost no commenced detail). **Vendor and consultancy
content** (e-invoicing vendors, ERP partners, PMS vendors) was useful for the
incumbent check but systematically frames the change as an urgent buying trigger;
it must never be used as the source of the legal state.

**How often dates/status changed.** Within this single pass, no date moved, but the
classification exercise itself changed the picture: W7's 2027 date is provisional
and subject to consultation, and W9 has no commencement at all. The lesson is that
the *status* field, not the date, is where the risk sits — a date without a legal
state is not usable.

**Is this source class worth routine monitoring?** **Yes, but narrowly.** The
legislative class reliably produced *dated, verifiable* changes and a clean
incumbent check, and it is the only class in the whole corpus that produced a
genuinely dated why-now (the Stocky sunset was vendor-driven, not legislative).
However, in this pass every legislative change died on **demonstrated occupation**
or **absent evidenced buyer** — the same failure modes as the non-regulatory
classes. Monitoring is worth repeating only if it is paired with a buyer-side
evidence step; a legislative watchlist on its own will keep producing
already-monetised seams.

**Sources worth watching (ranked):**
1. `legislation.gov.uk` commencement instruments and `bills.parliament.uk` Progress
   of Public Bills — for legal state and confirmed dates.
2. Regulator/ALB operational guidance and certified-software lists (NHSBSA, HMRC,
   HMLR, DfE) — because they name the concrete task and the existing tooling.
3. GOV.UK consultations and impact assessments — for population/cost clues only,
   never as a mandate.

**Not worth routine monitoring:** vendor/consultancy blogs as a source of legal
state; general trade press; anything that reports a change without a legal state.

**Recommendation on automated monitoring (issue's final criterion).** Do **not**
schedule scraping yet. This manual pass did not demonstrate useful non-duplicate
signals — every legislative observation was rejected on occupation or absent buyer —
so the precondition in the issue ("only after this manual pass demonstrates useful
non-duplicate signals") is not met. If monitoring is revisited, the cheapest useful
form is a **manual quarterly re-check of the three ranked sources above against the
watchlist in section 1**, not a scraper.

---

## 4. Correction to the run summary (stale row)

`runs/20260922T060326Z-normal/summary.md` line 200 still reads:

> | Reviewer-side outstanding audit | The `wonkybox` kill-#15 false-negative audit request remains open for the reviewer; no worker obligation | Reviewer's discretion | `reviews/` request file |

This is **stale**. The reviewer's response already exists at
`reviews/2026-09-21-false-negative-audit-wonkybox-chatgpt.md` (ChatGPT / GPT-5.6
Sol, 2026-09-21, verdict **kill upheld**), and it was recorded before the run in:

- `ideas/wonkybox/decision.md` — outcome, grounds, calibration lesson, reopening
  condition, "adjacent seed: not created";
- `reviews/2026-09-21-false-negative-audit-request-wonkybox.md` — status changed to
  "answered";
- `reviews/2026-09-21-review-queue-reconciliation.md` — row added and closing
  sentence replaced with "No review outcome is outstanding."

The run summary's own later text (line 212) already says the WonkyBox audit "was
answered with the kill upheld", so the summary is internally inconsistent. Per
`runs/README.md` a run directory is never rewritten, so this file is the correction
of record rather than an edit to `summary.md`. **No review outcome was overwritten
or ignored.**

---

## 5. Acceptance-criteria mapping

| Issue #15 acceptance criterion | Where satisfied |
| ------------------------------ | --------------- |
| Dated official-source watchlist records legal state, jurisdiction, dates and uncertainty | Section 1 (W1-W11) |
| Owner-nominated leads checked, deduplicated, included or explicitly deferred/rejected with reasons | Section 2 (I1-I4) |
| At least one non-regulatory source class searched; source-class budget and 15-20 pool preserved | Run summary + `observations/20260922T060326Z-normal.md`: 20 own observations, 10 regulatory/regulation-adjacent vs 10 non-regulatory; 12 classes searched incl. the previously underexplored "new datasets" class |
| Each promising legal change has an incumbent/free-tool check and a buyer-workflow hypothesis backed by source evidence | Observation rows O1-O20 each carry an incumbent/free-alternative check; the run summary's source-class table and the observation evidence columns cite the sources |
| Normal lab run records all triage outcomes, one false-negative audit, ≤3 full candidates, ≤1 regulation-derived candidate | Run summary: 0 promotions (0 regulation-derived), one false-negative audit (O3 Pharmacy First, upheld) |
| No idea advances on legal change alone; no outreach/spend/publication without owner approval | Run summary: 0 advances, 0 experiments started, no outreach/spend/publication; this file adds none |
| Run summary recommends whether legislative monitoring is worth repeating and which sources to watch | Section 3 |

---

## 6. Boundaries

No commits, pushes, issues, PRs or other publication; no contact with anyone; no
money spent; no accounts created; no commitments made; no experiment started;
`method/` not edited; no recorded review outcome overwritten. The GitHub issue
itself is untouched — the owner decides whether to post this response back.
