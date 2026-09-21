import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine.state import State  # noqa: E402


class TestState(unittest.TestCase):
    def test_new_seen_and_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "state.json")
            state = State(path)
            self.assertTrue(state.is_new("hn:1"))
            state.mark_seen([{"source_id": "hn:1"}])
            self.assertFalse(state.is_new("hn:1"))
            self.assertEqual(state.filter_new([{"source_id": "hn:1"}, {"source_id": "hn:2"}]), [{"source_id": "hn:2"}])
            state.record_run({"run_id": "r1"})
            state.record_clusters([{"cluster_id": "c-1", "label": "x", "independent_sources": 3, "priority": {"score": 80}}])
            state.save()

            reloaded = State(path)
            self.assertFalse(reloaded.is_new("hn:1"))
            self.assertEqual(reloaded.runs[0]["run_id"], "r1")
            self.assertEqual(reloaded.cluster_history[0]["cluster_id"], "c-1")
            self.assertEqual(reloaded.cluster_history[0]["priority_score"], 80)

    def test_seen_cap_trims_oldest(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = State(os.path.join(tmp, "state.json"), seen_cap=3)
            state.mark_seen([{"source_id": f"x:{i}"} for i in range(5)])
            self.assertEqual(len(state.seen_ids), 3)
            self.assertFalse(state.is_new("x:4"))
            self.assertTrue(state.is_new("x:0"))

    def test_cluster_history_replaces_same_cluster(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = State(os.path.join(tmp, "state.json"))
            state.record_clusters([{"cluster_id": "c-1", "label": "old"}])
            state.record_clusters([{"cluster_id": "c-1", "label": "new"}])
            self.assertEqual(len(state.cluster_history), 1)
            self.assertEqual(state.cluster_history[0]["label"], "new")


if __name__ == "__main__":
    unittest.main()
