# Decision record — `bikpayroll`

- **Idea:** `bikpayroll`
- **Date:** 2026-09-21
- **Run:** `20260921T081223Z-normal` (method 1.3.0) → `bikpayroll-incumbent-capability` scan (issue #5)
- **Decision:** kill
- **State:** `desk-screened` → `killed`
- **Actor:** worker (idea-worker), applying the experiment's precommitted decision rule

## What changed

A fresh discontinuity hunt found a dated, primary-evidenced mandate — mandatory
payrolling of benefits in kind from 6 April 2027 (HMRC policy paper 2026-07-13;
SI 2026/189 made 2026-09-14) — and a candidate was created around its
second-order operational seam: collecting, validating and reconciling
third-party benefit data into each pay run. It was novelty-checked before deep
research, then adversarially reviewed and parked with `defensible_wedge`
`unknown` pending a cheap desk scan.

**Issue #5 resolution:** the scan was executed on 2026-09-21 against the
population and thresholds fixed in `experiments/bikpayroll-incumbent-capability/plan.md`
before any searching. It found that named benefits platforms already ingest
provider benefit data and emit per-period taxable values for payroll — Zhoosh
Benefits for the medical-benefit seam (page dated 2026-08-04), with The Electric
Car Scheme (API/SFTP monthly payroll inputs) and Zest (provider-to-payroll
integrations) as further named platforms, plus Zellis/Benefex and IRIS's managed
end-to-end BiK payrolling service. The precommitted KILL branch (≥2 platforms
already ingest provider BiK data) fired. `defensible_wedge` is now `fail` and
the idea is killed. Full results: `experiments/bikpayroll-incumbent-capability/results.md`;
sources: `evidence/bikpayroll/2026-09-21-incumbent-capability-scan.md`.

The previous park record is preserved in the dossier and experiment queue; this
record supersedes the decision, not the history. The adversarial pass's recorded
dissent (kill recommended) was correct on the evidence the scan produced.

## Why now? (discovery gate)

Why-now strength: **strong**. Changed date 2026-06-24 (policy
confirmation/update window; SI 2026-09-14). Primary sources dated and registered
in `evidence/bikpayroll/2026-09-21-mandatory-bik-payrolling.md`. Provenance:
**fresh**. The discontinuity was real — it simply leads to a seam that is
already occupied.

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | unknown | Buyer hypothesis (SME finance/payroll; bureau principal) is identifiable but no budget owner or comparable spend is evidenced. `resolve_via`: bureau/employer interviews in escalation experiment. |
| painful_frequent_or_budgeted | unknown | Obligation is evidenced and recurring (monthly payroll) but buyer-felt pain and willingness to pay are not. `resolve_via`: willingness-to-pay test (escalation). |
| non_paid_distribution | unknown | Bureau/accountant channels plausible; no prospects or channel tests. `resolve_via`: channel test after capability scan. |
| defensible_wedge | **fail** | Scan found ≥2 named payroll/benefits platforms already ingesting provider BiK data (Zhoosh, Zest; plus The Electric Car Scheme, Zellis/Benefex, IRIS managed service) and insurers doing true monthly reconciliation. Precommitted rule fired KILL. Cites `evidence/bikpayroll/2026-09-21-incumbent-capability-scan.md`, `experiments/bikpayroll-incumbent-capability/results.md`. |
| no_network_effects_needed | pass | Single-sided tool; value does not require other users. Cites `evidence/bikpayroll/2026-09-21-mandatory-bik-payrolling.md`. |
| plausible_margins | unknown | Software margin only if provider ingestion is automated; services burden if manual. `resolve_via`: pilot/build estimate (moot after kill). |
| acceptable_risk | unknown | Handles payroll and medical-benefit personal data; DPIA/security needed. No regulated activity identified. `resolve_via`: DPIA before pilot (moot after kill). |
| cheap_disconfirming_test | pass | £0, ≤6h, ≤3d desk scan with pre-fixed kill thresholds; executed and decisive. Cites `experiments/bikpayroll-incumbent-capability/plan.md`. |
| not_all_optimistic | unknown | Viability rested on several unproven assumptions; the scan falsified the central one (providers/platforms do not occupy the seam). `resolve_via`: moot after kill. |

`defensible_wedge = fail` kills the idea, irrespective of the aggregate.

## Evidence considered

- `evidence/bikpayroll/2026-09-21-mandatory-bik-payrolling.md` (HMRC, SI
  2026/189, ATT, CIOT, ICAEW, Sage, ADP, Saffery).
- `evidence/bikpayroll/2026-09-21-incumbent-capability-scan.md` (HMRC
  publications; Zhoosh Benefits product page 2026-08-04; The Electric Car Scheme
  integrations; Zest; Zellis; IRIS blogs 2026-03-10 and 2026-06-23; Sage KB
  2026-06-23; BrightPay docs; Hooray Health & Protection 2026-04-13; Lex
  Autolease; Ayvens; Comcar/DriveSmart APIs; KPMG 2025-04-16; payrollexplained.uk
  2026-08-14).
- `experiments/bikpayroll-incumbent-capability/results.md` (verdict KILL against
  the pre-fixed rule).
- Adversarial pass by `idea-critic`, 2026-09-21 (kill recommendation; "do not
  advance"; wedge strictly `unknown` on cited evidence at the time).

## Scores

`ideas/bikpayroll/scorecard.json`: 9 of 10 dimensions scored; aggregate **50.5**
(scored_weight 95, raw 48.0), below the 65 threshold; gating dimensions problem
(2) and buyer budget (2) below 3; overall confidence **low**. The kill is driven
by the hard-filter failure, not by the aggregate.

## Review

Not triggered for this decision: the idea is killed, not advanced, and no
experiment exceeding 20 human-hours or £100 is proposed. Review status remains
`not-required`. (Had the scan escalated, the privacy/trust trigger would have
applied to any WTP experiment.)

## Reasons if killed

1. **The exact seam is productised.** Zhoosh Benefits records benefit changes
   with effective dates and sends payroll an employee-by-employee per-period
   taxable-value report, explicitly "without waiting for insurer invoices or
   rebuilding the numbers in spreadsheets" (2026-08-04) — the hypothesised
   bridge, already a product.
2. **Multiple credible platforms exist**, meeting the precommitted threshold:
   The Electric Car Scheme (API/SFTP monthly payroll inputs, works with all
   major payroll providers) and Zest (provider-to-payroll integration claims),
   with Zellis/Benefex and IRIS's managed service as enterprise/managed paths.
3. **Providers partly self-supply.** Bupa, Vitality and AXA do true monthly
   reconciliation and Bupa/Vitality expose downloadable monthly bills; fleet
   portals expose CSV/XLS reports.
4. **The remaining gap is a segment/execution gap, not a wedge** — SMEs without
   a benefits platform could be served, but only as a feature of benefits
   software or a managed service, contested from both ends.
5. **No escalation is available under the plan:** the rule's KILL branch fired,
   so no WTP experiment is proposed. Any further work here would be re-testing a
   falsified assumption.
6. **Precedent cluster:** `vetcma`, `prsregister`, `propident`, `packproof`,
   `agentready`, `wastetrack` and now `bikpayroll` all died on category
   capture. This is recorded as a discovery signal (see retrospective), and the
   filter is not weakened.

## False-negative audit

Kill #10 (shiftswap 1, wonkybox 2, grantscout 3, agentready 4, packproof 5,
vetcma 6, prsregister 7, propident 8, wastetrack 9, **bikpayroll 10**) triggers
the review-policy false-negative audit obligation.

**Worker self-audit (2026-09-21):** the kill is correct. The decision was
mechanical against thresholds fixed before searching; the evidence is dated and
public; the strongest counter-case (payroll *software* still requires manual
cash-equivalent entry, and some insurers still divide annual premiums by twelve)
describes an execution gap that adjacent platforms are already absorbing. The
worker's own dissent is preserved: if Zhoosh/Zest marketing overstates shipped
capability, the kill could be premature — that is exactly what an independent
audit should probe.

An external audit request has been raised at
`reviews/2026-09-21-false-negative-audit-request-bikpayroll.md` (requested from
ChatGPT; not yet answered). The audit outcome will be recorded here when it
lands; no outcome is fabricated.
