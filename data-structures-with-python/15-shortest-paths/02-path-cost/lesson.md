---
title: Add the weights along a proposed path
slug: path-cost
order: 2
language: python
runtime: pyodide
lesson_type: coding
summary: Measure a proposed route before trying to find the cheapest one.
seo_title: Add the weights along a proposed path | Python graph algorithms
seo_description: Measure a proposed route before trying to find the cheapest one.
seo_keywords:
  - Python
  - path cost
  - graph algorithms
---

Measure a proposed route before trying to find the cheapest one.

A path is an ordered list of vertices. For each consecutive pair, look for an outgoing edge from the first label to the second and add its weight. Counting vertices or counting edges answers a different question. Two paths with the same number of edges can have different total costs.

For example, a trip from dock through depot to market might cost 3 + 8 = 11, while dock through square to market costs 6 + 1 = 7. Both take two hops. BFS can minimize the hop count but cannot choose the cheaper route when weights differ.

The first helper scans one source's outgoing list. Unpack each tuple into `neighbor` and `weight`, and return the weight when the neighbor matches. The supplied final `KeyError` handles a missing arc. Do not use a truth-value check on the weight: zero must be returned as an ordinary valid cost. This lookup never invents a reverse arc.

The path function already validates the graph and every label in the supplied path. Complete its accumulation loop. `zip(path, path[1:])` pairs consecutive labels; for three labels it yields two pairs. An empty path and a one-vertex path cost zero because neither crosses an edge. A one-vertex path still requires that label to exist. Repeated vertices are permitted when their consecutive arcs exist, so this measures walks as well as simple paths.

The supplied `validate_weighted` checks endpoint closure, integer nonnegative weights, and duplicate outgoing targets. It is included here and in later lessons so manually supplied dictionaries obey the same representation as the builder. It does not alter the input.

Validation costs expected O(V + E). A path of L labels then performs L−1 outgoing-list scans, costing the sum of those source degrees, plus O(L) for the sliced labels used by `zip`. This list representation does not promise constant-time edge lookup. The resulting cost is a measurement, not a proof that the route is optimal.

The weighted representation is `dict[str, list[tuple[str, int]]]`: each outgoing entry is `(neighbor, weight)`. Every neighbor must be a key. Labels are strings; weights are nonnegative integers (not booleans). Zero is a real cost. Lists retain insertion order, self-loops are allowed, and each source has at most one entry for a given target. Reverse edges are separate. Supplied validation checks the entire graph, including unreachable components, before a shortest-path search begins.

## Worked trace

![Path A-B-D accumulates costs [0,6,7]; A-C-D accumulates [0,2,5]. Both use two edges, but A-C-D costs 5 rather than 7; a one-vertex path costs 0.](shortest-paths-path-cost-trace.svg)

Path cost sums directed edge weights, not vertices or edge count.

## Your Tasks

1. Return the matching outgoing edge's weight in `edge_weight`.
2. Accumulate the weight of every consecutive pair in `path_cost`.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
