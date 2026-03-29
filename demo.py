# ─────────────────────────────────────────────────────────────────────────────
# HEADER - Description and usage
# ─────────────────────────────────────────────────────────────────────────────

"""
demo.py - NanoGraph in action.

Loads a small knowledge graph of philosophers and the concepts they
developed, critiqued, and passed forward.
Demonstrates what falls out of (subject, predicate, object) for free.
"""

# ─────────────────────────────────────────────────────────────────────────────
# IMPORTS
# ─────────────────────────────────────────────────────────────────────────────

from nanograph import NanoGraph
from data_triples import TRIPLES

# ─────────────────────────────────────────────────────────────────────────────
# DEMO - Utility Functions
# ─────────────────────────────────────────────────────────────────────────────

# ── Display Triples ──────────────────────────────────────────────────────────
def displayTriples(TRIPLES: list) -> None:
    print(f"{'Subject':<15} {'Predicate':<15} {'Object':<30}")
    print("-" * 60)
    for subject, predicate, obj in TRIPLES:
        print(f"{subject:<15} {predicate:<15} {obj:<30}")


# ── Create sections ──────────────────────────────────────────────────────────
def section(title: str) -> None:
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print(f"{'─' * 60}")

# ── Build Graph ──────────────────────────────────────────────────────────────
def build_graph() -> NanoGraph:
    g = NanoGraph()
    for s, p, o in TRIPLES:
        g.add_triple(s, p, o)
    return g


# ─────────────────────────────────────────────────────────────────────────────
# DEMO - Main Function
# ─────────────────────────────────────────────────────────────────────────────

def main():

    # ── 0. Display Triples Data ──────────────────────────────────────────────

    section("DISPLAY TRIPLES")
    displayTriples(TRIPLES)

    # ── 1. Load Triples into Grapg Object ────────────────────────────────────

    section("LOAD GRAPHS")
    g = build_graph()
    print(f"\nLoaded: {g}")
    print(f"Predicates in use: {sorted(g.predicate_types())}")

    # ── 2. BFS vs DFS from socrates ──────────────────────────────────────────

    section("BFS from socrates  — breadth first: who is nearest?")
    print(g.bfs("socrates"))

    section("DFS from socrates  — depth first: how far does this go?")
    print(g.dfs("socrates"))

    print("""
            BFS surfaces plato first, then aristotle — proximity in the tradition.
            DFS immediately follows the chain to its end: socrates → plato → aristotle
            → kant → hegel → marx, then backtracks to explore nietzsche and heidegger.
            Same graph. Same data. Different questions about intellectual descent.
        """)

    # ── 3. Path finding ──────────────────────────────────────────────────────

    section("Paths: socrates → existentialism")
    paths = g.find_paths("socrates", "dialectic", max_depth=8)
    if paths:
        for path in paths:
            print("  " + " → ".join(path))
    else:
        print("  No path found.")

    print("""
            Nobody stated that Socrates led to existentialism.
            The graph derived it from the chain of influence and development.
            There are multiple routes — each is a different intellectual lineage.
        """)

    # ── 4. Contested concepts ────────────────────────────────────────────────

    section("Query: what concepts were developed?")
    for s, _, o in g.query(predicate="developed"):
        print(f"  {s} → {o}")

    section("Query: what concepts were critiqued?")
    for s, _, o in g.query(predicate="critiqued"):
        print(f"  {s} critiqued {o}")

    section("Contested concepts: developed by one thinker, critiqued by another")
    developed_concepts = {o for _, _, o in g.query(predicate="developed")}
    critiqued_concepts = {o for _, _, o in g.query(predicate="critiqued")}
    contested = sorted(developed_concepts & critiqued_concepts)
    for concept in contested:
        developer = [s for s, _, o in g.query(predicate="developed", obj=concept)]
        critic    = [s for s, _, o in g.query(predicate="critiqued", obj=concept)]
        print(f"  {concept}: developed by {developer}, critiqued by {critic}")

    print("""
            Nobody labelled these concepts as contested.
            The label emerged from the intersection of two query results.
            This is inference from structure alone — no rules engine required.
        """)

    # ── 5. Cycle detection ───────────────────────────────────────────────────

    section("Cycle detection — is the graph consistent?")
    print(f"  has_cycle(): {g.has_cycle()}")

    print("\n  Now adding: the_forms inspired plato")
    print("  (Plato developed the_forms AND was shaped by them — a philosophical chicken-and-egg)")
    g.add_triple("the_forms", "inspired", "plato")
    print(f"  has_cycle(): {g.has_cycle()}")

    print("""
            Plato developed the theory of forms.
            But was he also shaped by an intuition of the forms before he theorised them?
            The moment you represent that, the graph becomes cyclic.
            The cycle detector is not just a graph algorithm — it is a consistency check
            on whether your knowledge representation can handle this kind of claim.
        """)

# ─────────────────────────────────────────────────────────────────────────────
# DEMO - Main Conditional Block Checking 
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()