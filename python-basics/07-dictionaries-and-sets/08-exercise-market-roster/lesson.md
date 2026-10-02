---
title: 'Exercise: Build the Atlas Treasure Index'
slug: exercise-market-roster
order: 8
language: python
lesson_type: coding
runtime: pyodide
summary: 'Index treasure finds and visited locations in the Map Archive.'
seo_title: 'Exercise: Build the Atlas Treasure Index | Python Basics'
seo_description: 'Index treasure finds and visited locations in the Map Archive.'
seo_keywords:
- python collections-project
- beginner collections-project exercise
---

Ari needs an index of discoveries before leaving the Map Archive. Each record links a location to a treasure; returning to one location counts as another find, not another place. Keep the supplied data and build the index in task order.

Edit `main.py`, press **Run** to inspect the list, set, counts, and report, then **Submit** after each checkpoint.

## Your Tasks

1. Loop over `discoveries` and append each location in discovery order to `locations`.
2. Set `unique_locations` to a set of the values in `locations`.
3. Count each treasure in `treasure_counts` with the current count (or zero) plus one.
4. Set `report` with an f-string to `Map Archive at dawn: 2 places, 3 finds`.

The treasure index now distinguishes repeat finds from new places; Ari can follow it to the Save Shrine.
