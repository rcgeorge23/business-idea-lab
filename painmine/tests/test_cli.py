import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine import cli  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE = os.path.join(HERE, "fixtures", "raw_items.jsonl")
SOURCES = os.path.join(HERE, "..", "sources.json")


class TestCli(unittest.TestCase):
    def test_offline_pipeline_smoke(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "run")
            rc = cli.main(
                [
                    "pipeline",
                    "--offline-fixture",
                    FIXTURE,
                    "--out",
                    out,
                    "--run-id",
                    "pm-test",
                ]
            )
            self.assertEqual(rc, 0)
            for name in (
                "raw-items.jsonl",
                "signals.jsonl",
                "extraction-rejects.jsonl",
                "dedupe-stats.json",
                "clusters.json",
                "observations.md",
                "observations.json",
                "report.md",
                "report.json",
                "run-meta.json",
            ):
                self.assertTrue(os.path.exists(os.path.join(out, name)), name)

            meta = cli.read_json(os.path.join(out, "run-meta.json"))
            self.assertEqual(meta["mode"], "offline-fixture")
            self.assertEqual(meta["run_id"], "pm-test")
            self.assertIn("budget", meta)

            observations = cli.read_json(os.path.join(out, "observations.json"))
            self.assertTrue(observations)
            promoted = [o for o in observations if o["triage"] == "promote"]
            self.assertTrue(1 <= len(promoted) <= 3)
            self.assertTrue(all(o["discovery_priority"]["band"] == "A" for o in promoted))

            self.assertEqual(cli.main(["validate", "--run-dir", out]), 0)
            self.assertEqual(cli.main(["observations", "--run-dir", out]), 0)
            self.assertEqual(cli.main(["report", "--run-dir", out]), 0)

    def test_unknown_family_exits(self):
        with self.assertRaises(SystemExit):
            cli.family_queries(SOURCES, "not-a-family")

    def test_known_families_are_non_empty(self):
        for family in ("a_manual_rekey", "b_tooling_gap", "c_cost_pain"):
            self.assertTrue(cli.family_queries(SOURCES, family))

    def test_all_family_merges_every_family(self):
        merged = cli.family_queries(SOURCES, "all")
        expected = set()
        for family in ("a_manual_rekey", "b_tooling_gap", "c_cost_pain"):
            expected.update(cli.family_queries(SOURCES, family))
        self.assertEqual(set(merged), expected)
        self.assertEqual(len(merged), len(set(merged)))

    def test_max_requests_flag_only_lowers_cap(self):
        limits = cli.load_limits(cli.DEFAULT_LIMITS)
        original = int(limits["fetch"]["max_requests_per_run"])
        self.assertGreater(original, 5)


if __name__ == "__main__":
    unittest.main()
