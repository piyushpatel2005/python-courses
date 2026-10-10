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

You don't always need the whole route. A list slice works like a string slice: `checkpoints[:2]` gives you the first two items, stopping before index `2`. The slice is a new list; the original stays unchanged.

The supplied `for` loop prints every checkpoint. A step is optional: `checkpoints[::2]` would select every other item.

Change `near_checkpoints` in `main.py`. Run should still print the full route, followed by `['Pass', 'Bridge']`. Submit when the shorter route is right.

## Your Task

1. Set `near_checkpoints` to a slice of the first two `checkpoints`.
