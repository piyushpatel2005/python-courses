---
title: 'Exercise: Build a Market Roster'
slug: exercise-market-roster
order: 8
language: python
lesson_type: coding
runtime: pyodide
summary: Build a practical signup summary from Python collections.
seo_title: 'Exercise: Build a Market Roster | Python Basics'
seo_description: Build a practical signup summary from Python collections with an
  editable Python example and checked task.
seo_keywords:
- python collections-project
- beginner collections-project exercise
---

At the market, volunteers recorded names and activity choices. A repeat signup must count once as a person but twice as a booking. Use the library demo as a pattern with new data and a different report; all records are local browser data and no `input()` is needed.

This is a separate exercise. Edit `main.py`, press **Run** to inspect the output, then **Submit** to check the numbered tasks.

Build one checkpoint at a time in `main.py`. Run to inspect the printed list, set, dictionary and report; Submit to check each task.

## Your Tasks

1. Loop over `signups` and append each name in signup order to `names`.
2. Set `unique_names` to a set of the names in `names`.
3. Count each signup activity in `activity_counts` using its current count (or zero) plus one.
4. Set `report` with an f-string to `Market Hall at 10:00: 2 people, 3 bookings`.
