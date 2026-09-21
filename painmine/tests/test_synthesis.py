import json
import os
import sys
import types
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine.llm import OpenCodeGo  # noqa: E402
from painmine.synthesis import (  # noqa: E402
    SYNTH_FIELDS,
    compare_interpretations,
    deterministic_interpretation,
    independent_synthesis,
    synthesis_prompts,
)


def sample_cluster():
    return {
        "cluster_id": "c-1",
        "role": "Accountant",
        "label": "Accountant: xero, excel, manual",
        "named_systems": ["Xero", "Excel"],
        "evidence": [{"statement": "We manually export Xero to Excel every month."}],
    }


def sample_signals():
    return [
        {
            "signal_id": "s1",
            "source_type": "hn_algolia",
            "published_at": "2026-01-01T00:00:00Z",
            "target_role": "Accountant",
            "pain_statement": "We manually export Xero to Excel every month.",
            "current_workaround": "Copy and paste the transactions.",
            "named_systems": ["Xero", "Excel"],
            "extraction_provenance": {"cue_groups": ["manual"]},
        },
        {
            "signal_id": "s2",
            "source_type": "stack_exchange",
            "published_at": "2026-06-01T00:00:00Z",
            "target_role": "Accountant",
            "pain_statement": "Month end reconciliation is done by hand in Excel.",
            "current_workaround": "Download both reports and reconcile manually.",
            "named_systems": ["Xero"],
            "extraction_provenance": {"cue_groups": ["manual"]},
        },
    ]


class FakeLLM:
    def __init__(self, payloads):
        self.budget = types.SimpleNamespace(llm_enabled=True)
        self._payloads = list(payloads)

    def run(self, prompt, agent=None):
        text = self._payloads.pop(0)
        return {"ok": True, "text": text, "model": "opencode-go/deepseek-v4.1-flash", "cost_usd": 0.0}


class TestSynthesis(unittest.TestCase):
    def test_deterministic_interpretation_has_all_fields(self):
        interpretation = deterministic_interpretation(sample_cluster(), sample_signals())
        for field in SYNTH_FIELDS:
            self.assertIn(field, interpretation)
        self.assertEqual(interpretation["buyer"], "Accountant")
        self.assertIn("Xero", interpretation["opportunity_seam"])

    def test_prompts_are_different_and_independent(self):
        prompt_a, prompt_b = synthesis_prompts(sample_cluster(), sample_signals())
        self.assertNotEqual(prompt_a, prompt_b)
        self.assertIn("oldest first", prompt_a)
        self.assertIn("strongest evidence first", prompt_b)
        self.assertIn("Buyer", prompt_a.replace("buyer", "Buyer"))
        self.assertNotIn("interpretation_a", prompt_b)

    def test_compare_preserves_disagreement(self):
        a = {"buyer": "Accountant", "job": "Month end close", "pain": "manual export", "current_workaround": "spreadsheet", "opportunity_seam": "integration between xero and excel"}
        b = {"buyer": "Bookkeeper", "job": "Payroll", "pain": "manual export", "current_workaround": "spreadsheet", "opportunity_seam": "integration between xero and excel"}
        comparison = compare_interpretations(a, b)
        self.assertIn("pain", comparison["agree"])
        disagree_fields = {d["field"] for d in comparison["disagree"]}
        self.assertIn("buyer", disagree_fields)
        self.assertIn("job", disagree_fields)
        for item in comparison["disagree"]:
            self.assertIn("interpreter_a", item)
            self.assertIn("interpreter_b", item)

    def test_skipped_when_llm_disabled(self):
        record = independent_synthesis(sample_cluster(), sample_signals(), None)
        self.assertEqual(record["mode"], "deterministic-baseline")
        self.assertEqual(record["status"], "skipped-llm-disabled")
        self.assertIn("baseline_interpretation", record)

    def test_dual_model_mode_records_both_interpretations(self):
        payload_a = json.dumps({"buyer": "Accountant", "job": "Month end close", "pain": "manual export", "current_workaround": "spreadsheet", "opportunity_seam": "xero excel integration"})
        payload_b = json.dumps({"buyer": "Accountant", "job": "Month end close", "pain": "manual export", "current_workaround": "spreadsheet", "opportunity_seam": "xero excel integration"})
        record = independent_synthesis(sample_cluster(), sample_signals(), FakeLLM([payload_a, payload_b]))
        self.assertEqual(record["mode"], "two-independent-model-calls")
        self.assertEqual(record["status"], "completed")
        self.assertEqual(record["comparison"]["agreement_ratio"], 1.0)
        self.assertEqual(record["interpreters"]["a"]["model"], "opencode-go/deepseek-v4.1-flash")

    def test_dual_model_mode_handles_partial_failure(self):
        class Broken:
            budget = types.SimpleNamespace(llm_enabled=True)

            def run(self, prompt, agent=None):
                return {"ok": False, "text": "", "error": "timeout", "model": "m", "cost_usd": 0.0}

        record = independent_synthesis(sample_cluster(), sample_signals(), Broken())
        self.assertEqual(record["status"], "partial")
        self.assertEqual(record["interpreters"]["a"]["ok"], False)
        self.assertEqual(record["interpreters"]["a"]["error"], "timeout")
        self.assertEqual(record["interpreters"]["b"]["error"], "timeout")

    def test_type_signature_accepts_real_llm_instance(self):
        from painmine.budget import Budget
        llm = OpenCodeGo({"llm": {"enabled": False}}, Budget({"llm": {"enabled": False}}))
        self.assertIsInstance(llm, OpenCodeGo)


if __name__ == "__main__":
    unittest.main()
