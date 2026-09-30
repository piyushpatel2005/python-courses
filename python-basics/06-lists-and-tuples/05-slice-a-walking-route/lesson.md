---
title: Loop and Slice a Route
slug: slice-a-walking-route
order: 5
language: python
lesson_type: coding
runtime: pyodide
summary: Loop over a list and slice out a sublist.
seo_title: Loop and Slice a Route | Python Basics
seo_description: Loop over a list and slice out a sublist with an editable Python
  example and checked task.
seo_keywords:
- python list-loop-slice
- beginner list-loop-slice exercise
---

A `for` loop visits each stop in order. Like string slicing, `stops[:2]` makes a **new list** of the first two items; a third slice value is the step (`stops[::2]` takes every other). The original remains intact.

This is an editable worked demo. Edit `main.py`, press **Run** to compare the result, then **Submit** to check your small change. The next lesson transfers the idea to a different setting.

Change `morning_stops` to the first two stops; Run should print `Dock`, `Park` and the shorter list; then Submit.

## Your Task

1. Set `morning_stops` to a slice of the first two `stops`.
