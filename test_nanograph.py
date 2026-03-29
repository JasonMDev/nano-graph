# ─────────────────────────────────────────────────────────────────────────────
# HEADER - Description and usage
# ─────────────────────────────────────────────────────────────────────────────

"""
test_nanograph.py - Unit tests for NanoGraph.

Run with:
    python test_nanograph.py
"""

# ─────────────────────────────────────────────────────────────────────────────
# IMPORTS
# ─────────────────────────────────────────────────────────────────────────────

import unittest
from nanograph import NanoGraph

# ─────────────────────────────────────────────────────────────────────────────
# CLASS - TestNanoGraph
# ─────────────────────────────────────────────────────────────────────────────

class TestNanoGraph(unittest.TestCase):

    # ── SetUp ─────────────────────────────────────────────────────────────

    def setUp(self):
        self.g = NanoGraph()
        self.g.add_triple("tesla", "manufactures", "model_s")
        self.g.add_triple("model_s", "has_feature", "autopilot")
        self.g.add_triple("tesla", "has_ceo", "elon_musk")
        self.g.add_triple("model_s", "has_feature", "supercharging")
        self.g.add_triple("model_3", "has_feature", "autopilot")

    # ── Structure ─────────────────────────────────────────────────────────────

    def test_node_count(self):
        self.assertEqual(self.g.node_count, 6)  # tesla, model_s, model_3, autopilot, elon_musk, supercharging

    def test_triple_count(self):
        self.assertEqual(self.g.triple_count, 5)

    def test_duplicate_triple_raises(self):
        with self.assertRaises(ValueError):
            self.g.add_triple("tesla", "manufactures", "model_s")

    def test_predicate_types(self):
        self.assertEqual(self.g.predicate_types(), {"has_ceo", "manufactures", "has_feature"})

    # ── Query ─────────────────────────────────────────────────────────────────

    def test_query_predicate_wildcard(self):
        results = self.g.query(predicate="has_feature")
        self.assertEqual(len(results), 3)

    def test_query_subject_and_predicate(self):
        results = self.g.query(subject="model_s", predicate="has_feature")
        self.assertEqual(len(results), 2)

    def test_query_object_wildcard(self):
        results = self.g.query(obj="autopilot")
        self.assertEqual(len(results), 2)

    def test_query_no_match_returns_empty(self):
        results = self.g.query(subject="model_3", predicate="manufactures")
        self.assertEqual(results, [])

    # ── Traversal ─────────────────────────────────────────────────────────────

    # ── Path finding ──────────────────────────────────────────────────────────

    # ── Cycle detection ───────────────────────────────────────────────────────



# ─────────────────────────────────────────────────────────────────────────────
# TEST SUITE - Utility Functions
# ─────────────────────────────────────────────────────────────────────────────

# ── Create sections ──────────────────────────────────────────────────────────

def section(title: str) -> None:
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print(f"{'─' * 60}")
    print(f"\n")

# ─────────────────────────────────────────────────────────────────────────────
# TEST SUITE - Main Function
# ─────────────────────────────────────────────────────────────────────────────

def main():
    section("TESTS COMPLETED")

# ─────────────────────────────────────────────────────────────────────────────
# TEST SUITE - Main Conditional Block Checking 
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
    unittest.main(verbosity=2)

