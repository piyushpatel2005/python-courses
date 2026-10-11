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

Build an index of the archive's treasure discoveries. A second find at the same location is another discovery, but it is not another place. You'll keep the visit order in a list, distinct places in a set, and treasure counts in a dictionary.

Keep the supplied data. Edit `main.py` and work down the tasks, using Run to inspect each result and Submit to check it. The final report should use your calculated values, so it stays correct when the discoveries change.

## Your Tasks

1. Loop over `discoveries` and append each location in discovery order to `locations`.
2. Set `unique_locations` to a set of the values in `locations`.
3. Count each treasure in `treasure_counts` with the current count (or zero) plus one.
4. Build `report` with an f-string using both values in `location`, the count of `unique_locations`, and the count of `discoveries`. The supplied data should give `Map Archive at dawn: 2 places, 3 finds`.
