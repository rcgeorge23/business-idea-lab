# Latent-opportunity false-negative audit (issue #16)

- **Run:** 20260922T072821Z-normal (LAB_RUN_ID unset; run id is the UTC timestamp)
- **Date:** 2026-09-22
- **Method:** 1.7.0 (latent-opportunity route added under issue #16)
- **Scope:** every documented idea (19), every seed (12), and the triage rejections
  recorded in the three observation pools, audited retrospectively for possible
  false negatives under the new latent-opportunity lens.

## What this audit is and is not

This is a **retrospective review**, not an automatic resurrection exercise. For each
potentially affected case it records the original decision and the evidence at the
time, what latent buyer benefit or changed capability may have been missed, any new
dated evidence available now, the current substitute and incumbent response, whether
a cheap behavioural test is possible, and a **keep-closed / investigate /
propose-reopening** decision with reasons.

Original kill and triage decisions and their citations are preserved. No historical
score, evidence level or hard-filter result is changed. A case that merits further
work would need a **new dated reassessment** and the ordinary review and lifecycle
gates; the latent route confers no automatic score or validation status.

The audit explicitly revisits ideas rejected because **no customer articulated the
need**, **no obvious pain statement existed**, or **competitors appeared to cover
only the old workflow** — the three patterns the latent route is designed to catch.

## Summary of outcomes

| Outcome | Count | Cases |
| --- | --- | --- |
| Keep closed | 17 | shiftswap, wonkybox, grantscout, agentready, packproof, vetcma, prsregister, propident, wastetrack, bikpayroll, apispend, ewsregister, agent-checkout-offplatform, vetlab-bridge, clinicdata-liberation, O10 HMLR, O16 clinic archive |
| Investigate (no reopening) | 3 | geonerd, reasonable-steps, aucly (all already parked with proposed experiments) |
| Propose reopening | 0 | — |
| Latent-specific re-read (no change) | 2 | vetlab-en18029-conformance (L1 calibration example), O20 validation service |

**No idea is reopened by this audit.** The latent route changes where observations
come from, not how they are scored; every case below fails on grounds the latent
lens does not touch (occupied seam, absent buyer, one-shot economics, network
effects, or hostile category margins).

## Killed ideas (15)

### shiftswap — keep closed
- **Original decision (2026-09-20, run 20260920T210550Z-normal):** killed, 44.2,
  Plausible. Hard-filter failures on non-paid distribution, defensible wedge,
  network effects, margins and all-optimistic viability.
- **Latent lens:** the latent route asks whether a buyer might value a capability
  they have not requested. ShiftSwap's problem is not unarticulated — venues and
  staff both articulate the pain — it is that the function is given away inside
  rota tools venues already own and the model needs two-sided density before value
  exists.
- **New evidence:** none gathered; no dated change to the rota-tool landscape.
- **Substitute / incumbent response:** existing rota tools bundle the function.
- **Cheap behavioural test possible?** Yes in principle, but it would test a
  proposition the latent route does not rescue (network effects).
- **Decision:** keep closed. The latent route cannot lift a
  `no_network_effects_needed` failure.

### wonkybox — keep closed
- **Original decision:** killed, 36.8, Plausible. Oddbox loss-making at ~GBP 27m
  revenue as the anchor; same filter failures as shiftswap.
- **Latent lens:** consumer food-waste pain is articulated, not latent; the failure
  is category economics, not unarticulated demand.
- **New evidence:** none; the false-negative audit response
  (reviews/2026-09-21-false-negative-audit-wonkybox-chatgpt.md, ChatGPT/GPT-5.6 Sol,
  2026-09-21) upheld the kill and set a reopening condition requiring independently
  verifiable small-scale economics plus credible repeat purchase/retention and a
  plausible low-paid-acquisition route, evaluated as a **new proposition**.
- **Decision:** keep closed. The latent route does not address the recorded
  reopening condition.

### grantscout — keep closed
- **Original decision:** killed, 55.8, Plausible. Veto on defensible_wedge: GovOwed
  occupies the flat-fee wedge and GOV.UK "Find a grant" provides free authoritative
  discovery. Adjacent seed grantscout-application-quality recorded.
- **Latent lens:** the surviving observation (application quality / win rate) is
  already captured as a seed and is a **different service idea**, not a latent
  benefit the buyer failed to articulate.
- **New evidence:** none.
- **Decision:** keep closed; the seed remains the correct home for the surviving
  observation.

### agentready — keep closed
- **Original decision:** killed, 49.0, Plausible. Discontinuity real but captured by
  the incumbents who created it; readiness becoming a standard free platform
  capability. Seed agent-checkout-offplatform recorded.
- **Latent lens:** the off-platform segment is the latent-adjacent question, and it
  is already a seed; the seed's own check (do off-platform merchants pay a third
  party with a non-paid route?) is the right next step, not a reopening.
- **New evidence:** none.
- **Decision:** keep closed; seed remains unexplored.

### packproof — keep closed
- **Original decision:** killed, 53.0, Plausible. Real deadline attracted a complete
  competitive field; fragmented expensive buyer; standard feature set; UK incumbent
  anchors GBP 49/mo. Seed uk-epr-small-producer-tooling recorded (later dropped).
- **Latent lens:** packaging-compliance pain is articulated and the field is
  complete; nothing unarticulated survives.
- **New evidence:** none.
- **Decision:** keep closed.

### vetcma — keep closed
- **Original decision:** killed, 61.0, Plausible. defensible_wedge fail — VetGuard
  GBP 49/mo, pricebook.vet free, vetcompliance.co.uk free scanner, Vetstoria,
  Provet. Only unserved sub-job (estimate-to-bill bridge) too small; seed
  vet-estimate-bridge recorded.
- **Latent lens:** the estimate-to-bill bridge is the latent-adjacent observation and
  is already a seed.
- **New evidence:** none.
- **Decision:** keep closed; seed remains unexplored.

### prsregister — keep closed
- **Original decision:** killed, 59.0, Plausible. defensible_wedge fail — register
  free via GOV.UK, Lettable GBP 19/mo, Goodlord/Fixflo/OpenRent/Landlord Vision/
  Homelet own the agent workflow; the no-bulk-upload/API gap is a feature incumbents
  can add. Seed prs-listing-precheck recorded.
- **Latent lens:** the pre-check observation is already a seed.
- **New evidence:** none.
- **Decision:** keep closed.

### propident — keep closed
- **Original decision:** killed, 49.0, Plausible. defensible_wedge fail —
  identifiers lower cost for everyone, CCOD index already mirrored and sold at
  GBP 1.00/title, data is OGL; buyer clarity and willingness to pay unproven; the
  future AML monitoring job is speculative and enterprise-held.
- **Latent lens:** the future AML monitoring job is the latent-adjacent question, but
  it is speculative and enterprise-held; the HMLR contractual-control dataset
  opportunity was separately captured as the seed land-control-data-intelligence.
- **New evidence:** none.
- **Decision:** keep closed; the seed is the correct home.

### wastetrack — keep closed
- **Original decision:** killed, 58.9, Plausible. Receiver-side opportunity already
  served by a populated government-recognised provider market with free options and
  bundled weighbridge/waste-management systems. Cross-border green-list/DIWASS gap
  preserved as seed cross-border-green-list-waste-bridge.
- **Latent lens:** the cross-border gap is already a seed.
- **New evidence:** none.
- **Decision:** keep closed.

### bikpayroll — keep closed
- **Original decision:** killed, 50.5, Plausible. Exact seam productised by Zhoosh
  Benefits; multiple credible platforms (The Electric Car Scheme, Zest); providers
  partly self-supply (Bupa/Vitality/AXA). Desk-only incumbent-capability scan
  completed (experiments/bikpayroll-incumbent-capability/results.md).
- **Latent lens:** the pain is articulated (payroll benefit administration) and the
  seam is occupied.
- **New evidence:** none.
- **Decision:** keep closed.

### apispend — keep closed
- **Original decision:** killed, 40.0, Plausible. defensible_wedge fail — standard
  API-gateway/FinOps functionality with at least five vendors; no buyer/willingness-
  to-pay/channel/margin evidence.
- **Latent lens:** the failure is absent buyer evidence, which the latent route
  explicitly cannot supply ("the buyer does not know they need it yet" is never a
  substitute for evidence).
- **New evidence:** none.
- **Decision:** keep closed.

### ewsregister — keep closed
- **Original decision:** killed, 44.6, Plausible. defensible_wedge fail — free
  authoritative Microsoft EWS usage report plus tenant controls; residual work is
  one-shot migration services served by MSPs/consultancies; temporary market
  expiring mid-2027.
- **Latent lens:** the durable post-migration job is the latent-adjacent question,
  but no evidence a named MSP segment pays today for third-party EWS discovery.
- **New evidence:** none.
- **Decision:** keep closed.

### agent-checkout-offplatform — keep closed
- **Original decision:** killed, 49.2, Plausible. defensible_wedge fail — off-platform
  gap served by hosted UCP hubs, platform/middleware vendors, an open-source Shopify
  proxy and commerce-integration agencies; services-heavy with continuous spec
  maintenance.
- **Latent lens:** the off-platform merchant question is already the seed
  agent-checkout-offplatform.
- **New evidence:** none.
- **Decision:** keep closed; seed remains unexplored.

### vetlab-bridge — keep closed
- **Original decision:** killed, 47.4, Plausible. defensible_wedge fails — ManuCare
  already markets universal lab-result import, DataHub Vet normalises PIMS data;
  not_all_optimistic also fails; why-now weak (a standard not a mandate); IDEXX can
  bundle at no incremental fee.
- **Latent lens:** the latent route does not rescue a standard that is not a mandate
  and a seam an incumbent can bundle free.
- **New evidence:** none.
- **Decision:** keep closed.

### clinicdata-liberation — keep closed
- **Original decision:** killed, 49.5, Plausible. defensible_wedge fails —
  ValueStreamAI already sells the exact UI-level extraction method and receiving
  vendors give an adequate substitute free in onboarding; not_all_optimistic also
  fails; buyer-behaviour evidence is a competitor's published list bands (inferred
  budget capped at 2); documented database-backup alternative for at least one EOL
  system.
- **Latent lens:** the small-clinic archive question is already the seed
  clinic-legacy-managed-archive, whose own open question (who pays at small-clinic
  tier?) remains unanswered.
- **New evidence:** none.
- **Decision:** keep closed; seed remains unexplored.

## Parked ideas (3) — investigate, no reopening

### geonerd — investigate (already parked with a proposed experiment)
- **Original decision:** rescored 65.3 -> 49.5 under method 1.1.0, moved down to
  adversarially-researched, Promising, review approved. Experiment
  geonerd-demand-spike proposed, approval not granted.
- **Latent lens:** AI-assistant visibility is a change-driven discontinuity, not a
  latent benefit; the parked state and the proposed demand experiment are the
  correct route.
- **New evidence:** none gathered this audit.
- **Decision:** investigate via the existing proposed experiment; no reopening.

### reasonable-steps — investigate (already parked with a proposed experiment)
- **Original decision:** 54.0, adversarially-researched, Promising, review
  not-required. Experiment reasonable-steps-willingness proposed, approval not
  granted.
- **Latent lens:** the Employment Rights Act duty is a dated regulatory change, not
  a latent benefit.
- **New evidence:** none.
- **Decision:** investigate via the existing proposed experiment; no reopening.

### aucly — investigate (already parked with a proposed experiment)
- **Original decision:** 60.0, adversarially-researched, Commercial evidence,
  review not-required. Experiment aucly-channel-test proposed, approval not granted.
- **Latent lens:** Aucly is the calibration case for the evergreen-category
  treatment; the latent route does not change its score or state. Its why_now
  strength is 'absent' and its persistence thesis is the relevant question, already
  handled by the archetype-aware cap.
- **New evidence:** none.
- **Decision:** investigate via the existing proposed experiment; no reopening.

## Desk-screened idea (1) — latent-specific re-read, no change

### vetlab-en18029-conformance — keep as-is (L1 calibration example)
- **Original decision:** 44.2, desk-screened, Plausible, review not-required.
  Experiment vetlab-en18029-conformance-buyer-wedge proposed, approval not granted.
- **Latent lens:** this is the named calibration example **L1** in
  method/calibration.md — a plausible latent opportunity (UK independent vet
  practices manually re-keying lab results; DIN EN 18029:2026-04 published April
  2026 plus current document/LLM tooling makes a narrow conformance bridge newly
  buildable) that should reach a cheap test without a prior complaint. All six
  admissibility fields are present.
- **Effect of the latent route:** none on the score or state. The idea stays parked
  at desk-screened 44.2 with its proposed buyer-wedge experiment; the latent route
  does not change its score.
- **Decision:** keep as-is; the calibration example demonstrates the admit boundary.

## Seeds (12)

| Seed | Status | Latent-lens outcome |
| --- | --- | --- |
| grantscout-application-quality | unexplored | keep as seed; the surviving observation from a defensible_wedge kill |
| agent-checkout-offplatform | promoted | already promoted; no change |
| uk-epr-small-producer-tooling | dropped | keep dropped; no new dated evidence |
| vet-estimate-bridge | unexplored | keep as seed |
| prs-listing-precheck | unexplored | keep as seed |
| corporate-property-aml-monitor | unexplored | keep as seed |
| cross-border-green-list-waste-bridge | unexplored | keep as seed |
| prs-self-managing-landlord | unexplored | keep as seed |
| vetlab-standard-conformance | promoted | already promoted; no change |
| clinic-legacy-managed-archive | unexplored | keep as seed; its own open question (who pays at small-clinic tier?) is unanswered |
| vetlab-reference-list-management | unexplored | keep as seed |
| land-control-data-intelligence | unexplored | keep as seed; a "wait for the data to exist" play, not a latent-benefit play |

No seed is promoted or dropped by this audit. Seeds carry no score, confidence or
evidence level and become candidates only after fresh research from scratch.

## Triage rejections re-read under the latent lens

The three observation pools were grepped for rejections that failed because no
customer articulated the need, no obvious pain statement existed, or competitors
appeared to cover only the old workflow.

### O10 HMLR contractual control (run 20260922T060326Z-normal) — keep closed
- **Original triage:** rejected on absent evidenced buyer/problem — duty pre-launch,
  HMLR owns the submission channel, no practitioner evidence of recurring pain or
  budget.
- **Latent lens:** the submission workflow is a mandated task, not a latent benefit;
  the later published dataset is already captured as the seed
  land-control-data-intelligence.
- **Decision:** keep closed; seed is the correct home.

### O16 clinic legacy archive (run 20260922T060326Z-normal) — keep closed
- **Original triage:** rejected on demonstrated occupation plus absent evidenced
  small-clinic budget — six named enterprise/NHS archives.
- **Latent lens:** the small-clinic archive question is already the seed
  clinic-legacy-managed-archive; the latent route cannot supply the missing buyer
  evidence.
- **Decision:** keep closed; seed remains unexplored.

### O20 owner intake I1 validation service (run 20260922T060326Z-normal) — keep closed
- **Original triage:** rejected on absent evidenced problem and absent persistence
  thesis — could not establish continued paid pain despite reachable alternatives or
  a credible persistence mechanism; the intake's persistence claim is an assertion
  and does not lift the missing-why-now cap.
- **Latent lens:** this is the closest case to a latent hypothesis in the corpus (a
  founder may not articulate a need for candid validation before building), but it
  fails the six-field test: no dated observable evidence of the buyer's current
  behaviour or constraint, no concrete mechanism, and no cheap behavioural test that
  does not require outreach. The intake's own proposed test (a tightly specified
  paid pilot) is the right shape but remains unauthorised.
- **Decision:** keep closed. If the owner wants to pursue it, the correct route is
  the human-led sourcing/framing review or a proposed experiment, not a latent
  promotion.

## Conclusion

The latent-opportunity route does **not** revive any killed idea, promote any seed,
or overturn any triage rejection. Every case fails on grounds the latent lens does
not touch: an occupied seam, absent buyer evidence, one-shot economics, network
effects, or hostile category margins. The two cases that come closest to a latent
hypothesis (O20 validation service; the vetlab-en18029-conformance L1 example) are
handled correctly — one is rejected for failing the six-field test, the other is
parked with a proposed experiment and its score unchanged.

This is the expected result: the latent route is a **sourcing addition**, not a
scoring change, and the audit confirms it does not bypass `defensible_wedge` or
revive weak ideas by assertion.

## Boundaries

No commits, pushes, issues, pull requests or other publication. No contact, spend,
accounts or commitments. No experiment started. No historical score, evidence level
or hard-filter result changed. Original kill and triage decisions and their
citations preserved.
