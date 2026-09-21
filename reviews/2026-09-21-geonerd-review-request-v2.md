# Review request: GeoNerd: AI visibility digest for UK accountancy practices

- **Idea:** `geonerd`
- **Date:** 2026-09-21
- **Trigger:** Rescore under method 1.1.0 moved the idea down from validation-ready to adversarially-researched; proposed transition is a downward park, not an advance
- **State:** `adversarially-researched`
- **Proposed transition:** validation-ready -> adversarially-researched (rescore under method 1.1.0; review re-requested on the new revision)
- **Reviewed revision:** `uncommitted working tree after commit f5a856d (issue #2 recalibration)`
- **Requested from:** ChatGPT (independent reviewer; not market validation)

## What the reviewer must decide

Whether `validation-ready -> adversarially-researched (rescore under method 1.1.0; review re-requested on the new revision)` is justified by the evidence in this repository, or whether the idea should receive `changes-requested` or be `killed`.

## State and scores

| Dimension | Weight | Score | Confidence | Evidence |
|---|---|---|---|---|
| problem_severity_frequency | 15 | 2 | low | `evidence/geonerd/2026-09-20-wedge-strategy.md` |
| buyer_budget_clarity | 15 | 3 | medium | `evidence/geonerd/2026-09-20-wedge-strategy.md`, `evidence/geonerd/2026-09-20-competitive-teardown.md` |
| evidence_strength | 15 | 2 | low | `evidence/geonerd/2026-09-20-spike-findings.md`, `evidence/geonerd/2026-09-20-competitive-teardown.md` |
| distribution | 10 | 2 | low | `evidence/geonerd/2026-09-20-wedge-strategy.md` |
| differentiation | 10 | 2 | medium | `evidence/geonerd/2026-09-20-competitive-teardown.md` |
| validation_speed_cost | 10 | 4 | high | `evidence/geonerd/2026-09-20-demand-validation-plan.md` |
| feasibility | 5 | 3 | medium | `evidence/geonerd/2026-09-20-spike-findings.md` |
| economics | 10 | 2 | low | `evidence/geonerd/2026-09-20-wedge-strategy.md` |
| founder_fit | 5 | unscored | none | - |
| risk | 5 | 3 | medium | `evidence/geonerd/2026-09-20-competitive-teardown.md` |

- Weighted total: **49.5 / 100** (threshold 65, meets_threshold=False)
- Scored weight: 95 / 100
- Overall confidence: **low**
- Evidence level: `Promising`
- Vetoes: none

## Hard filters

| Filter | Status | Note | Evidence / resolve_via |
|---|---|---|---|
| economic_buyer | pass | Owner/partner of a 1-20 staff UK practice owns the problem and controls a marketing/BD budget; the product price is trivial against the value of one new client. | `evidence/geonerd/2026-09-20-wedge-strategy.md` |
| painful_frequent_or_budgeted | unknown | Pain and urgency are assumed by analogy with search-visibility tracking; no accountant has been observed describing the problem unprompted or paying for a fix (assumption A2). Previously recorded as pass on the strength of an assumption; corrected under weights 1.1.0. | `resolve via: geonerd-demand-spike interviews: whether practices raise the problem unprompted, what they currently do about it, and whether >=2 of 5 commit at >=GBP19/mo.` |
| non_paid_distribution | unknown | Directory outreach, professional communities, SEO and a benchmark report are plausible non-paid channels, but none has produced a scan, reply or conversation yet (assumption A4). | `resolve via: Measure directory-outreach reply and scan-start rates and community-post yield during the spike; >=1 non-network channel producing a conversation resolves it.` |
| defensible_wedge | unknown | The proposed wedge (vertical depth + honest measurement + plain-language actions) can be described, but TendorAI and SearchScore already contest AI visibility for UK accountants and free checkers cover the generic case. Describable positioning is not evidence of a defensible wedge. | `resolve via: Interview reactions to positioning and price against TendorAI/SearchScore and the free checkers; a differentiated job (not price) must be confirmed by buyers.` |
| no_network_effects_needed | pass | The market-level prompt set is shared infrastructure; a single practice receives a useful scan and digest without any other customer. | `evidence/geonerd/2026-09-20-wedge-strategy.md` |
| plausible_margins | unknown | Contribution is modelled positive only at untested density (>=10 customers/market at GBP19.99) with untested UI-equivalent collection cost (assumption A5). | `resolve via: Record the actual provider bill for the manual/automated scans and the achieved density after the spike; positive contribution at observed density resolves it.` |
| acceptable_risk | pass | No regulated data; email is the only personal data; vendors are only cited, not scraped into a product. Third-party surface dependency and incumbent contest are recorded as manageable. | `evidence/geonerd/2026-09-20-competitive-teardown.md` |
| cheap_disconfirming_test | pass | A 1-week demand spike with a pre-fixed decision rule can disprove the central assumption (practices commit at >=GBP19/mo) for <=GBP50 and <=20 human-hours. | `evidence/geonerd/2026-09-20-demand-validation-plan.md` |
| not_all_optimistic | pass | The pre-fixed stop rule kills the idea on 0/5 commitments even if every optimistic reading holds; an iterate path and an API-cost fallback are documented. | `evidence/geonerd/2026-09-20-demand-validation-plan.md` |

## Strongest supporting case

- Accountancy is dense in shared AI buying questions, the buyer is identifiable
  and reachable through non-paid professional communities, and the incumbent
  landscape leaves a genuine gap between free checkers and £299/mo
  done-for-you services. A £19.99/mo decision aid is a rounding error against
  the value of one new client, and the "honest measurement" angle is a credible
  response to documented UI/API noise (6–24% brand overlap).

## Why now?

- **What changed:** general-purpose AI assistants and AI Overviews became a
  mainstream surface for local buying questions ("best accountant for contractors
  in <city>"), making "does the AI recommend us?" a new, invisible channel for
  practices that already track Google visibility.
- **When:** AI Overviews rolled out broadly from May 2024; assistant-style
  answering had become mainstream by then. Recorded as `changed_date`
  2024-05-14.
- **Evidence:** `evidence/geonerd/2026-09-20-wedge-strategy.md` (AIO/YMYL
  exposure, adoption statistics), `evidence/geonerd/2026-09-20-spike-findings.md`
  (measurement-surface disagreement between UI and API).
- **Why it materially improves the opportunity:** the change created the
  category, not just the problem. A tool that reports AI recommendations could
  not have existed as a business before assistants were answering buying
  questions at scale.
- **Have competitors responded?** Yes, substantially: TendorAI, Tramwai,
  AireStream and SearchScore already sell to UK accountants or the same
  professional-services buyer. This is why `defensible_wedge` is `unknown`, not
  `pass`, and why `differentiation` is capped at 2.
- **Strength:** `strong` on the existence of the discontinuity; `weak` on
  GeoNerd uniquely capturing it. The why-now supports the category, not the
  company.

## Novelty / incumbent sanity check

| Check | Finding |
|---|---|
| Does this exact product already exist? | Yes, close variants: TendorAI scans AI visibility for UK ICAEW/ACCA accountants; SearchScore has audited 1,038 UK accountancy firms. |
| Multiple credible providers? | Yes — TendorAI, Tramwai (£299/mo), AireStream, SearchScore (from $25/mo), plus free checkers in Ahrefs/Semrush. |
| Is the proposed wedge already a standard feature? | Partly: multi-surface tracking and schema advice are standard; "plain-language monthly change digest for the owner" is not clearly standard. |
| Is an authoritative/free alternative adequate? | Unknown — free checkers cover measurement but not the digest/actions job; adequacy is exactly what the demand spike must test. |
| Has a well-capitalised company demonstrated hostile unit economics? | Not in this niche (incumbents are small vendors); no evidence either way. |
| Is this merely a feature of an established category? | Risk it is a feature of "AI visibility tools" rather than a standalone product; the vertical + pricing wedge is the argument against, and it is unproven. |
| Reason to continue despite these | The check does not kill the idea: no incumbent has demonstrated satisfaction of this buyer, and the price/language gap between free checkers and £299/mo services is testable cheaply. |

## Strongest disconfirming case

- The wedge may be an artefact of desk research. TendorAI already sells AI
  visibility to UK accountants and SearchScore has audited 1,038 UK accountancy
  firms; if either satisfies even two of five interviewed practices, the stop
  rule fires. Owners may treat the free scan as a one-off curiosity and never
  pay monthly ("nice to know, not worth £20"). The honest-measurement
  positioning may actively reduce perceived value by admitting the number is
  noisy. If collection costs land at the top of the modelled range or API
  proxies are indefensible, unit economics fail at any reachable density. None
  of these has been tested. Under method 1.1.0 the desk-only case scores 49.5,
  below the 65 validation-ready threshold — the idea is parked rather than
  presented as validated.

## Unresolved assumptions

- A1: owners/partners of 1–20-staff practices will personally pay ≥£19/mo for a
  monthly digest.
- A2: AI invisibility is a felt, frequent problem for them (not merely
  interesting when shown).
- A3: the free scan creates enough pull to yield ≥25% email capture.
- A4: at least one non-paid channel produces conversations with non-network
  practices.
- A5: collection cost stays ≤£95/market/month at launch, or an API-equivalent
  proxy is defensible.
- A6: the contractor/IR35 specialism is the right beachhead rather than "small
  practice serving local SMEs".
- A7: monthly cadence matches the buyer's decision rhythm.

## Cheapest decisive experiment

The 1-week demand spike in `experiments/geonerd-demand-spike/plan.md`: five
conversations with target practices, a manual scan for each, a within-subject
£9/£19/£29 price ladder, and a pre-fixed decision rule (≥2 of 5 commit at
≥£19/mo **and** ≥25% email capture **and** ≥1 non-network conversation).
Estimated bound: £50, 20 human-hours, 7 calendar days — at the review
threshold, not above it. Falsification target: A1 and A3. It also resolves the
`unknown` hard filters (`painful_frequent_or_budgeted`, `non_paid_distribution`,
`defensible_wedge`, `plausible_margins`).

## Experiment register

- `geonerd-demand-spike` status=`proposed` approval.granted=`False` plan=`experiments/geonerd-demand-spike/plan.md` results=`none`
  - Central assumption: Owner-partners of 1-20-staff UK accountancy practices will pay at least £19/month for a monthly AI visibility digest after seeing a free scan.
  - Kill condition: Zero of five interviewed practices make any concrete commitment at any price, or the dominant reaction is 'interesting but I would not pay' after the iterate week, or interviewed practices already pay for a satisfying incumbent.

## Decision record

Rescored under method 1.1.0 and the tightened rubric. The desk case no longer
reaches the `validation-ready` threshold: 65.3 → **49.5** (threshold unchanged at
65). State moves down from `validation-ready` to `adversarially-researched`. The
`geonerd-demand-spike` experiment remains proposed and is unaffected by the
state change (experiments are decoupled from `validation-ready` under 1.1.0).

Why the score fell, dimension by dimension:

| Dimension | 1.0.0 | 1.1.0 | Reason for change |
|---|---|---|---|
| problem_severity_frequency | 3 | 2 | Pain inferred by analogy; no buyer observed. Analogy cap. |
| buyer_budget_clarity | 3 | 3 | Held: buyer identified and incumbents already sell to them (weak budget-line evidence). |
| evidence_strength | 3 | 2 | All internal desk research; no buyer-derived or independent evidence. |
| distribution | 3 | 2 | Channels plausible, no prospects produced. Plausible-channels cap. |
| differentiation | 3 | 2 | TendorAI/SearchScore already contest the position. Direct-overlap cap. |
| validation_speed_cost | 4 | 4 | Held: 1-week, £50, pre-fixed decision rule. |
| feasibility | 4 | 3 | Manual scan feasible; collection pipeline unproven. |
| economics | 4 | 2 | Modelled only, no tested input. Modelled-economics cap, low confidence. |
| founder_fit | null | null | Still no evidence about the actual founder. |
| risk | 3 | 3 | Held: no regulated data; claims verifiable. |

## Machine-readable review block

```json
{
  "status": "requested",
  "requested_from": "ChatGPT (independent reviewer, routed by the human owner)",
  "request_path": "reviews/2026-09-21-geonerd-review-request-v2.md",
  "last_reviewed_revision": null,
  "history": [
    {
      "date": "2026-09-20",
      "from": "not-required",
      "to": "requested",
      "actor": "bootstrap",
      "reason": "Bootstrap seed at validation-ready under issue #1; independent review requested because the idea was proposed at an advanced state."
    },
    {
      "date": "2026-09-21",
      "from": "requested",
      "to": "requested",
      "actor": "worker",
      "reason": "Rescored under weights 1.1.0: assumption-based passes corrected to unknown, inferred pain/plausible distribution/modelled economics capped, weighted_total 65.3 -> 49.5, state moved down to adversarially-researched. New request revision issued (v2); original request preserved. Nothing has been reviewed yet."
    }
  ]
}
```

## Instructions to the reviewer

1. Work only from the repository artefacts listed below. Do not fetch or assume outside data.
2. Attack the weakest link: unsupported inference, convenience evidence, mis-scored dimension, a `pass` hard filter that is only an assumption, an over-generous why-now claim, premature advancement, missed legal/platform risk, or a hard filter that should have failed.
3. State a verdict: `changes-requested`, `approved`, or `killed`.
4. For each finding, give the evidence checked and the condition that would change the verdict.
5. Write the response as `reviews/2026-09-21-geonerd-<reviewer>-<model>.md` following `templates/review/response.md`.
6. A second model is not market validation. Agreement is not demand evidence and cannot advance the idea beyond `validation-ready`.

## Artefacts for review

- `ideas/geonerd/dossier.md`
- `ideas/geonerd/scorecard.json`
- `ideas/geonerd/decision.md`
- `evidence/geonerd/`
- `experiments/index.json`
- `ideas/index.json`


## Resolution

- **Status:** answered — approved
- **Response:** `reviews/2026-09-21-geonerd-chatgpt-gpt-5.6-sol.md`
- **Recorded:** 2026-09-21
- **Note:** Reviewer approved the 65.3 -> 49.5 rescore, the downward park and the unknown hard filters; approval is not demand evidence and does not advance the idea. Caveats preserved in the response file.
