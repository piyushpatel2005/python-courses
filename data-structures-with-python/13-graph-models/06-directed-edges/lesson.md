---
title: "Store directed edges in only one list"
slug: "directed-edges"
order: 6
language: "python"
runtime: "pyodide"
lesson_type: "coding"
summary: "Model a one-way handoff between workshop stages."
seo_title: "Store directed edges in only one list | Python graph algorithms"
seo_description: "Model a one-way handoff between workshop stages."
seo_keywords:
  - "Python"
  - "directed edges"
  - "graph algorithms"
---

Model a one-way handoff between workshop stages.

A directed edge has a source and a destination. A handoff from inspection to packing says that packing may follow inspection; it does not create a handoff back to inspection. The order of the arguments now carries meaning.

This lesson intentionally starts a fresh `DirectedGraph` class. Its supplied constructor and `add_vertex` use the same independent-list representation as before. We do not inherit the undirected mutation methods: their promise to update both endpoints would be wrong for this model. Each value in `adj: dict[str, list[str]]` contains outgoing neighbors only.

Implement one directed insertion. Check that both endpoints exist before changing state, raising `KeyError` otherwise. Reject a self-loop with `ValueError`, as in the previous model. Return `False` if the destination is already in the source list. For a new edge append only to the source list and return `True`. The destination's own list is unchanged.

A reverse edge is a separate edge. If inspection points to packing, adding packing-to-inspection is allowed and creates a directed cycle of length two. Duplicate detection therefore checks the ordered pair, not an unordered pair of labels. Preserve each source's neighbor insertion order rather than sorting it.

Do not infer reachability from a single list. One edge makes two vertices adjacent in a particular direction; a path may require several edges. The next module will follow those paths. For now, inspect which list changes after each insertion. An outgoing duplicate check costs O(outdegree(source) + 1) time, including the amortized append, and a successful insertion adds O(1) space. The short-label dictionary operations use their expected cost model.

## A small example

```python
handoffs = {"inspect": ["pack"], "pack": []}
print("pack" in handoffs["inspect"])  # True
print("inspect" in handoffs["pack"])  # False
```

## Worked trace

![Directed edges A to B and B to D give A:[B], B:[D], C:[], D:[]. The A,B,D matrix is [[0,1,0],[0,0,1],[0,0,0]]; reverse edges are absent.](graph-models-directed-edges-trace.svg)

Lists store outgoing neighbors; the displayed matrix omits isolated C.

## Your Tasks

1. Raise `KeyError` if either endpoint is missing, before any mutation.
2. Reject a self-loop with `ValueError`.
3. Return `False` for an edge already present.
4. Append the new outgoing entry and return `True`.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
