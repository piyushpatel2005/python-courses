---
title: 'Exercise: rank pickup points'
slug: exercise-sort-and-top
order: 12
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Sort a full table and return a requested number of largest values.
seo_title: 'Exercise: rank pickup points | Introduction to Pandas'
seo_description: Sort a full table and return a requested number of largest values.
seo_keywords:
  - pandas
  - python
  - data selection
hints:
  - Use descending sort_values for the full ranking and nlargest(count, "visits") for the short list.
---

The pickup team wants a full ranking and a short whiteboard list. Use the `visits` column for both, but keep these as separate functions so each view can be requested independently.

Keep all columns and original labels, and leave the input unchanged. `count` is nonnegative. A short list may contain fewer rows only when fewer are available. At a tied cutoff, nlargest keeps the earlier tied rows by default rather than adding extra rows. The full ranking need not choose a particular order within ties.

After task 1, Run should show Yard, Gate, Hall. After task 2, the second table should show Yard and Gate. The desk can now choose and rank records; the next section checks whether those records are usable.

## Your Tasks

1. Return all rows in descending `visits` order from `rank_points(frame)`.
2. Return the `count` rows with the largest `visits` from `top_points(frame, count)`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
