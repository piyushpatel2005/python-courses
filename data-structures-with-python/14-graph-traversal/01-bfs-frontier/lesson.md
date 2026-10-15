---
title: Discover neighbors before adding them to the BFS queue
slug: bfs-frontier
order: 1
language: python
runtime: pyodide
lesson_type: coding
summary: Build the operation that adds newly found stations to a breadth-first search
  frontier.
seo_title: Discover neighbors before adding them to the BFS queue | Python graph algorithms
seo_description: Build the operation that adds newly found stations to a breadth-first
  search frontier.
seo_keywords:
  - Python
  - bfs frontier
  - graph algorithms
---

Build the operation that adds newly found stations to a breadth-first search frontier.

The frontier contains discovered vertices that still need their outgoing edges examined. Breadth-first search (BFS) uses a queue: remove from the left and add on the right. That order lets every vertex one edge away be examined before vertices two edges away. `collections.deque` supplies `popleft()` and `append()` without the shifts caused by removing the first item of a list.

Discovery is earlier than processing. Suppose two queued stations both lead to the loading bay. Mark the bay as seen when the first station adds it, not when it eventually leaves the queue. The second station then skips it. This keeps one queue entry per vertex, even when several routes meet or an input list repeats a neighbor.

The helper receives three mutable objects. `neighbors` is read-only input; `seen` and `frontier` belong to the caller and must change in place. The supplied loop and condition locate new labels. Your two edits record discovery and schedule the work. Step 1 can pass even while the queue remains empty: its test inspects only the discovery set. Step 2 checks that new labels go to the queue tail in neighbor order. Together, marking and enqueueing ensure repeated neighbor entries are scheduled only once.

For example, begin with `seen = {"oven"}` and a queue containing `"oven"`. Discovering `["rack", "sink", "rack"]` adds two labels, not three. Their order in the queue is rack then sink. Sets provide membership, but we never iterate the set to choose the queue order.

One call examines d neighbor entries in expected O(d) time and adds at most d set and queue entries. A full BFS will reuse this helper for each processed vertex.

Inputs in this module are closed adjacency dictionaries: every neighbor is also a key. Labels are strings. Lists give outgoing neighbors in the order to follow; the algorithms do not sort them or mutate the input. Repeated entries and self-loops are safe for traversal because discovery is remembered. An undirected input stores each edge in both directions. Unless stated otherwise, a missing start raises `KeyError`, and only the start's reachable region is visited.

Costs assume expected constant-time hashing on short labels. V counts vertices and E counts stored neighbor entries. The examples are small enough for readable traces; a visited set is still necessary even on a small cycle.

## Worked trace

![BFS from A has queue [B, C] after A, then [C, D] after B. D is marked when enqueued, so C does not enqueue it again; the queue spans adjacent distance layers.](graph-traversal-bfs-frontier-trace.svg)

FIFO frontier has its front at left; discover B before C and mark on enqueue. In this undirected example, each edge is stored in both directions and B precedes C in A's neighbor list.

## Your Tasks

1. Mark each unseen neighbor in `seen` when it is discovered.
2. Append that newly discovered neighbor to the queue.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
