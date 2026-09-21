# Evidence: migration pain and receiving-vendor migration tooling

- **Idea / scope:** `clinicdata-liberation`
- **Register:** evidence
- **Source:** upheal.com, therapy EHR migration analysis (2026-09-01); nookal.com guided-import description (2026-06-22)
- **Accessed / dated:** 2026-09-21
- **Credibility:** vendor claim (receiving-vendor marketing) + practitioner framing

## Claim(s) supported

- Migrating out of an incumbent therapy EHR (SimplePractice) requires three separate export operations (demographics CSV, client-details CSV with a manual date range, and a data-export ZIP).
- Session notes export as PDFs rather than editable text, and chart PDFs arrive disconnected and password-protected by default.
- The workaround costs 4–5 weeks of overlap plus 10–15 hours of manual effort; guided self-serve migration tooling reduces it to 2–3 hours of setup plus an overnight import by validating, auto-matching clients and auto-attaching charts.
- Receiving vendors (Upheal, Nookal) are the parties building this tooling, i.e. the switch is a competitive acquisition channel for them.

## Exact detail

- Named pain: PDF-only notes cannot be edited or trended; disconnected charts must be manually re-associated with the right client; password protection blocks bulk processing.
- This matches the structural pattern (unstructured documents + re-association) that a productised liberation service would target.

## Why it is credible

The pain is described concretely with the exact export operations and failure modes, and it is corroborated by an independent receiving vendor (Nookal) describing the same export/load/sanity-check sequence.

## What it does NOT show

- It is written by a vendor whose product is the migration destination; inclusion of the "before" pain is a sales device.
- It does not show that a standalone third-party service can win when the receiving vendor gives guided migration away as part of onboarding.
- It does not establish pricing for third-party extraction in the UK therapy/allied-health tier.

## Links

- https://upheal.com/ (accessed 2026-09-21; article dated 2026-09-01)
- https://nookal.com/ (accessed 2026-09-21; article dated 2026-06-22)
- Used by: `ideas/clinicdata-liberation/scorecard.json#problem_severity_frequency`
- Used by: `ideas/clinicdata-liberation/scorecard.json#differentiation`
- Used by: `ideas/clinicdata-liberation/decision.md`
