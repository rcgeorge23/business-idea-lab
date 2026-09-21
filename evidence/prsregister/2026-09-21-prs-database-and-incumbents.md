# Evidence register — PRS Database registration and marketing-compliance support (England)

- Idea: `prsregister`
- Run: `20260921T075410Z-normal`
- Date: 2026-09-21
- Register type: evidence + inference (append-only)

## Evidence (dated external sources)

| # | Source | Publisher | Date | URL | What it establishes |
|---|--------|-----------|------|-----|---------------------|
| E1 | The Private Rented Sector Database Regulations 2026 (draft, laid before Parliament) | legislation.gov.uk / MHCLG | laid 2026; page updated 18 Sep 2026; Explanatory Memorandum 8 Sep 2026 | https://www.legislation.gov.uk/ukdsi/2026/9780348286861 | Establishes the PRS Database and operator; mandatory landlord and dwelling entries; annual fee set by the operator; duty to keep entries current; agents/advertisers prohibited from marketing a relevant rental property without an active Landlord Registration Number and Property Registration Number. |
| E2 | Renters' Rights Act 2025 (c. 26) | legislation.gov.uk | Royal Assent 27 Oct 2025 | https://www.legislation.gov.uk/ukpga/2025/26 | Primary legislation; Part 2 ss.75–92 provide for the database; the Act also bans rental bidding/asking-rent publication and limits upfront rent. |
| E3 | Lettable — "the compliance operating system for letting in 2026" | Lettable | accessed 21 Sep 2026 | https://lettable.co | Competitor already selling PRS Database readiness assessment, a deadline engine and a document generator from £19/month (Solo). |
| E4 | Letting-industry coverage of the PRS Database rollout | Homelet; Property Week; The Independent Landlord; LandlordZONE; Ultralets | Aug–Sep 2026 | https://www.homelet.co.uk ; https://www.propertyweek.com ; https://theindependentlandlord.com ; https://www.landlordzone.co.uk ; https://www.ultralets.co.uk | Rollout region-by-region from 15 Dec 2026 (West Midlands first) through 14 Nov 2027; fee reported at £65 per property per year; MHCLG prototype tested with ~300 landlords; no known bulk-upload/API for agents. |
| E5 | Incumbent letting/agent software | Goodlord; Fixflo; OpenRent; Landlord Vision; Arthur; NRLA | accessed 21 Sep 2026 | https://www.goodlord.co ; https://www.fixflo.com ; https://www.openrent.co.uk ; https://www.landlordvision.co.uk | Established agents'/landlords' software with compliance/document features that can absorb registration and certificate workflows. |
| E6 | EveryGuard (operator of VetGuard) product statement | VetGuard / EveryGuard | accessed 21 Sep 2026 | https://vetguard.uk/ | States the company already builds compliance tools for "care homes, nurseries, hotels, letting agents", i.e. a multi-vertical compliance-tool factory already active in letting. |

## Inference (conclusions citing the above)

- I1 (from E1, E2): A mandatory registration and a marketing prohibition create a dated, legally enforced job for every English landlord and letting agent, rolling out from 15 Dec 2026. (confidence: high)
- I2 (from E3, E5, E6): The commercial job is already contested by a purpose-built £19/month competitor plus mainstream letting software and a multi-vertical compliance-tool operator; the underlying registration is delivered by a free government service. The wedge is not defensible. (confidence: high)
- I3 (from E4): The only structural gap reported is the absence of a bulk-upload/API for agents — a narrower integration wedge, recorded as seed `prs-listing-precheck`. (confidence: medium)

## Assumptions (falsifiable, not evidence)

- A1: Letting agents will pay for a separate tool rather than use their existing software or the free GOV.UK service. Falsified by agent outreach showing bundling already satisfies them.
- A2: Trade bodies (Propertymark/ARLA, NRLA) provide an unpaid distribution route. Unverified.

## Unresolved

- Whether the operator will expose an API for agents at launch; if it does, the bulk-integration seed weakens.
