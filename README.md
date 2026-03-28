# NanoGraph

**A knowledge graph in pure Python. No libraries. No magic. Under 300 lines.**


---

## The Question This Answers

> Can you implement a knowledge graph — with traversal, path-finding, and cycle detection — in pure Python, with no libraries?

Yes. And you should, at least once.

Most graph libraries are epistemically neutral. They store structure and traverse it efficiently, but they have no opinion about what the structure *means*. When you implement the traversal yourself, you make those choices explicit. The code becomes the epistemology.

---

## What It Demonstrates

A knowledge graph built from `(subject, predicate, object)` triples is the simplest possible knowledge representation. And yet even at this minimal level, interesting things fall out for free:

- **Predicates form an implicit type system.** You never declare that `kant` is a philosopher. The fact that he appears as the subject of `developed` and `influenced` edges tells you.
- **BFS and DFS answer different questions.** Breadth-first finds what is *near* a node — proximity in the network. Depth-first follows a chain to its end — the full extent of a line of reasoning. Same graph. Same data. Different epistemologies.
- **Intersection of query results produces inference.** A concept developed by one thinker and critiqued by another is a *contested concept* — but nobody labelled it that. The label emerges from two queries and a set operation.
- **Cycles are structural contradictions.** In a graph of philosophical influence, a cycle doesn't just mean a loop. It means your knowledge representation contains a claim that cannot be consistently ordered in time. The cycle detector is an inconsistency detector.

---

## How to Run It

No dependencies. Requires Python 3.10+.

```bash
git clone https://github.com/JasonMDev/nano-graph.git
cd nano-graph
python test_nanograph.py   # runs the unit tests
python demo.py        # runs the demo
```

Expected output from the demo includes:

- BFS and DFS traversal from Socrates across a graph of philosophical influence
- All paths from Socrates to existentialism (derived, not stated)
- Contested concepts — developed by one thinker, critiqued by another
- Cycle detection triggered by a representational paradox in Plato's theory of forms

---

## Files


### File Tree Structure
nano-graph/<br>
├── nanograph.py<br>
├── demo.py<br>
├── test_nanograph.py<br>
├── README.md<br>
├── LICENSE<br>


### Files Description
| File | Purpose |
|------|---------|
| `nanograph.py` | The graph class |
| `test_nanograph.py` | The unit tests for the graph class |
| `demo.py` | A worked example using philosophers, concepts, and their relationships |

---

## The Graph Class

```python
from nanograph import NanoGraph

g = NanoGraph()
g.add_triple("kant",      "influenced",  "hegel")
g.add_triple("hegel",     "developed",   "dialectic")
g.add_triple("nietzsche", "critiqued",   "dialectic")

# Traverse
g.bfs("kant")           # breadth-first from kant
g.dfs("kant")           # depth-first from kant

# Query (None = wildcard)
g.query(predicate="critiqued")              # everything ever critiqued
g.query(subject="nietzsche")               # everything nietzsche did
g.query(predicate="developed", obj="dialectic")  # who developed dialectic?

# Analyse
g.find_paths("kant", "dialectic")          # all paths between two nodes
g.has_cycle()                              # consistency check
g.predicate_types()                        # what kinds of relationships exist?
```

---

## Why This Matters

LLMs are very good at sounding true. They are not good at being true.

A language model asked "which philosophers critiqued Hegel's idealism?" will produce a confident, fluent answer. It may be correct. It may not be. You cannot tell, because there is no structure behind the claim — only pattern-matched text.

This graph, loaded with verified triples, answers the same question by traversal. The answer is auditable. Every step is traceable. The reasoning is in the structure, not the fluency.

This is the first piece of a larger argument: that formal knowledge representation — not bigger models or better prompts — is what makes AI systems epistemically trustworthy.

---

## Part of a Larger Project

This sprint is part of an ongoing public portfolio exploring knowledge graphs, inference, and provenance tracking for AI systems.

The through-line: building infrastructure that can tell the difference between a confident assertion and a verified fact.

Follow along: [newsletter link](https://duckduckgo.com)

---

## Licence

MIT — see ['LICENSE'](https://github.com/JasonMDev/nano-graph/blob/main/LICENSE)
