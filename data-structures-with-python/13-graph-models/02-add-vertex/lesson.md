---
title: "Add a vertex without erasing its neighbors"
slug: "add-vertex"
order: 2
language: "python"
runtime: "pyodide"
lesson_type: "coding"
summary: "Let an existing graph register one more station while keeping its current connections."
seo_title: "Add a vertex without erasing its neighbors | Python graph algorithms"
seo_description: "Let an existing graph register one more station while keeping its current connections."
seo_keywords:
  - "Python"
  - "add vertex"
  - "graph algorithms"
---

Let an existing graph register one more station while keeping its current connections.

The constructor creates the first collection of vertices. `add_vertex` handles a later arrival. Its job is deliberately small: establish one key without changing any existing key or neighbor list.

Membership must be checked before assignment. The expression `vertex in self.adj` asks whether the label is registered, even when its neighbor list is empty. Testing the list's truth value would confuse an isolated vertex with an absent vertex. Those are different states.

Consider a map with `{"kiln": ["rack"], "rack": ["kiln"]}`. Registering `"sink"` adds one empty list. Registering `"kiln"` again must leave the link to the rack intact. Unconditionally assigning an empty list would erase half of that link and break the undirected representation.

Return `True` only when a new key was inserted; return `False` for an already registered label. This makes the mutation visible without forcing the caller to compare whole dictionaries. The method does not create edges, rearrange labels, or share another vertex's list. The completed constructor is already in the starter, so you can concentrate on this one state transition.

The graph still uses string labels, insertion-ordered neighbor lists, no self-loops, and no parallel edges. Under the expected dictionary cost model, one insertion takes expected amortized O(1) time and adds O(1) storage. Hashing very long labels is additional work; these examples treat labels as short identifiers.

## A small example

```python
registered = {"drying": []}
print("drying" in registered)  # True
print(bool(registered["drying"]))  # False
```

## Worked trace

![Starting with A:[B] and B:[A], adding C returns True and creates C:[]. Adding A again returns False and preserves A:[B], so the existing edge is not lost.](graph-models-add-vertex-trace.svg)

Each new vertex gets a fresh list; adding an existing vertex leaves its neighbors intact.

## Your Tasks

1. Return `False` immediately when `vertex` already exists.
2. Insert a missing vertex with a fresh list and return `True`.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
