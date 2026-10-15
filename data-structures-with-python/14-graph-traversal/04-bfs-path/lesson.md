---
title: Recover a shortest-hop path from parents
slug: bfs-path
order: 4
language: python
runtime: pyodide
lesson_type: coding
summary: Return the stations on a shortest-hop route, rather than just its length.
seo_title: Recover a shortest-hop path from parents | Python graph algorithms
seo_description: Return the stations on a shortest-hop route, rather than just its
  length.
seo_keywords:
  - Python
  - bfs path
  - graph algorithms
---

Return the stations on a shortest-hop route, rather than just its length.

A distance says how far away a station is. A parent says which earlier station first discovered it. While BFS scans outgoing edges, store that predecessor at the same moment the neighbor becomes seen. Do not replace it on later encounters: the first discovery already has minimum hop count, and preserving it makes equal-length choices follow neighbor order.

The start has parent `None`. The annotation `str | None` means each parent value is either a string label or that stopping marker. It is not an absent dictionary entry. In particular, the empty string is a valid label, so a loop must check `current is not None` rather than the truth value of `current`.

Suppose a parent map contains foyer → None, hall → foyer, loft → hall. Starting at loft produces `["loft", "hall", "foyer"]`. That is useful while walking the links but points backward for a caller. Reverse the completed list once to return foyer, hall, loft. Inserting repeatedly at index zero would move existing elements on every step.

The starter supplies endpoint validation and unreachable handling. Both requested endpoints must exist or `bfs_path` raises `KeyError`. If the target exists but BFS never records it, return an empty list. A start-to-itself query returns a one-label path. `backward_chain` receives a valid BFS parent tree and a recorded target; it does not accept arbitrary cyclic parent maps.

The three checkpoints separate finding parents, following them, and orienting the result. They use independent fixtures, so you can test the backward walk before the final reversal is written. All previous functions remain available.

Parent discovery costs expected O(Vr + Er) time and O(Vr) space. Following and reversing a path of L labels costs O(L) time and storage. No graph edge or neighbor order changes.

Inputs in this module are closed adjacency dictionaries: every neighbor is also a key. Labels are strings. Lists give outgoing neighbors in the order to follow; the algorithms do not sort them or mutate the input. Repeated entries and self-loops are safe for traversal because discovery is remembered. An undirected input stores each edge in both directions. Unless stated otherwise, a missing start raises `KeyError`, and only the start's reachable region is visited.

Costs assume expected constant-time hashing on short labels. V counts vertices and E counts stored neighbor entries. The examples are small enough for readable traces; a visited set is still necessary even on a small cycle.

## Worked trace

![Predecessors for A,B,C,D are [None,A,A,B]. Following D to B to A and reversing gives [A,B,D], a shortest path of two edges; A-C-D ties. A to A gives [A]; Z is unreachable.](graph-traversal-bfs-path-trace.svg)

Unweighted BFS records first discovery; exploring B before C resolves the tie. In this undirected example, each edge is stored in both directions and B precedes C in A's neighbor list.

## Your Tasks

1. Record the discovering vertex as each new neighbor's parent.
2. Build `backward_chain` by following parents from target to `None`.
3. Reverse the collected chain in `bfs_path` before returning it.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
