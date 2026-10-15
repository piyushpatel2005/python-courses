---
title: Restart BFS to find undirected components
slug: connected-components
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: Group every station by which other stations it can reach in an undirected
  network.
seo_title: Restart BFS to find undirected components | Python graph algorithms
seo_description: Group every station by which other stations it can reach in an undirected
  network.
seo_keywords:
  - Python
  - connected components
  - graph algorithms
---

Group every station by which other stations it can reach in an undirected network.

A single BFS stops when its frontier is empty. That proves it has exhausted one reachable region, not necessarily the whole graph. Disconnected stations need another start. A connected component is a maximal group linked by paths; its members need not all have direct edges to one another.

This lesson requires symmetric undirected adjacency lists. It does not compute strongly connected components of a directed graph. With one-way links, reachability from one start need not be mutual, so the same restart recipe would not define the grouping promised here. Symmetry is an input precondition, not a new validation task.

The outer loop visits keys in dictionary insertion order. When a key has not been assigned to an earlier component, the supplied `collect_component` calls the completed BFS. Your first change records all returned members in the outer seen set. Your second change retains the member list as one group. The BFS list gives each group its internal order; the first unseen key determines group order.

For a network with west connected to east and a separate shed, starting at west yields west, east. Recording both means the outer loop skips east. It then starts again at shed and stores a singleton group. An empty graph returns an empty list; an isolated station is a real one-member component.

Although the helper creates a fresh local BFS seen set, the components are disjoint. Once the outer set is updated, no vertex starts a redundant search. Across all calls, the function takes expected O(V + E) time and O(V) total working and result storage. Missing the shared update can repeat entire traversals, even if a small example looks plausible.

Earlier functions are unchanged. The component helper has no hidden dependencies on tests: the complete BFS and its queue helper are included in this file.

## Worked trace

![A shared visited set groups vertices into [A,B], [C,D] and [Z]. After finishing A's component, the outer scan restarts at C and then Z, giving three components.](graph-traversal-connected-components-trace.svg)

Undirected graph; isolated vertices count, and an empty graph has zero components.

## Your Tasks

1. Add the collected component members to the shared `seen` set.
2. Append each newly collected component to `groups`.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
