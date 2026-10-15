---
title: Read a weighted shortest route from its parents
slug: reconstruct-weighted-path
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: Turn a completed weighted search into a forward route that a caller can follow.
seo_title: Read a weighted shortest route from its parents | Python graph algorithms
seo_description: Turn a completed weighted search into a forward route that a caller
  can follow.
seo_keywords:
  - Python
  - reconstruct weighted path
  - graph algorithms
---

Turn a completed weighted search into a forward route that a caller can follow.

Dijkstra's distance table tells the cost of each cheapest route. Its parent table records the last edge responsible for each strict improvement. Following those links backward reconstructs a route with that cost. Use the parents from the same search run as the distances; mixing tables from different sources has no meaningful interpretation.

The mechanics resemble BFS reconstruction, but the parent meaning is different. BFS saves the first discovery. Dijkstra can replace a parent's value when a cheaper route appears. If depot was first reached directly from dock at cost 9, then improved through office to cost 6, depot's final parent is office. Reconstructing from an old parent would return a route that does not match the final distance.

Begin at the requested target, append it, then repeatedly replace the current label with its parent. Stop at `None`. The collected list runs backward, so reverse it once. The separate `weighted_chain` helper makes that backward walk independently testable before the final forward-path checkpoint.

The supplied wrapper checks reachability before following any links. Every vertex has a parent entry, and both the source and unreachable vertices have parent `None`. That marker alone cannot distinguish them. A finite distance identifies a reachable vertex; infinity means return an empty path. A missing target raises `KeyError`. A source-to-itself route contains just the source, not an empty list.

For example, parents may record cellar → pantry → kitchen → None. The backward helper returns cellar, pantry, kitchen; the caller receives kitchen, pantry, cellar. An empty string may be a label, so compare the stopping marker with `is not None` rather than relying on truthiness.

Inputs to reconstruction must be valid completed search tables, not arbitrary cyclic parent mappings. For a route of L vertices, the walk and reversal take O(L) time and O(L) output space. No new graph search is needed, and no input dictionary is changed. The included `path_cost` helper can independently check that a reconstructed route's edge sum equals its recorded shortest distance.

## Worked trace

![Predecessors for A,B,C,D,Z are [None,A,A,C,None]. Walking backward from D gives [D,C,A]; reversing once returns [A,C,D]. Reachability must be checked before following predecessors.](shortest-paths-reconstruct-weighted-path-trace.svg)

Use the weighted search's predecessor table; None alone does not distinguish source from unreachable.

## Your Tasks

1. Follow the weighted parent links from target to the `None` marker.
2. Reverse the collected chain to return source-to-target order.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
