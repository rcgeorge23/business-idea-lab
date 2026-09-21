# Issue #6 convergence review: did the source budget change anything?

- **Date:** 2026-09-21
- **Method version:** 1.4.0 (source-class budget, discovery-only)
- **Run reviewed:** `runs/20260921T085149Z-normal` (USD 0.015021, validator pass,
  3 candidates, 0 advances)
- **Question this answers:** issue #6's seven convergence questions, and whether
  the source-budget rule should be retained, changed or removed.

## What the run did

The seed register was reviewed first (two seeds shallowly re-checked, one
promoted to a from-scratch candidate, one new adjacent seed recorded). The
candidate maximum was filled with three **non-regulatory** candidates - the
first run with zero regulation-derived candidates - and all three were killed on
`defensible_wedge`:

| Candidate | Score | Source class | Kill reason |
|---|---|---|---|
| `apispend` | 40.0 | Platform pricing/access changes | Attribution/chargeback is already standard gateway and FinOps functionality (WSO2 AI Gateway, Moesif, Workato, Arcade, n8n) |
| `ewsregister` | 44.6 | Incumbent EOL / forced migration | Microsoft's free EWS usage report plus mailbox controls cover the core need; residual work is one-shot MSP migration services |
| `agent-checkout-offplatform` | 49.2 | Platform rule/access changes (from seed `agent-checkout-offplatform`) | Hosted UCP hubs, commerce middleware, platform-native support and an open-source proxy already serve the off-platform gap |

Also recorded: two searches failed with HTTP 429 (new APIs / datasets class
incomplete - reported, not papered over); platform pricing/access and new
technical capability were searched for the first time, having been flagged
unsearched in the previous two runs.

## The seven questions

1. **Did the source-budget rule materially diversify where ideas came from?**
   Yes, mechanically and materially: 3 of 3 slots were non-regulatory
   (limit ≤ 1 regulatory), and the two fresh candidates came from classes the
   lab had never searched. The run is the first with no mandate-derived
   candidate at all.
2. **Did non-regulatory sourcing uncover different classes of problem?**
   Yes. Previous runs produced compliance/readiness products (vet price lists,
   PRS registers, waste tracking, BiK bridging). This run produced metered-API
   cost attribution, a platform-shutdown usage register, and agentic-checkout
   off-platform assurance - a genuinely different hypothesis space about
   *operational* problems rather than *obligation* problems.
3. **Are candidates becoming less obvious or better defended?**
   No - the opposite is now the pattern. The non-regulatory candidates were
   killed by the same filter and by recognisably the same mechanism: a
   well-capitalised vendor already occupies the seam, or the residual work is a
   one-shot service with no recurring wedge. Scores fell (40.0, 44.6, 49.2) and
   the kill margin widened; none reached the threshold discussion.
4. **Did the lab have to force weak candidates to satisfy the source budget?**
   No filler was manufactured. The third slot was a seed promoted only after its
   shallow re-check survived and it was then researched from scratch (own
   fingerprint, evidence and hard filters); it was killed on its own merits. A
   two-candidate run would have been acceptable, and the summary says so
   explicitly.
5. **Is `defensible_wedge` still the dominant rejection reason?**
   Yes - it is now the binding rejection for the last three runs' entire output
   (agentready, packproof, vetcma, prsregister, propident, wastetrack,
   bikpayroll, apispend, ewsregister, agent-checkout-offplatform).
6. **Is there evidence the problem is deeper than source-class allocation?**
   Yes, and this run is the cleanest evidence for it: changing the source class
   changed what the candidates were about but not how they died. Wherever the
   lab looks - regulatory or not - the reachable opportunities are either
   already served by capitalised platform/infrastructure/incumbent vendors or
   are one-shot services with thin margins. The issue #4 retrospective set this
   as the escalation trigger; it has now fired. The limit looks structural
   (hypothesis space and market position) rather than bibliographic.
7. **Should the source-budget rule be retained, changed or removed?**
   **Retain unchanged for now.** It worked exactly as designed: it stopped
   regulatory discontinuities consuming the budget by default, it forced genuine
   coverage of unsearched classes, and it did not produce filler or weaken any
   filter. Removing it would return to the compliance-heavy default with no
   evidence that default was better; tightening it further (e.g. harder quotas)
   would risk quota-driven research for no proven gain. Its first real test is
   whether a **human-led sourcing/framing review** changes the hypothesis space
   - e.g. different buyer profiles (businesses that already pay for a bad
   workaround), a service/agency model instead of product, or a different
   geography - rather than the class list.

## Recommendation to the human owner

- **Do not weaken `defensible_wedge`.** A crowding finding is a valid outcome
  of a falsification loop.
- **Escalate now, as issue #4's retrospective pre-committed:** commission the
  human-led review of discovery sourcing and framing before more runs re-roll
  the same product shapes. The loop is generating and rejecting competently; the
  bottleneck is the hypothesis space, not the evidence discipline.
- Keep the budget rule in place, route the pending method 1.4.0 review, and
  decide the experiment queue (`reasonable-steps-willingness` still deferred per
  issue #6; no approval-required experiment was run).
- Ledger housekeeping done this issue: `bikpayroll`'s scorecard experiment block
  now records `completed` with its results path, matching the experiment index.

## Status

- Sources searched and their success/failure are recorded in the run summary;
  the budget outcome is recorded as met.
- No scoring, threshold, hard-filter, evidence-level or lifecycle change was
  made in this issue; the only method change was the discovery-only source
  budget (1.4.0), which remains `requested` for independent review.
- Repo validation passes with 6 explained warnings (historical runs under
  methods 1.0.0-1.3.0; no false-negative audit is currently due).
