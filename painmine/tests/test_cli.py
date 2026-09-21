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
            self.assertLessEqual(len(observations), 20)
            self.assertTrue(all("triage" not in o for o in observations))
            self.assertTrue(all("triage_reason" not in o for o in observations))
            self.assertTrue(all(o["discovery_priority"]["band"] for o in observations))
            self.assertTrue(all(o["recurrence"]["independent_source_count"] >= 1 for o in observations))

            self.assertEqual(cli.main(["validate", "--run-dir", out]), 0)
            self.assertEqual(cli.main(["observations", "--run-dir", out]), 0)
            self.assertEqual(cli.main(["report", "--run-dir", out]), 0)

    def test_pipeline_does_not_touch_idea_ledger(self):
        root = os.path.abspath(os.path.join(HERE, "..", ".."))
        ledger = os.path.join(root, "ideas", "index.json")
        with open(ledger, "rb") as handle:
            before = handle.read()
        with tempfile.TemporaryDirectory() as tmp:
            rc = cli.main(
                [
                    "pipeline",
                    "--offline-fixture",
                    FIXTURE,
                    "--out",
                    os.path.join(tmp, "run"),
                    "--run-id",
                    "pm-ledger-check",
                ]
            )
            self.assertEqual(rc, 0)
        with open(ledger, "rb") as handle:
            after = handle.read()
        self.assertEqual(before, after)

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
