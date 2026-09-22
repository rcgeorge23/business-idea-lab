# Evidence: CORRECTION — Aucly acquisition traffic is largely non-human

- **Idea / scope:** `aucly`
- **Register:** assumption (owner-supplied, unverified)
- **Source:** owner statement in the lab session, 2026-09-22 ("those 2,333 visitors
  are mainly bots"), correcting the interpretation of
  `evidence/aucly/2026-09-21-seo-and-acquisition.md`. Independent verification
  from `/home/richard/projects/aucly-seo-reports` was **blocked** — the path is
  outside the permitted external-directory scope, so only the directory listing
  could be seen, not file contents.
- **Accessed / dated:** 2026-09-22
- **Credibility:** owner assertion about their own first-party data (not
  externally checkable as stated; treated as an assumption until filtered
  metrics are produced)

## Claim(s) supported

- **CORRECTION to `2026-09-21-seo-and-acquisition.md`:** the "2,333 total
  visitors" figure in the acquisition export is **largely automated traffic
  (bots/crawlers)**, per the owner. It should not be read as 2,333 human
  prospects who failed to convert.
- **Corroborating first-party detail (evidence):** the same source file already
  records a large internal discrepancy for the overlapping period — Cloudflare
  Web Analytics reported **130 visits** (2026-08-21 → 2026-09-17) while the
  product's own `/api/reporting/acquisition` export reported **2,333 visitors**
  (2026-08-24 → 2026-09-13). An ~18× gap between a bot-filtered edge analytics
  tool and an application-level counter is consistent with the application
  counter including non-human requests.
- **Inference (lower confidence):** the UK organic/SEO channel is therefore
  **not cleanly negatively evidenced**; the accurate state is "human reach is
  unmeasured / the channel is effectively untested", rather than "2,333 real
  visitors produced 0 conversions".

## Exact detail

- Owner statement, verbatim: "those 2333 visitors are mainly bots" (2026-09-22).
- Existing figures, from `2026-09-21-seo-and-acquisition.md`: Cloudflare 260
  pageviews / 130 visits; acquisition export totalVisitors 2,333, accountsCreated
  0, auctionsCreated 0, auctionsLaunched 0, paymentsCompleted 0, revenue 0.00;
  GSC 45 clicks / 921 impressions / 4.9% CTR (2026-08-21 → 2026-09-17).
- Windows are near-identical but not identical (Cloudflare 08-21 → 09-17;
  export 08-24 → 09-13), so the gap is indicative, not exact.
- The acquisition export is an application-level counter; nothing in the
  recorded evidence shows a bot filter, user-agent classification or human
  verification on that endpoint.

## Why it is credible

- The owner operates the platform and can see server-side logs and request
  patterns directly.
- The Cloudflare-versus-export discrepancy is independent first-party evidence
  that the export over-counts relative to the edge analytics.
- It is consistent with the GSC data: only 45 clicks and 921 impressions in the
  window cannot plausibly generate 2,333 human site visitors, let alone 2,333
  from organic search.

## What it does NOT show

- It does not quantify the bot share, nor show how many genuine human visitors
  there were (possibly very few).
- It does not show that the SEO/conversion funnel works; it only removes a
  misleading denominator.
- It does not show that the £0 revenue / 0 accounts figure is wrong — those
  outcomes stand.
- It does not establish that unpaid organic search can work; it establishes that
  the recorded metric cannot decide the question.
- **Resolve via:** re-pull the acquisition/analytics data with bot filtering
  (Cloudflare bot score, user-agent/served-request exclusion, or a server-side
  filter), and base any channel judgement on human-session counts; then re-score
  `distribution` confidence accordingly.

## Links

- Corrects: `evidence/aucly/2026-09-21-seo-and-acquisition.md`
- Used by: `ideas/aucly/scorecard.json#distribution`,
  `ideas/aucly/scorecard.json#hard_filters.non_paid_distribution`,
  `ideas/aucly/decision.md`, `ideas/aucly/dossier.md`,
  `ideas/aucly/expansion-assessment.md`,
  `observations/20260922T100404Z-normal.md`
