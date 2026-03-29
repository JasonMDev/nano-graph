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

    def bfs(self, start: str) -> list[str]:
        """
        Breadth-first traversal from start.
        Visits closest nodes first — answers "what is near this node?"
        """
        if start not in self._nodes:
            return []
        visited, queue, order = set(), deque([start]), []
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)
            for neighbour in self._adjacency.get(node, []):
                if neighbour not in visited:
                    queue.append(neighbour)
        return order

    def dfs(self, start: str) -> list[str]:
        """
        Depth-first traversal from start.
        Follows each branch to its end — answers "how far does this go?"
        """
        if start not in self._nodes:
            return []
        visited, order = set(), []

        def _visit(node: str) -> None:
            if node in visited:
                return
            visited.add(node)
            order.append(node)
            for neighbour in self._adjacency.get(node, []):
                _visit(neighbour)

        _visit(start)
        return order

    def find_paths(self, start: str, end: str, max_depth: int = 6) -> list[list[str]]:
        """
        Find all paths between start and end nodes.
        Returns a list of paths, each path a list of node ids.
        """
        if start not in self._nodes or end not in self._nodes:
            return []
        paths: list[list[str]] = []

        def _search(current: str, path: list[str], depth: int) -> None:
            if depth > max_depth:
                return
            if current == end:
                paths.append(list(path))
                return
            for neighbour in self._adjacency.get(current, []):
                if neighbour not in path:
                    path.append(neighbour)
                    _search(neighbour, path, depth + 1)
                    path.pop()

        _search(start, [start], 0)

        unique_paths = list(set(tuple(p) for p in paths))
        unique_paths = [list(p) for p in unique_paths]

        return unique_paths

    def has_cycle(self) -> bool:
        """
        Detect whether the graph contains a cycle.
        Uses three-colour DFS: white (unvisited), grey (in progress), black (done).
        A grey neighbour means we've found a back edge — a cycle.
        """
        WHITE, GREY, BLACK = 0, 1, 2
        colour = {node: WHITE for node in self._nodes}

        def _dfs(node: str) -> bool:
            colour[node] = GREY
            for neighbour in self._adjacency.get(node, []):
                if colour[neighbour] == GREY:
                    return True
                if colour[neighbour] == WHITE and _dfs(neighbour):
                    return True
            colour[node] = BLACK
            return False

        return any(
            _dfs(node)
            for node in self._nodes
            if colour[node] == WHITE
        )

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