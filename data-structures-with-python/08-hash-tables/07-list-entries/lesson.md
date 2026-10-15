---
title: "List the stored pairs"
slug: "list-entries"
order: 7
language: "python"
runtime: pyodide
lesson_type: "coding"
summary: "Return a shallow snapshot of entries in bucket traversal order."
seo_title: "List the stored pairs | Data structures with Python"
seo_description: "Return a shallow snapshot of entries in bucket traversal order."
seo_keywords:
  - Python
  - list entries
  - data structures
---

A stock report needs every stored pair, not one key lookup. Traverse the outer bucket list in index order, and each bucket in its current pair order. Append each pair to a new result list.

This order is a representation detail, not alphabetical order or global insertion order. Keys in different buckets may appear in a different order from their arrival. Do not sort them. Within one bucket, insertions append, updates replace in place, and deletions remove only their pair, so the supplied methods already define the traversal order.

For a schematic example independent of the hash function, if bucket zero contains `( "ink", 2 )` and bucket one contains `( "paper", 5 )` followed by `( "tape", 1 )`, the snapshot follows that order. Empty buckets contribute nothing. An empty table returns a new empty list.

The snapshot is shallow. Appending or removing a pair in the returned list must not change the table's bucket lists. But mutable value objects are still shared: changing a stored list through the snapshot also changes that same object when retrieved by get. The method copies references into a new outer result, not every value recursively.

Enumeration takes O(m + n) time for m buckets and n pairs, including visits to empty buckets. The result takes O(n) space. Calling it O(n) without mentioning m can hide the cost of a very sparse table. This method will later supply the key/value pairs needed to rebuild the table under a new capacity.

## Build it in small steps

This task is one collection operation: walk the buckets and return a fresh list of their pairs. There is no separate validation branch to implement.

## Your Tasks

1. Collect the bucket pairs into a new shallow list in traversal order.

Edit `main.py` one step at a time. Run uses the supplied probe; an unfinished field or return value may print a reminder. Submit checks the numbered steps in order, so you can see each completed step before finishing the next.
