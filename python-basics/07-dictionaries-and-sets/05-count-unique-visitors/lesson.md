---
title: 'Count Unique Atlas Stops'
slug: count-unique-visited_stops
order: 5
language: python
lesson_type: coding
runtime: pyodide
summary: 'Turn repeated location visits into a set of unique stops.'
seo_title: 'Count Unique Atlas Stops | Python Basics'
seo_description: 'Turn repeated location visits into a set of unique stops.'
seo_keywords:
- python sets
- beginner sets exercise
---

A route can visit the same stop more than once. A set keeps only distinct values, so `set(visited_stops)` gives you the places visited without counting repeats.

Sets do not have a dependable display order. If you want to display the values in order, use `sorted()`; this demo prints only their count. To create an empty set, use `set()`; `{}` creates an empty dictionary.

Edit `main.py` to count distinct stops. Run should print `2`, then Submit.

## Your Task

1. Set `unique` to a set built from `visited_stops`.
