# Issue #5 retrospective: BiK seam resolved, backlog reconciled, next-run sourcing

- **Date:** 2026-09-21
- **Method version:** 1.3.0
- **Scope:** parts 1–4 of issue #5 — no normal candidate generation was run

## What this issue changed

1. **BiK payroll seam resolved.** The pre-committed desk scan
   (`experiments/bikpayroll-incumbent-capability`) met its KILL branch: at least
   two named platforms already ingest provider benefit data and emit per-period
   taxable payroll values (Zhoosh Benefits, The Electric Car Scheme, with Zest
   and Zellis/Benefex as further evidence), and three insurers do true monthly
   reconciliation. `bikpayroll` moved `desk-screened → killed` (kill #10) with
   `defensible_wedge = fail` and dated citations in
   `evidence/bikpayroll/2026-09-21-incumbent-capability-scan.md`.
2. **Review backlog reconciled, not fabricated.** Seven requests are open and
   no reviewer response exists; the honest status of all of them is recorded in
   `reviews/2026-09-21-review-queue-reconciliation.md`. Nothing was marked
   answered or superseded by a reviewed method, and no history was rewritten.
   A kill-#10 false-negative audit request was raised for the BiK kill.
3. **Experiment queue written** (`experiments/queue.md`) with run/defer/cancel
   recommendations. No approval-required experiment was started.

## Should another normal discovery run happen?

**Yes — but only after the human owner routes the review backlog (or explicitly
accepts the unresolved debt), and only with a changed sourcing rule.** Three
consecutive discovery efforts have produced a `defensible_wedge` kill cluster
(agentready, packproof, vetcma, prsregister, propident, wastetrack, bikpayroll —
seven kills). The issue #4 convergence review already concluded this is partly a
source-class artefact: easily searchable regulatory/mandate discontinuities
consume the discovery budget by default, and the resulting compliance-tool
candidates are exactly the ones incumbents bundle away. The filter is working
correctly; the sourcing needs to change.

### Proposed sourcing rule (discovery-only — for review before adoption)

**Source-class budget.** Of the up-to-three candidates a run may promote:

- **at least two must come from non-regulatory classes**, drawn from a fixed
  rotation: (a) poor or overpriced narrow incumbent software; (b) software
  shutdowns, EOL, forced migrations; (c) newly accessible APIs or datasets;
  (d) awkward integrations between established systems; (e) manual
  spreadsheet/email/PDF workflows; (f) platform pricing, access or rule changes;
  (g) expensive repetitive professional services newly automatable with current
  AI; (h) underserved subsegments of an existing category;
- **at most one may be a regulatory/mandate discontinuity** (any candidate
  whose why-now is primarily legislation, consultation or a new mandated
  format), and it must record the second-order operational seam it addresses;
- **at least one previously unsearched class must be attempted** each run
  (platform pricing and standalone new technical capability are the current
  gaps), recorded in the run summary even when it yields nothing.

This is a **discovery rule, not a scoring advantage**: no weights, threshold,
hard filter, evidence level or candidate limit changes. It would be method
`1.4.0`, recorded in `method/CHANGELOG.md`, with a review request raised before
the next run adopts it — the same path as previous method changes. It needs the
human owner's routing because the method-change review chain 1.1.0 → 1.3.0 is
itself outstanding.

### If adopted, the next run should aim at

- one candidate from classes (b), (d) or (e) — forced migrations, integration
  gaps and manual document flows are where operational seams persist;
- one candidate from an unsearched class (platform pricing/access, or new
  technical capability applied to a repetitive professional service);
- at most one mandate-derived candidate, with its second-order seam explicit;
- the seed register re-checked (at least `prs-listing-precheck` or
  `agent-checkout-offplatform`), remembering seeds become candidates only via
  fresh research and never inherit parent scores.

### Signal to keep watching

If the next run again returns several reasonable candidates all killed on
`defensible_wedge`, that is a signal to review **discovery sourcing and
candidate framing**, never to relax the filter. Three consecutive such runs
should escalate to the reviewer explicitly.

## Status pointers

- Method 1.3.0 review still `requested`; method chain 1.1.0 → 1.3.0 can be
  answered cumulatively.
- False-negative audits outstanding: ShiftSwap (kill #5) and BiK (kill #10).
- Live experiments awaiting human approval: `reasonable-steps-willingness`
  (recommended first), `aucly-channel-test` (second),
  `geonerd-demand-spike` (defer until GeoNerd review v2 is routed).
- Compliance: no commits, pushes, contact, spend, accounts, publication or
  commitments; no experiment requiring approval was started; scoring, threshold
  and hard-filter semantics unchanged.
