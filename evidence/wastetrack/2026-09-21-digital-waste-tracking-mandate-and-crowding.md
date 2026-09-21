# Evidence: Digital Waste Tracking mandate and provider crowding

- **Idea / scope:** `wastetrack`
- **Register:** evidence
- **Source:** legislation.gov.uk, GOV.UK, Defra approved-software list, provider comparison pages
- **Accessed / dated:** 2026-09-21
- **Credibility:** primary (legislation and government service pages) plus vendor claims where stated

## Claim(s) supported

- The Digital Waste Tracking (England) Regulations 2026, SI 2026/729, were made on
  24 June 2026 and come into force on 1 October 2026 in England.
- Permitted waste facility operators must keep specified information in a digital waste
  record and submit it within two working days, and must correct errors; a written-record
  fallback applies to digitally-excluded operators.
- A Defra-approved software list exists and providers must pass production approval
  tests; at least one independent comparison (18 August 2026) lists 54 providers and
  another (undated, accessed 21 September 2026) states "around 79 providers".
- Multiple providers advertise free or very low-cost offerings (IntelliWaste "free
  forever"; Simple Digital Waste Tracking free; LoadSnap £0 then from £25/mo;
  WasteBolt £17.49/mo; QWTN/WasteNote from £10-12/mo).
- Phase 2 (carriers, brokers and dealers) becomes mandatory in October 2027, so the
  wedge is not confined to the 1 October 2026 receiver deadline.

## Exact detail

- SI 2026/729: made 24 June 2026, in force 1 October 2026; fee £26/year payable by the
  operator of a permitted facility; records within two working days (excluding weekends
  and bank holidays); correction duty (reg 7); outage provisions (reg 6).
  https://www.legislation.gov.uk/uksi/2026/729/body/made
- GOV.UK digital waste tracking service: public beta from 28 April 2026; mandatory for
  receiving-site operators from October 2026 (England & Wales; January 2027 Scotland &
  NI); Phase 2 for carriers/brokers/dealers mandatory October 2027; API-first with a
  spreadsheet fallback for non-software receivers until at least October 2027. Approx
  populations: 12,000 waste site operators; 150,000 registered waste exemption holders;
  300,000 registered waste carriers, brokers and dealers.
  https://www.gov.uk/government/publications/digital-waste-tracking-service/digital-waste-tracking-service
- Defra-approved software list (providers must pass approval tests and integrate the
  report-receipt-of-waste API):
  https://www.gov.uk/government/publications/report-receipt-of-waste-choose-a-software-provider/report-receipt-of-waste-choose-a-software-provider
- Crowding: BreakerHQ, "All 54 waste tracking providers on the GOV.UK list, compared",
  18 August 2026 — https://breakerhq.co.uk/news/every-provider-compared. LoadSnap
  compare page states "there are around 79 providers on it" and lists free/low-cost
  tiers; https://www.loadsnap.co.uk/compare. WasteTrace positions as a carrier-focused
  companion at £29/vehicle/mo with "no migration, no double-keying";
  https://www.wastetrace.co.uk/. IntelliWaste advertises "free forever";
  https://www.intelliwaste.co.uk/.
- Adjacent regime: EU DIWASS (Digital Waste Shipment System), Regulation (EU) 2024/1157
  and Implementing Regulation 2025/1290, enforcement from 21 May 2026, replaces paper
  Annex VII/IB/IA for transboundary waste movements; reported adoption ~18.1% of
  ~137,000 eligible operators. https://www.diwass-status.com/. UK green-list (Article 18)
  waste tracking was explicitly deferred to a future UK DWT phase.
- Waste carrier/broker/dealer registration reform: existing registrations cease to be
  valid from 22 July 2027; permit-based system.
  https://www.freshlawblog.com/2026/08/06/waste-carriers-brokers-and-dealers-reform-what-to-expect

## Why it is credible

The mandate and service design come from primary government sources (legislation and
GOV.UK). The crowding evidence is vendor/aggregator material, so it is treated as
credible secondary for the competitive picture, not as proof of market failure; the
Defra provider list is the authoritative existence proof of a populated market.

## What it does NOT show

- It does not show what share of the 12,000 permitted sites are still unserved, nor
  whether incumbents' free tiers are loss-leaders that will reprice.
- It does not prove buyer willingness to pay a new entrant, nor margins.
- Provider counts are self-reported by comparison sites and may double-count
  consultants, weighbridge vendors or resellers.

## Links

- Used by: `ideas/wastetrack/scorecard.json#hard_filters.defensible_wedge`
- Used by: `ideas/wastetrack/scorecard.json#dimensions.differentiation`
- Used by: `seeds/cross-border-green-list-waste-bridge.md`
