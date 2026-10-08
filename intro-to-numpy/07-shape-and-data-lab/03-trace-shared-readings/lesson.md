---
title: Trace shared readings
slug: trace-shared-readings
order: 3
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Check whether a reshape shares data with its input.
seo_title: Trace shared readings | Intro to NumPy
seo_description: Check whether a reshape shares data with its input.
seo_keywords:
  - numpy
  - array shape
  - trace shared readings
hints:
  - Read the shape of each intermediate array before editing another line.
---

# Trace shared readings

The observatory keeps a raw sensor strip and a display card. A reshape **may** be a view, but sometimes it requires a copy, especially after changing traversal order. Do not assume either outcome: `np.shares_memory(a, b)` checks the actual arrays. `grid.T.ravel()` reads down the original columns and can require its own storage.

This contiguous strip is a known shared-memory example. In `main.py`, change the **one** reshape argument from `(2, 3)` to `(3, 2)`. Run and look at the shape and sharing flag, then Submit. The true flag here is an observation, not a guarantee for all reshapes.

## Your Tasks

1. Change the card shape to `(3, 2)`. The supplied `np.shares_memory` check will show whether this particular card shares storage.
