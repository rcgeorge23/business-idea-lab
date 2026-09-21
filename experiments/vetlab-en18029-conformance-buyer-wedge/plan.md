# Experiment plan — Buyer-wedge test for EN 18029 conformance tooling

- **Experiment id:** `vetlab-en18029-conformance-buyer-wedge`
- **Idea:** `vetlab-en18029-conformance`
- **Status:** proposed (awaiting human approval; not started)
- **Created:** 2026-09-21
- **Method version:** 1.6.0
- **Cost bound:** £0 money, 12 human-hours, 21 calendar days
- **Approval:** required; not yet granted

## Central assumption

That veterinary laboratory software and PIMS/LIMS vendors, or the laboratories themselves, will fund EN 18029 conformance and reference-list tooling **before** any mandate requires it, because the code-list gap and API fragmentation create real implementation cost.

## Why this test

The candidate's binding uncertainty is the buyer, not the technology. No shipping conformance/reference-list product was found, but that is a negative finding; it does not prove willingness to pay. The cheapest decisive test is to check what vendors already publish about EN 18029/VetXML support and to ask a small number of named implementers whether a funded need exists. If the answer is no, the idea fails `economic_buyer` and `defensible_wedge` and should be killed.

## Procedure (all steps require human approval before any external contact)

1. **Desk step (no contact, 4 hours):** check the public documentation, release notes and integration pages of the VetXML member vendors (Animana, Assisi, AT Veterinary Systems, Dotvet, ezOfficeSystems, Provet Cloud, Robovet, RX Works, Teleos, Vet-One) and of the LIMS vendors Zendolims and LIMS.eu for any EN 18029 or VetXML conformance, reference-list or mapping-validation feature. Record each finding with a date and source.
2. **Interview step (approval-gated, 8 hours):** request short interviews with five named individuals across independent laboratories and PIMS/LIMS vendors from the public VetXML member and laboratory lists. Ask: (a) does EN 18029/VetXML conformance create work you must do; (b) is anyone funded to do it now; (c) who owns that budget; (d) would you pay for a maintained reference-list and conformance toolkit, and roughly how much; (e) what would you do instead if it were not available.
3. **Record:** one evidence file per material claim; no results are to be fabricated or extrapolated. If interviews cannot be arranged, record the experiment as untested rather than as a null result.

## Pre-fixed decision rule

- **Proceed** to a paid-pilot/willingness-to-pay design iff **at least 2 of 5** interviewees name a currently funded EN 18029/VetXML conformance or reference-list need, or commit to a paid pilot at a stated price.
- **Iterate once** if exactly 1 does, or if several name the need but cannot identify a budget owner.
- **Kill** if 0 of 5 name a funded need, or if the dominant response is that no work is needed until a mandate appears.

## Kill condition

Zero of five interviewees name a funded conformance/reference-list need, or the dominant response is that nothing will be done before a mandate; or the desk step shows a shipping vendor conformance/reference-list product that adequately occupies the exact seam for the defined buyer.

## Risks and limits

- Small buyer population: the UK diagnostic-laboratories software segment is small (USD 6.35m in 2025), so even a positive answer may not support a venture.
- Vendor-authored sources are treated as weak secondary evidence.
- No external contact may occur until the human owner grants approval.
