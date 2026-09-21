# Review queue reconciliation

- **Prepared by:** worker
- **Date:** 2026-09-21
- **Method version:** 1.3.0
- **Context:** issue #5, after the `bikpayroll-incumbent-capability` desk scan
- **Purpose:** reconcile the accumulated review backlog honestly — mark what is
  answered, what is superseded by a reviewed method, and what still requires a
  response. No outcome is recorded here that a reviewer has not actually given.

## What exists today

Review request files present in `reviews/` (listing checked 2026-09-21):

| # | Request | File | Raised | Trigger |
| - | - | - | - | - |
| 1 | GeoNerd at validation-ready (bootstrap) | `2026-09-20-geonerd-review-request.md` | 2026-09-20 | trigger 1 — proposed for validation-ready |
| 2 | GeoNerd rescored, parked, v2 request | `2026-09-21-geonerd-review-request-v2.md` | 2026-09-21 | re-request after revision change |
| 3 | ShiftSwap false-negative audit (kill #5) | `2026-09-21-false-negative-audit-request.md` | 2026-09-21 | trigger 6 |
| 4 | Method v1.1.0 (discontinuity-first discovery, tightened evidence) | `2026-09-21-method-v1.1.0-review-request.md` | 2026-09-21 | trigger 2 |
| 5 | Method v1.2.0 (scoped why-now cap) | `2026-09-21-method-v1.2.0-review-request.md` | 2026-09-21 | trigger 2 |
| 6 | Method v1.3.0 (second-order seams, seed-aware discovery) | `2026-09-21-method-v1.3.0-review-request.md` | 2026-09-21 | trigger 2 |
| 7 | BiK payroll false-negative audit (kill #10) | `2026-09-21-false-negative-audit-request-bikpayroll.md` | 2026-09-21 | trigger 6 |

**Response files present: none** as of this issue #5 reconciliation (2026-09-21).
See the post-response update at the end of this file — six independent responses
were committed later the same day under issue #6.

## Reconciliation

Because no reviewer has responded, the honest status of every item is:

- **Answered:** none.
- **Superseded by a later reviewed method:** none. A later method version only
  supersedes an earlier request if the later version has itself been reviewed
  and approved; method 1.3.0 is currently `requested`, so the 1.1.0 and 1.2.0
  requests remain materially relevant as the record of those changes.
- **Still materially relevant, awaiting response:** all seven items.

This is recorded without rewriting any history: the GeoNerd 1.0.0-era request
(#1) is preserved next to its v2 replacement (#2); the Worker's own self-audit
verdicts on ShiftSwap and BiK remain self-audits, not reviewer outcomes.

### Item notes

1. **GeoNerd v1 (2026-09-20).** Kept for provenance. The idea was rescored and
   parked on 2026-09-21, so the live question is #2.
2. **GeoNerd v2 (2026-09-21).** Live. Asks whether the 65.3 → 49.5 rescore and
   the downward move to `adversarially-researched` are right, and whether the
   demand spike should still be proposed while parked.
3. **ShiftSwap audit (kill #5).** Live. Asks whether the kill was correct given
   bundled shift-swap features, two-sided density and commodity pricing; also
   whether WonkyBox/GrantScout need re-audit and whether the
   `grantscout-application-quality` seed is the right adjacent opportunity.
4. **Method v1.1.0.** Live. The scoring/evidence/lifecycle tightening was never
   reviewed; later versions preserve its semantics, so a reviewer should treat
   this as the first delta in the 1.0.0 → 1.3.0 chain.
5. **Method v1.2.0.** Live. Scoped the missing-why-now cap to Plausible/Promising
   evidence levels. Small, but it *does* lift one score (Aucly problem 2 → 3).
6. **Method v1.3.0.** Live. Second-order discovery preference, seed-aware
   discovery, provenance and convergence recording. Discovery-only; weights,
   threshold and hard-filter semantics unchanged.
7. **BiK audit (kill #10).** Live and newly raised. Asks whether the incumbent
   capability scan over-read vendor marketing, and whether the
   `defensible_wedge` cluster implies a sourcing change rather than filter
   relaxation.

## Cumulative-review option (for the human owner)

Items 4–6 are cumulative deltas of one method. A reviewer may answer the whole
chain 1.0.0 → 1.3.0 in one pass, either as one response file per request or as
a single cumulative response referenced from each request. That is a routing
decision for the human owner; the worker cannot consolidate outcomes it has not
received.

## What would close each item

- Items 1–7 close when a reviewer response file exists and its verdict
  (`approved | changes-requested | killed`) and rationale are recorded in the
  relevant `review.history` entry next to the request.
- A `changes-requested` verdict must be answered explicitly in the next run
  (accept-and-change, or documented disagreement) — never silently dropped.

## Compliance

- No reviewer verdict was invented or inferred.
- No existing request file was edited or deleted.
- No `changes-requested` outcome exists, so no answer was owed this run.

## Post-response update (issue #6, 2026-09-21)

Six independent responses were committed the same day
(`reviews/2026-09-21-*-chatgpt-gpt-5.6-sol.md`, reviewer ChatGPT / GPT-5.6 Sol)
and reconciled into the repository's current state:

| Request | Outcome | Response file |
| - | - | - |
| GeoNerd v1 (2026-09-20) | **Superseded / historical provenance** — retained, not a substantive open review | n/a (v2 answered) |
| GeoNerd v2 | Answered — `approved` (rescore and park justified; no demand evidence; spike may stay proposed) | `2026-09-21-geonerd-chatgpt-gpt-5.6-sol.md` |
| ShiftSwap false-negative audit | Answered — `approved`, kill upheld; WonkyBox/GrantScout not reopened | `2026-09-21-shiftswap-chatgpt-gpt-5.6-sol.md` |
| Method v1.1.0 | Answered — `approved` (keep 65; monitor score coverage) | `2026-09-21-method-v1.1.0-chatgpt-gpt-5.6-sol.md` |
| Method v1.2.0 | Answered — `approved` (visitor-cohort caveat recorded) | `2026-09-21-method-v1.2.0-chatgpt-gpt-5.6-sol.md` |
| Method v1.3.0 | Answered — `approved` (regulatory-source bias confirmed; sourcing fix next) | `2026-09-21-method-v1.3.0-chatgpt-gpt-5.6-sol.md` |
| BiK false-negative audit (kill #10) | Answered — `approved`, kill upheld | `2026-09-21-bikpayroll-chatgpt-gpt-5.6-sol.md` |

**Genuinely outstanding reviews: none.** No approval here is market validation
and no idea was advanced on the strength of a reviewer verdict. Dissent and
caveats are preserved in the response files and in the affected
`review.history` entries.

## Later method reviews (added 2026-09-21, issue #8)

The method requests raised after this reconciliation were also answered:

| Request | Outcome | Response file |
| - | - | - |
| Method v1.4.0 (source-class budget) | `approved` — budget retained as a discovery-only experiment; no quota gaming; do not tighten | `2026-09-21-method-v1.4.0-chatgpt.md` |
| Method v1.5.0 (observation funnel) | `changes-requested` — funnel retained; archetype-aware missing-why-now cap and sampled triage false-negative audit required; threshold/filter/evidence semantics unchanged | `2026-09-21-method-v1.5.0-chatgpt.md` |

Method 1.6.0 implements the requested changes and carries
`reviews/2026-09-21-method-v1.6.0-review-request.md`. The only outstanding reviews
under the method track are that request and the `wonkybox` kill-#15 false-negative
audit request.
