# Search-intent observation pool

- **Run:** `20261013T055941Z-representative`
- **Date:** 2026-10-13
- **Method version:** 1.9.0
- **Mode:** representative
- **Qualified hypothesis shortlist:** 4 (target 3-5; fewer when weak — zero promotions, honest zero)
- **Archetype mix:** 4 search-led (archetype D); no change-driven, persistent, or latent promotions
- **Source mix:** SERP/pricing pages (all four), community/demand discussion (H1 + audit), job ads (latent pass)
- **Latent pass completed:** yes — 1 bounded search, 0 admissible latent observations

Search-intent-first sweep. No volumes, rankings, CPC, trends or difficulty
were invented; no search API or rank tool was used. Pricing pages are dated
operator-published prices (accessed 2026-10-13), not proof of demand. Blocked
or empty checks are recorded as no-result, never as absence of demand.
Search-volume-style evidence is treated as interesting but never as
willingness to pay.

## Qualified hypotheses (search-intent shortlist, v1.9.0)

| ID | Seed query / intent cluster | Job/task | Existing solutions (SERP, 2026-10-13) | Neglected sub-niche / wedge | Paid self-service hypothesis | Source class | Archetype | Dated demand evidence | Triage | Triage reason |
|----|-----------------------------|----------|----------------------------------------|-----------------------------|------------------------------|--------------|-----------|-----------------------|--------|---------------|
| H1 | `"certificate expiry" tracker software small business`; `reddit small business "training matrix" spreadsheet admin pain` — employee certificate/training expiry tracking | Track training/licence expiry dates, chase renewals, keep audit evidence | certtracker.app (waitlist; free/$29/$79/mo), getcerttracker.com ($49/mo), expirykeeper.com, expiryguard.app, expirationreminder.com, expiryscan.com ($26/mo), trainingmatrixsoftware.com (free ≤10, $17/mo), traingrid.app ($2,490/yr) | None evidenced; community answer is spreadsheet adequate <30 staff (firsthr 2026-04-21; r/selfhosted reply) | $17-49/mo self-serve tracker | SERP/pricing + community | search-led (D) | Microsoft Q&A 2015-05-12; r/SafetyProfessionals 2024-11-15; r/InternalAudit undated; r/smallbusiness undated; firsthr 2026-04-21; live pricing pages 2026-10-13 | rejected | Crowded free/cheap space with many recent entrants, free tiers, and spreadsheet-adequacy advice; no evidenced underserved sub-niche or operating seam; spend flows to incumbents |
| H2 | `"allergen matrix" software restaurant UK pricing` — allergen matrix/Natasha's Law labelling for UK food businesses | Build/maintain 14-allergen matrix, label PPDS, keep dated versions | allergen-matrix.com (free builder; £12/mo Pro), allergenkit.co.uk (free + £9/mo Pro), fohtools.co.uk/allergens (free), foodallergens.co.uk, Allergenius (£9-17/mo), Allergenie (trial) | None evidenced; official free FSA matrix + Food Standards Scotland MenuCal endorsed by competitors themselves | £9-17/mo self-serve allergen matrix | SERP/pricing | search-led (D) | Competitor pricing/review pages 2026; allergen-matrix.com content reviewed 2026-09-22 | rejected | Free builders + official free alternatives + £9-17/mo paid tiers from ≥4 vendors with 2025-26 entrants; no wedge; competitor existence alone was not the deciding factor |
| H3 | `veterinary practice laboratory reference ranges management software` — seed re-check `vetlab-reference-list-management` | Manage lab reference ranges/reference lists per species and analyser | IDEXX VetConnect PLUS + Catalyst ranges (bundled with analyzers), vetPMS lab module, Koko Labs (lab OS), ISWE LIMS (species/breed ranges), free Merck tables | None; ranges are maintained inside incumbent analyser/PIMS/LIMS ecosystems | Standalone reference-list tool — no evidenced buyer | SERP/incumbent systems | search-led (D) | IDEXX Catalyst reference-range PDF 2024-06-20; IDEXX/vetPMS/Koko/ISWE pages 2026; Merck tables reviewed 2022-2024 | rejected | Reference-range management is embedded and bundled in incumbents plus free authoritative tables; no organic wedge or neglected sub-niche for a standalone tool; seed re-check negative |
| H4 | `fire door inspection software UK price small business` — fire door inspection/compliance records | Schedule inspections, record results, produce compliance PDFs, manage remedials | firedoorapp.co.uk (£29/mo or £1.50/door), hivesuite.co.uk (£34.99-249.99/mo), certidoor.co.uk (£99-299/mo), auroradataltd.co.uk (£50/mo, demo-led), ignistrack.com | None evidenced in shallow pass; features deep (offline, QR, PDFs, integrations, portals) | Minimal solo-dev inspection tracker — no evidenced gap | SERP/pricing | search-led (D) | Pricing/guides accessed 2026-10-13; Aurora page published 2026-08-04 | rejected | Multiple UK vendors with self-serve pricing and deep vertical features; money-moving signal real but flowing to incumbents; no evidenced underserved sub-niche |

## Observations

| ID | Observation | Buyer | Source class | Signal lens (latent only) | Reg? | Archetype | Evidence source + date | Type | Incumbent/free check | Triage | Triage reason |
|----|-------------|-------|--------------|---------------------------|------|-----------|------------------------|------|----------------------|--------|---------------|
| O1 | Many small self-serve employee-certificate trackers with free tiers and low prices | SMB owners/office managers | SERP/pricing | — | No | search-led | certtracker.app/getcerttracker.com/expiryscan.com/trainingmatrixsoftware.com/traingrid.app, accessed 2026-10-13 | vendor | free tiers exist (certtracker.app free ≤3; trainingmatrix free ≤10) | rejected | free/low-cost crowding, no wedge (H1) |
| O2 | Community advice treats spreadsheets as adequate under ~30 staff | SMB owners | Community | shadow work | No | search-led | firsthr.app 2026-04-21; r/SafetyProfessionals 2024-11-15; r/InternalAudit undated | practitioner/secondary | Excel/Sheets free | rejected | adequacy evidence (H1) |
| O3 | Allergen matrix tools are free or £9-17/mo with official free matrices available | UK food businesses | SERP/pricing | — | No | search-led | allergen-matrix.com (reviewed 2026-09-22), allergenkit.co.uk, Allergenius, fohtools.co.uk, accessed 2026-10-13 | vendor/gov | FSA matrix + MenuCal free | rejected | crowding + official alternatives (H2) |
| O4 | Vet lab reference ranges are bundled with analyzers, PIMS and LIMS | Vet practices/labs | SERP/incumbents | — | No | search-led | IDEXX VetConnect PLUS + Catalyst ranges doc 2024-06-20; vetPMS/Koko/ISWE pages 2026 | vendor | Merck tables free | rejected | incumbent-embedded (H3, seed re-check) |
| O5 | UK fire door inspection tools span £29-299/mo or per-door with deep features | Inspection firms | SERP/pricing | — | Partial (BS 8214 record-keeping) | search-led | firedoorapp.co.uk, hivesuite.co.uk, certidoor.co.uk, auroradataltd.co.uk, accessed 2026-10-13 | vendor | none free; client portals included | rejected | crowded vertical (H4) |
| O6 | Organisations pay £26k-36k/yr for humans monitoring certificate expiry and filing evidence | Housing/facilities employers | Job ads | repeated manual tracking | Yes (statutory certs) | latent candidate (not admissible) | Pinnacle Group advert posted 2026-04-24 (£32k); Warrens £31,355; Voyage Care £26k; Warburtons £30-36k (Aug 2026 aggregators) | primary (employer) | n/a | not admissible | paid staff work, not an unarticulated buyer-benefit hypothesis; no tool dissatisfaction; buyers procurement-bound |
| O7 | Audit query found large vendor field with free plans and "use a spreadsheet" peer answers | SMB owners | Community/review sites | — | No | search-led | Capterra category page 2026; TalentGuard list 2026-01-05; ExpirationReminder comparison 2026-04-23; r/selfhosted thread; accessed 2026-10-13 | vendor/practitioner | free plans (VAIRKKO, Aptien, Remindax) | (audit) | supports upheld H1 rejection |

## Bounded latent-signal search pass (v1.8.2 procedure retained)

| Lens | Source class | Focus / query | Date | Yield |
|------|--------------|---------------|------|-------|
| Repeated shadow/manual tracking work; delayed renewals | Job ads (money-already-moving: salaries) | `compliance coordinator job description "spreadsheet" "expiry dates" duties UK 2026` | 2026-10-13 | No admissible latent observations. Ads show employers paying £26k-36k for manual certificate monitoring, tracking and evidence filing (Pinnacle Group 2026-04-24; ADP BAA KPI; iomgov Concerto). This evidences paid staff work, not an unarticulated buyer-benefit hypothesis; no dissatisfaction with tools, no evidenced non-consumption, and the employers (housing/facilities) are procurement-bound, outside self-serve organic acquisition. Six-field contract not met. |

Latent observations admissible this run: **0**. No promotions on latent grounds.

## Latent six-field blocks

None admissible this run (no latent observation met the six-field contract).

## Promoted observations

None. Honest zero: no hypothesis cleared the search-intent, wedge and
self-service gates strongly enough to promote. No filler candidates were
created.

## Triage false-negative audit

| Field | Value |
|-------|-------|
| Selected rejection | H1 (employee certificate/training expiry tracking) |
| Why this one | Highest-ambiguity rejection: real money-moving category, many entrants, free tiers — crowdedness could coexist with an underserved sub-niche |
| Original reasoning | Rejected: free tiers, several recent small entrants, purpose-built niches, spreadsheet adequacy under ~30 staff, no evidenced wedge |
| Evidence checked (2026-10-13) | `reddit small business "certificate tracking" software recommendation OR alternative spreadsheet`: Capterra "Best Certification Tracking Software 2026" category (Competency Manager, LearnWorlds, Arlo, Skillsoft, BIS Safety, Totara, Sertifier, Udutu); TalentGuard list 2026-01-05 (Expiration Reminder $39/mo — "UI feels dated"; VAIRKKO free plan/$4 per user; Aptien free plan; Certemy "expensive for small businesses"); ExpirationReminder comparison 2026-04-23 (Remindax free-forever tier, 25 items); r/selfhosted thread reply: "Try using the spreadsheet software you already are familiar with. I could recommend baserow or nocodb."; CertainCert (insurance-certificate niche, 2-10 employees) |
| Outcome | **Upheld** — no unmet-need or underserved sub-niche evidence found; vendor field is deep with free and low-cost tiers; peer answers remain spreadsheets/DIY |
| Implication | Shallow triage was adequate for this observation; incumbent existence alone was not the basis — the free-tier/official-alternative/adequacy pattern was, and it survives scrutiny. No triage-depth change recommended by this audit. |

## Notes

- **Money-already-moving outcome:** live self-serve pricing observed in all
  four categories (H1 $17-79/mo; H2 £9-17/mo; H3 bundled; H4 £29-299/mo or
  per-door) — spend is real but flows to existing products. No unmet demand
  evidenced.
- **Source-class budget:** 4/4 hypotheses from non-regulatory discovery
  evidence (SERP/pricing, community, job ads); 0 regulation-derived. The
  job-ads class was deliberately searched in the latent pass. Budget
  satisfied (≥2 of 3 candidate slots non-regulatory; ≤1 regulation-derived;
  ≥1 previously underexplored non-regulatory class actually searched).
- **Range checks:** second audit query variant (`"training matrix" software
  complaints OR "too expensive" OR clunky`) returned no results and is
  recorded as no-result, not as absence of demand.
- **Research promise vs search opportunity vs commercial validation:** kept
  distinct. No live landing pages, spend, outreach or accounts were used in
  this run; nothing beyond desk research and operator-published pricing pages.
