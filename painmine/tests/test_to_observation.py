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
    def test_band_a_with_persistence_promotes(self):
        obs = cluster_to_observation(craft_cluster(), 1)
        self.assertEqual(obs["id"], "PM-01")
        self.assertEqual(obs["triage"], "promote")
        self.assertEqual(obs["target_user_buyer"], "Accountant")
        self.assertIn("Xero", obs["incumbent_free_alternative_check"])
        self.assertEqual(obs["evidence"][0]["type"], "practitioner")
        self.assertIn("Not a business score", obs["triage_reason"])

    def test_band_a_without_persistence_is_watched(self):
        obs = cluster_to_observation(craft_cluster(strength="absent"), 1)
        self.assertEqual(obs["triage"], "watch")

    def test_band_b_is_watched_and_band_c_rejected(self):
        self.assertEqual(cluster_to_observation(craft_cluster(score=55, band="B"), 1)["triage"], "watch")
        self.assertEqual(cluster_to_observation(craft_cluster(score=20, band="C"), 1)["triage"], "reject")

    def test_regulatory_flag(self):
        self.assertFalse(cluster_to_observation(craft_cluster(), 1)["regulatory_derived"])
        self.assertTrue(cluster_to_observation(craft_cluster(regulatory=True), 1)["regulatory_derived"])

    def test_promotion_cap(self):
        clusters = [craft_cluster(cluster_id=f"c-{i}") for i in range(5)]
        observations = to_observations(clusters, max_promote=2)
        self.assertEqual(sum(1 for o in observations if o["triage"] == "promote"), 2)
        self.assertEqual(sum(1 for o in observations if o["triage"] == "watch"), 3)
        self.assertTrue(all("demoted" in o["triage_reason"] for o in observations if o["triage"] == "watch"))

    def test_observation_cap(self):
        clusters = [craft_cluster(cluster_id=f"c-{i}") for i in range(30)]
        self.assertEqual(len(to_observations(clusters, max_observations=20)), 20)

    def test_render_pool_uses_method_columns_and_audit_note(self):
        text = render_pool(to_observations([craft_cluster()], max_promote=3), {"run_id": "pm-test"})
        self.assertIn("| ID | Observation (problem / workflow) | Buyer | Source class | Reg? | Archetype |", text)
        self.assertIn("Triage false-negative audit", text)
        self.assertIn("PM-01", text)
        self.assertIn("Method 1.6", text)
        self.assertIn("No source was accessed through authentication", text)


if __name__ == "__main__":
    unittest.main()
