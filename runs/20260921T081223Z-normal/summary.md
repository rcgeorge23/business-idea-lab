# Run summary — `20260921T081223Z-normal`

- **Mode:** normal
- **Started / finished (UTC):** 2026-09-21T08:12:23Z / 2026-09-21T~09:10Z
- **Agent / model:** `idea-worker` / `opencode-go/deepseek-v4.1-flash`
- **Method version:** 1.3.0 (repo working tree; method not edited this run)
- **Input / output revision:** working tree with method 1.3.0 changes (uncommitted at run start); output changes listed below, not committed
- **Status:** success

## Seed register review

| Seed | Shallow re-check result | Action |
|---|---|---|
| `uk-epr-small-producer-tooling` | Real but low-burden obligation (fee £1,216 + £332 late), free GOV.UK reporting service, established compliance schemes (Valpak, ERP, Countrystyle); PRN/PERN duty contradictory across sources. Poor wedge. | **Dropped** (Outcome row appended; evidence registered under `evidence/packproof/`) |
| `corporate-property-aml-monitor` | HMLR CCOD mirror `landregistry.company` still serves at £1/title; no evidence the Companies/Overseas identifier tables have shipped. Prior `propident` defeat stands. | Kept `unexplored`; Outcome row appended with the no-change reason |
| `grantscout-application-quality` | Not re-checked this run (lower priority than the two above) | Unchanged |
| `agent-checkout-offplatform` | Not re-checked this run | Unchanged |
| `vet-estimate-bridge` | Not re-checked this run | Unchanged |
| `prs-listing-precheck` | Not re-checked this run | Unchanged |
| `cross-border-green-list-waste-bridge` | Created this run from the `wastetrack` rejection | New seed, `unexplored` |

## Source classes searched

| Source class | Searched | Notes |
|---|---|---|
| Legislation / regulation | Yes | SI 2026/729 (digital waste tracking), SI 2026/189 (PAYE/payrolling), SI 2026/3 (ERA commencement), EPR packaging regs, ROE amendment regs |
| Consultations / announced rules | Yes | Non-surgical cosmetics licensing (no timetable); HMRC BiK policy |
| New APIs / developer surfaces | Partial | Defra report-receipt-of-waste API and approved-provider PATs; payroll RTI field specs (126→32 fields) |
| New datasets | Yes | HMLR CCOD/overseas-entities identifier release (shallow; not evidenced as shipped) |
| Platform rule / pricing / access changes | No | Not searched this run |
| Incumbent disruption | Yes | QuickBooks Practice Manager closure Feb 2027; IRIS Keytime/PTP end-of-life Apr 2026; Bokio UK exit Jun 2026; QuickBooks Desktop |
| New technical capability | No | Not searched this run |
| Manual structured-data flows | Yes | Third-party BiK data into pay runs (the `bikpayroll` seam); receiver waste-record flow |
| Poor narrow incumbents | Partial | Waste-tracking free-tier and weighbridge-bundled providers |
| Mandated formats / submissions | Yes | DWT records; RTI BiK reporting; EPR packaging data |

## Why-now quality per candidate

| Candidate | Why now (what changed) | Strength | Competitors responded |
|---|---|---|---|
| `wastetrack` | SI 2026/729 made 2026-06-24, in force 2026-10-01, mandating digital waste records within two working days for permitted operators | strong | Yes — Defra-approved list; 54–79 providers catalogued, many with free tiers |
| `bikpayroll` | Mandatory real-time payrolling of BiK from 2027-04-06 (HMRC policy 2026-07-13; SI 2026/189 made 2026-09-14) | strong | Partially — payroll vendors building RTI fields; no cited provider-data-ingestion product |

## Candidate provenance and second-order analysis

| Candidate | Provenance | Second-order seam | Why not the obvious first-order product |
|---|---|---|---|
| `wastetrack` | fresh | Carrier/broker **pre-transit logging and chain-of-custody reconciliation** (producer → carrier → receiver); the candidate as framed was the receiver-side record tool | **Honest finding:** the framed product *was* first-order (record and submit), which is exactly why it died — the mandated submission is saturated. The second-order seam was identified but not adopted. |
| `bikpayroll` | fresh | Collecting, validating and reconciling **third-party benefit-provider data into each pay period** plus Class 1A NIC cash-flow | The headline product is a P11D/payroll-reporting tool; the seam is the ingestion/reconciliation layer across fleet, insurer and fuel-card data, not the tax calculation |

## What advanced

| Idea | From → to | Basis |
|---|---|---|
| `bikpayroll` | discovered → desk-screened | No hard-filter fail (worst status `unknown` with `resolve_via`); dated primary evidence for the problem; decision record written. **Not** advanced further. |

**Advances to `validation-ready`: 0.**

## What was killed

| Idea | Filter failed | Note |
|---|---|---|
| `wastetrack` | `defensible_wedge` | 54–79 approved providers incl. free tiers (`BreakerHQ` 2026-08-18; `LoadSnap`); wedge is a standard feature of an established category. Killed count 8 → 9. |

## What failed, was skipped, or was rejected pre-candidate

- **No `changes-requested` review exists**, so run-protocol step 9 was vacuous this run. The two open items (`geonerd` review v2, `shiftswap` false-negative audit) are `requested`, awaiting the reviewer/human, and were not overwritten.
- **Martyn's Law** (Terrorism (Protection of Premises) Act 2025): multiple commercial products plus free Home Office/ProtectUK guidance and a low-cost standard tier → rejected at novelty-check stage, not recorded as an idea.
- **Pensions dashboards**: strong 2026-10-31 deadline but enterprise/administrator-served; weak small-buyer wedge → not pursued.
- **Non-surgical cosmetics licensing**: why-now absent (no commencement timetable; repeated delay) → rejected pre-candidate.
- **Employment Rights Act 2025**: staged commencement, largely absorbed by HR SaaS → not pursued.
- **Incumbent disruption (accounting software EOL)**: real forced migrations (QuickBooks Practice Manager, IRIS Keytime/PTP, Bokio) but incumbents and migration services already target them; one-shot migration is services-heavy with a weak recurring wedge → observation, not a candidate.
- **No experiment was run** (none proposed is approved; approval is a human act). No experiment was proposed for the closest-to-threshold ideas because `geonerd` (49.5) and `aucly` (60.0) already carry proposed plans.

## Convergence assessment

Discovery is **not yet converging on less obvious opportunities**. Both candidates this run are UK mandate-driven compliance products; the strongest fresh seam (`bikpayroll`) is a decade-old workflow newly mandated, and the adversarial pass found it contested by the parties that own the data and the workflow. The `defensible_wedge` kill cluster now spans `vetcma`, `prsregister`, `propident`, `packproof`, `agentready` and `wastetrack`. The seed register gave one drop and one no-change; the fresh non-regulatory class (incumbent disruption) yielded only crowded migration events. Consistent with `retrospectives/2026-09-21-issue2-delta-review.md`, future runs should (a) search at least one non-regulatory, non-platform class, and (b) prefer second-order seams *inside* a mandate rather than the mandated submission itself.

## Limits encountered

- New candidates generated: **2 / 3**
- Unreviewed ideas after run: **0 / 10** (generation gate not triggered)
- Advances to `validation-ready`: **0 / 1**
- Web lookups: **13 / 25**
- Agent steps: **~45 / 80**
- Cost: not measurable from `raw.jsonl` (no usage events; `scripts/extract_usage.py` found 0 events); no external spend occurred, within the USD 1.00 bound by construction
- `scripts/validate_repo.py`: **PASS, 0 errors, 5 warnings** (pre-existing historical method-version warnings)
- Killed ideas: 9 (next false-negative audit due at the 10th kill)

## Decisions needing human input

| Item | What is needed |
|---|---|
| `bikpayroll-incumbent-capability` | Desk-only scan (no external contact); approval not required to start. Decide whether a future run runs it, or whether to kill `bikpayroll` on the adversarial case without spending the scan. Escalation to interviews would be a separate experiment needing approval. |
| `geonerd` review request v2 (`requested`) | Reviewer/human response; worker cannot advance `geonerd`. |
| `shiftswap` false-negative audit (`requested`) | Reviewer/human response; worker cannot close the audit. |
| Method reviews 1.1.0 / 1.2.0 / 1.3.0 (`requested`) | No responses recorded; the 1.3.0 review explicitly anticipated this run as its empirical check (recorded above). Method not edited this run. |
| Next false-negative audit | Due when the killed count reaches 10. |

## Review queue after this run

| Idea | State | Review status | Path |
|---|---|---|---|
| `geonerd` | adversarially-researched | requested | `reviews/2026-09-21-geonerd-review-request-v2.md` |
| `shiftswap` | killed | requested | `reviews/2026-09-21-false-negative-audit-request.md` |
| `wastetrack` | killed | not-required | — |
| `bikpayroll` | desk-screened | not-required | — |

## Next run should

1. Run the `bikpayroll-incumbent-capability` scan (or record a human decision to skip it) — it is the cheapest route to a `fail` or a documented gap.
2. Re-check at least one further unexplored seed, preferring `prs-listing-precheck` or `agent-checkout-offplatform`.
3. Search at least one non-regulatory, non-platform source class (new technical capability, platform rule change, poor narrow incumbent) as the retrospective proposes.
4. Avoid generating further "new mandate → submission tool" candidates unless a second-order seam inside the mandate is evidenced as unserved.

## Disallowed actions confirmation

No commits, pushes, issues, pull requests or other publication; no contact with any person; no money spent; no accounts created; no commitments made; no experiments run; `method/` not edited. No review outcome was overwritten or ignored. All changes are working-tree edits only.

## Operator note (added after the wrapper finalised the run)

The wrapper writes `run.json`, `usage.json` and `runs/index.jsonl` after this
summary is produced. The exact figures are **USD 0.008245**, 147,315 tokens
(input 37,702 / output 6,768 / reasoning 5,393) and finish time
**2026-09-21T08:21:23Z**; the authoritative values are in
`runs/20260921T081223Z-normal/run.json`. The "cost not measurable" line above
reflects mid-run observation only.
