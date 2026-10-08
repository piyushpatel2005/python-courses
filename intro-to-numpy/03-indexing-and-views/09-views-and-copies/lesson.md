---
title: See a view change its source
slug: views-and-copies
order: 9
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: A basic slice shares storage with its source; `.copy()` makes an independent array.
seo_title: See a view change its source | NumPy
seo_description: See how editing a NumPy slice changes its source, then use `.copy()` to preserve an independent snapshot.
seo_keywords:
  - NumPy
  - Python
  - views and copies
hints:
  - Make the copy before editing the view; check `np.shares_memory` in the test results.
---

A calibration window may share its storage with the full record.

A basic slice is a view: `np.shares_memory(source, view)` is true. `.copy()` makes separate storage, so changes to the copy leave the source alone. Fancy indexing also copies.

## Your Task

1. Change the view edit from `99` to `70`; Run prints the shared-memory flags and changed source.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check the change.
