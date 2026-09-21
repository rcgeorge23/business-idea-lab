# Evidence: no-export legacy clinical systems and UI-level extraction pricing

- **Idea / scope:** `clinicdata-liberation`
- **Register:** evidence
- **Source:** valuestreamai.com case study, "Extracting data from a legacy clinical system with no export" (2026-08-03)
- **Accessed / dated:** 2026-09-21
- **Credibility:** vendor claim (services vendor case study) — treated as indicative, not proven demand

## Claim(s) supported

- A real private practice was locked in a legacy clinical system with no CSV, API or export, and paid for extraction performed at the UI level inside the practice's own authenticated session (no credentials leave the practice; no access controls bypassed).
- Published price bands for this service: single-registry extraction £4k–12k / $5k–15k (2–4 weeks); multi-entity with clinical history and billing £12k–32k / $15k–40k (6–10 weeks); multi-site consolidation £32k+ (10+ weeks).
- Industry benchmarks for EHR migration: small-practice $5k–20k over 3–10 weeks; mid-market $20k–50k; enterprise Epic $100k–500k+.
- Many private/specialist/allied-health platforms are not ONC-certified, so the US certification-based export right does not reach them.

## Exact detail

- Method described: drive the legacy application's own UI as an authenticated user and capture structured records, rather than requiring a vendor export or database access.
- ONC context: >50 certified EHR vendors have exited since 2016 (ONC data); the §170.315(b)(10) full-population EHI export criterion does not help uncertified systems.

## Why it is credible

The method and the price bands are specific and consistent with independent migration benchmarks quoted in the same source; the ONC figures are attributed to a public dataset.

## What it does NOT show

- It is a single vendor's case study: it does not prove repeat demand or that buyers choose a third party over the receiving vendor's own migration service.
- It does not show UK-specific volumes or willingness to pay, and it does not prove the price bands are realised prices rather than list framing.
- It does not establish whether the same method is lawful under each source system's licence terms in the UK.

## Links

- https://valuestreamai.com/ (accessed 2026-09-21; case study dated 2026-08-03)
- Used by: `ideas/clinicdata-liberation/scorecard.json#buyer_budget_clarity`
- Used by: `ideas/clinicdata-liberation/scorecard.json#economics`
- Used by: `ideas/clinicdata-liberation/decision.md`
