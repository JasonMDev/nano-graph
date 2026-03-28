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

# TODO: Add imports here

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
    print(f"{'Subject':<15} {'Predicate':<15} {'Object':<25}")
    print("-" * 55)
    for subject, predicate, obj in TRIPLES:
        print(f"{subject:<15} {predicate:<15} {obj:<25}")


# ── Create sections ──────────────────────────────────────────────────────────

def section(title: str) -> None:
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print(f"{'─' * 60}")

# ─────────────────────────────────────────────────────────────────────────────
# DEMO - Main Function
# ─────────────────────────────────────────────────────────────────────────────

def main():

    section("DISPLAY TRIPLES")
    displayTriples(TRIPLES)



# ─────────────────────────────────────────────────────────────────────────────
# DEMO - Main Conditional Block Checking 
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()