---
title: "Remove a vertex and its incident edges"
slug: "remove-vertex"
order: 5
language: "python"
runtime: "pyodide"
lesson_type: "coding"
summary: "Retire a station without leaving its label in any remaining neighbor list."
seo_title: "Remove a vertex and its incident edges | Python graph algorithms"
seo_description: "Retire a station without leaving its label in any remaining neighbor list."
seo_keywords:
  - "Python"
  - "remove vertex"
  - "graph algorithms"
---

Retire a station without leaving its label in any remaining neighbor list.

Deleting a dictionary key is only part of removing a vertex. Every neighbor still has an entry pointing back to that vertex. Those entries must disappear as well, or a later traversal may try to visit a label that no longer exists.

An edge touching a vertex is called an incident edge. For this undirected graph, the vertex's own neighbor list names exactly the other lists that need repair. The existing `remove_edge` method already knows how to remove one symmetric connection. Reuse it for each incident edge, then delete the vertex key. Return `True` for an existing vertex and `False` for a missing one.

There is a mutation trap here. Calling `remove_edge` shortens the list you are traversing. If you iterate that same list directly, the next item can shift into the position you just passed and be skipped. Take a shallow copy of the neighbor labels before the loop. The strings need no deeper copying; only the changing list structure needs a stable snapshot.

Trace a station linked to three others. The snapshot keeps all three names while the live list shrinks from three entries to two, then one, then none. After deleting the dictionary key, scan the remaining lists mentally: none should contain the retired label. An isolated station takes the shorter path through the same method because its snapshot is empty.

The representation remains `dict[str, list[str]]`, with no self-loops or duplicate edges and insertion order for surviving vertices and neighbors. Reusing list-based edge removal can cost O(d(v)^2 + sum(d(u))) over neighbors u of v, plus constant overhead. The snapshot uses O(d(v)) extra space. Do not label this O(d(v)) time: searching and shifting those lists is real work.

## A small example

```python
pending = ["glaze", "fire", "cool"]
for name in list(pending):
    pending.remove(name)
print(pending)  # []
```

## Worked trace

![Removing A snapshots neighbors [B, C], removes A from both lists, then deletes key A. The result is B:[D], C:[], D:[B], with edge B-D preserved and C isolated.](graph-models-remove-vertex-trace.svg)

Use a neighbor snapshot rather than iterating a list while shrinking it.

## Your Tasks

1. Return `False` for a missing vertex.
2. Remove its incident edges using a snapshot of its neighbors.
3. Delete the now-isolated vertex key and return `True`.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
