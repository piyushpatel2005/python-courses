---
title: Slice a Route Label
slug: slice-a-route
order: 3
language: python
lesson_type: coding
runtime: pyodide
summary: Extract text with Python start and stop slices.
seo_title: Slice a Route Label | Python Basics
seo_description: Extract text with Python start and stop slices with an editable Python
  example and checked task.
seo_keywords:
- python slicing
- beginner slicing exercise
---

The transport desk needs the district from `WEST:TRAM`. A slice `text[start:stop]` includes the start but excludes the stop; omitting the start means zero, omitting the stop means the end. A slice past the end is safe, unlike a single invalid index.

This is an editable worked demo. Edit `main.py`, press **Run** to compare the result, then **Submit** to check your small change. The next lesson transfers the idea to a different setting.

Change `district` to slice out `WEST`; Run should print `WEST`, then Submit.

## Your Task

1. Slice `route` to set `district` to `"WEST"`.
