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
  - Check the actual raw and card arrays with the supplied shares_memory call.
---

# Trace shared readings

A new shape does not necessarily mean new storage. The observatory can keep a raw strip and a reshaped display card that both refer to the same readings. When two arrays share data, changing a shared reading through one array can affect the other.

A reshape returns a view when the layout allows it, but sometimes it needs a copy. `np.shares_memory(a, b)` checks whether these two arrays actually overlap in memory. To make an independent backup deliberately, use `.copy()`, as you did when working with slices.

The starter's consecutive values form a simple shared-storage example. Change the card shape in `main.py` and Run. The shape should change while the sharing flag stays `True`. That result describes this pair of arrays, not every possible reshape.

## Your Tasks

1. Reshape `raw` into a `(3, 2)` card. Leave the supplied sharing check in place to inspect the result, then Submit.
