---
title: "Add both halves of an undirected edge"
slug: "add-undirected-edge"
order: 3
language: "python"
runtime: "pyodide"
lesson_type: "coding"
summary: "Connect two registered workshop stations without creating a one-way link by accident."
seo_title: "Add both halves of an undirected edge | Python graph algorithms"
seo_description: "Connect two registered workshop stations without creating a one-way link by accident."
seo_keywords:
  - "Python"
  - "add undirected edge"
  - "graph algorithms"
---

Connect two registered workshop stations without creating a one-way link by accident.

An undirected edge can be followed in either direction. In our adjacency lists that one logical edge occupies two entries: the destination appears in the source list, and the source appears in the destination list. The invariant is symmetry: `b in adj[a]` exactly when `a in adj[b]`.

The shape is `dict[str, list[str]]`. Labels identify vertices; list positions record insertion order, not distances. Before mutating either list, verify that both endpoints are keys. Raise `KeyError` if either is missing. Check both endpoints first so a rejected request cannot leave half an edge behind. Next reject an edge from a vertex to itself with `ValueError`. This graph deliberately models a simple network without self-loops.

If the edge already exists, return `False` and leave both lists unchanged. Otherwise append one entry to each list and return `True`. Asking for the same connection in reverse order is also a duplicate. For example, once a kiln and drying rack are linked, connecting the rack to the kiln adds nothing.

Follow the mutation on paper: start with two empty lists, append the second label to the first list, then append the first label to the second list. Now inspect an unrelated isolated vertex; its list must still be empty. Do not call `add_vertex` from this operation, because silently creating a misspelled station would violate the missing-endpoint contract.

A duplicate check scans only a's neighbor list. With degree d(a), insertion takes expected amortized O(d(a) + 1) time, including the two list appends, and O(1) additional storage for a successful edge. Dictionary lookups assume short labels and expected constant-time hashing.

## A small example

```python
adj = {"kiln": ["rack"], "rack": ["kiln"], "sink": []}
print("kiln" in adj["rack"])  # True
print(adj["sink"])  # []
```

## Worked trace

![Adding A-B to A:[], B:[], C:[] returns True and stores A:[B], B:[A], C:[]. Repeating B-A returns False without adding a parallel edge.](graph-models-add-undirected-edge-trace.svg)

Simple undirected graph: reject missing endpoints and self-loops before mutation.

## Your Tasks

1. Raise `KeyError` if either endpoint is missing, before any mutation.
2. Reject a self-loop with `ValueError`.
3. Return `False` for an edge already present.
4. Append the new two symmetric entries and return `True`.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
