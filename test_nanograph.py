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

    def query(
        self,
        subject: Optional[str] = None,
        predicate: Optional[str] = None,
        obj: Optional[str] = None,
    ) -> list[tuple[str, str, str]]:
        """
        Pattern match against the triple store.
        None acts as a wildcard.
        e.g. query(predicate="manages") returns all management triples.
        """
        return [
            (s, p, o) for s, p, o in self._triples
            if (subject is None or s == subject)
            and (predicate is None or p == predicate)
            and (obj is None or o == obj)
        ]

    def neighbours(self, node: str) -> list[str]:
        """All nodes directly reachable from this node (any predicate)."""
        return self._adjacency.get(node, [])

    # ── Traversal ─────────────────────────────────────────────────────────────

    # ── Path finding ──────────────────────────────────────────────────────────

    # ── Cycle detection ───────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# TEST SUITE - Main Conditional Block Checking 
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    unittest.main(verbosity=2)
