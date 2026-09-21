# Evidence: veterinary interoperability structure, VetXML adoption and incumbent coverage

- **Idea / scope:** `vetlab-en18029-conformance`
- **Register:** evidence
- **Source:** Tandem Health analysis "Veterinary data integration" (tandemhealth.ai), dated 2026-08-31; VetXML consortium schema and member pages (vetxml.co.uk); VetEnvoy hub pages (vetenvoy.co.uk); esremedia veterinary billing/PIMS landscape article, 2026-07-30
- **Accessed / dated:** 2026-09-21
- **Credibility:** vendor claim (Tandem Health analysis) + credible secondary (esremedia); the consortium and hub pages are primary for membership and schema existence

## Claim(s) supported

- There are roughly 15 major PIMS in the UK/EU veterinary market with about 140 integration partners, producing on the order of 2,100 theoretical pairwise integrations.
- PIMS and laboratory APIs are described as "closed, undocumented or fee-gated", so integration is negotiated and bilateral rather than open.
- The largest players (IDEXX, Antech, Zoetis) build bilateral integrations themselves; independent and smaller laboratories sit "at the margins of integration investment".
- Existing intermediaries (Bitwerx, IDEXX DataPoint, Covetrus Connect) solve the connection and structural-mapping layers but not the semantic layer (meaning of analytes, units, reference ranges).
- VetXML publishes schemas for Lab Report (v1.4), Microchip Registration (v1.3.2) and Insurance Claim (v1.09); its member list includes Animana, Assisi, AT Veterinary Systems, Dotvet, ezOfficeSystems, Provet Cloud, Robovet, RX Works, Teleos and Vet-One.
- VetEnvoy operates a hub (LiveTime 24/7) for veterinary data exchange.
- The LIMS vendors surfaced (Zendolims, LIMS.eu) support generic HL7/XML/CSV exchange rather than a veterinary-specific conformance suite.
- No source surfaced any shipping conformance, test-fixture or reference-list-management product for EN 18029 or VetXML.

## Exact detail

- Tandem Health (2026-08-31): ~15 major PIMS × ~140 integration partners ≈ 2,100 theoretical integration pairs; APIs "closed, undocumented or fee-gated"; IDEXX/Antech/Zoetis build bilateral integrations; independent/smaller labs at the margins; Bitwerx, IDEXX DataPoint and Covetrus Connect bridge connection/structural layers only.
- VetXML consortium: schemas listed above; member list as above.
- esremedia (2026-07-30): veterinary billing/PIMS landscape including RoboVet, VetIT, Animana, ezyVet, Cornerstone, VisionVPM and Vetspace, with VetEnvoy as the exchange gateway.
- No EU or UK mandate for EN 18029 was found in any source reviewed.

## Why it is credible

The consortium and hub pages are first-party evidence of what exists and who is a member. The structural analysis is vendor-authored, so it is treated as a vendor claim rather than independent evidence of buyer demand; esremedia is a trade publication providing corroborating landscape detail. The absence of a conformance product is a negative finding from these searches, not a positive claim.

## What it does NOT show

It does not show that any PIMS, LIMS or laboratory will pay for conformance tooling, that adoption of EN 18029 is planned, or that the "2,100 integration pairs" figure translates into willingness to pay. The claim that no conformance product exists is bounded by the searches performed and could be falsified by a product not surfaced. It does not establish the size or budget of the buyer population.

## Links

- Used by: `ideas/vetlab-en18029-conformance/scorecard.json#differentiation`
- Used by: `ideas/vetlab-en18029-conformance/scorecard.json#problem_severity_frequency`
- Used by: `ideas/vetlab-en18029-conformance/scorecard.json#hard_filters`
