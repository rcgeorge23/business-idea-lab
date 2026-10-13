#!/usr/bin/env python3
"""Tests for scripts/build_dashboard.py under method 1.9.0 (schema v2 + legacy v1).

Covers: mixed-version ledgers building without phantom rows, version-aware
dimension/filter rendering, the schema-v2 SEO assessment section, honest
rendering when seo_assessment is absent, and the live all-v1 ledger.

Fixtures build minimal repositories in temporary directories; the live repo is
only read (read-only integration test) so no repository data is mutated.

Run with:  python3 -m unittest discover -s tests -v
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS_DIR))

import test_validate_repo as tvr  # noqa: E402

BUILD_SCRIPT = REPO_ROOT / "scripts" / "build_dashboard.py"

V1_DIMENSION_LABELS = [
    "Problem severity / frequency",
    "Buyer budget clarity",
    "Evidence strength",
    "Distribution",
    "Differentiation",
    "Validation speed / cost",
    "Feasibility",
    "Economics",
    "Founder fit",
    "Risk",
]

V2_DIMENSION_LABELS = [
    "Problem severity / frequency",
    "Buyer budget clarity",
    "Evidence strength",
    "SEO discoverability",
    "Self-service fit",
    "Distribution",
    "Founder fit",
    "Economics",
    "Validation speed / cost",
    "Feasibility",
    "Differentiation",
    "Risk",
]

V2_FILTER_LABELS = [
    "Clear economic buyer",
    "Painful / frequent / budgeted",
    "Non-paid distribution",
    "Defensible wedge",
    "No network effects needed",
    "Plausible margins",
    "Acceptable risk",
    "Cheap disconfirming test",
    "Not all-optimistic",
    "SEO discoverable",
    "Self-serve purchase",
    "Solo operator fit",
]


class DashboardTestCase(unittest.TestCase):
    def build(self, ideas: list[tuple[dict, dict]]) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        tvr.build_repo(root, ideas)
        return root

    def run_builder(self, root: Path) -> str:
        out = root / "dashboard.html"
        result = subprocess.run(
            [sys.executable, str(BUILD_SCRIPT), "--root", str(root), "--out", str(out), "--quiet"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, msg=result.stderr or result.stdout)
        self.assertTrue(out.exists(), msg="dashboard.html was not written")
        return out.read_text(encoding="utf-8")


class TestMixedVersionLedger(DashboardTestCase):
    def mixed_repo(self) -> Path:
        return self.build(
            [
                (tvr.make_entry("fixture-v2", "Fixture v2", 901), tvr.make_card_v2("fixture-v2", "Fixture v2", 901)),
                (tvr.make_entry("fixture-v1", "Fixture v1", 902), tvr.make_card_v1("fixture-v1", "Fixture v1", 902)),
            ]
        )

    def test_mixed_ledger_builds_without_error(self) -> None:
        html = self.run_builder(self.mixed_repo())
        self.assertIn("Fixture v2", html)
        self.assertIn("Fixture v1", html)

    def test_v2_dimension_and_filter_labels_render(self) -> None:
        html = self.run_builder(self.mixed_repo())
        for label in V2_DIMENSION_LABELS:
            self.assertIn(label, html, msg=f"missing v2 dimension label: {label}")
        for label in V2_FILTER_LABELS:
            self.assertIn(label, html, msg=f"missing v2 filter label: {label}")

    def test_seo_assessment_section_renders(self) -> None:
        html = self.run_builder(self.mixed_repo())
        self.assertIn("<h4>SEO assessment</h4>", html)
        self.assertIn("fixture query", html)
        self.assertIn("fixture intent cluster", html)
        self.assertIn("assumption-labelled fixture", html)
        self.assertIn("fixture cheap next check", html)

    def test_version_info_renders_for_both_schemas(self) -> None:
        html = self.run_builder(self.mixed_repo())
        self.assertIn("legacy v1", html)
        self.assertIn("1.2.0", html)
        self.assertIn("1.8.2", html)
        self.assertIn("1.3.0", html)
        self.assertIn("1.9.0", html)


class TestLegacyV1Rendering(DashboardTestCase):
    def v1_repo(self) -> Path:
        return self.build(
            [(tvr.make_entry("fixture-v1", "Fixture v1", 902), tvr.make_card_v1("fixture-v1", "Fixture v1", 902))]
        )

    def test_v1_card_renders_its_ten_dimensions(self) -> None:
        html = self.run_builder(self.v1_repo())
        for label in V1_DIMENSION_LABELS:
            self.assertIn(label, html, msg=f"missing v1 dimension label: {label}")

    def test_v1_card_has_no_phantom_v2_rows_or_section(self) -> None:
        html = self.run_builder(self.v1_repo())
        self.assertIn("legacy v1", html)
        self.assertNotIn("SEO discoverability", html)
        self.assertNotIn("Self-service fit", html)
        self.assertNotIn("SEO discoverable", html)
        self.assertNotIn("Self-serve purchase", html)
        self.assertNotIn("Solo operator fit", html)
        self.assertNotIn("<h4>SEO assessment</h4>", html)


class TestV2WithoutSeoAssessment(DashboardTestCase):
    def test_missing_seo_assessment_does_not_crash(self) -> None:
        card = tvr.make_card_v2("fixture-v2", "Fixture v2", 901)
        del card["seo_assessment"]
        root = self.build([(tvr.make_entry("fixture-v2", "Fixture v2", 901), card)])
        html = self.run_builder(root)
        self.assertIn("<h4>SEO assessment</h4>", html)
        self.assertIn("No SEO assessment recorded.", html)


class TestLiveRepository(unittest.TestCase):
    def test_live_all_v1_ledger_builds(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        out = Path(tmp.name) / "dashboard.html"
        result = subprocess.run(
            [sys.executable, str(BUILD_SCRIPT), "--root", str(REPO_ROOT), "--out", str(out), "--quiet"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, msg=result.stderr or result.stdout)
        html = out.read_text(encoding="utf-8")
        self.assertIn("legacy v1", html)


if __name__ == "__main__":
    unittest.main(verbosity=2)
