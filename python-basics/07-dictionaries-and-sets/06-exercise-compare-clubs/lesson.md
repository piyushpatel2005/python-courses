---
title: 'Exercise: Compare Atlas Routes'
slug: exercise-compare-clubs
order: 6
language: python
lesson_type: coding
runtime: pyodide
summary: 'Find common and Ari-only stops with set operations.'
seo_title: 'Exercise: Compare Atlas Routes | Python Basics'
seo_description: 'Find common and Ari-only stops with set operations.'
seo_keywords:
- python sets
- beginner sets exercise
---

Ari and a scout explored overlapping routes. Convert Ari’s list to a set to remove repeats. Convert the scout’s list too before using `&` to find shared stops or `-` to keep only Ari’s. Sort the printed sets to make the checkpoint predictable.

Edit `main.py`, **Run** to inspect the three groups, then **Submit**.

## Your Tasks

1. Set `ari_route` to a set built from `ari_stops`.
2. Set `overlap` to the intersection of `ari_route` and `scout_stops`.
3. Set `ari_only` to the difference between `ari_route` and `scout_stops`.
