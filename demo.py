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

# ─────────────────────────────────────────────────────────────────────────────
# DATA - Triples
# ─────────────────────────────────────────────────────────────────────────────

TRIPLES = [
    # Lines of influence between thinkers
    ("socrates",     "influenced",  "plato"),
    ("plato",        "influenced",  "aristotle"),
    ("aristotle",    "influenced",  "kant"),
    ("kant",         "influenced",  "hegel"),
    ("kant",         "influenced",  "wittgenstein"),
    ("hegel",        "influenced",  "marx"),
    ("hegel",        "influenced",  "nietzsche"),
    ("hegel",        "influenced",  "heidegger"),
    ("nietzsche",    "influenced",  "heidegger"),
    ("heidegger",    "influenced",  "sartre"),

    # Concepts each thinker developed
    ("plato",        "developed",   "the_forms"),
    ("plato",        "developed",   "logos"),
    ("kant",         "developed",   "categorical_imperative"),
    ("hegel",        "developed",   "dialectic"),
    ("hegel",        "developed",   "idealism"),
    ("marx",         "developed",   "materialism"),
    ("nietzsche",    "developed",   "will_to_power"),
    ("wittgenstein", "developed",   "language_games"),
    ("heidegger",    "developed",   "being"),
    ("sartre",       "developed",   "existentialism"),

    # Concepts each thinker critiqued
    ("aristotle",    "critiqued",   "the_forms"),
    ("marx",         "critiqued",   "idealism"),
    ("nietzsche",    "critiqued",   "categorical_imperative"),
    ("wittgenstein", "critiqued",   "logos"),
]

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


    # ── 4. Contested concepts ────────────────────────────────────────────────


    # ── 5. Cycle detection ───────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# DEMO - Main Conditional Block Checking 
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()