# Experiment results: BiK incumbent-capability scan

- **ID:** `bikpayroll-incumbent-capability`
- **Idea:** `bikpayroll`
- **Dates run:** 2026-09-21 (desk scan, same day; within the 3-day timebox)
- **Recorded by:** worker (transcribed from public sources; no external contact)
- **Approval record:** not required — desk-only scan, approval.required `false` in
  `experiments/index.json` before the scan began. After completion the index
  records `approval.granted = true`, granted by the worker on 2026-09-21, to
  document that the scan was authorised only by its own pre-committed plan
  (population, thresholds, safeguards) and involved no external contact.

## What actually happened

The scan was executed against the vendor and provider population fixed in
`plan.md` before any searching: six UK payroll vendors (Sage, IRIS, BrightPay,
Xero, QuickBooks, Thesaurus/Staffology), fleet/leasing and medical-insurer
providers, and benefits-administration platforms. Public sources only: vendor
documentation, help centres, product pages, blogs, a broker interview article
and government policy material. No trials, accounts, demos or contact with any
party.

The planned population was adjusted once, before findings were interpreted:
Xero and QuickBooks published no BiK-specific ingestion material in searches,
so they are recorded as "no material found" rather than silently dropped, and
fleet findings were concentrated on Lex Autolease and Ayvens (the two whose
public export material was retrievable). The decision thresholds were not
touched after results arrived.

Findings against each scan row are registered in
`evidence/bikpayroll/2026-09-21-incumbent-capability-scan.md`. The decisive
finding: named benefits platforms and adjacent product suites already ingest
provider benefit data and emit per-period taxable values into payroll, and
several medical insurers already do true monthly reconciliation.

## Raw numbers

Scan-table rows: 21 sources across the fixed population (payroll vendors 9, fleet/leasing 4, medical insurers 2, benefits platforms 5, practitioner/regulatory 4 — some sources cover more than one row).

| Metric | Target | Actual | Notes |
|---|---|---|---|
| Payroll vendors with documented per-period BiK ingestion | (investigate) | 1 of 6 (IRIS, managed service; other payroll products require manual or CSV entry) | IRIS blog 2026-03-10; Sage KB 2026-06-23; BrightPay docs; no material found for Xero/QuickBooks |
| Benefits/payroll platforms already ingesting provider BiK data | threshold ≥2 for KILL | 4 named with evidence: **Zhoosh Benefits**, **The Electric Car Scheme**, **Zest**, **Zellis** (with Benefex) | Zhoosh is the exact hypothesised seam |
| Benefit providers supplying machine-readable monthly data | threshold ≥3 for KILL | 3 medical insurers with true monthly reconciliation (Bupa, Vitality, AXA, broker-sourced); 2+ fleet portals with XLS/CSV exports | Format not specified for insurer bills; not needed for the verdict |
| Payroll-vendor public roadmaps for April 2027 ingestion | (investigate) | IRIS: compliance committed 2026-06-23; Sage/BrightPay: guidance to prepare, no ingestion commitment found | |
| Desk time used | ≤6 human-hours | ~4 hours | Within bound |

## Quotes / raw artefacts

- Zhoosh Benefits, product page (2026-08-04): "Payroll receives an
  employee-by-employee report that includes taxable values, a benefit breakdown,
  and a clear record of what has changed"; the page states it works "without
  waiting for insurer invoices or rebuilding the numbers in spreadsheets".
- The Electric Car Scheme, tech-and-integrations page: "We integrate directly
  with your payroll via API or SFTP, providing clear monthly inputs with no
  manual processing required".
- Zest: "connects with the benefits providers and HR and payroll systems you
  use, updating information automatically" (product site, includes SFTP and
  complex transformations).
- IRIS blog (2026-03-10): "Our managed benefits in kind service handles the
  end-to-end process on your behalf ... with no separate system or manual
  workarounds required".
- Broker quoted in Hooray Health & Protection (2026-04-13): "Those providers
  that are ahead of the game currently and do true monthly reconciliation are
  Bupa, Vitality and AXA"; "Bupa and Vitality have good online employer zones
  that allow advisors and clients to view and download monthly bills".
- payrollexplained.uk (2026-08-14): "The tax calculation is honestly the easy
  bit; getting a medical premium into the system before cut-off is the product
  problem." (Articulates the seam; also shows the market discussing it publicly.)

Full source table with URLs, dates, capability claims, frequency, fee and
evidence quality is in the evidence register.

## Contradictions and surprises

- **The exact seam is already productised.** The scan expected, at best, partial
  bridging by large enterprise suites. Instead a dedicated benefits platform
  (Zhoosh) markets precisely the "insurer data → per-period taxable payroll
  report" job, dated 2026-08-04 — before the mandate even starts.
- **Salary-sacrifice providers self-serve.** The Electric Car Scheme already
  pushes monthly payroll inputs by API/SFTP, so the car side of the seam is
  contested from the provider end, not just by payroll vendors.
- **Negative evidence pointing the other way.** Sage and BrightPay still
  describe manual cash-equivalent entry, and IRIS Cascade does not calculate
  cash equivalents — so payroll-vendor *software* is genuinely behind. This is
  the strongest case for the idea, and it is not enough: the platform category
  absorbs the gap, and a new entrant's wedge would be a feature of benefits
  software or a managed service.
- **Insurer monthly reconciliation is mixed but moving.** Some insurers still
  divide the annual premium by twelve; the leading three do true monthly
  reconciliation. A bridge could have found a short-term niche among laggard
  insurers, but that is serving the laggards' clients with data the insurer
  controls — a fragile position, not a defensible wedge.

## Verdict against the pre-fixed decision rule

**KILL.** The rule's second branch is met: ≥2 named payroll/benefits platforms
already ingest provider BiK data — Zhoosh Benefits (explicit, exact seam, dated
2026-08-04) and Zest (provider-to-payroll integrations), with The Electric Car
Scheme and Zellis/Benefex as further named cases. The first branch is also
partially evidenced (Bupa, Vitality, AXA true monthly reconciliation) but the
source does not specify machine-readable formats, so it is recorded as partial
rather than relied upon.

Per the decision rule: record `defensible_wedge = fail` with citations, move
`bikpayroll` to `killed`, and record why. The unresolved questions the PARK
branch would have preserved (payroll-vendor software gaps, laggard insurers) do
not survive as a wedge because they are being served by an adjacent, already
occupied category.

## Follow-up

- Idea state proposed: `killed` (worker may only record; kill stands on the
  precommitted rule, not on human judgement)
- Human decision (if made): none required for the kill; the human may dispute it
  via the false-negative audit (see `## False-negative audit` in the decision
  record)
- Next experiment (if any): none. An escalation WTP test was contemplated by the
  plan and is **not** proposed: the rule's KILL branch fired, so per the plan no
  escalation is available.
