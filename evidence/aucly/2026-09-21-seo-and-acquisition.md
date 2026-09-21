# Evidence: Aucly SEO / acquisition performance

- **Idea / scope:** `aucly`
- **Register:** evidence
- **Source:** `/home/richard/projects/aucly-seo-reports` (report generator, HEAD `14596f3`), generated
  reports `latest*.md` / `latest*.json` (retrieved 2026-09-20) and `archive/2026-09-14.*`;
  primary data endpoints: Google Search Console `sc-domain:aucly.co.uk`, Cloudflare Web Analytics,
  and `https://aucly.co.uk/api/reporting/acquisition`
- **Accessed / dated:** 2026-09-21 (SEO data windows 2026-08-15 → 2026-09-17; acquisition export window 2026-08-24 → 2026-09-13)
- **Credibility:** primary (first-party analytics exports from the live product)

## Claim(s) supported

- Aucly's organic search traffic is very small: **45 clicks / 921 impressions / 4.9% CTR / average position
  15.56** in the latest GSC window (2026-08-21 → 2026-09-17).
- The top query is the brand name `aucly` (10 clicks, position 1.3). Commercial non-brand queries —
  "school fundraiser auctions" (65 impressions), "school fundraiser auctions london" (44),
  "fundraising auctions for schools" (31) — produced **zero clicks**.
- Cloudflare reports **260 pageviews / 130 visits** over the same window, with prior windows effectively zero
  because the collector was only recently deployed.
- The acquisition export for 2026-08-24 → 2026-09-13 recorded **2,333 total visitors** but
  **0 accounts created, 0 auctions created, 0 auctions launched, 0 payments completed and £0.00 revenue**.
- Aucly has invested materially in SEO (schools, PTAs and independent-schools landing pages, ~19 blog posts
  including case studies and comparison guides, an SEO experiment lifecycle and funnel instrumentation plans);
  the current measured yield from that investment is negligible.

## Exact detail

- GSC (latest): 45 clicks, 921 impressions, CTR 4.9%, average position 15.56. Top pages: homepage 23 clicks/161
  impressions; `/online-auctions-for-schools` 15 clicks/382 impressions; independent-schools page 3/121;
  `/pricing` 1/86. Previous window (2026-08-15 → 09-11, archived 2026-09-14): 25 clicks, 877 impressions, 2.9% CTR.
- Cloudflare (2026-08-21 → 2026-09-17): 260 pageviews, 130 visits, 17 paths; admin paths such as
  `/admin/acquisition`, `/admin/dashboard`, `/admin/users`, `/organiser/dashboard` appear, indicating heavy
  internal use relative to public traffic.
- Acquisition export (source `https://aucly.co.uk/api/reporting/acquisition`): totalVisitors 2,333;
  accountsCreated 0; auctionsCreated 0; auctionsLaunched 0; paymentsCompleted 0; revenue 0.00. All
  `"revenue"` values in the archived JSON are `0.0` and no non-zero `"payments"` values exist anywhere.

## Why it is credible

These are direct first-party exports with documented API endpoints and retained raw JSON, committed in the
reporting repository; they can be re-pulled for the same windows by anyone with access.

## What it does NOT show

- The windows are short (4-5 weeks) and the Cloudflare collector is new, so this is not lifetime traffic.
- It does not prove SEO cannot work long-term; it shows the current pipeline produces effectively no signups
  or conversions.
- It says nothing about acquisition via direct outreach, referrals, social media or the owner's network,
  which may be where the ~7 paid auctions came from.
- It cannot distinguish "SEO failing" from "conversion path failing" without event-level funnel data.

## Links

- Used by: `ideas/aucly/scorecard.json#distribution`, `ideas/aucly/scorecard.json#evidence_strength`,
  `ideas/aucly/decision.md`
