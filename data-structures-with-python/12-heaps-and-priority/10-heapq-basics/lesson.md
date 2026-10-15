---
title: "Heapq basics"
slug: "heapq-basics"
order: 10
language: "python"
runtime: "pyodide"
lesson_type: "coding"
summary: "In `heapq_order`, drain the copied heap with `heapq.heappop` into a new ordered result."
seo_title: "Heapq basics | Data structures with Python"
seo_description: "You have implemented the repair operations yourself. Now use Python's `heapq` module for the same min-heap behavior. The module operates on ordinary lists, so the caller still owns the representation and must preserve its invariant."
seo_keywords:
  - Python
  - "Heapq basics"
---

You have implemented the repair operations yourself. Now use Python's `heapq` module for the same min-heap behavior. The module operates on ordinary lists, so the caller still owns the representation and must preserve its invariant.

## Work through the idea

`heapq.heapify(items)` rearranges a list into a min-heap in place and returns `None`. `heapq.heappush(items, value)` inserts one item, and `heapq.heappop(items)` removes the minimum. Reading `items[0]` peeks at the root when the list is nonempty. Those functions do not create a separate heap object.

For this exercise, copy the input sequence to an ordinary list, heapify it once, and repeatedly pop into a result list. A copy matters because heapify mutates its argument. Assigning `heap = values` would create an alias and reorder the caller's list before you even start removing items.

Do not assign the result of heapify back to the heap variable. Its return value is `None`, not the rearranged list. The list you passed in is the object to keep using. Also check whether the heap is nonempty before popping; popping an empty heap raises `IndexError`.

This lesson starts a fresh standard-library implementation. The custom class from earlier stages is not required here. Using library heap operations is now the intended technique, whereas calling a library sorter would skip the heap practice.

## Build it in checkpoints

Build and drain are separate functions here. `make_heap` must return the copied list after calling heapify, not heapify's `None` result. The supplied first line of `heapq_order` requests that copy. Once the first checkpoint passes, finish the draining loop without adding another heap construction.

## Contract and cost

`heapq_order(values)` returns a new ascending list, preserving duplicates and leaving the input unchanged. Use `heapq.heapify` once on a copied list and `heapq.heappop` until empty. No stability guarantee is made for records with equal comparison keys. Use only the established min-heap APIs.

Heapify costs O(n); repeated pops cost O(n log n) overall. The working heap and result each use O(n) space. Peek is O(1), while individual heap pushes and pops require logarithmic repair work.

## Your Tasks

1. In `make_heap`, copy the input, heapify the copy, and return the owned heap list.
2. In `heapq_order`, drain the copied heap with `heapq.heappop` into a new ordered result.

Edit `main.py`, then press **Run** to inspect the supplied probe and **Submit** to check each task. Complete the numbered changes in order. The supplied code keeps earlier operations available; you do not need to copy anything from another lesson.
