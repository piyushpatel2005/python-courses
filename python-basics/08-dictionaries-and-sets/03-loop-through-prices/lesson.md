---
title: 'Loop Through Beacon Map Entries'
slug: loop-through-prices
order: 3
language: python
lesson_type: coding
runtime: pyodide
summary: 'Use dictionary items() to inspect keyed beacon marks.'
seo_title: 'Loop Through Beacon Map Entries | Python Basics'
seo_description: 'Use dictionary items() to inspect keyed beacon marks.'
seo_keywords:
- python dictionary-loop
- beginner dictionary-loop exercise
---

A dictionary loop can read a key and its value together. `beacon_marks.items()` produces pairs, and `for landmark, marks in ...` unpacks each pair into two names. This is the same unpacking idea you used with tuples.

Use `.keys()` when you only need keys, or `.values()` when you only need values.

The starter currently collects mark counts. Edit `main.py` to collect landmarks instead. Run should print `['ridge', 'cove']`, then Submit.

## Your Task

1. Loop through `beacon_marks.items()` and append each key to `landmarks`.
