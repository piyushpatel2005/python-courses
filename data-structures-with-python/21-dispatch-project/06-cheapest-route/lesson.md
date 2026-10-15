---
title: "Return a cheapest weighted route"
slug: cheapest-route
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: "Reconstruct a cheapest route from a supplied local Dijkstra helper."
seo_title: "Return a cheapest weighted route in Python"
seo_description: "Reconstruct a cheapest route from a supplied local Dijkstra helper."
seo_keywords:
  - Python
  - cheapest-route
hints:
  - "Zero is a reachable cost; only infinity means no route. Reverse the backward predecessor chain."
---

The fewest roads may not give the cheapest trip. The supplied `cheapest_route(start, destination)` returns `(cost, path)`, where path is a list of site IDs. Existing sites with no route return `(None, [])`; an existing site routed to itself returns `(0, [start])`. Missing names raise `KeyError`.

This stage supplies `_distances(start)`, a local Dijkstra helper rather than importing a class from another lesson. It returns distance and predecessor dictionaries. Distances start at infinity except for the source. The heap stores `(distance, sequence, site)`, and the sequence counter prevents site names from settling ties. Each successful relaxation updates the predecessor and pushes the improved distance. A popped entry whose distance no longer matches the dictionary is stale and is skipped.

Read that helper and the supplied route wrapper before completing the two result helpers. The constructor already rejects negative weights, which Dijkstra requires. Zero-cost edges are allowed. Equal-cost candidates do not replace predecessors: the first strict improvement wins, with input neighbor order and heap sequence making that policy deterministic. Self-loops cannot improve a nonnegative distance.

For example, depot → yard costing 9 can lose to depot → store → yard costing 2 + 3. Once the helper finishes, start at the destination and follow predecessors backward to the source. Append each site, then reverse the collected list. A missing predecessor on the reachable source is expected; it marks the end of reconstruction.

The lazy heap can contain O(E) entries. The supplied helper takes O(V + E log(E+1)) time and O(V + E) working space; reconstruction adds at most O(V) time and output space. This bound describes this implementation, not every possible Dijkstra variant.

The method is a read-only query. It must not dispatch a job or alter the copied network. The final session will combine this result with catalog lookup and reachability, while preserving the separate contracts of those operations.

## Supplied setup and small steps

The supplied route wrapper validates sites, runs the local Dijkstra helper, and combines cost with your reconstructed path. First recognize an unreachable distance. Then reconstruct a path whose predecessor chain is known to be valid; this helper never receives an unreachable target.

## Your Tasks

1. Complete `route_exists(distance, destination)` to distinguish infinity from every reachable cost, including zero.
2. Complete `rebuild_path(previous, start, destination)` to follow a valid predecessor chain and return the path in forward order.

Edit `main.py`. Run should find the cheaper two-road route rather than the direct road. Submit checks the same operation on additional small cases.
