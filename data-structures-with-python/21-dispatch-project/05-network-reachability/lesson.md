---
title: "Check directed network reachability"
slug: network-reachability
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: "Check directed road reachability with BFS without changing dispatch state."
seo_title: "Check directed network reachability in Python"
seo_description: "Check directed road reachability with BFS without changing dispatch state."
seo_keywords:
  - Python
  - network-reachability
hints:
  - "Mark a neighbor seen at the moment it joins the frontier."
---

A job can be known and queued even when its destination is unreachable from the current depot. Add a query that checks the road map before a dispatcher chooses to act. This method reports reachability; it does not mutate queues or complete jobs.

The constructor copied a directed weighted adjacency dictionary. Each key is a site, and each outgoing edge is `(neighbor, weight)`. A listed road permits travel only in that direction. Ignore weights for reachability: any sequence of directed edges establishes a path, regardless of total cost.

The supplied `can_reach(start, destination)` uses breadth-first search. Validate both site names first and raise `KeyError` if either is missing. An existing site reaches itself by a path with zero edges. Start a deque with the starting site and mark it seen immediately. When exploring a neighbor for the first time, mark it before enqueueing it so converging roads cannot enqueue it repeatedly.

For example, roads depot → shed and shed → dock allow depot to reach dock. They do not imply that dock can return to depot. A self-loop should not trap the search, and a disconnected site remains unreachable. Explore neighbors in their stored order. The returned value is only a boolean, but the queue must still expand sites breadth-first and at most once.

Stop when you find the destination, or return `False` once the frontier is empty. Each reachable site enters the queue at most once. The search uses O(V + E) time in the worst case and O(V) working space, with expected constant-time set membership under normal hashing assumptions.

The supplied checkpoint asks both directions on a one-way route. Reachability answers whether a trip is possible; the next method will compare its cost. Keep the existing intake, priority, history, and catalog behavior unchanged; the new method only reads the map.

## Supplied setup and small steps

The BFS queue loop is supplied. You implement endpoint validation and one frontier-expansion step. The second test calls that step twice to catch delayed visited marking without requiring a completed traversal.

## Your Tasks

1. Complete `check_sites(start, destination)` to reject either missing endpoint with `KeyError`.
2. Complete `queue_unseen(site, seen, frontier)` to append unvisited neighbors in stored order, marking each on enqueue.

Edit `main.py`. Run compares travel in both directions on the same one-way road. Submit checks the same operation on additional small cases.
