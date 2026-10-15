---
title: Settle cheapest distances with scan-based Dijkstra
slug: dijkstra-scan
order: 4
language: python
runtime: pyodide
lesson_type: coding
summary: Build Dijkstra's algorithm using a plain scan to choose the next vertex.
seo_title: Settle cheapest distances with scan-based Dijkstra | Python graph algorithms
seo_description: Build Dijkstra's algorithm using a plain scan to choose the next
  vertex.
seo_keywords:
  - Python
  - dijkstra scan
  - graph algorithms
---

Build Dijkstra's algorithm using a plain scan to choose the next vertex.

At first the source has distance zero and all other vertices have infinity. Infinity means that no route has been found yet. A settled vertex has its final shortest distance. Repeatedly choose the unsettled vertex with the smallest finite tentative distance, settle it, and relax its outgoing edges.

Nonnegative weights make this choice safe. Any route through a still-unsettled vertex already costs at least the selected distance before adding more nonnegative edges. It cannot later make the selected vertex cheaper. Negative edges break that argument; the supplied graph validation rejects them before any search, including negative edges in unreachable components.

Consider dock-to-yard costing 8 and dock-to-desk costing 2, with desk-to-yard costing 3. The first expansion records yard at 8 and desk at 2. The scan chooses desk next and improves yard to 5. Marking yard final at first discovery, as BFS does for hop counts, would freeze the wrong answer.

The initializer and minimum selector are separate helpers so each checkpoint has a small observable outcome. The selector returns `None` when no finite unsettled distance remains. This stops on disconnected graphs without pretending that infinity is a useful route. Scan dictionary entries in order and replace the selected label only for a strictly smaller distance; equal-distance ties keep the earlier key.

The supplied main loop maintains settled state and returns `(distances, parents)`. Every vertex appears in both dictionaries. Unreachable vertices retain infinity and parent `None`; the source also has parent `None`, but its zero distance distinguishes it. Complete the outgoing relaxation loop using the previous lesson's helper.

Each selection examines up to V distances and at most V vertices are selected. Relaxations examine E outgoing entries overall. Time is O(V² + E), with O(V) auxiliary storage. Validation adds expected O(V + E), which does not change that bound. Costs assume short-label hashes and bounded-cost arithmetic.

The weighted representation is `dict[str, list[tuple[str, int]]]`: each outgoing entry is `(neighbor, weight)`. Every neighbor must be a key. Labels are strings; weights are nonnegative integers (not booleans). Zero is a real cost. Lists retain insertion order, self-loops are allowed, and each source has at most one entry for a given target. Reverse edges are separate. Supplied validation checks the entire graph, including unreachable components, before a shortest-path search begins.

## Worked trace

![After settling A, distances for A,B,C,D,Z are [0,6,2,infinity,infinity]. Settling C relaxes D to 5; settlement order is A,C,D,B. Z stays at infinity and the scan stops.](shortest-paths-dijkstra-scan-trace.svg)

Dijkstra requires nonnegative weights and selects the smallest unsettled distance.

## Your Tasks

1. Create an infinity distance entry for every graph vertex.
2. Set the start vertex's distance to zero.
3. Select the smallest finite unsettled distance, preserving first-seen ties.
4. Relax every outgoing edge of the selected vertex.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
