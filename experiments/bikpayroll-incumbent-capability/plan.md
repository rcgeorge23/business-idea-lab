# Experiment plan — `bikpayroll-incumbent-capability`

- **ID:** `bikpayroll-incumbent-capability`
- **Idea:** `bikpayroll`
- **Created:** 2026-09-21
- **Status:** proposed
- **Approval:** not required for the desk scan (no external contact, spend, accounts or commitments). Any subsequent interview stage is a separate experiment and requires human approval.

## Central assumption

Benefit providers and payroll/benefits platforms will **not** supply or absorb per-period benefit-in-kind data for employer payroll, leaving a paying third-party bridge.

## Hypothesis

If the incumbent capability scan finds no more than one benefit provider and no payroll/benefits platform already supplying or ingesting machine-readable per-period BiK data, then the ingestion/reconciliation seam is genuinely unserved and worth a willingness-to-pay test.

## Test design

- **Population / sample (desk only):**
  - The 6 largest UK payroll software vendors (e.g. Sage, IRIS, BrightPay, Xero, QuickBooks, Thesaurus/Staffology) — published API/import capability for per-period BiK values and any provider integrations/roadmaps.
  - 5 major vehicle leasing/fleet providers and 5 medical insurers / fuel-card providers — whether client portals already export machine-readable benefit data, at what frequency, and at what (if any) separate employer fee.
  - Benefits-administration platforms (e.g. Benefex, Zellis, employee-benefit suites) — whether they offer provider-to-payroll BiK ingestion.
- **What participants see / do:** nothing — this is public-document and vendor-material desk research. No one is contacted.
- **Recruitment route:** none.
- **Instrumentation:** a fixed scan table with one row per vendor/provider and columns: source URL, date, capability claim, frequency, fee, evidence quality. Findings are written to an evidence register entry.
- **Timebox:** ≤3 calendar days, ≤6 human-hours.
- **What is deliberately NOT included:** contacting vendors, requesting demos, creating accounts, or interviewing employers/bureaus (that is the escalation stage and needs separate approval).

## Decision rule (fixed before running)

| Outcome | Verdict | Action |
|---|---|---|
| ≥3 named benefit providers supply or publicly roadmap machine-readable per-period benefit data to employer payroll at no separate employer fee, **OR** ≥2 payroll/benefits platforms already ingest provider BiK data | **KILL** | Record `defensible_wedge = fail` with citations; move `bikpayroll` to `killed`; record why. |
| ≤1 provider does so and no platform does, but payroll-vendor roadmaps are silent | **PARK** | Keep `desk-screened`, wedge stays `unknown`; do not advance. |
| No provider and no platform does so **and** a documented payroll-vendor roadmap gap exists | **ESCALATE** | Propose the willingness-to-pay test (new experiment, approval required). |

## Kill condition

Either threshold in the KILL row — this directly falsifies the "unserved seam" claim.

## Cost bound

- Money (GBP): 0
- Human hours: 6
- Calendar days: 3

## Risks and safeguards

- **Risk:** confirmation bias in a scan run by the candidate's author. Safeguard: fixed vendor list and pre-committed thresholds written before searching; every row must cite a dated public source; negative findings are recorded with the same effort as positive ones.
- **Risk:** mistaking vendor marketing for capability. Safeguard: accept only documented import formats, API references or explicit roadmap statements.
- No privacy, legal or external-contact risk: desk-only.

## Results

Not yet run.
