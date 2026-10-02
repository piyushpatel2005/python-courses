---
title: "Slice a Ridge Route: Demo"
slug: slice-a-walking-route
order: 5
language: python
lesson_type: coding
runtime: pyodide
summary: Loop through checkpoints and slice a short route.
seo_title: "Slice a Ridge Route: Demo | Python Basics"
seo_description: Loop through checkpoints and slice a short route.
seo_keywords: [python basics, lists and tuples, lantern atlas]
---

# Slice a Ridge Route: Demo

A `for` loop visits each checkpoint in order. Like string slicing, `checkpoints[:2]` makes a new list of the first two; `checkpoints[::2]` would take every other one. The original list stays intact.

Change `near_checkpoints` in `main.py` to the first two checkpoints. Run should print the full route and then `['Pass', 'Bridge']`; Submit to check.

## Your Task

1. Set `near_checkpoints` to a slice of the first two `checkpoints`.
