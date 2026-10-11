---
title: "Exercise: Decode Route Fields"
slug: exercise-slice-ticket
order: 4
language: python
lesson_type: coding
runtime: pyodide
summary: Slice a cavern sign into a route prefix and beacon code.
seo_title: "Exercise: Decode Route Fields | Python Basics"
seo_description: Slice a cavern sign into a route prefix and beacon code.
seo_keywords: [python basics, strings, lantern atlas]
---

# Exercise: Decode Route Fields

The sign `ARC:2048` contains two pieces of information: a three-letter route and a four-digit beacon code. The colon at index `3` separates them.

Keep `ticket` unchanged and read each piece with a slice. The beacon code should stay a string; there's no calculation to do with it here.

## Your Tasks

1. Set `route_name` to a slice containing the first three characters of `ticket`.
2. Set `number` to a slice containing the four characters after the colon.

Run `main.py` as you work. The first task should give `ARC None`; both tasks should give `ARC 2048`. Submit to check the two slices separately.
