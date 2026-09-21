# Evidence: Aucly build and operating burden

- **Idea / scope:** `aucly`
- **Register:** evidence
- **Source:** `/home/richard/projects/aucly-micronaut` @ `c6bf305b5` — git history, `FEATURES.md`,
  `README.md`, `AGENTS.md`, `plans/done/` (~40+ implementation plans), `docs/`, deployment references
  (Railway Postgres/Redis; `prompts/done/auction-account-lifecycle-recocvery-prompt-for-a-plan.md:164`)
- **Accessed / dated:** 2026-09-21 (repository first commit 2025-07-30; HEAD at inspection)
- **Credibility:** primary (repository history and the project's own documentation)

## Claim(s) supported

- The decision to build Aucly was made and executed without any recorded pre-build validation artefact.
  The repository's first commits (2025-07-30) already implement an index page, followed immediately by
  authentication, roles and auction CRUD. No idea screening, demand test or experiment record exists.
- Aucly is a substantial, actively maintained product: auction CRUD and scheduling, proxy bidding, bidder
  invitations, post-sale winner management, Collect Payments (external payments plus optional Stripe card
  links), delivery tracking, branded auction pages, AI-generated item descriptions, promotion packs, reminder
  emails, Brevo transactional email delivery/status, referrals/vouchers, and accessibility work.
- Operating infrastructure is hosted (Railway, Postgres/Redis), with test and production profiles.
- Product development and maintenance burden is ongoing and material: ~40+ completed plans and a large
  FEATURES.md changelog covering features well beyond the core auction loop.
- There is no evidence in the repository of paid marketing spend, sales outreach tooling, or a systematic
  sales pipeline.

## Exact detail

- First commit: `04566e4ea feat: Index page now rendering` (2025-07-30). Pricing tiers seeded 2025-08-21.
- `plans/done/` includes collect-payments v1-v3, FREE_TIER_LAUNCH_ENTITLEMENT_PLAN, funnel instrumentation,
  lightweight first-party behaviour analytics, Lingfield case-study plan, BLOG_INDEX, and more.
- `FEATURES.md` documents features such as post-sale payment and delivery workflows, Brevo transactional
  status, AI descriptions, auction duplicate/edit and accessibility — breadth indicating continued investment.
- `AGENTS.md` (2025-08-12) shows AI-assisted development practice; `docs/` includes acquisition tracking,
  SEO experiment lifecycle, SEO metadata review and product activity events plans.

## Why it is credible

Direct repository evidence: commit dates, file contents and the project's own plans. The maintenance burden is
observable from the breadth and recency of changes, not inferred from memory.

## What it does NOT show

- It does not quantify hours or money spent; no time-tracking or cost ledger is committed.
- It does not show whether the build investment has been recovered (it has not, on available evidence).
- Feature breadth is not evidence of customer demand; it mostly demonstrates founder effort and the ease of
  adding features in a small self-built platform.
- It does not prove no validation happened outside the repository; it proves no validation artefact was
  recorded in it.

## Links

- Used by: `ideas/aucly/scorecard.json#feasibility`, `ideas/aucly/scorecard.json#economics`,
  `ideas/aucly/pre-launch-assessment.md`
