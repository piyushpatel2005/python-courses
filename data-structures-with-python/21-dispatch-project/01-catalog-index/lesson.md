---
title: "Index the dispatch catalog"
slug: catalog-index
order: 1
language: python
runtime: pyodide
lesson_type: coding
summary: "Create a validated job catalog whose records are independent of caller dictionaries."
seo_title: "Index the dispatch catalog in Python"
seo_description: "Create a validated job catalog whose records are independent of caller dictionaries."
seo_keywords:
  - Python
  - catalog-index
hints:
  - "The duplicate guard must not store anything; copy and storage are separate helpers."
---

Build a small dispatch workbench for a repair depot. Over eight stages, one object will connect a catalog, waiting queue, priority heap, undo history, route map, and load report. Every stage includes the completed earlier code. The data stays in memory; this project does not send vehicles or contact a service.

`dict[str, str | int]` describes the job records: string keys map to string or integer fields. `tuple[int | None, list[str]]` in later route queries means a cost (or `None`) paired with a path. These hints document contracts; validation still checks actual values.

Start with the catalog. Jobs have exactly five fields: `id`, `destination`, `priority`, `day`, and `units`. IDs are nonempty strings. Smaller integer priorities are more urgent. Day is a zero-based index in the reporting window, and units is a nonnegative integer workload. Destinations must name an existing site. The supplied `_validate_job` enforces those rules; the supplied `register` calls it before changing anything.

Store a copy of each job under its ID in `self.catalog` and return that ID. Reject duplicate IDs with `ValueError` rather than silently overwriting a job that may already be queued. These fields contain immutable values, so a shallow dictionary copy is enough. For example, registering a job called `seal-window` should not let a later edit to the caller's dictionary change its recorded workload.

The supplied constructor creates all the storage needed later. `deque` supplies FIFO append and left-pop operations. `heapq` supplies min-heap push and pop. A list holds history. `active` is a set of IDs already queued or completed; undo will release an ID for resubmission.

`LoadIndex` is a local Fenwick adapter from the range-structure idea: `add(day, amount)` changes one day, `prefix(stop)` totals days before stop, and `range_sum(start, stop)` uses half-open bounds. It converts zero-based days to one-based tree positions and uses lowbit jumps. Callers validate bounds. You will use this helper later, not reimplement it.

`_network_copy` validates and copies a directed weighted adjacency dictionary. Site IDs are strings, neighbor lists preserve supplied order, weights are nonnegative integers, self-loops are allowed, and duplicate outgoing destinations are rejected. Missing endpoints are errors. Dictionary catalog operations are expected O(1) under normal hashing assumptions; constructing the whole workbench costs O(V + E + days), before registering jobs.

## Supplied setup and small steps

The supplied `register` method validates the fields and returns the ID after storage succeeds. You write three separate operations: reject an existing ID, copy a record, and store the already-copied record. `copy_record` is static because it does not need workbench state.

## Your Tasks

1. Complete `ensure_new_id(job_id)` to raise `ValueError` only when the ID is already in the catalog.
2. Complete `copy_record(job)` to return an independent shallow copy.
3. Complete `store_record(job_id, record)` to store the already-copied record under its ID.

Edit `main.py`. Run prints the registered ID and the catalog record stored under it. Submit checks the same operation on additional small cases.
