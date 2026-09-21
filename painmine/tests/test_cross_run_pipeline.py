import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine import cli  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE_RUN1 = os.path.join(HERE, "fixtures", "raw_items.jsonl")
FIXTURE_RUN2 = os.path.join(HERE, "fixtures", "raw_items_run2.jsonl")


def run_pipeline(out_dir, fixture, state_path, run_id):
    return cli.main(
        [
            "pipeline",
            "--offline-fixture",
            fixture,
            "--out",
            out_dir,
            "--run-id",
            run_id,
            "--state",
            state_path,
        ]
    )


def read_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_text(path):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def accounting_cluster(clusters):
    candidates = [c for c in clusters if c.get("role_family") == "accounting"]
    if not candidates:
        raise AssertionError("no accounting cluster in %r" % (clusters,))
    return max(candidates, key=lambda c: c.get("independent_sources", 0))


class TestCrossRunPipeline(unittest.TestCase):
    """End-to-end proof that state survives a full pipeline run (issue #10)."""

    def test_cross_run_recurrence_and_no_inflation(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = os.path.join(tmp, "state.json")
            out1 = os.path.join(tmp, "run1")
            out2 = os.path.join(tmp, "run2")
            out3 = os.path.join(tmp, "run3")

            self.assertEqual(run_pipeline(out1, FIXTURE_RUN1, state, "pm-run1"), 0)
            self.assertEqual(run_pipeline(out2, FIXTURE_RUN2, state, "pm-run2"), 0)
            self.assertEqual(run_pipeline(out3, FIXTURE_RUN1, state, "pm-run3"), 0)

            run1_cluster = accounting_cluster(read_json(os.path.join(out1, "clusters.json")))
            stable_id = run1_cluster["cluster_id"]

            # Run 2 restates the same problem from independent sources and must
            # accumulate under the same stable cluster identity.
            run2_clusters = read_json(os.path.join(out2, "clusters.json"))
            matched = [c for c in run2_clusters if c["cluster_id"] == stable_id]
            self.assertEqual(len(matched), 1)
            lineage = matched[0]["lineage"]
            self.assertEqual(lineage["action"], "matched")
            self.assertGreaterEqual(lineage["match_score"], 0.35)
            self.assertEqual(lineage["first_seen_run"], "pm-run1")
            self.assertIn("role_family", lineage["matched_via"])

            meta2 = read_json(os.path.join(out2, "run-meta.json"))
            self.assertEqual(meta2["state_health"]["status"], "ok")
            self.assertGreaterEqual(meta2["cross_run"]["linked"], 1)
            self.assertGreaterEqual(meta2["cross_run"]["exact"], 1)

            report2 = read_json(os.path.join(out2, "report.json"))
            self.assertTrue(report2["history"]["history_available"])
            entry2 = report2["history"]["clusters"][stable_id]
            self.assertEqual(entry2["runs_seen"], 2)
            self.assertEqual(entry2["current_independent_sources"], 3)
            self.assertGreater(
                entry2["cumulative_independent_sources"], entry2["current_independent_sources"]
            )
            self.assertTrue(report2["recurrence_cumulative_measurable"])
            self.assertGreaterEqual(report2["volumes"]["cross_run_duplicates"], 1)
            self.assertIn(
                "## Cross-run evidence state (issue #10)",
                read_text(os.path.join(out2, "report.md")),
            )

            # Run 3 repeats run 1 exactly: the same evidence refreshes, never inflates.
            meta3 = read_json(os.path.join(out3, "run-meta.json"))
            self.assertEqual(meta3["cross_run"]["linked"], 0)
            report3 = read_json(os.path.join(out3, "report.json"))
            entry3 = report3["history"]["clusters"][stable_id]
            self.assertEqual(entry3["runs_seen"], 3)
            self.assertEqual(
                entry3["cumulative_independent_sources"],
                entry2["cumulative_independent_sources"],
            )
            self.assertEqual(report3["volumes"]["cross_run_duplicates"], 0)


if __name__ == "__main__":
    unittest.main()
