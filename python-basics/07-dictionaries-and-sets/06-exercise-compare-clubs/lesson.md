---
title: 'Exercise: Compare Atlas Routes'
slug: exercise-compare-clubs
order: 6
language: python
lesson_type: coding
runtime: pyodide
summary: 'Find common and Adi-only stops with set operations.'
seo_title: 'Exercise: Compare Atlas Routes | Python Basics'
seo_description: 'Find common and Adi-only stops with set operations.'
seo_keywords:
- python sets
- beginner sets exercise
---

Compare Adi's route with a scout's route. The starter calls the first route `ari_stops` and the second `scout_stops`; keep those variable names as you work.

Convert the lists to sets before comparing them. The intersection operator `&` keeps stops in both sets. The difference operator `-` keeps stops in the left set but not the right, so the order matters.

Edit `main.py`. The supplied printout sorts the sets so you can read the three groups consistently. Run, then Submit.

## Your Tasks

1. Set `ari_route` to a set built from `ari_stops`.
2. Set `overlap` to the intersection of `ari_route` and `scout_stops`.
3. Set `ari_only` to the difference between `ari_route` and `scout_stops`.
