# Issue #18 response — five narrow open-banking workflow hypotheses

- **Issue:** rcgeorge23/business-idea-lab#18, "Investigate five narrow open-banking
  workflow hypotheses through the lab"
- **Run:** 20260922T072821Z-normal (method 1.7.0)
- **Written:** 2026-09-22
- **Boundary note:** I cannot comment on, label or close the GitHub issue. This is
  the local response of record; the owner decides what to post.

## What was done

1. **Staged all five hypotheses as unvalidated owner-nominated intake** in
   `intake/2026-09-22-open-banking-hypotheses.md`, each with source URLs and dates,
   buyer/job hypothesis, provider and regulatory position, disconfirming incumbent
   evidence, overlaps and key unknowns. No score, confidence or evidence level was
   assigned at intake.
2. **Ran a normal observation sweep** including the strongest open-banking
   observations supported by current evidence, recorded in
   `observations/20260922T072821Z-normal-openbanking.md` (16 observations, 0
   promotions).
3. **Shallow-triaged every observation** with a recorded reason, and performed the
   sampled triage false-negative audit (O1, upheld with a source-quality caveat).

## Acceptance criteria mapping

| Criterion | Status | Where |
|---|---|---|
| All five hypotheses durably staged as unvalidated intake with sources, overlaps and unknowns | Met | `intake/2026-09-22-open-banking-hypotheses.md` (H1–H5) |
| Provider/regulatory and duplicate checks documented for each | Met | Intake file, per-hypothesis "Provider/regulatory position", "Disconfirming incumbent evidence", "Overlaps" sections |
| At least the leading PTA and narrow SME exception hypotheses receive shallow triage with every deferral/rejection having a reason | Met | Pool O1 (PTA) and O4 (SME invoice exceptions), both rejected with reasons; all 16 rows carry a triage reason |
| Any full candidate promoted only through a normal Method 1.6 run, not directly from this ticket | Met | Zero promotions this run; nothing was inserted into the scored ledger |
| Run summary says which if any niche merits a cheap approved experiment and why the others do not | Met | Run summary, "Decisions needing human input" and "Next run should" |

## Per-hypothesis outcome

| Hypothesis | Observation | Outcome | Reason |
|---|---|---|---|
| H1 PTA cross-channel reconciliation | O1, O3, O13 | Rejected | BOPP's dashboard is described as solving the reconciliation job and is bundled exclusively and at a discount to Parentkind members; the population is small and transaction values low (average GBP 7.48). The satisfaction evidence is provider-published, so the audit records a caveat. |
| H2 Invoice-to-bank exception reconciliation | O4, O14 | Rejected | Ledge already sells partial/batched/inconsistently-referenced payment matching with exception resolution; Sage Intacct and SAP Ariba ship partial matching and exception workflows; Xero/QuickBooks ship bank feeds and rules. No named vertical with a residual exception was evidenced. |
| H3 Data-minimal evidence collection | O7, O15 | Rejected | Thirdfort already sells consented statement retrieval; Blackbullion serves student funding; PayPoint/AperiData serves Citizens Advice; "Open Banking for Good" already paired fintechs with debt charities. No named scheme with an unserved review was evidenced. |
| H4 Flexible collection/arrears | O5, O6 | Rejected | GoCardless already sells recurring Pay by Bank with routing, balance checks and automatic retries at scale; the failure data is the incumbent's own marketing case. |
| H5 Lender/broker evidence packs | O10 | Rejected | Least-researched hypothesis; the FCA roadmap is a statement of intent, not proof of a gap, and the latent observation fails the six-field test. |

## Which niche, if any, merits a cheap approved experiment

**None on this evidence.** Every hypothesis died on demonstrated occupation by a
named incumbent that already serves the exact job, or on absent evidenced buyer
pain. The closest to a live question is **H1**, and only because its occupation
evidence is provider-published rather than independent: if the owner wants to
spend a small amount of effort, the cheapest useful step is to read independent
PTA treasurer accounts (forums, committee minutes, umbrella-body guidance) for a
cross-channel close-out step BOPP's dashboard does not cover. That is desk
research, not an experiment, and it needs no approval. No external conversation,
bank-data access, consent flow, pilot or spend is proposed.

## Boundaries

No bank data was accessed, no consent flow was run, no prospect was contacted, no
pilot was started, no money was spent and no public claim was made. No idea was
inserted into the scored ledger. No method change was made by this ticket. The
GitHub issue was not commented on, labelled or closed.
