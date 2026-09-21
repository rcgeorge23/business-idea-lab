# Issue #7 post-run review: opportunity-observation funnel

- **Run:** `20260921T091851Z-normal` (method 1.5.0)
- **Date:** 2026-09-21
- **Cost:** USD 0.016822 (bound 1.00); ~15 minutes; web lookups ~38/40
- **Outcome:** 20 observations, 18 rejected in shallow triage, 2 promoted, both
  killed (`defensible_wedge` + `not_all_optimistic`), 0 advances
- **Pool:** `observations/20260921T091851Z-normal.md`
- **Summary:** `runs/20260921T091851Z-normal/summary.md`
- **Kills:** `vetlab-bridge` 47.4/100 (kill #14), `clinicdata-liberation`
  49.5/100 (kill #15)

This is the issue #7 review of whether breadth-before-depth improved discovery.
It changes no scoring rule. The kill-#15 false-negative audit obligation was
raised separately for `wonkybox`
(`reviews/2026-09-21-false-negative-audit-request-wonkybox.md`).

## Candidate outcomes

| Candidate | Obs | Source class (reg.) | Provenance | Why-now | Result |
|---|---|---|---|---|---|
| `vetlab-bridge` | O17 | Awkward integrations (non-reg.) | fresh | weak (DIN EN 18029 Apr 2026) | killed on `defensible_wedge` (ManuCare, DataHub Vet); 47.4 |
| `clinicdata-liberation` | O25 | Incumbent EOL + re-keying (non-reg.) | fresh | strong (2026 EOL cluster) | killed on `defensible_wedge` (ValueStreamAI, receiving-vendor migration); 49.5 |

Source-budget outcome: met - 2/2 promotions non-regulatory, 0
regulation-derived; previously underexplored classes searched (incumbent
disruption/EOL; new technical capability; deep pass on poor narrow incumbent
software).

## Answers to the issue's post-run questions

1. **Did 15-20 observations materially broaden the hypothesis space?** Yes. The
   pool covered 12 source classes and 17 distinct problem areas, most of which
   had never been swept (garage/dental/optical/pharmacy incumbents, construction
   daywork, manufacturer order intake, recruitment timesheets, hotel OTA
   reconciliation, conveyancing admin, enterprise archiving). Both promotions
   came from seams not previously examined. Breadth was real, not cosmetic.
2. **Did persistent-market-failure sourcing uncover different opportunities?**
   Different subject matter, same rejection class. Persistent observations (15
   of 20) produced the niche-incumbent and back-office workflows the issue asked
   for, and forced explicit "why does this persist?" answers (market too small,
   incumbents bundling the job, channel ownership). But every one of those
   workflows already had several credible vendors in it.
3. **Did shallow triage eliminate obvious incumbent-captured ideas cheaply?**
   Yes. 18 of 20 observations were rejected before full research with cited
   competitor checks and recorded reasons, at roughly one-tenth of a normal
   deep-research run's cost in the same session. The triage reasons in the pool
   are specific (named vendors, pricing, free alternatives), not impressions.
4. **Were the promoted candidates stronger than those from previous runs?**
   Not demonstrably. 47.4 and 49.5 sit between the previous run's 40.0/44.6/49.2
   and the earlier parked ideas; both died on the same filter with named
   competitors. On this single run, breadth did not raise candidate quality.
5. **Did breadth reduce or merely postpone `defensible_wedge` failures?**
   Mostly postpone. Twenty observations narrowed to two promotions, and both
   then failed the same filter. Breadth changed which seams were examined, not
   whether shipping competitors already occupied them.
6. **Did the observation stage become superficial or noisy at this volume?**
   No. Each row carries a dated source, evidence type, an incumbent/free
   alternative check and a triage reason; nothing was promoted on one weak
   source. Caveat: several rows rest on a single vendor or practitioner source,
   and HTTP 429 failures truncated some searches - acceptable for triage, not
   for candidates (candidates were researched from scratch).
7. **Is 15-20 the appropriate pool size?** Yes, for now. Twenty observations plus
   two full candidates fitted comfortably in ~15 minutes and 38 lookups. The
   ceiling did not feel binding; increasing it would dilute evidence per row and
   squeeze the lookup budget without addressing the binding constraint.
8. **Retain, adjust or revert the funnel?** Retain unchanged. The funnel did
   exactly what it was designed to do - broaden sourcing, make triage explicit,
   stop early deep research on obvious dead ends - at negligible cost. No
   template, limit or size change is proposed.
9. **Which source classes look most productive for a small bootstrapped
   business?** In this run: incumbent disruption / EOL-migration and awkward
   integrations between established systems produced the only promotions;
   practitioner evidence (forums, reviews, support threads, job ads) was the
   most useful evidence type for triage. Poor narrow incumbent software was the
   *most crowded* class - every incumbent examined already had several modern
   entrants. Keep mandatory coverage of all three but weight the next sweep
   toward EOL/migration seams and practitioner complaint evidence.
10. **Any evidence that scoring or hard filters need review?** None. Both kills
    were evidenced; neither candidate approached the threshold; scores in the
    40s reflect genuine gaps, not scoring artifacts. The bottleneck remains
    discovery/sourcing - finding seams where no product ships - which is a
    finding to escalate, not a reason to weaken `defensible_wedge`. One honest
    tension is recorded: archetype-B candidates carry `why_now.strength:
    absent`, so the v1.2.0 cap keeps `problem_severity_frequency` and
    `differentiation` at 2; that is correct treatment under the current method,
    but it means persistent-market observations must clear the threshold on
    buyer, evidence and economics evidence alone. No change is proposed; the
    issue #7 method review has been asked to consider it.

## Verdict and status

- Funnel retained as written (method 1.5.0); no scoring, threshold, hard-filter,
  evidence-level or lifecycle change.
- The third consecutive all-`defensible_wedge` cluster is escalated to the human
  owner for a sourcing/framing review before the next worker sweep, consistent
  with the issue #4 escalation trigger.
- Method 1.5.0 review is `requested`
  (`reviews/2026-09-21-method-v1.5.0-review-request.md`); the 1.4.0 request was
  superseded while still `requested` and is retained for cumulative review.
- Validation: PASS, 0 errors; 8 warnings all explained (7 historical run method
  versions; 1 kill-audit due - the audit request above is the response).
- No external/approval-required experiment was run; `reasonable-steps-willingness`
  remains deferred (proposed, unapproved).

## Reconciliation note (added 2026-09-21, issue #8)

- Corrected review state: an independent response to the v1.4.0 request was
  subsequently received (`reviews/2026-09-21-method-v1.4.0-chatgpt.md`) and
  **approved** v1.4.0; it was not left unresolved. Method 1.5.0 superseded v1.4.0,
  and the v1.5.0 request was answered **`changes-requested`**
  (`reviews/2026-09-21-method-v1.5.0-chatgpt.md`). Method 1.6.0 implements the
  requested changes. This note corrects only the review bookkeeping; the run
  results, evidence and verdict above are unchanged.
