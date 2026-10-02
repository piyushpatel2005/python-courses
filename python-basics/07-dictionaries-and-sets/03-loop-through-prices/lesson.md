---
title: 'Loop Through Beacon Map Entries'
slug: loop-through-beacon_marks
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

The archive lists beacon marks by landmark. `beacon_marks.items()` yields each key and value together; `for landmark, marks in ...` unpacks them. `.keys()` gives keys alone and `.values()` gives values alone.

Edit `main.py` so Run prints `["ridge", "cove"]` instead of the mark counts; **Submit** to check. The next exercise uses a different cache map.

## Your Task

1. Loop through `beacon_marks.items()` and append each key to `landmarks`.
