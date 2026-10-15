---
title: Keep zero-cost routes distinct from unreachable targets
slug: unreachable-and-zero-weights
order: 7
language: python
runtime: pyodide
lesson_type: coding
summary: Give callers an explicit unreachable result without discarding valid zero-cost
  travel.
seo_title: Keep zero-cost routes distinct from unreachable targets | Python graph
  algorithms
seo_description: Give callers an explicit unreachable result without discarding valid
  zero-cost travel.
seo_keywords:
  - Python
  - unreachable and zero weights
  - graph algorithms
---

Give callers an explicit unreachable result without discarding valid zero-cost travel.

Zero and absence must remain different throughout the pipeline. A tuple `(neighbor, 0)` is an edge. A distance of zero means a route costs nothing, which can happen at the source or along a chain of zero-weight edges. Infinity means no route was found. Testing `if distance` would incorrectly reject every zero-cost destination.

The search implementations already support zero weights. This lesson adds an API boundary: return `(cost, path)` for a reachable target and `(None, [])` for an unreachable one. The annotation `int | None` makes that distinction visible to a caller without requiring them to understand our internal infinity marker. The separate `reachable` predicate receives a value from a validated search table, so it need only distinguish infinity from finite distances.

Consider dock-to-desk at cost zero and desk-to-yard at cost zero. Yard is reachable with path dock, desk, yard and total cost zero. A separate island has no path at all and gets the absent-cost marker. The fact that both zero and `None` are false in a condition is precisely why the API must compare explicitly.

A zero-cost cycle is also valid input. Strict improvement during relaxation prevents the same zero-cost route from being rescheduled forever. It also avoids replacing a settled parent with an equal-cost back edge. You do not need to modify Dijkstra, relaxation, or reconstruction; those completed definitions are supplied unchanged.

The wrapper validates the requested target's existence first. A missing target raises `KeyError`, while a present unreachable target returns the normal absence result. The search validates the source and all graph edges, including disconnected ones. Empty graphs therefore have no valid endpoint query.

This wrapper runs the heap search once and reconstructs at most one route. Time remains O(V + E log(E + 1)) plus O(L) reconstruction, with O(V + E) search space and O(L) returned path space. The final project will reuse one search for several destinations rather than repeating it unnecessarily.

## Worked trace

![Distances from A for A,B,C,D,Z are [0,0,4,0,infinity]. Real zero-weight edges form path A-B-D at cost 0; absent A-Z leaves Z unreachable with no predecessor.](shortest-paths-unreachable-and-zero-weights-trace.svg)

Zero weight is a valid edge, not absence; relax only strict distance improvements.

## Your Tasks

1. Treat every finite distance, including zero, as reachable.
2. Return `(None, [])` for a known but unreachable target.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
