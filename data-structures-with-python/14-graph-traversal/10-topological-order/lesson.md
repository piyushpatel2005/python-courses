---
title: Schedule directed dependencies with topological order
slug: topological-order
order: 10
language: python
runtime: pyodide
lesson_type: coding
summary: Order workshop stages so every prerequisite appears before the stage that
  depends on it.
seo_title: Schedule directed dependencies with topological order | Python graph algorithms
seo_description: Order workshop stages so every prerequisite appears before the stage
  that depends on it.
seo_keywords:
  - Python
  - topological order
  - graph algorithms
---

Order workshop stages so every prerequisite appears before the stage that depends on it.

A directed edge u → v now means u must happen before v. A topological order respects every such edge, but it need not be unique. It exists only when the graph has no directed cycle. A cycle would require a stage to precede itself through a chain of dependencies.

Kahn's algorithm counts incoming edges. A count of zero means no unfinished prerequisite remains, so that vertex is ready. The supplied setup places all initially ready vertices into a queue in dictionary key order. Remove one, record it, and subtract one from each outgoing target's count. When a count reaches zero, append that target to the ready queue.

Imagine frame and wiring both precede inspection. Processing frame reduces inspection's count from two to one, so inspection must wait. Processing wiring reduces it to zero, making it ready. Enqueuing whenever the count merely decreases would schedule work before all prerequisites were satisfied.

The first checkpoint builds the counts independently. The second releases dependencies during the supplied queue loop. The last detects failure: if fewer than V vertices were output, remaining vertices are blocked by a cycle. Raise `ValueError` rather than returning a plausible but incomplete schedule. The empty graph returns an empty order.

This function accepts closed directed lists, including repeated edge records. Count and decrement every stored occurrence consistently; do not deduplicate only one side. A self-loop prevents its vertex from reaching zero. Initial ties follow key order, while newly released ties follow outgoing neighbor order. The algorithm does not sort either list.

Each vertex enters the ready queue at most once, and each stored edge is counted and later released once. Expected time is O(V + E) with O(V) auxiliary storage. Unlike the preceding cycle visitor, this implementation needs no recursion. The completed order is a dependency schedule, not a shortest path or a DFS visit list.

## Worked trace

![Indegrees for A,B,C,D start at [0,1,1,2]. Removing A makes [B,C] ready; removing B then C makes D ready, producing topological order [A,B,C,D].](graph-traversal-topological-order-trace.svg)

Kahn's algorithm processes zero-indegree vertices; fewer than V outputs signals a directed cycle.

## Your Tasks

1. Count every incoming stored edge in `initial_indegrees`.
2. Release each outgoing dependency and enqueue its target when its count reaches zero.
3. Raise `ValueError` if the queue ends before all vertices are output.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
