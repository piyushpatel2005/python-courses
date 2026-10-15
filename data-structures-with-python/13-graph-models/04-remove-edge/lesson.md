---
title: "Remove an edge without removing its vertices"
slug: "remove-edge"
order: 4
language: "python"
runtime: "pyodide"
lesson_type: "coding"
summary: "Remove one workshop connection while leaving both stations registered."
seo_title: "Remove an edge without removing its vertices | Python graph algorithms"
seo_description: "Remove one workshop connection while leaving both stations registered."
seo_keywords:
  - "Python"
  - "remove edge"
  - "graph algorithms"
---

Remove one workshop connection while leaving both stations registered.

Removing an undirected connection is another two-list operation. Delete the destination from the source list and the source from the destination list. Removing only one entry would change the meaning of the graph depending on which endpoint you start from.

This method has a forgiving absence policy. Return `False` if either endpoint is missing or if the edge does not exist. Unlike adding an invalid edge, removing an absent edge is an idempotent request: repeating a successful removal changes nothing the second time. A self-pair also returns `False` because this graph cannot contain self-loops.

When the edge exists, remove its two entries and return `True`. Both dictionary keys remain, even if they now have empty lists. Keeping the vertices makes it possible to reconnect them later. Other neighbors keep their relative order; deleting the middle element from a Python list already has that behavior.

Suppose the kiln has neighbors `["rack", "sink", "door"]`. Removing the kiln-to-sink link leaves `["rack", "door"]`; the sink loses only `"kiln"`. The operation must not clear the kiln's entire list. The supplied methods already guarantee unique symmetric entries, so you do not need a loop that removes duplicate copies or repairs malformed input.

The starter carries forward the completed constructor and insertion methods. Treat `adj: dict[str, list[str]]` as the representation maintained by those methods, not as an arbitrary external dictionary to sanitize. A list removal searches for the entry and shifts later references. Removing both halves takes O(d(a) + d(b) + 1) time and O(1) auxiliary space under the same short-label hash model.

## A small example

```python
neighbors = ["rack", "sink", "door"]
neighbors.remove("sink")
print(neighbors)  # ['rack', 'door']
```

## Worked trace

![Removing A-B leaves A:[C], B:[], C:[A]: both directions of A-B disappear, but vertex B and edge A-C remain. Repeating the removal returns False without changing the graph.](graph-models-remove-edge-trace.svg)

Undirected edge removal keeps vertex keys and removes both neighbor references.

## Your Tasks

1. Return `False` when the requested edge is absent.
2. Remove both entries of an existing edge and return `True`.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
