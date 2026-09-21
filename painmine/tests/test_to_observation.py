import json
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from painmine.to_observation import cluster_to_observation, render_pool, to_observations  # noqa: E402


def evidence(sid, statement, date="2026-08-01T00:00:00Z"):
    return {
        "signal_id": sid,
        "source_type": "hn_algolia",
        "source_url": f"https://example.test/{sid}",
        "published_at": date,
        "author": f"author-{sid}",
        "statement": statement,
        "systems": ["Xero", "Excel"],
        "confidence": 0.8,
    }


def craft_cluster(score=85, band="A", strength="strong", regulatory=False, cluster_id="c-test"):
    vat = " and the VAT return figures" if regulatory else ""
    return {
        "cluster_id": cluster_id,
        "role": "Accountant",
        "role_family": "accounting",
        "label": "Accountant: xero, excel, manual",
        "named_systems": ["Xero", "Excel"],
        "source_types": ["hn_algolia", "stack_exchange"],
        "member_signal_ids": ["s1", "s2", "s3"],
        "independent_sources": 3,
        "duplicate_count": 0,
        "first_seen": "2026-01-01T00:00:00Z",
        "last_seen": "2026-08-01T00:00:00Z",
        "evidence": [
            evidence("s1", f"We still manually export Xero transactions to Excel every month{vat}."),
            evidence("s2", "Copy and paste between Xero and Excel takes hours every week."),
            evidence("s3", "Re-keying the client data into Excel is error prone.", "2026-07-01T00:00:00Z"),
        ],
        "priority": {
            "score": score,
            "band": band,
            "vendor_led_risk": "low",
            "disclaimer": "Discovery priority only; not a business score and not market validation.",
        },
        "persistence": {
            "strength": strength,
            "limb2_persistence_mechanism": {"supported_mechanisms": ["partial_or_manual_integration"]},
        },
        "archetype": {"archetype": "persistent", "why_now": None},
    }


class TestToObservation(unittest.TestCase):
    def test_observation_carries_no_method_triage_labels(self):
        obs = cluster_to_observation(craft_cluster(), 1)
        self.assertEqual(obs["id"], "PM-01")
        self.assertNotIn("triage", obs)
        self.assertNotIn("triage_reason", obs)
        blob = json.dumps(obs)
        for label in ('"promote"', '"watch"', '"reject"', '"candidate"', '"lifecycle"'):
            self.assertNotIn(label, blob)
        self.assertEqual(obs["target_user_buyer"], "Accountant")
        self.assertIn("Xero", obs["incumbent_free_alternative_check"])
        self.assertEqual(obs["evidence"][0]["type"], "practitioner")

    def test_priority_band_is_an_input_not_a_state(self):
        # Changing the discovery band changes ranking metadata only: the record
        # has no lifecycle field, so it cannot advance, park or kill an idea.
        band_a = cluster_to_observation(craft_cluster(score=85, band="A"), 1)
        band_c = cluster_to_observation(craft_cluster(score=20, band="C"), 1)
        self.assertEqual(set(band_a), set(band_c))
        self.assertEqual(band_a["discovery_priority"]["band"], "A")
        self.assertEqual(band_c["discovery_priority"]["band"], "C")
        for obs in (band_a, band_c):
            self.assertNotIn("triage", obs)
            self.assertNotIn("lifecycle", obs)
            self.assertNotIn("candidate_state", obs)

    def test_regulatory_flag(self):
        self.assertFalse(cluster_to_observation(craft_cluster(), 1)["regulatory_derived"])
        self.assertTrue(cluster_to_observation(craft_cluster(regulatory=True), 1)["regulatory_derived"])

    def test_recurrence_and_extraction_blocks(self):
        obs = cluster_to_observation(craft_cluster(), 1)
        self.assertEqual(obs["recurrence"]["independent_source_count"], 3)
        self.assertEqual(obs["recurrence"]["source_type_count"], 2)
        self.assertIn("duplicate_of", obs["recurrence"]["note"])
        self.assertEqual(obs["extraction"]["min_confidence"], 0.8)
        self.assertEqual(obs["extraction"]["max_confidence"], 0.8)
        self.assertTrue(obs["extraction"]["caveats"])

    def test_observation_cap_and_no_filler(self):
        clusters = [craft_cluster(cluster_id=f"c-{i}") for i in range(30)]
        self.assertEqual(len(to_observations(clusters, max_observations=20)), 20)
        self.assertEqual(len(to_observations(clusters, max_observations=2)), 2)
        self.assertEqual(to_observations([]), [])

    def test_small_pool_is_not_padded(self):
        observations = to_observations([craft_cluster()])
        self.assertEqual(len(observations), 1)
        text = render_pool(observations, {"run_id": "pm-test"})
        self.assertIn("Pool size: 1", text)
        self.assertIn("never padded with filler", text)

    def test_empty_pool_renders_without_filler(self):
        text = render_pool([], {"run_id": "pm-test"})
        self.assertIn("Pool size: 0", text)
        self.assertIn("no clusters met the minimum size in this run", text)

    def test_render_pool_input_contract(self):
        text = render_pool(to_observations([craft_cluster()]), {"run_id": "pm-test"})
        self.assertIn("ranked observation INPUTS only", text)
        self.assertIn("does not consume", text)
        self.assertIn("Triage false-negative audit", text)
        self.assertIn("PM-01", text)
        self.assertIn("Method 1.6", text)
        self.assertIn("No source was accessed through authentication", text)
        self.assertIn("never writes", text)
        self.assertNotIn("| Triage |", text)
        self.assertNotIn("## Promoted observations", text)
        self.assertNotIn("demoted", text)


if __name__ == "__main__":
    unittest.main()
