---
title: Store directed edges with nonnegative integer costs
slug: weighted-adjacency
order: 1
language: python
runtime: pyodide
lesson_type: coding
summary: Give each directed connection a cost so a route planner can compare travel
  expense rather than hop count.
seo_title: Store directed edges with nonnegative integer costs | Python graph algorithms
seo_description: Give each directed connection a cost so a route planner can compare
  travel expense rather than hop count.
seo_keywords:
  - Python
  - weighted adjacency
  - graph algorithms
---

Give each directed connection a cost so a route planner can compare travel expense rather than hop count.

The previous adjacency lists stored only destination labels. This module starts a fresh `WeightedGraph` variation: each neighbor entry is a two-item tuple containing a label and an integer weight. The constructor is supplied and gives each vertex a separate empty list. Earlier unweighted builders are not changed or inherited.

For example, `{"dock": [("market", 7)], "market": []}` describes a one-way trip costing seven units. The market does not automatically gain a return trip. An empty outgoing list may belong to a destination that receives many routes; it does not necessarily mean the vertex is isolated.

This course uses nonnegative integer costs, including zero. Reject a negative number, a float, or a boolean with `ValueError`. Python treats booleans as a kind of integer, so `type(weight) is int` expresses our deliberately narrower domain. Restricting weights to integers also avoids NaN and infinity as input costs. Later, infinity will be an internal marker for an unreachable distance, not an edge weight.

Check endpoints before weights, and both before mutation. An unknown endpoint raises `KeyError`; it must not silently create a new vertex. If the ordered pair already exists, return `False` without changing its original weight. Updating a cost is outside this builder's contract. A new arc appends once and returns `True`. Self-loops are allowed; nonnegative loops cannot improve a shortest route to their own vertex.

Neighbor order is insertion order, including equal-weight alternatives. Each insertion scans the source's outgoing list for a duplicate, taking O(outdegree(source) + 1) expected time under short-label hashing and adding O(1) storage. The graph uses O(V + E) storage. These are algorithmic counts; arithmetic on very large Python integers has an additional size-dependent cost.

## Worked trace

![Outgoing weighted lists are A:[(B,6),(C,2)], B:[(D,1)], C:[(D,3)], D:[] and Z:[]. D has incoming edges but no outgoing edges; Z is isolated.](shortest-paths-weighted-adjacency-trace.svg)

Directed adjacency entries pair neighbor with weight; do not add reverse arcs.

## Your Tasks

1. Reject a missing endpoint with `KeyError`.
2. Reject a negative or non-integer weight with `ValueError`.
3. Return `False` when this directed edge already exists.
4. Append the new `(target, weight)` entry and return `True`.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
