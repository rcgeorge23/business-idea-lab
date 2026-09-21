# Run summary — `20260921T100247Z-normal`

- **Mode:** normal
- **Started:** 2026-09-21T10:02:47Z
- **Finished:** 2026-09-21T10:10:21Z
- **Agent / model:** idea-worker / opencode-go/deepseek-v4.1-flash
- **Method version:** 1.6.0 (weights 1.2.0)
- **Input revision:** `b25fe8c`
- **Output revision:** `b25fe8c` (no commit made)
- **Status:** success

## Seed register review

The register held 10 seeds (1 dropped, 1 promoted, 8 unexplored) at the start. The index was reviewed, and the most promising unexplored seed was shallowly re-checked and then fully researched from scratch.

| Seed | Shallow re-check result | Action |
|---|---|---|
| `vetlab-standard-conformance` | Most promising: a concrete, dated trigger (DIN EN 18029:2026-04) with no vendor implementation found and a named class of implementers. Re-checked against current incumbents. | **Promoted** to full candidate `vetlab-en18029-conformance` (own evidence, filters and score; inherits nothing from `vetlab-bridge` or `vetlab-bridge`'s 47.4 kill). |
| `grantscout-application-quality` | Index-level review only; no new evidence surfaced this run bearing on win-rate/application-quality supply. | Retained `unexplored`. |
| `vet-estimate-bridge` | Index-level review only; the vet fee-transparency incumbent set from the `vetcma` kill remains the relevant competition. | Retained `unexplored`. |
| `prs-listing-precheck` | Index-level review only; PRS rollout timing unchanged from the source evidence. | Retained `unexplored`. |
| `corporate-property-aml-monitor` | Index-level review only; HMLR identifier rollout timing unchanged. | Retained `unexplored`. |
| `cross-border-green-list-waste-bridge` | Index-level review only; DIWASS adoption figure unchanged from the source evidence. | Retained `unexplored`. |
| `prs-self-managing-landlord` | Index-level review only; still a consumer (non-B2B) buyer, unresolved. | Retained `unexplored`. |
| `clinic-legacy-managed-archive` | Index-level review only; archive crowding question from the parent kill still unresolved. | Retained `unexplored`. |
| `agent-checkout-offplatform` | Already promoted in a prior run; the resulting idea was killed. | Retained `promoted`. |
| `uk-epr-small-producer-tooling` | Already dropped. | Retained `dropped`. |

This run was **not** seed-only: 17 of 18 swept observations were fresh, and the single promotion was a seed re-checked and researched from scratch.

## Opportunity observations

| Metric | Value |
|---|---|
| Observations in pool | 18 (`observations/20260921T100247Z-normal.md`) |
| Source-class distribution | regulatory/regulation-derived 5; non-regulatory 13 |
| Change-driven / persistent | 5 / 13 |
| Rejected in shallow triage | 17 |
| Principal triage rejection reasons | Credible vendors demonstrably occupying the exact proposed seam (customs extraction, MGA bordereaux, eSource→EDC, freight double-entry, holiday parks, loss adjusters, equine, schools, security, used-car data); adequate/free authoritative alternative (MTD software, BNG free calculator, farm assurance portal); buyer exclusion by threshold (CBAM); no economic buyer / platform-mediated buyer (Building Safety Act golden thread); weak sources only (equine). |
| Promoted to full candidates | 1 |
| Promoted observation and why | **O5** DIN EN 18029 / VetXML exchange — structural wedge: a standard published April 2026 *before* any vendor implementation, with a concrete operational gap (the standard explicitly excludes the required code lists) and no shipping conformance/reference-list product found. |
| Pool file | `observations/20260921T100247Z-normal.md` |

## Triage false-negative audit

| Field | Value |
|---|---|
| Observation selected | O11 — funeral director management/finance software (non-regulatory; poor/expensive narrow incumbent) |
| Why selected | Strong practitioner/problem evidence (user complaints, £12k–18k/yr incumbent pricing, a £7/funeral entrant) rejected because incumbents/entrants appeared to occupy the seam — the classic high-ambiguity rejection. |
| Original triage reasoning | Credible vendors demonstrably occupy the exact seam (case management, documents/e-signature, payments). |
| Additional evidence checked | FuneralHQ buyer's guide (2026-05-03, $250/location/mo, unlimited users/cases, QuickBooks Online), Passare (ITQlick 2026-07-12), Osiris, SRS/Tribute, PlotBox, Mortec, eFD, Funeral365, FuneraliQ+, Ensembl. |
| Outcome | **Upheld** — multiple credible vendors ship the complete seam, not just announced features. |
| Confusion tests | (1) existence vs satisfaction: dissatisfaction real but vendors actively addressing it; (2) feature vs complete solution: incumbents ship the whole case; (3) enterprise vs niche: purpose-built small-firm vendors exist; (4) vendor claims vs demonstrated capability: FuneralHQ/Passare shipping; (5) one-shot vs recurring: all subscription. |
| Implication for triage depth | First audit of this class and no overturn; triage depth adequate here. A single overturn would not have changed anything; repeated overturns would trigger a triage-depth review. |

## Source classes searched

| Source class | Regulatory? | Searched? | What it yielded |
|---|---|---|---|
| Legislation / regulation | yes | yes | CBAM SI 2026/995, MTD for ITSA thresholds, BNG duties, EUDR timing — all crowded or buyer-excluding; no promotion. |
| Consultations / announced rules | yes | yes (via prior evidence and this sweep) | Building Safety Act golden-thread duties — real, but platform-mediated buyer; not promoted. |
| Mandated formats / submissions | yes | yes | EN 18029 exchange standard (O5, promoted); EUDR DDS — crowded. |
| New APIs / developer surfaces | no | yes | Veterinary PIMS/lab APIs (closed/undocumented/fee-gated) as context for O5. |
| New datasets | no | yes | HMLR/corporate ownership context (prior evidence); nothing new this run. |
| Platform rule / pricing / access changes | no | yes | Cox Automotive terminating VINCUE MMR/KBB data access (O18) — data controlled by incumbent, crowded. |
| Incumbent disruption (EOL / shutdown / migration) | no | yes | FMS6 → FMS Connected forced migration and access restriction (O16) — incumbent-owned. |
| Poor / expensive narrow incumbent software | no | yes | Funeral (O11), holiday parks (O13), loss adjusters (O14), equine (O15), schools (O16), security (O17), farm (O12) — all occupied. |
| New technical capability (esp. AI on repetitive service work) | no | yes | Customs-broker AI document extraction (O6), clinical eSource→EDC (O9) — well-funded vendors occupy. |
| Manual structured-data flows / re-keying | no | yes | Customs entry (O6), MGA bordereaux (O8), clinical transcription (O9), freight bookings (O7) — crowded. |
| Awkward integrations between established systems | no | yes | Freight TMS/CargoWise ↔ QuickBooks (O7), farm ↔ QuickBooks (O12), school MIS/FMS (O16), security scheduling/payroll/billing (O17) — occupied. |
| Underserved subsegments | no | yes | Small subcontractors (O10), small/independent labs (O5) — O10 failed on buyer economics; O5 promoted. |
| Technical standards / interoperability (non-regulatory) | no | yes (previously underexplored) | EN 18029 / VetXML — the one promotion. |
| Practitioner / community evidence | no | yes | Reddit r/freightforwarding and r/SupplyChainLogistics (2025-10-30, 2026-03-10, 2026-04-19); user reviews for funeral/farm/equine software. |

**Source-budget outcome:** satisfied. There is 1 candidate slot used of a maximum 3; it is **non-regulatory** (technical standard / interoperability), so the requirement that at least 2 of 3 slots be non-regulatory is met with zero regulation-derived candidates (limit ≤1). At least one previously underexplored non-regulatory class — technical standards/interoperability, supported by practitioner-community evidence — was actually searched. No filler candidate was manufactured to fill slots.

## Why-now quality

| Candidate | Archetype | Why now | Strength | Persistence thesis | Competitors responded |
|---|---|---|---|---|---|
| `vetlab-en18029-conformance` | Change-driven (with persistent-underinvestment overlay) | DIN EN 18029:2026-04 (E) published April 2026, giving a common veterinary lab-exchange format for the first time. | **weak** (a standard, not a mandate; no implementation or budget evidenced) | **absent** — limb 1 (continued pain/workaround) is partially evidenced, but no credible persistence mechanism was affirmatively established; the cap is therefore **not** lifted and is not treated as a scoring bonus. | No dedicated conformance/reference-list product found; VetXML free schemas/hub and middleware (Bitwerx, Covetrus Connect) are adjacent only. |

## Candidate provenance

| Candidate | Observation ID | Provenance | Source class (regulatory?) | Why it qualifies | Second-order seam | Why not the obvious first-order product |
|---|---|---|---|---|---|---|
| `vetlab-en18029-conformance` | O5 | `seed:vetlab-standard-conformance` | Technical standard / interoperability (non-regulatory) | A structural wedge: a new standard exists before any vendor has implemented it, and the standard itself omits the code lists required for unambiguous exchange, so conformance/mapping tooling is a real implementation job with no shipping product found. | Acknowledgement-protocol and error reconciliation, plus reference-list/code-list management and mapping validation between lab-internal and exchanged codes. | A lab→PIMS results-delivery bridge is already occupied by ManuCare and DataHub Vet (parent idea `vetlab-bridge`, killed on `defensible_wedge`); selling to the implementers of the standard is the distinct seam. |

## What advanced

| Idea | From | To | Why |
|---|---|---|---|
| `vetlab-en18029-conformance` | new candidate (promoted from observation O5) | `desk-screened` | No hard-filter `fail`; at least one dated problem source; decision record written. Score 44.2/100 (below the 65 threshold), so **not** advanced to `validation-ready`. |

## What was killed

None this run.

## What failed or was skipped

- No idea reached `validation-ready`, so no review was triggered and there was no advance (0 of 1 used).
- No interviews or external tests were started: the proposed experiment is `proposed` and requires human approval.
- The desk step of the proposed experiment was not run because it sits inside the approval-gated plan; treated as not yet executed rather than as a null result.

## Convergence assessment

- 17 of 18 observations were rejected at triage, and the dominant reason remains **crowding / a credible vendor occupying the exact proposed seam** — the same pattern flagged by the issue7 funnel review and the issue6 convergence review.
- The run deliberately responded to that guidance by hunting a **structural** wedge (a standard published before vendors implement it) rather than another generic integration or data-bridge shape, and that is the single promotion.
- Still, the sweep found no second structural wedge, and the poor/expensive-narrow-incumbent and manual-re-keying classes remain exhaustively crowded. Discovery is only partially converging on less obvious opportunities; the issue6 escalation (human-led sourcing/framing review) should be considered.

## Limits encountered

| Limit | Used | Cap |
|---|---|---|
| New candidates | 1 | 3 |
| Unreviewed ideas before generation stop | 0 | 10 |
| Advances to `validation-ready` | 0 | 1 |
| Web lookups | ~30 | 40 |
| Evidence entries for the new idea | 3 | 8 |
| Agent steps | within budget | 120 |
| Cost | ≈USD 0.02 (estimate) | USD 1.00 |
| Timeout | within budget | 3600s |

## Decisions needing human input

| Decision | Options | Deadline / trigger | Where recorded |
|---|---|---|---|
| Approve the proposed buyer-wedge experiment | Approve (12 human-hours, £0, 21 days) / amend / decline | Before any external contact | `experiments/vetlab-en18029-conformance-buyer-wedge/plan.md` |
| Three standing unapproved experiments | Approve / decline each | No deadline | `experiments/index.json` (`geonerd-demand-spike`, `reasonable-steps-willingness`, `aucly-channel-test`) |
| Convergence escalation | Accept the issue6/issue7 recommendation to run a human-led sourcing/framing review before further funnel runs; or commission a method calibration; or continue sweeps as-is | Before the next run | `retrospectives/issue6-convergence-review.md`, `retrospectives/issue7-funnel-review.md` |
| Reviewer-side outstanding audit | The `wonkybox` kill-#15 false-negative audit request remains open for the reviewer; no worker obligation | Reviewer's discretion | `reviews/` request file |

## Review queue after this run

| Idea | Review status | Request | Outstanding since |
|---|---|---|---|
| `vetlab-en18029-conformance` | not-required | — | — |
| All other ideas | not-required / approved | — | — |

No `changes-requested` review existed at orientation and none is outstanding. The review-queue reconciliation file (`reviews/2026-09-21-review-queue-reconciliation.md`) continues to apply: method 1.5.0's `changes-requested` was answered by method 1.6.0, which was approved.

## Next run should

- Act on the human decision above; if the convergence escalation is accepted, do not run another same-shaped funnel sweep unchanged.
- If the buyer-wedge experiment is approved and returns a funded need, advance `vetlab-en18029-conformance` only after the gating dimensions reach ≥3 with cited evidence.
- Otherwise re-check the remaining unexplored seeds (`clinic-legacy-managed-archive`, `cross-border-green-list-waste-bridge`) from scratch, and hunt structural wedges in classes not yet swept.

## Confirmation

No disallowed actions were taken: no commits, pushes, issues or pull requests; no contact with anyone; no money spent; no accounts created; no content published; no commitments made; no experiment started (only proposed); `method/` was not edited; and no `changes-requested` review was overwritten or ignored.
