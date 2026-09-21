# Evidence: PIMS API openness, per-clinic access fees and the long tail

- **Idea / scope:** `vetlab-bridge`
- **Register:** evidence
- **Source:** vetsoftwarehub.com, veterinary PIMS integration paper, Part 9 (2026)
- **Accessed / dated:** 2026-09-21
- **Credibility:** credible secondary (structured industry survey/paper)

## Claim(s) supported

- Overall PIMS API openness averages 1.95/5; no named PIMS vendor was rated 4 or 5 by integrators.
- 57% of named-PIMS practices are on-premise, where third-party access runs through a DB-layer middleware (BitWerX, AllyDVM, Covetrus Connect); 43% are cloud, where the PIMS vendor gatekeeps "sanctioned" access.
- Per-clinic access fees of $30–50/month are economically asymmetric: they filter out low-priced or early-stage integrators, which the paper calls an "equity gap" for smaller clinics.
- The bottom six PIMS by ISV satisfaction (Pulse, Impromed, Neo, Avimark, ezyVet, Cornerstone) serve roughly 79% of practices and are aggregator-owned.
- A small open/no-fee group (Instinct, NectarVet, Provet, Lupa, Digitail, VetCove) permits cheaper integration; Provet reports 150+ integration partners.

## Exact detail

- ISV satisfaction top: Instinct 4.25, Vetspire 3.70, Shepherd 3.57, NectarVet 3.50, Provet 3.27.
- ISV satisfaction bottom: Pulse 1.20, Impromed 1.44, Neo 1.86, Avimark 2.08, ezyVet 2.19, Cornerstone 2.33.
- Each lab connection is proprietary; SNOMED-CT Veterinary Extension / VeNOM exist but are rarely used operationally.

## Why it is credible

The paper publishes per-vendor ratings and a methodology-level split (on-prem vs cloud access routes) that is specific and falsifiable, rather than a vendor's own marketing claim.

## What it does NOT show

- It is a single paper, not independently replicated, and the ratings are integrity-sensitive to who responded.
- It does not show that a semantic-layer bridge is the commercially best response, nor that the long tail is addressable at low cost.
- It does not cover UK/EU-specific standards (VetXML, DIN EN 18029), which are assessed in separate entries.

## Links

- https://vetsoftwarehub.com/ (accessed 2026-09-21)
- Used by: `ideas/vetlab-bridge/scorecard.json#differentiation`
- Used by: `ideas/vetlab-bridge/decision.md`
