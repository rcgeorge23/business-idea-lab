# Seed — Veterinary exchange reference-list / code-list management and mapping service

- **Seed id:** `vetlab-reference-list-management`
- **Origin idea:** `vetlab-en18029-conformance` (itself promoted from observation O5, run `20260921T100247Z-normal`)
- **Recorded:** 2026-09-21
- **Status:** unexplored

## Observation

DIN EN 18029:2026-04 (E) specifies the veterinary laboratory exchange files and a data dictionary but explicitly excludes the code lists required for unambiguous exchange. The originating research found no maintained veterinary reference-list or cross-walk service covering analytes, units, species, methods and sample types, and no mapping between each laboratory's internal codes and the exchanged codes. Any implementation of the standard needs such shared, versioned reference data.

## Why it is materially different from its parent

The parent candidate sells a conformance and mapping-validation **toolkit** (schema validation, test fixtures, certification reports, exception queues) primarily to vendors and laboratories. This seed is a **content-and-governance** proposition: maintaining, versioning and licensing the reference lists themselves plus cross-walks between lab-specific and exchanged codes, with a different potential buyer (a national body, a consortium, or the laboratories collectively) and subscription economics independent of any single vendor's implementation.

## Why it is only a seed

No evidence yet shows that any body will fund, govern or mandate a shared list, and a voluntary standard may leave each lab to maintain its own mappings. It must be researched from scratch — its own fingerprint, evidence, hard filters and scorecard — and it inherits no score, evidence level or conclusion from the parent candidate or from the killed idea `vetlab-bridge`.

## Evidence pointers

- `evidence/vetlab-en18029-conformance/2026-09-21-en18029-standard-scope.md`
- `evidence/vetlab-en18029-conformance/2026-09-21-vet-interoperability-and-incumbents.md`
