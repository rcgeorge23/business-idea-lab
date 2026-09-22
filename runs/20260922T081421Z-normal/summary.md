# Run summary - 20260922T081421Z-normal

- **Mode:** normal
- **Run id:** 20260922T081421Z-normal (`LAB_RUN_ID` was unset, so the run id is the current UTC timestamp)
- **Started / finished:** 2026-09-22 (single working session)
- **Agent / model:** idea-worker / opencode-go/deepseek-v4.1-flash
- **Method version:** 1.7.0
- **Input revision:** 1f495ce
- **Output revision:** uncommitted
- **Status:** success (validator pass)
- **Trigger:** GitHub issue #19, "Explore narrow software opportunities for independent trades and small trade firms"

## Seed register review

| Seed | Shallow re-check result | Action |
| --- | --- | --- |
| grantscout-application-quality | Not re-checked this run (no trades relevance) | None |
| vet-estimate-bridge | Not re-checked this run (no trades relevance) | None |
| prs-listing-precheck | Not re-checked this run (no trades relevance) | None |
| corporate-property-aml-monitor | Not re-checked this run (no trades relevance) | None |
| cross-border-green-list-waste-bridge | Not re-checked this run (no trades relevance) | None |
| prs-self-managing-landlord | Not re-checked this run (no trades relevance) | None |
| clinic-legacy-managed-archive | Not re-checked this run (no trades relevance) | None |
| vetlab-reference-list-management | Not re-checked this run (no trades relevance) | None |
| land-control-data-intelligence | Not re-checked this run (no trades relevance) | None |
| agent-checkout-offplatform | Promoted seed, already an idea | None |
| vetlab-standard-conformance | Promoted seed, already an idea | None |
| uk-epr-small-producer-tooling | Dropped | None |

No seed was promoted, dropped or added. The run was a targeted issue-driven sweep, not a
seed-only cycle, and no seed covers trades, variations, certificates, heat-pump grants or
safety-check coordination.

## Opportunity observations

| Metric | Value |
| --- | --- |
| Observations in pool | 18 (target 15-20) |
| Source-class distribution | 14 non-regulatory / 4 regulatory or regulation-adjacent |
| Change-driven / persistent market failure / latent opportunity | 5 / 11 / 2 |
| Rejected in shallow triage | 18 |
| Principal triage rejection reasons | Demonstrated occupation by shipping products for the defined buyer (O1-O4, O6, O8-O15, O18); buyer mismatch (O4); one-shot economics (O7); feature-completeness complaint rather than standalone opportunity (O13); no plausible economic buyer at a viable price (O14); latent observations failing the six-field admissibility test (O16, O17) |
| Promoted to full candidates | 0 (<= 3) |
| Promoted observations and why | None. No observation survived shallow triage; zero promotions is valid and no filler was manufactured |

The pool file is `observations/20260922T081421Z-normal.md`. Observations carry no score,
confidence or evidence level, and triage survival confers no inherited positive evidence.

## Triage false-negative audit

| Field | Record |
| --- | --- |
| Observation selected | O1 - on-site variations (H1) |
| Why selected (vs other rejections) | Strongest practitioner evidence in the pool (quantified: 92% asked for out-of-scope work, 62% regularly, ~GBP 2,600/year lost, 34% unpaid) and rejected because a GBP 9.99/month incumbent appeared to occupy the seam - exactly the existence-vs-satisfaction confusion the audit tests |
| Original triage reasoning | Demonstrated occupation: a shipping product at GBP 9.99/month already implements capture + no-login acknowledgement + invoice carry-through for the defined buyer |
| Additional evidence checked | TradePlanr variations feature page; KRBR change-order article (2026-07-08); TradeDraft variation page (2026-07-25); Buildxact variations help article. No practitioner complaint found that the incumbent workflow is inadequate, too expensive or missing a step |
| Confusion tests | Existence vs satisfaction: full workflow implemented, not merely present. Feature vs solution: complete solution. Enterprise vs niche: free plan and GBP 9.99/month tier aimed at micro-firms. Claims vs capability: shipped functionality. One-shot vs recurring: variations recur and the incumbent charges monthly |
| Outcome | Upheld |
| Implication for triage depth | Adequate for this observation. Caveat: satisfaction evidence is the incumbent's own feature page, so the audit cannot rule out that micro-firms find the workflow too heavy; no practitioner evidence of that was found |

## Source classes searched

| Source class | Searched | Regulatory? | What it yielded |
| --- | --- | --- | --- |
| Legislation / regulation | Yes | Yes | CIS changes from 6 April 2026 (O5, O11, O12) - all served by accounting platforms |
| Consultations / announced rules | Yes | Yes | Nothing trades-relevant found |
| Mandated formats / submissions | Yes | Yes | MCS MID registration and BUS voucher deadlines (O3, O10) - served by CompliancePack/Payaca |
| New APIs / developer surfaces | Yes | No | Nothing trades-relevant found |
| New datasets | Yes | No | Nothing trades-relevant found |
| Platform rule / pricing / access changes | Yes | No | ServiceM8 per-job pricing, Jobber USD-first pricing (O8) - served by flat-fee competitors |
| Incumbent disruption (EOL, shutdown, migration) | Yes | No | Migration pain (O7), rapid certificate-product launches (O15) - evidence against an unserved gap |
| Poor / expensive narrow incumbent software | Yes | No | The core of the sweep: per-user pricing, certificate gating, weak offline (O1, O2, O4, O6, O8, O13, O14, O18) |
| New technical capability (esp. AI on repetitive service work) | Yes | No | AI board scanning and OCR already productised (O9) |
| Manual structured-data flows / re-keying | Yes | No | Certificate and grant documentation (O2, O3) - served |
| Awkward integrations between established systems | Yes | No | Xero/QuickBooks/FreeAgent sync is a standard feature (S11) |
| Underserved subsegments of an existing category | Yes | No | Micro-firms served by free/flat-fee plans (O14) |

**Source-budget outcome:** not applicable - zero candidates were promoted (0
regulation-derived against a limit of 1). The mandatory biased classes were all searched and
no filler was manufactured.

## Why-now quality

No candidate rows: zero candidates were promoted. Every change-driven observation had a dated
trigger (CIS 6 April 2026; MCS MIS 3005-D 2025-12-05; Ofgem BUS guidance updated 2026-09-18;
certificate-product launches 2026) and each was rejected on demonstrated occupation, not on
why-now quality.

## Candidate provenance

None - zero candidates.

## What advanced

Nothing. 0 of 1 validation-ready advances used.

## What was killed

Nothing. Ledger counts unchanged: 19 total, 0 unreviewed, 15 killed.

## What failed or was skipped

- Zero promotions; no candidate research, no adversarial pass, no experiment proposed.
- No independent practitioner evidence was found that any incumbent workflow is inadequate
  for the defined buyer; the satisfaction evidence is vendor-published.
- No trades-relevant new dataset or live consultation was found (two source classes yielded
  nothing).
- No external test, outreach or spend occurred.

## Convergence assessment

This is the **sixth consecutive all-rejection run** and the **fifth consecutive funnel run
rejecting on demonstrated occupation**. Changing the source class (schools, open banking,
trades) changed what the observations were about, not how they died. The trades sweep is
notably worse than the others: the market is not merely occupied, it is price-competitive
with free tiers, so even the quantified pain (GBP 2,600/year lost to unpaid variations) does
not create an opening. No filter was weakened and no threshold changed. The run repeats the
escalation recorded in `retrospectives/2026-09-21-issue6-convergence-review.md` and
`retrospectives/2026-09-21-issue7-funnel-review.md`: a human-led sourcing/framing review is
the recommended next step before another same-shaped sweep.

## Limits encountered

| Limit | Used |
| --- | --- |
| Candidates generated | 0 / 3 |
| Unreviewed after run | 0 / 10 |
| Advances to validation-ready | 0 / 1 |
| Web lookups | ~40 / 40 (at the cap) |
| Evidence entries | 0 |
| Cost | USD 0.00 (no model calls; desk research only) |
| Timeout | within 3600 s |

## Decisions needing human input

| Decision | Options | Deadline / trigger | Where recorded |
| --- | --- | --- | --- |
| Convergence escalation | Commission a human-led sourcing/framing review; or continue sweeps as-is; or accept the ITERATE verdict | Before another same-shaped funnel run | This summary; prior retrospectives |
| Method 1.7.0 review | Route `reviews/2026-09-22-method-v1.7.0-review-request.md` to the independent reviewer | Before treating the latent route as calibrated | `reviews/2026-09-22-method-v1.7.0-review-request.md` |
| Standing experiments | Approve, amend or decline the four proposed experiments | Before any external contact | `experiments/index.json` |

## Review queue after this run

| Idea | Review status | Request | Outstanding since |
| --- | --- | --- | --- |
| All 19 ideas | not-required or approved | - | - |
| Method 1.7.0 | requested | `reviews/2026-09-22-method-v1.7.0-review-request.md` | 2026-09-22 |

No `changes-requested` review was outstanding at the start of this run and none was created.

## Next run should

1. Not run another unchanged same-shaped funnel sweep; act on the convergence decision first.
2. Respond to the method 1.7.0 review when it lands.
3. If sweeps continue, hunt for seams where a buyer already pays for a bad workaround and
   where the incumbent is demonstrably inadequate rather than merely present.

## Confirmation

No disallowed actions were taken: no commits, pushes, issues, pull requests or other
publication; no contact with any person; no money spent; no external accounts created; no
commitments made; no experiment started; `method/` was not edited during this run; no review
outcome was overwritten or ignored. The GitHub issue itself was not modified.
