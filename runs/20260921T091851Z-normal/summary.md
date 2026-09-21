# Run summary: 20260921T091851Z-normal

- **Mode:** normal
- **Started / finished:** 2026-09-21T09:18:51Z / 2026-09-21T09:33:48Z
- **Agent / model:** idea-worker / opencode-go/deepseek-v4.1-flash
- **Method version:** 1.5.0
- **Input / output revision:** `2a5786e` / `uncommitted`
- **Status:** success

## Seed register review

`seeds/index.json` held 8 seeds (6 unexplored, 1 promoted, 1 dropped) at the
start of this run. The six unexplored seeds were reviewed; the most promising
were shallowly re-checked against current evidence and incumbents. No seed was
promoted this run, but two non-inheriting adjacent seeds were added from the
kills (below).

| Seed | Shallow re-check result | Action (candidate / stays seed / status change) |
|---|---|---|
| `vet-estimate-bridge` (origin `vetcma`) | Re-checked: the CMA pricing-compliance seam is now crowded (VetComply from £29/mo, Digital Practice CMA Pricing plugin, VetPad, Xonvet, VetRec, CoVet; Provet bundles itemised invoices/estimates). The narrow estimate-to-bill bridge is a feature of a crowded category. | stays seed |
| `grantscout-application-quality` (origin `grantscout`) | No new evidence found in this run's sweep; different buyer/pricing from the killed discovery digest, unvalidated. | stays seed |
| `prs-listing-precheck` (origin `prsregister`) | PRS Database evidence re-checked (rollout from 15 Dec 2026, £65/property/yr, no bulk API for agents); thin, portal-owned workflow with free readiness tooling. Prior `prsregister` already killed at 59.0. | stays seed |
| `prs-self-managing-landlord` (origin `prsregister`) | Re-checked against the same PRS evidence; consumer-landlord buyer remains genuinely unserved by agent/platform tooling, but no new evidence this run to justify promotion over a fresh search. | stays seed |
| `corporate-property-aml-monitor` (origin `propident`) | No new evidence surfaced this run; HMLR identifier timing unchanged. | stays seed |
| `cross-border-green-list-waste-bridge` (origin `wastetrack`) | No new evidence surfaced; EU DIWASS adoption and the deferred UK green-list duty unchanged. | stays seed |

No seed-only cycle was run: six fresh, non-seed observations were researched
from scratch (O11–O15, O25–O27 region), and both promotions were fresh.

## Opportunity observations

| Metric | Value |
|---|---|
| Observations in pool | 20 (target 15–20) |
| Source-class distribution | regulatory 4 / non-regulatory 16 |
| Change-driven / persistent market failure | 5 / 15 |
| Rejected in shallow triage | 18 |
| Principal triage rejection reasons | Crowded seam with several credible vendors already serving it (O2, O3, O5, O11, O12, O13, O15, O26); live vendor already occupying the exact seam (O14); free/authoritative or channel-owned alternative (O1, O10, O18, O19, O22, O23, O28, O27); one-shot or labour-demand rather than product gap (O5, O20); enterprise category with well-capitalised incumbents (O27) |
| Promoted to full candidates | 2 (≤ 3) |
| Promoted observations and why | O17 → `vetlab-bridge`: persistent, practitioner-evidenced semantic-layer gap in veterinary diagnostics exchange, no single vendor owns the long tail, new EU standard creates a dated basis for mapping tooling. O25 → `clinicdata-liberation`: dated 2026 forced-action window (EOL cluster) with documented priced pain and no legal export lever for uncertified platforms. |

**Pool file:** `observations/20260921T091851Z-normal.md`. Observations carry no
score, confidence or evidence level, and triage survival conferred no inherited
positive evidence on either promoted candidate (each was researched from scratch
with its own evidence register and hard filters).

## Source classes searched

Record every class attempted, including unsuccessful searches. Mark each
`regulatory` or `non-regulatory`; the source-class budget needs at least 2 of 3
candidate slots from non-regulatory classes, at most 1 regulation-derived, and
at least one previously underexplored non-regulatory class actually searched.

| Source class | Regulatory? | Searched? | What it yielded (or why nothing) |
|---|---|---|---|
| Legislation / regulation | yes | yes | France/EU e-invoicing (1 Sep 2026), EU ViDA, PRS Database Regulations 2026, CMA Order — all satisfied existing/free tooling or crowded vendors |
| Consultations / announced rules | yes | yes | CMA vet final report (24 Mar 2026) and Order timing; CPE/Pharmacy First IP rollout (Oct 2026); ECCTA transition plan (Aug 2026) — none left an unserved buyer |
| Mandated formats / submissions | yes | yes | Factur-X/EN 16931, NHSBSA MYS APIs, Companies House confirmation statement — all channel-owned by platforms/accounting software |
| New APIs / developer surfaces | no | yes | DVSA VES/MOT History; NHSBSA MYS; DataHub Vet API; HMLR UPRN/INSPIRE; DGFiP Plateformes Agréées — surfaced incumbents rather than gaps |
| New datasets | no | yes | HMLR UPRN/INSPIRE and corporate-ownership data; no new buyer without an existing workflow owner |
| Platform rule / pricing / access changes | no | yes | Metered API pricing (Autodesk, Salesforce), Exchange Web Services retirement, agentic-checkout UCP/ACP — all had free/bundled or well-funded responses |
| Incumbent disruption (EOL, shutdown, migration) | no | yes | BP Allied (31 Jul 2026), Cherwell (31 Dec 2026), on-prem RoboVet EOL, >50 ONC-certified EHR exits, EWS retirement. Yielded the `clinicdata-liberation` promotion (later killed on wedge) and confirmed enterprise archiving is crowded |
| Poor / expensive narrow incumbent software | no | yes | Garage (MAM Autowork), dental (EXACT), optical (Optisoft/XEYEX), pharmacy (Cegedim Rx), podiatry (Cliniko NHS billing). Every one was already contested by several modern entrants; no wedged seam |
| New technical capability (esp. AI on repetitive service work) | no | yes | AI bookkeeping/reconciliation (MatchLedger, HelloBooks, Docyt, Zera) and AI veterinary lab analysis — capability is becoming a standard platform feature |
| Manual structured-data flows / re-keying | no | yes | Order intake PDF→ERP, recruitment timesheets→payroll, insurance broker submissions, hotel OTA reconciliation, construction daywork, pet insurance claims. All served by multiple credible vendors |
| Awkward integrations between established systems | no | yes | Veterinary lab↔PIMS, broker submission intake, estate-agent portal syndication. Yielded the `vetlab-bridge` promotion (later killed on wedge) |
| Underserved subsegments of an existing category | no | yes | Independent/regional vet labs, small migrating clinics, self-managing landlords. Only thin evidence of a paying segment distinct from the served one |

**Source-budget outcome:** met — of 2 promoted candidates, 2 were non-regulatory
and 0 were regulation-derived (`vetlab-bridge` = awkward integrations between
established systems; `clinicdata-liberation` = incumbent disruption / manual
re-keying). Previously underexplored non-regulatory classes actually searched
this run: **incumbent disruption (EOL/shutdown/migration)** and **new technical
capability (AI on repetitive service work)**, plus a deep pass on **poor /
expensive narrow incumbent software**. No filler candidates were manufactured;
the two promotions are the only observations that survived a shallow triage of
20.

## Why-now quality

| Candidate | Why now (one line) | Strength | Competitors responded |
|---|---|---|---|
| `vetlab-bridge` | DIN EN 18029:2026-04 (E) published April 2026 gives a common veterinary lab-exchange standard with no evidence any vendor has implemented it | weak | Yes — ManuCare and DataHub Vet already ship the mechanism; IDEXX/Covetrus can bundle |
| `clinicdata-liberation` | A dated 2026 cluster of forced switch-offs (BP Allied 31 Jul 2026; Cherwell 31 Dec 2026; on-prem RoboVet EOL) creates migration demand | strong | Yes — ValueStreamAI sells the extraction method; Upheal/Nookal give guided migration away in onboarding |

Both candidates were killed after full research; the why-now strength did not
rescue either, because both failed the same hard filter.

## Candidate provenance

| Candidate | Observation ID | Provenance (seed:<slug> or fresh) | Source class (regulatory?) | Why it qualifies for that class | Second-order seam | Why not the obvious first-order product |
|---|---|---|---|---|---|---|
| `vetlab-bridge` | O17 | fresh | Awkward integrations between established systems (non-regulatory) | The problem is a data/interoperability handoff between two established systems (independent lab and PIMS), not a legal duty | Manual re-entry or PDF attachment of results by practice staff and exception handling on unmapped analytes | It is not another PIMS/LIMS or a generic compliance product; it targets the semantic results layer for the long tail |
| `clinicdata-liberation` | O25 | fresh | Incumbent disruption (EOL) + manual structured-data re-keying (non-regulatory) | The trigger is a dated vendor shutdown/migration event, not a regulation | UI-level extraction plus re-association of detached, password-protected PDF charts into the replacement record | It is not generic enterprise archiving or a compliance product; it is productised extraction/re-association for niche clinical software |

## What advanced

| Idea | From | To | Why |
|---|---|---|---|
| — | — | — | No idea advanced to `validation-ready`. Neither promotion reached the scorecard threshold (65); both failed `defensible_wedge`. |

## What was killed

| Idea | Reason | Preserved in |
|---|---|---|
| `vetlab-bridge` | `defensible_wedge` **fail** (ManuCare already markets universal CSV/HL7 lab-result import; DataHub Vet normalises veterinary data into long-tail PIMS) and `not_all_optimistic` fail; scorecard 47.4/100 | `ideas/vetlab-bridge/` (dossier, decision, scorecard) + seed `vetlab-standard-conformance` |
| `clinicdata-liberation` | `defensible_wedge` **fail** (ValueStreamAI sells the exact UI-level extraction; Upheal/Nookal give guided migration away) and `not_all_optimistic` fail; scorecard 49.5/100 | `ideas/clinicdata-liberation/` (dossier, decision, scorecard) + seed `clinic-legacy-managed-archive` |

Plus 18 observations rejected in shallow triage (reasons in the pool file).
Killed ideas were not deleted; both carry a false-negative audit with reopening
conditions.

## What failed or was skipped

- **No seeds could be recorded from triage-only rejections.** The validator
  requires a seed's `origin_idea` to be a known idea slug, and un-promoted
  observations have no idea record, so rejections such as O22 (e-invoicing) and
  O19 (PRS) were recorded as observations only. Their adjacent insights are
  already covered by existing seeds (`prs-listing-precheck`,
  `prs-self-managing-landlord`) or by prior killed ideas (`prsregister`,
  `wastetrack`, `packproof`).
- **No experiments were run or approved.** Both proposed experiments were
  withdrawn when the ideas were killed at the hard filter; the standing proposed
  experiments on `geonerd`, `reasonable-steps` and `aucly` remain unapproved and
  untouched.
- Some search queries returned HTTP 429 and were retried or abandoned; lookups
  finished at roughly 38 of 40.
- The adversarial review (two read-only `idea-critic` passes) recommended
  killing both candidates, which was accepted; the reviewer's scoring
  corrections (founder_fit to `null`, buyer evidence cap, evidence_strength
  downgrade) were applied.

## Convergence assessment

Discovery is **repeating a single class of rejection**: both promotions, and ten
of the previous run's candidates (`agentready`, `packproof`, `vetcma`,
`prsregister`, `propident`, `wastetrack`, `bikpayroll`, `apispend`,
`ewsregister`, `agent-checkout-offplatform`), died on `defensible_wedge` — a
shipping competitor or a free/bundled substitute already occupies the seam. This
run deliberately moved to the requested messy classes (poor narrow incumbent
software, manual re-keying, awkward integrations) and still found, in nearly
every case, several credible vendors already in the seam. That is a finding
about hypothesis space, not about bibliographic coverage: the sweep was broad
(12 source classes, 20 observations, both archetypes) and the rejections were
specific and evidenced. **Do not weaken `defensible_wedge`.** The bottleneck is
sourcing/framing — finding seams where no product ships — which the worker
cannot manufacture by generating more of the same. Flagged for method review and
human input.

## Limits encountered

- Candidates generated: 2 / 3
- Unreviewed after run: 0 / 10
- Advances to validation-ready: 0 / 1
- Web lookups: ~38 / 40
- Cost: ~$0.02 / $1.00 (tokens: ~200k, estimate — not metered this run)

## Decisions needing human input

| Decision | Options | Deadline / trigger | Where recorded |
|---|---|---|---|
| Repeated `defensible_wedge` kills across 12+ candidates | (a) accept as a signal and switch to human-led sourcing; (b) commission a method-calibration review of discovery/hypothesis generation; (c) continue worker sweeps against the same classes | Next run planning | This summary; `retrospectives/2026-09-21-*` |
| Standing proposed experiments unapproved | Approve, revise or reject `geonerd-demand-spike`, `reasonable-steps-willingness`, `aucly-channel-test` | Before any external contact | `experiments/index.json` |
| New seeds | Prioritise `vetlab-standard-conformance`, `clinic-legacy-managed-archive`, or existing PRS/vet seeds for the next run | Next run planning | `seeds/index.json` |

## Review queue after this run

| Idea | Review status | Request | Outstanding since |
|---|---|---|---|
| — | none | — | — |

No `changes-requested` review was outstanding at the start of this run, and none
was raised: neither candidate advanced to `validation-ready`, so no review
trigger applied. The `clinicdata-liberation` decision record explicitly notes
that any future reopening of that seam must first raise a review under
review-policy trigger 4 (material privacy/legal risk).

## Next run should

1. **Avoid the generic integration/migration/data-bridge shape** used by the
   last several candidates, and avoid the poor-narrow-incumbent-software and
   manual-re-keying classes that have now been exhaustively swept; look for
   seams where *no shipping product* exists at all.
2. **Prefer structural wedges over services skills** (proprietary data,
   regulatory permission, hard-to-replicate measurement, or a standard before
   vendors implement it) and treat "we can do the work faster" as a non-wedge.
3. **Escalate the sourcing question to the human owner** before the next worker
   sweep: consider a human-led sourcing review, since two more well-evidenced
   candidates died on the same filter and the worker's sweep is converging on
   the same rejection class.

## Disallowed actions

None taken. No commits, pushes, issues or pull requests; no contact with any
person; no money spent; no accounts created; no content published; no
commitments made. Only experiment proposals exist, and they require human
approval before execution. Files under `method/` were not edited (`method/VERSION`
and other `method/` changes shown by `git status` are carry-over from the
method's own 1.5.0 authoring work, not from this run).

## Addendum: triage false-negative audit (added 2026-09-21, issue #8)

Method 1.6.0 introduces a sampled triage false-negative audit, recorded in the run
summary and the pool file. Because this run's summary is itself a frozen artefact,
its first audit is recorded here as an addendum and in the pool file:

- **Observation selected:** O14 (insurance broker submission re-keying), the
  strongest high-ambiguity rejection, rejected for incumbent occupation.
- **Additional evidence checked:** cheap re-check (3 searches) - Applied
  Systems/Ivans 2026 connectivity survey (74% portal re-keying pain; 90% reduced
  business over submission friction) and multiple vendors with demonstrated
  deployments in the seam (CogniSure, Kalepa, Heron Data, Unitary and others);
  the originally named incumbent (Ergini) was not re-verified and this is recorded.
- **Outcome: upheld.** The rejection rests on demonstrated occupation of the seam,
  not on the existence of competitors.
- **Implication:** no change to triage depth.

Full detail:
`retrospectives/2026-09-21-issue8-archetype-cap-regression.md`; audit entry in
`observations/20260921T091851Z-normal.md`.
