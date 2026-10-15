---
title: Build a route planner that reuses one weighted search
slug: route-planner
order: 8
language: python
runtime: pyodide
lesson_type: coding
summary: Produce a route report for each requested destination using one search from
  a shared origin.
seo_title: Build a route planner that reuses one weighted search | Python graph algorithms
seo_description: Produce a route report for each requested destination using one search
  from a shared origin.
seo_keywords:
  - Python
  - route planner
  - graph algorithms
---

Produce a route report for each requested destination using one search from a shared origin.

A workshop dispatch board may ask for routes from the same loading dock to several stations. Running Dijkstra once per destination repeats the same work. Its completed distance and parent tables already describe every reachable destination. The supplied `plan_routes` function therefore validates target labels and performs exactly one heap search before constructing reports.

A report is a dictionary with `target`, `cost`, and `path`. The target is the requested label. A reachable cost is an integer, including zero, and its path runs from source to target. For an unreachable station, the supplied branch returns `None` and an empty path. The annotation `dict[str, object]` allows these different value types without hiding the field meanings; this is a small report format, not a general graph representation.

Complete the reachable report first. Then loop through the requested target list and append each report. Do not convert requests to a set: caller order matters, and repeated requests remain repeated rows. Each call to reconstruction creates a fresh path list, so editing one returned report cannot silently change another row for the same destination.

For example, requests for yard, island, and dock produce a normal cheapest route, an unreachable result, and a zero-cost source-only route. Repeating yard produces another independent row. An empty request list returns no rows, but the supplied function still validates and searches from the source; a misspelled source is not silently accepted just because there are no destinations.

All earlier graph and algorithm definitions remain in the starter. Your final edits assemble their results rather than reimplementing the search. Unknown requested labels raise `KeyError`; malformed weights are rejected by the common validation helper. Equal-cost choices follow the heap's enqueue-order tie rule.

If R destinations are requested and their returned paths contain L labels in total, reporting adds O(R + L) time and output storage. The one heap search costs O(V + E log(E + 1)) time and O(V + E) auxiliary space. The completed planner distinguishes shortest hops from cheapest cost, preserves directedness, and reports disconnected destinations without confusing them with free routes.

## Your Tasks

1. Build a reachable target's report with its cost and reconstructed path.
2. Append one report per requested target, preserving request order and duplicates.

Edit `main.py`. Each numbered comment marks one checkpoint; replace its placeholder without changing the supplied code around it. Run shows the supplied probe, and Submit checks each task separately. You can submit after any step.
