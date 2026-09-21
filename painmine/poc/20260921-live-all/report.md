# painmine run report — live-20260921-all

- Generated: 2026-09-21T10:37:30Z
- Mode: live-public-sources | family: all
- Queries: `we still do this manually`, `"copy and paste" spreadsheet monthly report`, `"re-key" data between systems`, `"double entry" excel process`, `"manually export" csv import`, `"is there software that" small business`, `"looking for an alternative to" spreadsheet`, `"our current software doesn't"`, `"wish it integrated with"`, `"there has to be a better way" admin`, `"hours every week" manual data entry`, `"we pay someone to" enter data`, `"too expensive" small business software`, `"minimum contract" software`, `"enterprise plan" feature locked`
- Sources requested: hn_algolia, stack_exchange, github_issues, reddit_public_json

## Volumes

- raw_items: 150
- extracted_signals: 139
- extraction_rejects: 11
- extraction_reject_reasons: {'statement_too_short': 8, 'no_pain_cue': 3}
- duplicates_removed: 18
- duplicate_ratio: 0.129
- clusters_total: 6
- clusters_with_buyer: 3
- clusters_band_a: 1
- clusters_band_b: 3
- clusters_band_c: 2
- clusters_independent_ge_3: 6

## Cost, runtime and limits

- requests_used: 24
- requests_limit: 24
- items_collected: 150
- items_limit: 240
- llm_enabled: False
- llm_calls: 0
- llm_calls_limit: 6
- llm_input_tokens: 0
- llm_output_tokens: 0
- llm_tokens_limit: 40000
- llm_usd: 0.0
- llm_usd_limit: 0.25
- elapsed_seconds: 43.84
- wall_limit_seconds: 420
- stopped: True
- stop_reason: request limit (24) reached
- recorded_at: 2026-09-21T10:38:14.460426Z

## Source access (attempted)

| source | requests | ok | failed | items | errors |
| --- | --- | --- | --- | --- | --- |
| hn_algolia | 15 | 10 | 5 | 50 | per-source item cap reached |
| stack_exchange | 15 | 10 | 5 | 50 | per-source item cap reached |
| github_issues | 15 | 3 | 12 | 50 | per-source item cap reached |
| reddit_public_json | 15 | 0 | 15 | 0 | HTTP 403; budget stopped: request limit (24) reached |

## Top clusters

| cluster | role | indep | members | priority | band | persistence | archetype | systems |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| c-5d98df96 | Bookkeeper | 6 | 6 | 70.8 | A | weak | persistent | Excel, QuickBooks |
| c-054ee3da | ? | 4 | 4 | 67.5 | B | weak | persistent | Notion |
| c-4ff80e18 | E-commerce operator | 10 | 10 | 67.0 | B | strong | persistent | Excel, Gmail, MySQL, Outlook, WooCommerce |
| c-0610fb64 | ? | 3 | 3 | 51.0 | B | weak | persistent | - |
| c-4b0d977b | ? | 3 | 3 | 47.5 | C | absent | persistent | - |
| c-f574f024 | Administrator | 5 | 5 | 41.0 | C | absent | persistent | - |

## Quality checks

- Recurrence measurable (>=3 independent sources in a cluster): True
- Vendor-led risk mix: {'low': 6}
- Lowest-confidence extractions (manual audit targets):
  - a5959d17c645c377 (conf 0.27): Despite all of the advances in technology, we still do this manually - in a conference room or a zoom meeting.
  - 1a12678fd8448930 (conf 0.27): They could simply push it to a repository on GitHub instead of assigning employees to do this manually.
  - a092401148fd27e4 (conf 0.27): As someone who wrote x86 optimization code professionally in the 90s, do we need to do this manually still in 2025?
  - 22b5e880ee12861f (conf 0.27): The limits on that are not technical; they have to do with (1) how much work we still do manually—the classic "no time to do things that would make the things t
  - 6835bcbe1ff67fd3 (conf 0.27): translating text, coming up with generic copy text, adding some illustrations to articles, etc.), then yes AI is robbing you of your job and there will be a lot

## Preliminary recommendation: ITERATE

At least one band-A cluster with a persistence thesis; iterate sources and run dual synthesis.

Discovery-priority scores are not business scores and not market validation. Method 1.6 scoring, hard filters and lifecycle gates are unchanged and still apply downstream.
