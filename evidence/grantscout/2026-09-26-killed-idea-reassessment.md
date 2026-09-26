# Evidence: GrantScout post-kill reassessment

- **Idea / scope:** `grantscout` — matched UK government-grant discovery digest for small businesses
- **Register:** evidence + inference (append-only reassessment; original kill preserved)
- **Source:** GOV.UK grant-search service and GovOwed pricing page
- **Accessed / dated:** 2026-09-26
- **Credibility:** primary government service plus vendor claim

## Claim(s) supported

- GOV.UK continues to provide free government-grant search and eligibility filtering. The linked service remains labelled BETA, includes saved searches/notifications and application sign-in, and says more grants and functionality are planned. [S1, S2]
- GovOwed continues to advertise a free scan, a £29 one-off report, £199 for ten reports and a £499/year accountant plan, with matching, rule-level eligibility explanations, deadlines and drafted applications/repeated searches. These are current vendor offers, not verified transactions. [S3]
- The separate application-quality seed was rechecked in `runs/20260925T163230Z-normal`; Tatton and EchoGrant advertised services/prices but the review did not establish small-SME purchase volume, software gap or distribution. The seed remains distinct and non-inheriting. [S4]
- The original decision records a 62.1 total under the initial assessment. The scorecard was subsequently recalculated in commit `98c87acf` under method/weights v1.1.0: raw weighted points 53.0 across scored weight 95, yielding 55.8. The current scorecard and idea index both report 55.8; this is a later rescore, not a new 2026-09-26 rescore. [S5]

## Exact detail

- [S1] GOV.UK, Find government grants guidance: https://www.gov.uk/guidance/find-government-grants — free service purpose and search/eligibility guidance.
- [S2] Live service: https://www.find-government-grants.service.gov.uk/ — BETA label, saved searches/notifications, applications sign-in and roadmap text checked 2026-09-26.
- [S3] GovOwed pricing: https://govowed.uk/pricing — live vendor offer and listed prices checked 2026-09-26. Performance claims are vendor statements.
- [S4] `runs/20260925T163230Z-normal/summary.md`, plus the non-inheriting seed `grantscout-application-quality` — adjacent application-support research, not proof for the grant-discovery digest.
- [S5] `ideas/grantscout/decision.md` (original total 62.1); `ideas/grantscout/scorecard.json` and `ideas/index.json` (current recorded 55.8); commit `98c87acf` (re-score under method/weights 1.1.0, including hard-filter changes).

## Why it is credible

The free service is operated by GOV.UK. GovOwed’s current page directly establishes that the offer and prices are being advertised, but no sales, conversion or customer count was verified. The score reconciliation is supported by version history and current machine-readable ledger values.

## What it does NOT show

- It does not show how many SMEs use either service, GovOwed’s paid conversion/retention, or buyer satisfaction.
- Government’s roadmap does not prove that future improvements will satisfy every niche, but no specific neglected segment or paid workaround has been evidenced.
- Neither public pricing nor adviser service offers demonstrate that SMEs pay for a standalone recurring discovery digest.
- The application-quality seed is not evidence for the original discovery product and must not inherit its score.

## Reassessment (inference)

- **Buyer:** SME owners/accountants are plausible users, but a separate buyer budget for discovery is not demonstrated.
- **Problem:** grant eligibility/discovery may be time-consuming; however, the public service already supports search, eligibility, saved queries and alerts.
- **Alternatives / wedge:** GovOwed advertises the same flat-fee match/report position while the authoritative free service is improving. `defensible_wedge` remains `fail` for the broad matched digest.
- **Distribution / economics:** accountant referrals and organic acquisition remain unmeasured; public data and low-price competitors constrain recurring margins.
- **Risk / next evidence:** stale or inaccurate eligibility interpretation could undermine trust. Reopening would require a specific eligible grant segment materially missed by GOV.UK, evidence that buyers already pay for that gap, and a reachable distribution path. This desk review did not find those conditions.
- **Score history:** retain the original 62.1 in the original decision as the pre-v1.1.0 result; 55.8 is the current rescored ledger value. The scorecard is not changed by this reassessment.

## Links

- Used by: `ideas/grantscout/decision.md` (2026-09-26 reassessment and score-history clarification)
- Related prior evidence: `evidence/grantscout/2026-09-20-free-government-grant-discovery.md`; `evidence/grantscout/2026-09-20-incumbent-pricing-and-contingency.md`
