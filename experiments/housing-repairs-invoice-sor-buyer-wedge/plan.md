# Experiment plan: buyer-wedge interviews for provider-side invoice-to-SOR validation

- **ID:** `housing-repairs-invoice-sor-buyer-wedge`
- **Idea:** `housing-repairs-invoice-sor-validation`
- **Created:** 2026-09-22
- **Status:** proposed
- **Approval:** required (human owner) — **not granted**

## Central assumption

A UK housing provider's repairs finance function would buy a **standalone** provider-side invoice-to-SOR validation check, rather than wait for its existing housing-management suite vendor to add one.

This is the single assumption whose failure kills the idea. The desk scan (2026-09-22) found no vendor occupying the seam, so the remaining question is not "does a product exist" but "would the buyer buy it separately."

## Hypothesis

If repairs finance managers at UK housing providers are asked how they currently handle contractor invoice validation and what they would do if a standalone check were offered, then at least two of five will describe an active, budgeted intent to buy a standalone tool (or a current workaround they pay for), because the control is documented as failing and the work is currently absorbed by salaried staff.

Stated so that it can be wrong: the expected failure mode is that providers say they would rather wait for their suite vendor, or that the check is "a feature, not a product."

## Test design

- **Population / sample:** 5 repairs finance managers or Heads of Landlord Services at UK housing providers (housing associations, local-authority housing or ALMOs) of differing sizes. Deliberately include at least one provider with a recent audit finding on invoice authorisation if one can be identified from public records.
- **What participants see or do:** a 30-minute semi-structured interview. No product demo, no pricing sheet, no commitment request. Questions cover: how contractor invoices are validated today; who does it and how long it takes; whether the control has ever failed and what happened; whether they have ever evaluated or bought a tool for it; what they would do if a standalone check existed; and who would have to approve the purchase.
- **Recruitment route:** to be identified by the owner. Candidate non-paid routes: the CIH and NHF finance networks; the internal-audit partnerships that publish repairs audit findings; direct approach to providers named in published audit reports. **No contact happens until approval is recorded.**
- **Instrumentation / what is recorded:** verbatim notes per interview, with direct quotes labelled as quotes; a tally of (a) providers describing a current paid workaround, (b) providers who have evaluated a tool, (c) providers who would buy standalone, (d) providers who would wait for their suite vendor.
- **Timebox:** 21 calendar days from approval.
- **What is deliberately NOT included:** no product build, no demo, no pricing test, no pilot, no access to any provider's invoice or works-order data, no contact with contractors, no publication.

## Decision rule (fixed before running)

| Outcome | Verdict | Action |
|---|---|---|
| ≥2 of 5 providers describe an active budgeted intent to buy a standalone check, or a current paid workaround they would replace | proceed | Design a pricing/commitment test as a second experiment |
| Exactly 1 of 5, or the dominant answer is "we would wait for our suite vendor" | iterate | Re-scope toward a contractor-side or integration-partner variant, or park |
| 0 of 5, or the dominant answer is "this is a feature, not a product" | stop | Kill the idea on `defensible_wedge` and record the reason |

## Kill condition

**Stop** if 0 of 5 providers describe any budgeted intent to buy a standalone check, or if the dominant answer across the sample is that they would wait for their existing housing-management vendor to add the feature. Either result means the seam is a feature of an incumbent suite rather than a standalone product, which is a `defensible_wedge` failure.

## Cost bound

- Money: GBP 0
- Human hours: 12
- Calendar days: 21

Below the 20-human-hour / GBP 100 review threshold, so no independent review request is required before approval.

## Risks and safeguards

- **No contact, spend or publication until `approval.granted` is true and recorded by the human owner.** The worker may only propose this experiment.
- **No personal or commercial data is collected.** The interview asks about process, not about specific invoices, contractors or individuals.
- **No provider is named in any published artefact** without explicit permission; findings are reported in aggregate.
- **The decision rule is fixed before the experiment runs** and must not be changed mid-experiment. If the rule turns out to be wrong, a new experiment is recorded rather than editing this one.
- **Negative and messy results are first-class.** A stop verdict from a well-run set of interviews is a success, not a failure.
- **The sample is small (5) and non-random.** The result is directional evidence about the central assumption, not market validation.

## Results

Not yet run. To be filled in by the human owner or transcribed verbatim from owner-supplied material, with dates, what actually happened, the numbers the decision rule needs, anything that contradicted expectations, and raw artefacts or links to them.
