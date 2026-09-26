# Decision record: PPWR packaging compliance for small UK brands and exporters

- **Idea:** `packproof`
- **Date:** 2026-09-21
- **Run:** `20260921T065316Z-normal`
- **Decision:** kill
- **State:** `discovered` -> `killed`
- **Actor:** worker

## What changed

Generated from the PPWR discontinuity (Regulation (EU) 2025/40, generally applicable from 12 August 2026), which creates dated labelling, DoC, technical-file and EPR duties for packaged goods placed on the EU market, including for UK exporters and importers. The regulatory change is strong; the commercial position is not — several credible providers already sell PPWR workflows, including a UK-branded tier from £49/mo.

## Why now? discovery gate

- **Changed:** PPWR duties apply from 12 August 2026 (PFAS limits, traceability/labelling, technical documentation, importer DoC retention, per-Member-State EPR).
- **Changed date:** 2026-08-12
- **Evidence:** `evidence/packproof/2026-09-21-ppwr-incumbent-landscape.md`
- **Strength:** strong for the change; adverse for a new entrant.
- **Competitors responded:** yes — PPWR Copilot (UK, £49–£499/mo), PPWRify (Germany), PPWR Connect, Trace One ("9,000+ brands"). The novelty/incumbent check failed on "exact product exists", "multiple credible providers", "already a standard feature" and "feature of a category".

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | unknown | Brands/importers identifiable; budget evidenced only by vendor (weak secondary). |
| painful_frequent_or_budgeted | unknown | Legal exposure credible; buyer pain/budget not evidenced. |
| non_paid_distribution | unknown | Referral routes plausible only. |
| defensible_wedge | fail | Multiple live providers incl. a UK £49/mo tier; feature of an established category. |
| no_network_effects_needed | unknown | Likely per-customer; not explicitly assessed. |
| plausible_margins | unknown | No cost model; incumbent price anchors downward. |
| acceptable_risk | unknown | Compliance liability requires legal scoping. |
| cheap_disconfirming_test | unknown | Not specified because the wedge already fails. |
| not_all_optimistic | unknown | Would require winning a fragmented segment at incumbent-set prices. |

## Evidence considered

- `evidence/packproof/2026-09-21-ppwr-incumbent-landscape.md` (primary regulation/government sources plus multiple dated vendor pages).

## Scores

Weighted total **53.0** against threshold **65** (meets threshold: false). Details in `ideas/packproof/scorecard.json`. Gating dimensions: problem 3/5, buyer 2/5, evidence strength 4/5.

## Review

No review triggered or required: hard-filter rejection below threshold. Review status `not-required`.

## Reasons if killed

A real deadline attracted a complete competitive field before the deadline arrived. The buyer is fragmented and expensive to reach, the product is the category's standard feature set, and a UK incumbent already anchors price at £49/mo for a heavier tool than a micro-entrant could profitably build. The ~30 pending implementing acts reward incumbent monitoring capacity rather than create an opening. What would change the decision: evidence that a specific settled duty or the separate UK EPR regime is materially underserved by existing vendors and reachable through a non-paid channel (see seed `uk-epr-small-producer-tooling`).

## False-negative audit (killed ideas only)

- Audited: no — this is kill #5, which triggered the audit; the audit was performed against the oldest un-audited killed idea (`shiftswap`) and recorded in `ideas/shiftswap/decision.md`.
- Reviewer / date: worker, 2026-09-21 (external review requested: `reviews/2026-09-21-false-negative-audit-request.md`)
- Verdict: kill upheld for `packproof` on the same reasoning; only a specific underserved sub-duty would reopen it.
- What new evidence would justify reopening: evidence that UK small producers/importers actively pay for PPWR/EPR tooling and that one settled duty is underserved.

## Post-kill reassessment (2026-09-26; current-score rank among killed ideas: 5/5)

Fresh evidence is registered at
`evidence/packproof/2026-09-26-killed-idea-reassessment.md`. The European
Commission confirms that PPWR generally applies from 2026-08-12 and that the
Environmental Omnibus is still a proposal under consideration, not enacted
law. PPWR Copilot continues to advertise UK-priced £49/£199/£499 tiers and a
manual review offer. UK packaging EPR remains a separate regime with a free
reporting service; it is not a substitute for EU PPWR duties.

The broad small-brand PPWR dossier/label/declaration suite remains **killed**:
`defensible_wedge` remains fail, with no specific settled duty, underserved
buyer segment, paid workaround or reachable route established. The current
offer confirms continued competitive supply, not sales or customer satisfaction.
Historical score 53.0 and prior outcomes are unchanged; no rescore or state
transition is made. Reopening would require evidence for a defined obligation
and buyer segment that existing providers do not serve, alongside demonstrated
payment and a credible non-paid channel.
