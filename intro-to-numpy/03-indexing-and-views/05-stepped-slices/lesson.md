---
title: Cut a stepped window
slug: stepped-slices
order: 5
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: '`a[start:stop:step]` includes `start` and excludes `stop`.'
seo_title: Cut a stepped window | NumPy
seo_description: '`a[start:stop:step]` includes `start` and excludes `stop`. Practice
  NumPy in the browser.'
seo_keywords:
  - NumPy
  - Python
  - stepped slices
hints:
  - The stop `-1` excludes the final item; step `2` skips one item each time.
---

A meter records regular samples, but you only need every other one.

`a[start:stop:step]` includes `start` and excludes `stop`. Assigning through a slice changes the original array; NumPy can fill several slots with one scalar.

![Stepped slice selects alternating indexed cells in a NumPy array](array-slice-window.svg)

## Your Task

1. Change the slice assignment from `0` to `-1`; Run shows which original slots changed.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check the change.
