---
title: Follow one branch with recursive DFS
slug: dfs-recursive
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: Use recursive calls to follow a route as far as possible before returning
  to a waiting neighbor.
seo_title: Follow one branch with recursive DFS | Python graph algorithms
seo_description: Use recursive calls to follow a route as far as possible before returning
  to a waiting neighbor.
seo_keywords:
  - Python
  - dfs recursive
  - graph algorithms
---

Use recursive calls to follow a route as far as possible before returning to a waiting neighbor.

Depth-first search (DFS) records a vertex on entry, explores its first unseen neighbor completely, then resumes the interrupted call at the next neighbor. The call stack remembers that suspended work. This differs from BFS, which finishes a whole distance layer before processing the next one.

For example, a foyer has neighbors gallery and terrace. The gallery leads to a storeroom. Recursive DFS records foyer, gallery, storeroom, then terrace. That order describes exploration, not shortest distance. A deep branch may reach a target before a much shorter branch is considered.

The helper receives a shared `seen` set and output list. It first returns if the vertex is already seen. Mark before making recursive calls: on a cycle, postponing the mark until return would allow the same vertex to call itself indirectly forever. Recording the label is a separate checkpoint from recording discovery because the two collections have different jobs.

The wrapper validates the start and provides fresh state for every run. It is supplied, as are the earlier BFS functions. Complete only the marked entry, output, and recursion operations. Each recursive call uses the same set and list; making a fresh set in each call would forget discoveries made by other branches.

DFS works on directed outgoing lists as well as undirected symmetric lists. It follows the given neighbor order and ignores disconnected vertices. Duplicate entries and self-loops terminate because the entry guard checks the shared set. The graph itself stays unchanged.

For the reachable region, time is expected O(Vr + Er). The seen set and output use O(Vr) storage; recursive depth can also reach Vr. Python has a recursion limit, so these examples deliberately use small graphs. A long chain can exceed that limit even though the graph has no cycle. The next lesson replaces recursive frames with explicit ones rather than raising the recursion limit.

## Worked trace

![Recursive DFS discovers [A,B,D,C], with all four calls active at the deepest point. C has only visited neighbors, so calls return to D, B and A; A then skips visited C.](graph-traversal-dfs-recursive-trace.svg)

Alphabetical neighbors; mark a vertex before recursion to avoid cycling. The illustrated neighbor lists happen to be alphabetical; the function follows the lists as supplied and does not sort them.

## Your Tasks

1. Mark the current vertex seen on entering `dfs_visit`.
2. Append that newly entered vertex to `order`.
3. Recursively visit its neighbors in their supplied order.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
