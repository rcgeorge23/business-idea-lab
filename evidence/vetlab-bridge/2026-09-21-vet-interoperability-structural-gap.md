# Evidence: structural interoperability gap in veterinary diagnostics exchange

- **Idea / scope:** `vetlab-bridge`
- **Register:** evidence
- **Source:** tandemhealth.ai, "Why veterinary software interoperability remains limited in Europe" (2026-08-31); priorknowledgeandpractice.substack.com, Dave Kincaid, three-layer interoperability model (2025-08-25)
- **Accessed / dated:** 2026-09-21 (article dates 2026-08-31 and 2025-08-25)
- **Credibility:** credible secondary (industry analysis) + practitioner (substack by an interoperability practitioner)

## Claim(s) supported

- Veterinary interoperability work has solved the **connection** and **structural** layers but not the **semantic** layer, so lab results still arrive as PDFs that staff re-enter or attach by hand.
- There is no veterinary equivalent of the European Health Data Space and no EU/UK mandate for PIMS open APIs or a standardised lab-result format.
- GDPR protects owner data, not animal clinical data, so data-portability rights do not create a legal lever for animal records.
- Bilateral integrations exist between the large reference labs (IDEXX, Antech, Zoetis) and larger PIMS only; independent/smaller labs cannot justify certified integrations.
- Practices that use specialist or regional labs "almost always" have no automated exchange.

## Exact detail

- Typical European workflow: the lab returns a PDF by email or portal; practice staff manually re-enter values or attach the PDF; transcription error risk follows.
- Middleware named: Bitwerx, IDEXX DataPoint, Covetrus Connect — described as translating the connection and structural layers but not the semantic layer.
- Proposed remedy in the practitioner model: intelligent backend translation/mapping between lab result formats and PIMS fields.
- UK XML standard VetXML is adopted by some UK PIMS vendors and insurers, but global fragmentation persists.

## Why it is credible

Two independent sources (an industry analysis and a practitioner model) converge on the same three-layer diagnosis and the same gap (semantics, not transport), and both name concrete middleware rather than making a generic complaint.

## What it does NOT show

- It does not show that practices or independent labs will pay a third party, nor at what price.
- It does not quantify the size of the affected population or the frequency of the re-entry task.
- It is not vendor-neutral primary evidence about any specific PIMS's API; it is analysis, so incumbent claims were checked separately.
- It does not establish that DataHub Vet, ManuCare or Bitwerx cannot close the semantic gap themselves.

## Links

- https://tandemhealth.ai/ (accessed 2026-09-21; article dated 2026-08-31)
- https://priorknowledgeandpractice.substack.com/ (accessed 2026-09-21; article dated 2025-08-25)
- Used by: `ideas/vetlab-bridge/scorecard.json#problem_severity_frequency`
- Used by: `ideas/vetlab-bridge/decision.md`
