# ─────────────────────────────────────────────────────────────────────────────
# HEADER - Description and usage
# ─────────────────────────────────────────────────────────────────────────────

"""
nanograph.py - A knowledge graph in pure Python.

Triples: (subject, predicate, object)

"""

# ─────────────────────────────────────────────────────────────────────────────
# IMPORTS
# ─────────────────────────────────────────────────────────────────────────────

from collections import deque
from typing import Optional

# ─────────────────────────────────────────────────────────────────────────────
# GRAPH CLASS
# ─────────────────────────────────────────────────────────────────────────────

class NanoGraph:
    """
    A directed knowledge graph built from (subject, predicate, object) triples.
    Nodes are any strings that appear in subject or object position.
    """

    def __init__(self):
        self._triples: list[tuple[str, str, str]] = []
        self._nodes: set[str] = set()
        self._adjacency: dict[str, list[str]] = {}

    # ── Mutation ──────────────────────────────────────────────────────────────

    def add_triple(self, subject: str, predicate: str, obj: str) -> None:
        """Add a triple. Raises ValueError on exact duplicate."""
        triple = (subject, predicate, obj)
        if triple in self._triples:
            raise ValueError(f"Triple already exists: {triple}")
        self._triples.append(triple)
        self._nodes.add(subject)
        self._nodes.add(obj)
        self._adjacency.setdefault(subject, []).append(obj)

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

    # ── Introspection ─────────────────────────────────────────────────────────

    @property
    def node_count(self) -> int:
        return len(self._nodes)

    @property
    def triple_count(self) -> int:
        return len(self._triples)

    def predicate_types(self) -> set[str]:
        """Return the set of all predicates used in the graph."""
        return {p for _, p, _ in self._triples}

    def __repr__(self) -> str:
        return f"NanoGraph(nodes={self.node_count}, triples={self.triple_count})"