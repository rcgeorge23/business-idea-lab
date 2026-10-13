#!/usr/bin/env python3
"""Tests for scripts/validate_repo.py under method 1.9.0 (schema v2 + legacy v1).

Covers: search-intent evidence handling, honest-unknown handling in seo_assessment,
founder-fit / self-service gates, schema/version migration rules, historic ledger
compatibility, and run-mode acceptance.

Fixtures build minimal repositories in temporary directories; the live repo is only
read (read-only integration test) so no repository data is mutated.

Run with:  python3 -m unittest discover -s tests -v
"""

from __future__ import annotations

import copy
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import validate_repo as vr  # noqa: E402

DATE = "2026-10-13"
METHOD_VERSION = "1.9.0"
POOL_REF = "observations/2026-10-13-fixture.md"


def write_json(root: Path, rel: str, data) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return path


def write_text(root: Path, rel: str, text: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def seo_assessment() -> dict:
    """A minimally complete, honest seo_assessment fixture (unknowns allowed)."""
    return {
        "seed_queries": [
            {
                "query": "fixture query",
                "intent_cluster": "fixture intent cluster",
                "demand_evidence": [
                    {"source": "https://example.com/forum/thread", "date": DATE}
                ],
            }
        ],
        "serp_landscape": {
            "checked_date": DATE,
            "queries_checked": ["fixture query"],
            "pages": [],
            "ai_overview_observed": "unknown",
        },
        "organic_entry_feasibility": {
            "assessment": "fixture assessment",
            "notes": "fixture notes",
            "unknowns": [],
        },
        "conversion_mechanics": {
            "path": "fixture self-service path",
            "requirements": [],
            "notes": "fixture notes",
        },
        "traffic_to_revenue_scenarios": {
            "assumptions_label": "assumption-labelled fixture",
            "conservative": "conservative fixture narrative",
            "modest": "modest fixture narrative",
            "optimistic": "optimistic fixture narrative",
        },
        "seo_risks": {
            "zero_click_ai": "fixture risk",
            "seasonality": "fixture risk",
            "platform_dependency": "fixture risk",
            "other": "fixture risk",
        },
        "unknowns": [{"item": "fixture unknown", "next_check": "fixture cheap next check"}],
    }


def make_card_v2(slug: str, title: str, idea_id: int, *, state: str = "desk-screened") -> dict:
    dims = {
        key: {
            "weight": weight,
            "score": 3,
            "confidence": "medium",
            "rationale": "fixture rationale",
            "evidence": [f"evidence/{slug}/fixture.md"],
        }
        for key, weight in vr.DIMENSIONS.items()
    }
    filters = {
        key: {"status": "unknown", "note": "fixture unknown", "resolve_via": "fixture resolve"}
        for key in vr.HARD_FILTERS
    }
    return {
        "schema_version": 2,
        "method_version": METHOD_VERSION,
        "weights_version": "1.3.0",
        "idea_id": slug,  # ledger convention: idea_id equals the slug string
        "slug": slug,
        "title": title,
        "state": state,
        "updated": DATE,
        "archetype": "search-led",
        "dimensions": dims,
        "hard_filters": filters,
        "vetoes": [],
        "aggregate": {
            "scored_weight": 100,
            "raw_weighted_points": 60.0,
            "weighted_total": 60.0,
            "threshold": 65,
            "meets_threshold": False,
        },
        "confidence": "medium",
        "review": {"status": "not-required", "history": []},
        "experiment": {},
        "seo_assessment": seo_assessment(),
    }


def make_card_v1(slug: str, title: str, idea_id: int, *, state: str = "desk-screened") -> dict:
    dims = {
        key: {
            "weight": weight,
            "score": 3,
            "confidence": "medium",
            "rationale": "fixture rationale",
            "evidence": [f"evidence/{slug}/fixture.md"],
        }
        for key, weight in vr.DIMENSIONS_V1.items()
    }
    filters = {
        key: {"status": "unknown", "note": "fixture unknown", "resolve_via": "fixture resolve"}
        for key in vr.HARD_FILTERS_V1
    }
    return {
        "schema_version": 1,
        "method_version": "1.8.2",
        "weights_version": "1.2.0",
        "idea_id": slug,  # ledger convention: idea_id equals the slug string
        "slug": slug,
        "title": title,
        "state": state,
        "updated": DATE,
        "dimensions": dims,
        "hard_filters": filters,
        "vetoes": [],
        "aggregate": {
            "scored_weight": 100,
            "raw_weighted_points": 60.0,
            "weighted_total": 60.0,
            "threshold": 65,
            "meets_threshold": False,
        },
        "confidence": "medium",
        "review": {"status": "not-required", "history": []},
        "experiment": {},
    }


def make_entry(slug: str, title: str, idea_id: int, *, state: str = "desk-screened") -> dict:
    return {
        "id": slug,  # ledger convention: entry id equals the slug string
        "slug": slug,
        "title": title,
        "industry": "software-it",
        "state": state,
        "discovered": DATE,
        "updated": DATE,
        "evidence_level": "Plausible",
        "score": 60.0,
        "confidence": "medium",
        "why_now": {
            "changed": "search-led evergreen fixture",
            "why_it_matters": "fixture why it matters",
            "competitors_responded": "fixture competitor response",
            "strength": "not-required",
            "evidence": [POOL_REF],
        },
        "fingerprint": {
            "buyer": "fixture buyer",
            "problem": "fixture problem",
            "mechanism": "fixture mechanism",
            "keywords": ["fixture"],
        },
        "paths": {
            "dir": f"ideas/{slug}",
            "dossier": f"ideas/{slug}/dossier.md",
            "decision": f"ideas/{slug}/decision.md",
            "scorecard": f"ideas/{slug}/scorecard.json",
        },
        "review": {"status": "not-required"},
        "experiment": {},
    }


def build_repo(root: Path, ideas: list[tuple[dict, dict]]) -> None:
    """Build a minimal repo containing the given (entry, card) pairs."""
    write_text(root, "method/VERSION", METHOD_VERSION)
    write_text(root, POOL_REF, "# fixture observation pool\n")
    for entry, card in ideas:
        slug = entry["slug"]
        write_text(root, f"ideas/{slug}/dossier.md", "# fixture dossier\n")
        write_text(root, f"ideas/{slug}/decision.md", "# fixture decision\n")
        write_json(root, f"ideas/{slug}/scorecard.json", card)
        write_text(root, f"evidence/{slug}/fixture.md", "fixture evidence\n")
    by_state: dict[str, int] = {}
    for entry, _ in ideas:
        by_state[entry["state"]] = by_state.get(entry["state"], 0) + 1
    index = {
        "schema_version": 2,
        "method_version": METHOD_VERSION,
        "updated": DATE,
        "limits": dict(vr.LIMITS),
        "counts": {
            "total": len(ideas),
            "unreviewed": sum(1 for e, _ in ideas if e["state"] == "discovered"),
            "by_state": by_state,
            "killed": by_state.get("killed", 0),
        },
        "ideas": [entry for entry, _ in ideas],
    }
    write_json(root, "ideas/index.json", index)
    write_json(
        root,
        "experiments/index.json",
        {"schema_version": 2, "method_version": METHOD_VERSION, "updated": DATE, "experiments": []},
    )
    write_json(
        root,
        "seeds/index.json",
        {"schema_version": 2, "method_version": METHOD_VERSION, "updated": DATE, "seeds": []},
    )
    (root / "runs").mkdir(parents=True, exist_ok=True)
    (root / "runs" / "index.jsonl").write_text("", encoding="utf-8")


def simple_repo(tmp: str) -> Path:
    root = Path(tmp)
    slug = "fixture-idea"
    entry = make_entry(slug, "Fixture idea", 900)
    card = make_card_v2(slug, "Fixture idea", 900)
    build_repo(root, [(entry, card)])
    return root


class ValidatorTestCase(unittest.TestCase):
    def build(self, ideas: list[tuple[dict, dict]]) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        build_repo(root, ideas)
        return root

    def assert_no_errors(self, root: Path) -> None:
        report = vr.run(root)
        self.assertEqual([], report.errors, msg="\n".join(report.errors))


class TestValidRepos(ValidatorTestCase):
    def test_valid_v2_repo_passes(self) -> None:
        root = self.build([(make_entry("fixture-idea", "Fixture idea", 900), make_card_v2("fixture-idea", "Fixture idea", 900))])
        report = vr.run(root)
        self.assertEqual([], report.errors, msg="\n".join(report.errors))
        self.assertEqual([], report.warnings, msg="\n".join(report.warnings))

    def test_legacy_v1_card_still_passes_beside_v2(self) -> None:
        root = self.build(
            [
                (make_entry("fixture-v2", "Fixture v2", 901), make_card_v2("fixture-v2", "Fixture v2", 901)),
                (make_entry("fixture-v1", "Fixture v1", 902), make_card_v1("fixture-v1", "Fixture v1", 902)),
            ]
        )
        report = vr.run(root)
        self.assertEqual([], report.errors, msg="\n".join(report.errors))

    def test_live_repository_passes(self) -> None:
        """Historic ledger compatibility: the real repo must validate clean."""
        report = vr.run(REPO_ROOT)
        self.assertEqual([], report.errors, msg="\n".join(report.errors))


class TestSchemaVersioning(ValidatorTestCase):
    def test_legacy_card_at_new_method_rejected(self) -> None:
        card = make_card_v1("fixture-idea", "Fixture idea", 900)
        card["method_version"] = METHOD_VERSION
        root = self.build([(make_entry("fixture-idea", "Fixture idea", 900), card)])
        report = vr.run(root)
        self.assertTrue(any("schema v2" in err for err in report.errors), msg="\n".join(report.errors))

    def test_v2_requires_current_method_version(self) -> None:
        card = make_card_v2("fixture-idea", "Fixture idea", 900)
        card["method_version"] = "1.8.2"
        root = self.build([(make_entry("fixture-idea", "Fixture idea", 900), card)])
        report = vr.run(root)
        self.assertTrue(any("method_version" in err for err in report.errors), msg="\n".join(report.errors))

    def test_v2_requires_archetype(self) -> None:
        card = make_card_v2("fixture-idea", "Fixture idea", 900)
        del card["archetype"]
        root = self.build([(make_entry("fixture-idea", "Fixture idea", 900), card)])
        report = vr.run(root)
        self.assertTrue(any("archetype" in err for err in report.errors), msg="\n".join(report.errors))

    def test_v2_requires_seo_assessment(self) -> None:
        card = make_card_v2("fixture-idea", "Fixture idea", 900)
        del card["seo_assessment"]
        root = self.build([(make_entry("fixture-idea", "Fixture idea", 900), card)])
        report = vr.run(root)
        self.assertTrue(any("seo_assessment" in err for err in report.errors), msg="\n".join(report.errors))

    def test_v2_wrong_weights_version_rejected(self) -> None:
        card = make_card_v2("fixture-idea", "Fixture idea", 900)
        card["weights_version"] = "1.2.0"
        root = self.build([(make_entry("fixture-idea", "Fixture idea", 900), card)])
        report = vr.run(root)
        self.assertTrue(any("weights_version" in err for err in report.errors), msg="\n".join(report.errors))

    def test_unknown_schema_version_rejected(self) -> None:
        card = make_card_v2("fixture-idea", "Fixture idea", 900)
        card["schema_version"] = 3
        root = self.build([(make_entry("fixture-idea", "Fixture idea", 900), card)])
        report = vr.run(root)
        self.assertTrue(any("schema_version" in err for err in report.errors), msg="\n".join(report.errors))


class TestSeoAssessment(ValidatorTestCase):
    def card_with_seo_mutation(self, mutate) -> Path:
        card = make_card_v2("fixture-idea", "Fixture idea", 900)
        mutate(card["seo_assessment"])
        return self.build([(make_entry("fixture-idea", "Fixture idea", 900), card)])

    def test_demand_evidence_requires_source_and_date(self) -> None:
        def strip_source(seo):
            del seo["seed_queries"][0]["demand_evidence"][0]["source"]

        report = vr.run(self.card_with_seo_mutation(strip_source))
        self.assertTrue(any("demand_evidence" in err for err in report.errors), msg="\n".join(report.errors))

        def strip_date(seo):
            del seo["seed_queries"][0]["demand_evidence"][0]["date"]

        report = vr.run(self.card_with_seo_mutation(strip_date))
        self.assertTrue(any("date" in err for err in report.errors), msg="\n".join(report.errors))

    def test_seed_queries_required(self) -> None:
        report = vr.run(self.card_with_seo_mutation(lambda seo: seo.update(seed_queries=[])))
        self.assertTrue(any("seed_queries" in err for err in report.errors), msg="\n".join(report.errors))

    def test_volume_reported_must_be_string_when_present(self) -> None:
        def add_numeric_volume(seo):
            seo["seed_queries"][0]["demand_evidence"][0]["volume_reported"] = 1200

        report = vr.run(self.card_with_seo_mutation(add_numeric_volume))
        self.assertTrue(any("volume_reported" in err for err in report.errors), msg="\n".join(report.errors))

    def test_volume_reported_string_allowed(self) -> None:
        def add_string_volume(seo):
            seo["seed_queries"][0]["demand_evidence"][0]["volume_reported"] = "reported as 'low hundreds'"

        self.assert_no_errors(self.card_with_seo_mutation(add_string_volume))

    def test_enum_enforcement(self) -> None:
        report = vr.run(self.card_with_seo_mutation(lambda seo: seo["serp_landscape"].update(ai_overview_observed="maybe")))
        self.assertTrue(any("ai_overview_observed" in err for err in report.errors), msg="\n".join(report.errors))

        def add_bad_page(seo):
            seo["serp_landscape"]["pages"].append({"url": "https://example.com", "type": "video", "notes": "n"})

        report = vr.run(self.card_with_seo_mutation(add_bad_page))
        self.assertTrue(any("type" in err for err in report.errors), msg="\n".join(report.errors))

    def test_unknown_seo_keys_rejected(self) -> None:
        report = vr.run(self.card_with_seo_mutation(lambda seo: seo.update(invented_traffic=1000)))
        self.assertTrue(any("unknown seo_assessment keys" in err for err in report.errors), msg="\n".join(report.errors))

    def test_honest_empty_unknowns_allowed(self) -> None:
        def clear_unknowns(seo):
            seo["unknowns"] = []
            seo["organic_entry_feasibility"]["unknowns"] = []

        self.assert_no_errors(self.card_with_seo_mutation(clear_unknowns))

    def test_unknowns_need_next_check(self) -> None:
        def bad_unknown(seo):
            del seo["unknowns"][0]["next_check"]

        report = vr.run(self.card_with_seo_mutation(bad_unknown))
        self.assertTrue(any("next_check" in err for err in report.errors), msg="\n".join(report.errors))

    def test_serp_pages_may_be_absent_when_evidence_blocked(self) -> None:
        # An empty pages list with ai_overview_observed=unknown is the honest
        # recording for blocked or unverifiable SERPs; it must not be an error.
        def blocked(seo):
            seo["serp_landscape"]["pages"] = []
            seo["serp_landscape"]["ai_overview_observed"] = "unknown"

        self.assert_no_errors(self.card_with_seo_mutation(blocked))


class TestFounderFitGates(ValidatorTestCase):
    def test_solo_operator_fit_failure_requires_killed_state(self) -> None:
        card = make_card_v2("fixture-idea", "Fixture idea", 900)
        card["hard_filters"]["solo_operator_fit"] = {"status": "fail", "note": "support burden too high"}
        root = self.build([(make_entry("fixture-idea", "Fixture idea", 900), card)])
        report = vr.run(root)
        self.assertTrue(any("killed" in err for err in report.errors), msg="\n".join(report.errors))

    def test_failed_gate_with_killed_state_passes(self) -> None:
        card = make_card_v2("fixture-idea", "Fixture idea", 900, state="killed")
        card["hard_filters"]["solo_operator_fit"] = {"status": "fail", "note": "support burden too high"}
        entry = make_entry("fixture-idea", "Fixture idea", 900, state="killed")
        root = self.build([(entry, card)])
        report = vr.run(root)
        self.assertEqual([], report.errors, msg="\n".join(report.errors))

    def test_self_serve_purchase_pass_requires_evidence(self) -> None:
        card = make_card_v2("fixture-idea", "Fixture idea", 900)
        card["hard_filters"]["self_serve_purchase"] = {"status": "pass", "note": "no evidence"}
        root = self.build([(make_entry("fixture-idea", "Fixture idea", 900), card)])
        report = vr.run(root)
        self.assertTrue(any("self_serve_purchase" in err for err in report.errors), msg="\n".join(report.errors))


class TestWhyNow(ValidatorTestCase):
    def test_not_required_needs_no_changed_date(self) -> None:
        entry = make_entry("fixture-idea", "Fixture idea", 900)
        self.assertNotIn("changed_date", entry["why_now"])
        root = self.build([(entry, make_card_v2("fixture-idea", "Fixture idea", 900))])
        report = vr.run(root)
        self.assertEqual([], report.errors, msg="\n".join(report.errors))

    def test_strong_requires_changed_date(self) -> None:
        entry = make_entry("fixture-idea", "Fixture idea", 900)
        entry["why_now"]["strength"] = "strong"
        root = self.build([(entry, make_card_v2("fixture-idea", "Fixture idea", 900))])
        report = vr.run(root)
        self.assertTrue(any("changed_date" in err for err in report.errors), msg="\n".join(report.errors))

    def test_illegal_strength_rejected(self) -> None:
        entry = make_entry("fixture-idea", "Fixture idea", 900)
        entry["why_now"]["strength"] = "evergreen"
        root = self.build([(entry, make_card_v2("fixture-idea", "Fixture idea", 900))])
        report = vr.run(root)
        self.assertTrue(any("strength" in err for err in report.errors), msg="\n".join(report.errors))


class TestRuns(ValidatorTestCase):
    def run_line(self, mode: str) -> dict:
        return {
            "run_id": "20261013T000000Z-test",
            "mode": mode,
            "status": "success",
            "started_at": "2026-10-13T00:00:00Z",
            "finished_at": "2026-10-13T00:01:00Z",
            "agent": "idea-worker",
            "model": "fixture-model",
            "method_version": METHOD_VERSION,
            "validation": "pass",
            "summary": "runs/20261013T000000Z-test/summary.md",
        }

    def test_representative_mode_accepted(self) -> None:
        root = self.build([(make_entry("fixture-idea", "Fixture idea", 900), make_card_v2("fixture-idea", "Fixture idea", 900))])
        line = self.run_line("representative")
        (root / "runs" / "index.jsonl").write_text(json.dumps(line) + "\n", encoding="utf-8")
        (root / "runs" / "20261013T000000Z-test").mkdir(parents=True, exist_ok=True)
        (root / "runs" / "20261013T000000Z-test" / "summary.md").write_text("# fixture run\n", encoding="utf-8")
        report = vr.run(root)
        self.assertEqual([], report.errors, msg="\n".join(report.errors))

    def test_illegal_mode_rejected(self) -> None:
        root = self.build([(make_entry("fixture-idea", "Fixture idea", 900), make_card_v2("fixture-idea", "Fixture idea", 900))])
        line = self.run_line("manual")
        (root / "runs" / "index.jsonl").write_text(json.dumps(line) + "\n", encoding="utf-8")
        report = vr.run(root)
        self.assertTrue(any("illegal mode" in err for err in report.errors), msg="\n".join(report.errors))


class TestSeedsAndExperiments(ValidatorTestCase):
    def test_seed_cannot_inherit_score(self) -> None:
        root = self.build([(make_entry("fixture-idea", "Fixture idea", 900), make_card_v2("fixture-idea", "Fixture idea", 900))])
        seed = {
            "id": "fixture-seed",
            "slug": "fixture-seed",
            "title": "Fixture seed",
            "origin_idea": "fixture-idea",
            "observation": "fixture observation",
            "why_materially_different": "fixture difference",
            "recorded": DATE,
            "status": "unexplored",
            "evidence": [POOL_REF],
            "score": 60.0,
        }
        write_json(root, "seeds/index.json", {"schema_version": 2, "method_version": METHOD_VERSION, "updated": DATE, "seeds": [seed]})
        write_text(root, "seeds/fixture-seed.md", "# fixture seed\n")
        report = vr.run(root)
        self.assertTrue(any("score" in err for err in report.errors), msg="\n".join(report.errors))


if __name__ == "__main__":
    unittest.main(verbosity=2)
