# GeoNerd — dossier

- Idea id: `geonerd`
- State: `adversarially-researched` (parked; was `validation-ready` under method 1.0.0)
- Evidence level: `Promising` (category analysis; no buyer-derived evidence)
- Seeded: 2026-09-20, as a bootstrap entry under issue #1; rescored 2026-09-21 under method 1.1.0
- Method version: 1.1.0

## One-sentence proposition

> GeoNerd tells a UK accountancy practice, in plain English, whether AI
> assistants recommend them when local business owners ask for an accountant —
> and what to do about it — for £19.99/month.

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

## Buyer

- UK accountancy practices, 1–20 staff, owner-managed, serving local SMEs.
- First beachhead: contractor/IR35 specialists and small-practice accountants.
- Decision maker: owner or partner. Purchase size is small relative to the value
  of one new client, so willingness to pay is not assumed to require
  sophistication — this is the core buyer hypothesis, restated as assumption A1
  below.
- Budget-line evidence: incumbents already charge this buyer (TendorAI to UK
  accountants; SearchScore to the same SME/professional buyer base), which shows
  a budget line exists but not that it is spent on GeoNerd. No buyer has been
  contacted or observed. See `evidence/geonerd/2026-09-20-wedge-strategy.md`
  and `evidence/geonerd/2026-09-20-competitive-teardown.md`.

## Problem

- AI assistants increasingly answer "best accountant for contractors in
  <city>"-class questions; the practice cannot see whether it appears, who
  appears instead, or why.
- The problem is assumed painful/frequent by analogy (the same practice tracks
  Google visibility), not demonstrated. Assumption A2. Under method 1.1.0 this
  scores 2 with low confidence and the `painful_frequent_or_budgeted` hard
  filter is `unknown`.
- Relevant evidence: `evidence/geonerd/2026-09-20-wedge-strategy.md`
  (AIO/YMYL exposure section), `evidence/geonerd/2026-09-20-spike-findings.md`
  (measurement-surface disagreement).

## Mechanism / wedge

- Free domain-in scan → named competitor + citation report + three plain-language
  actions; paid monthly digest: "three things changed this month. One matters."
- Defensibility rests on **vertical depth** (one shared prompt set per market
  makes sampling cheap and benchmarks meaningful), **honest measurement**
  (explicit sample sizes and noise bands), and **plain-language actions** — not
  on measurement breadth.
- Contested: TendorAI targets the same vertical; SearchScore is cheaper; free
  checkers anchor measurement at £0. See
  `evidence/geonerd/2026-09-20-competitive-teardown.md`. `defensible_wedge` is
  therefore `unknown`.

## Distribution

- Free scan → email capture; SEO for "AI visibility for accountants"-class
  queries; a public vertical benchmark report; AccountingWEB / ICAEW / ACCA /
  AAT communities; practice-management partnerships.
- Explicitly not paid acquisition at launch (CAC would swamp £19.99).
- All channel yields are unmeasured. Assumption A4; scored 2 under 1.1.0
  (plausible channels, no demonstrated prospect flow).

## Economics

- Collection: 30 prompts × 2 surfaces × 3 samples/week per market; UI-equivalent
  £60–95/market/month → at £19.99/mo the product needs ≥10 customers per market
  to contribute positively; at d=25 contribution ≈ £13.34/customer.
- Cost model is desk-calculated, not tested against a real provider bill.
  Assumption A5. Under 1.1.0 modelled-only economics score 2 with low
  confidence. Source: `evidence/geonerd/2026-09-20-wedge-strategy.md`.

## Founder fit

- Not scored: no evidence is recorded about the founder's distribution, domain
  access or time budget beyond the existence of the GeoNerd research repo. This
  dimension is deliberately left null rather than guessed.

## Strongest supporting case

- Accountancy is dense in shared AI buying questions, the buyer is identifiable
  and reachable through non-paid professional communities, and the incumbent
  landscape leaves a genuine gap between free checkers and £299/mo
  done-for-you services. A £19.99/mo decision aid is a rounding error against
  the value of one new client, and the "honest measurement" angle is a credible
  response to documented UI/API noise (6–24% brand overlap).

## Adversarial case (strongest case this is wrong)

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

## Decision log

| Date | Actor | Decision | Rationale |
|---|---|---|---|
| 2026-09-20 | bootstrap (human owner, issue #1) | Seed at `validation-ready`; request independent review | GeoNerd already has a full desk-research base and a specified decisive test; primary demand and commercial validation remain outstanding, so no further advance is permitted |
| 2026-09-21 | worker (issue #2) | Rescore under method 1.1.0: 65.3 → 49.5; move down to `adversarially-researched`; re-request review with the new revision | Tightened semantics: inferred pain, plausible distribution, modelled economics and a contested wedge no longer score as demonstrated. The threshold is unchanged, so the honest score parks the idea; the demand spike remains proposed and is now the route back up |
