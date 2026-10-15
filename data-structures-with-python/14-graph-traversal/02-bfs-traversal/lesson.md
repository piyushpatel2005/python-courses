---
title: Process the BFS queue in layers
slug: bfs-traversal
order: 2
language: python
runtime: pyodide
lesson_type: coding
summary: Turn the discovery helper into a traversal that returns the order of processed
  stations.
seo_title: Process the BFS queue in layers | Python graph algorithms
seo_description: Turn the discovery helper into a traversal that returns the order
  of processed stations.
seo_keywords:
  - Python
  - bfs traversal
  - graph algorithms
---

Turn the discovery helper into a traversal that returns the order of processed stations.

The starter retains `discover` from the previous lesson. The queue begins with the start, and the seen set already contains it. Inside the supplied loop, `popleft()` removes the oldest waiting vertex. Record that vertex, then pass its outgoing list to `discover`. The helper both marks and enqueues new neighbors, so the loop never needs to schedule a vertex twice.

Consider an entrance connected to a studio and a garden, in that order. The studio leads to a darkroom. After processing the entrance, the queue is studio, garden. Processing the studio adds the darkroom at the right, behind the garden. BFS therefore visits entrance, studio, garden, darkroom. A stack would reach the darkroom earlier and would not preserve breadth-first layers.

The return value is a list, not a set. Several BFS orders can be mathematically valid; this course makes the answer reproducible by following supplied neighbor order. Dictionary key order does not override a vertex's neighbor list. Vertices in an unrelated component do not appear at all.

Validate the start before creating traversal state. An unknown label is different from an isolated vertex: the first is an error, while the second produces a one-item visit list. The temporary return below the validation checkpoint keeps the starter runnable; it is unreachable after the requested check is complete.

Each reachable vertex enters and leaves the queue once. Each of its neighbor entries is examined once. If Vr and Er describe the reachable region, traversal takes expected O(Vr + Er) time and O(Vr) auxiliary space, including the queue, set, and returned order. The graph itself is not copied.

Inputs in this module are closed adjacency dictionaries: every neighbor is also a key. Labels are strings. Lists give outgoing neighbors in the order to follow; the algorithms do not sort them or mutate the input. Repeated entries and self-loops are safe for traversal because discovery is remembered. An undirected input stores each edge in both directions. Unless stated otherwise, a missing start raises `KeyError`, and only the start's reachable region is visited.

Costs assume expected constant-time hashing on short labels. V counts vertices and E counts stored neighbor entries. The examples are small enough for readable traces; a visited set is still necessary even on a small cycle.

## Worked trace

![BFS from A visits [A, B, C, D]. After each visit the queue is [B,C], [C,D], [D], then []; isolated Z is never enqueued.](graph-traversal-bfs-traversal-trace.svg)

Visit B before C and mark vertices on discovery; traverse only A's reachable component. In this undirected example, each edge is stored in both directions and B precedes C in A's neighbor list.

## Your Tasks

1. Raise `KeyError` when `start` is not a graph key.
2. Record each dequeued vertex in `order`.
3. Use `discover` to queue its unseen outgoing neighbors.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
