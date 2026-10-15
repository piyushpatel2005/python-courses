---
title: "Count incoming and outgoing edges"
slug: "graph-degrees"
order: 8
language: "python"
runtime: "pyodide"
lesson_type: "coding"
summary: "Find which workflow stages receive handoffs and which stages send them."
seo_title: "Count incoming and outgoing edges | Python graph algorithms"
seo_description: "Find which workflow stages receive handoffs and which stages send them."
seo_keywords:
  - "Python"
  - "graph degrees"
  - "graph algorithms"
---

Find which workflow stages receive handoffs and which stages send them.

A directed vertex has two degree counts. Its outdegree counts edges leaving it; its indegree counts edges entering it. A source can have no incoming edges but several outgoing edges. A terminal stage can have the opposite pattern.

Return a dictionary mapping every vertex to `(indegree, outdegree)`. The annotation `dict[str, tuple[int, int]]` expresses that shape: string keys, with two integer counts in each value. Include isolated vertices as `(0, 0)` and keep dictionary insertion order. Counts must describe the supplied adjacency mapping without changing its lists.

Initialize an incoming counter for every key, including vertices that appear in no neighbor list. Then scan outgoing lists. Each edge contributes one to its target's incoming count. A vertex's outgoing count is the number of distinct targets in its own list. This exercise treats repeated entries as repeated records of the same edge, so count them once per source. `dict.fromkeys(neighbors)` is a convenient insertion-preserving way to visit each target once.

A supplied self-loop contributes one incoming and one outgoing edge to the same vertex. This conversion function accepts loops even though our earlier builder rejected them; it is a separate read-only analysis contract. Input must be closed: every target is a key. For an undirected simple graph represented symmetrically, incoming and outgoing counts happen to match its ordinary degree. Do not divide either count by two.

With V vertices and E stored neighbor entries, initializing counters and scanning the lists takes expected O(V + E) time. The result and incoming counters use O(V) space; per-list deduplication needs at most O(V) temporary entries for a closed graph. This cost assumes expected constant-time hash operations on short labels.

## A small example

```python
arrows = {"mix": ["bake"], "bake": [], "cool": ["bake"]}
print(sum("bake" in targets for targets in arrows.values()))  # 2
```

## Your Tasks

1. Count incoming edges once per distinct source-target pair.
2. Count each vertex's distinct outgoing targets.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
