# Issue #21 response - Pivot to SEO-first, self-service micro-SaaS discovery

- **Issue:** [#21](https://github.com/rcgeorge23/business-idea-lab/issues/21) - Pivot Business Idea Lab to SEO-first, self-service micro-SaaS discovery (opened 2026-10-10).
- **Run:** `20261013T055941Z-representative` (manual representative run under method 1.9.0; recorded with `scripts/finalize_run.py --mode representative`).
- **Date:** 2026-10-13.
- **Artefacts:** `method/VERSION` 1.9.0, `method/CHANGELOG.md`, `method/discovery.md`, `method/run-protocol.md`, `method/scorecard.md`, `method/calibration.md`, `method/evidence-policy.md`, `method/lifecycle.md`, `method/retriage.md`; `reviews/2026-10-13-method-v1.9.0-review-request.md`; `scripts/validate_repo.py`, `scripts/build_dashboard.py`, `scripts/build_review_request.py`, `scripts/finalize_run.py`; `tests/test_validate_repo.py`, `tests/test_build_dashboard.py`; `templates/*`; `AGENTS.md`, `.opencode/agent/idea-worker.md`, `scripts/prompts/lab-run.md`, `README.md`; `observations/20261013T055941Z-representative.md`; `runs/20261013T055941Z-representative/summary.md`; `ideas/housing-repairs-invoice-sor-validation/retriage-2026-10-13.md`.
- **Boundary note:** this document is a record for the owner. The worker does not approve external tests, outreach, spend or publication; the representative run performed only repository work and public, read-only web searches.

## Outcome

Method 1.9.0 implements the pivot and has been exercised once end to end. Discovery now starts from exact search queries and tasks rather than regulatory change; every new candidate must carry a required `seo_assessment` block; the scorecard schema v2 (weights 1.3.0) makes SEO-led discoverability and self-service fit prominent dimensions with three matching hard filters; the legacy ledger is preserved unchanged under a version-aware validator; and the representative run returned an honest zero promotions from four researched hypotheses, with one triage false-negative audit upheld.

## What changed (issue #21 change areas)

1. **Search-intent-first discovery.** `method/discovery.md` and `method/run-protocol.md` replace the 15-20 observation quota with a qualified shortlist of 3-5 hypotheses (fewer when weak; honest zero valid) following query -> task -> existing solutions -> neglected sub-niche -> paid self-service hypothesis. Evergreen search-led candidates (archetype D) need no contrived why-now: `why_now.strength: not-required`, judged on their `seo_assessment`. The bounded latent-signal pass, triage false-negative audit, source-class budget and money-already-moving sourcing bias are retained.
2. **Structured SEO assessment.** Schema v2 requires `seo_assessment`: exact seed queries and intent clusters; demand evidence with source and date (reported volumes only where credible); SERP landscape with named pages, types and dates; qualitative organic entry feasibility; self-service conversion mechanics; assumption-labelled conservative/modest/optimistic traffic-to-revenue scenarios; SEO risks (AI overviews/zero-click, seasonality, platform dependency); and honest unknowns with low-cost next checks. Invented volumes, rankings, CPC, trends or difficulty remain forbidden; blocked checks are recorded as unknown, never as absence or as positive evidence.
3. **Founder-fit and self-service gates with rescoring.** Schema v2 (new cards only, weights 1.3.0; threshold 65 unchanged) weights `seo_discoverability` 14 and `self_service_fit` 10, raises `founder_fit` to 10 (build complexity, support burden, maintenance, owner time) and reduces `differentiation` to 3 at idea stage. Three hard filters join the original nine: `seo_discoverable`, `self_serve_purchase`, `solo_operator_fit`. All 20 legacy cards stay frozen at schema 1 / weights 1.2.0 / method 1.8.2 and are never rewritten; the validator accepts them under a version-aware legacy branch.
4. **Actionable brief per promoted candidate.** Templates and docs now require, for every promoted candidate: user/job/problem/product with the free-alternative gap; evidenced queries/clusters and SERP/competitor URLs; organic-entry hypothesis; self-service onboarding and monetisation; minimal first version with implementation/ops/support burden; honest downside; and one cheap falsifiable experiment that defaults to low-touch, no-cold-outreach options (manual SERP audit, Search Console evidence, free utility, owner-approved landing page, opt-in waitlist, organic conversion tracking, paid self-service purchase test), labelled desk vs behavioural with a feasible horizon (`method/run-protocol.md` step 10).
5. **Execution path wired through.** Prompts, agent instructions, templates, schemas, validators, dashboard/reporting, test fixtures and the README were updated together; `python3 scripts/validate_repo.py` passes (0 errors; warnings are historic run/method records); `python3 -m unittest discover -s tests -v` passes 35 tests covering schema/version migration, legacy ledger compatibility, SEO unknown handling, gate failure semantics, `why_now: not-required`, representative mode and mixed-version dashboard rendering; `dashboard.html` was regenerated from the ledgers.

## Representative run (demonstration)

Run `20261013T055941Z-representative`, pool `observations/20261013T055941Z-representative.md`, summary `runs/20261013T055941Z-representative/summary.md`. Shortlist 4 of a 3-5 target; 4/4 non-regulatory source classes (search-intent/SERP, vendor pricing, community, job ads); 0 regulation-derived; 0 promotions; 0 admissible latent observations; 1 triage false-negative audit (upheld).

| # | Hypothesis (seed query family) | Source classes searched | Triage outcome | Principal reason |
|---|---|---|---|---|
| H1 | employee certificate/training expiry tracking | SERP/pricing, community, comparison content | rejected | free tiers and many 2025-26 entrants; community advice treats spreadsheets as adequate under ~30 staff; no evidenced underserved wedge |
| H2 | UK restaurant allergen matrix | SERP/pricing, official alternatives | rejected | free builders plus FSA blank matrix / MenuCal and GBP 9-17/mo vendors; no wedge |
| H3 | veterinary lab reference-range management (seed re-check `vetlab-reference-list-management`) | incumbent ecosystem docs | rejected, seed recorded negative | ranges bundled in IDEXX analyser/reporting, PIMS lab modules and LIMS; free Merck tables |
| H4 | fire door inspection records | SERP/pricing, vendor comparison content | rejected | GBP 29-299/mo vendors with deep vertical features (offline capture, QR, PDFs, integrations) |

Triage rejected all four on recorded negative evidence (category crowding, free/official alternatives, incumbent bundling), never on competitor existence alone. Money already moving was observed in every category (live pricing pages, per-door pricing) but flowing to existing products; the latent-signal pass (job ads, lens: repeated shadow/manual tracking work) found organisations paying GBP 26k-36k for certificate-expiry monitoring but no unarticulated buyer-benefit hypothesis meeting the six-field contract, so no latent promotion. The audit re-checked H1 against recommendation/comparison sources dated 2026-01-05 and 2026-04-23 and upheld the rejection.

## Acceptance criteria mapping

| # | Criterion | Status | Evidence |
|---|---|---|---|
| 1 | Run starts from query/task intent, not predominantly regulatory/news; returns up to 3-5 researched ideas or honest zero | Met | run began from exact queries; 4 hypotheses researched; honest zero promotions, no filler |
| 2 | Dated query/SERP evidence, named self-service path, monetisation, ops burden, competitive alternatives, labelled uncertainty per idea | Met at triage depth (no promoted candidate needed a full brief) | pool file records queries, access date 2026-10-13, named pages/prices/alternatives; `seo_assessment` schema and templates enforce the full brief; no candidate reached promotion |
| 3 | Housing-repairs SOR rejected or deprioritised on founder-fit grounds | Met | `ideas/housing-repairs-invoice-sor-validation/retriage-2026-10-13.md`: `seo_discoverable`, `self_serve_purchase` and `solo_operator_fit` all fail on recorded evidence; original card/decision unchanged |
| 4 | A narrow category can survive competitors without contrived discontinuity when a credible wedge is evidenced | Met as capability; not exercised | archetype D + cap exemption in `method/discovery.md`/`scorecard.md`; no credible wedge was evidenced in this run, so nothing was promoted |
| 5 | Missing volumes/blocked SERPs never fabricated or used as confident positive evidence | Met | no volume/ranking/CPC/trend/difficulty figures invented; unknowns and blocked checks recorded with next checks; validator enforces unknown handling; SEO evidence quality table in the summary |
| 6 | Financial estimates assumption-labelled | Met | `traffic_to_revenue_scenarios.assumptions_label` is required; no new candidate economics produced; legacy estimates untouched |
| 7 | Falsifiable low-touch next steps, not default interviews | Met | `method/run-protocol.md` step 10 default experiment menu; housing-repairs interview experiment remains proposed/ungranted; no interviews proposed in this run |
| 8 | Method version updated; docs/prompt/templates/schema/validators/tests/dashboard consistent; historic evidence auditable | Met | method 1.9.0 + changelog + review request; validator PASS; 35 tests; dashboard regenerated; all 20 legacy scorecards byte-identical and passing under the legacy branch |
| 9 | Demonstrate with >=1 dry-run/representative run; document outcomes, limitations, follow-ups; no manufactured ideas | Met | representative run recorded with run metadata, pool, summary, validation; limitations below; zero manufactured ideas |

## Source-class budget and audit

- Candidate slots: 2 of the 3 maximum must come from non-regulatory classes - in practice 4/4 hypotheses were non-regulatory; 0 were primarily regulation-derived. A previously underexplored non-regulatory class (money-already-moving job ads describing repetitive admin) was actually searched, with its no-result recorded.
- Searches outside the run's budget: none; approximately 7 lookups of the 40 allowed and no spend.
- Triage false-negative audit: exactly one triage-rejected hypothesis (H1) re-checked cheaply; outcome upheld; no change to triage depth.

## Honest limitations and unknowns

- This is a single manual pass by the same worker that wrote the method; it demonstrates mechanics and honesty, not independent evidence that the pivot finds better ideas. An owner-initiated `scripts/run.sh --dry-run` under the new prompt would add integration evidence.
- No paid rank/volume/CPC/difficulty tooling was available; demand evidence is documented SERP snapshots and public pages. The method forbids inventing metrics, so uncertainty remains labelled rather than resolved.
- No promoted candidate means the full schema-v2 scorecard and `seo_assessment` were exercised by tests and fixtures, not by a live idea card. Multi-run convergence under 1.9.0 is not yet evidenced.
- Method review `reviews/2026-10-13-method-v1.9.0-review-request.md` is `requested`; reviews for 1.7.0, 1.8.0 and 1.8.2 remain unfulfilled. Reviewer feedback could require changes under a new version.
- The owner may disagree with the v2 weights or the archetype-D exemption; both are documented in the review request for that purpose.

## What would change the conclusion

- Any of H1-H4 gaining dated evidence of an underserved sub-niche (e.g. an organic query cluster with real self-service intent and no adequate incumbent) could justify promotion through the normal funnel and a full brief.
- A `changes-requested` method review would be answered explicitly in the next run under a new version, never overwritten.
- If repeated 1.9.0 runs keep returning zero promotions from competitive categories, the next convergence review should widen intent clusters and re-check the remaining unexplored seeds (for example `grantscout-application-quality`, `prs-listing-precheck`, `payer-care-invoice-reconciliation`).

## Confirmation

No pull requests were opened or modified; no contact, spend, accounts, public-facing content or commitments were made. Repository changes (including this run and the method pivot) were committed and pushed as part of the task; the worker's shell `git commit`/`git push` remain blocked by the local permission configuration, so commits were created through the authenticated GitHub API path used for issue #20.
