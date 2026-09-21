# Addendum — Stack Exchange site expansion (2026-09-21)

Added after this run's summary was written, at the owner's request
("Ok what other sources are worth checking?" → "yes please"). The run
directory is not rewritten; this file is the record of the follow-up change.

## Why

Stack Exchange collection was pinned to `stackoverflow` only. The network's
business-user sites (Web Applications, Money, Workplace, Freelancing, ...) are
on the same public API v2.3 with the same unauthenticated quota, so rotating
sites reaches on-thesis audiences without extra requests.

## What changed

- `painmine/sources.json` — the `stack_exchange` class now declares
  `options.sites` (11 sites, Stack Overflow first) and a `site_rotation` note.
- `painmine/fetch.py` — `fetch_stack_exchange(query, cap, budget, site=...)`
  takes the site from options; item ids include the site
  (`se:<site>:<question>:<kind>:<id>`) because question ids are only unique
  within a site; the fallback link uses the site's own domain; the status
  records the site. `collect(...)` accepts `source_options` and rotates by
  query position (`sites[i % len(sites)]`), so request count is unchanged.
- `painmine/cli.py` — `source_options()` reads per-source options from
  `sources.json`; `run_pipeline` passes them to `collect` and records them in
  `run-meta.json` under `source_options`.
- Tests — `painmine/tests/test_fetch.py` adds site-in-URL/item-id, default
  site, rotation-without-extra-requests and no-options-default cases;
  `painmine/tests/test_cli.py` asserts the config wiring and the meta field.
- Docs — `painmine/README.md` (Part 2) and `painmine/SPIKE-REPORT.md` (source
  table row 2) note the rotation.

## Verification

- `python3 -m unittest discover -s painmine/tests -t .` → 126 tests, OK.
- Live probe (5 requests): `stackoverflow` 5 items, `webapps` 5, `money` 5,
  `workplace` 4, `freelancing` 0 — all HTTP 200.
- Pipeline `pm-local-sites` (`--sources stack_exchange --max-requests 5`):
  5/5 requests, 25 raw items, 23 signals, 0 clusters; only Stack Overflow
  matched the family's quoted queries, which is expected for literal phrases
  on smaller sites.

No commits, pushes, issues, PRs, outreach or spend; no authentication bypass.
