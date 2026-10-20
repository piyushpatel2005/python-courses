---
title: "Slice a delivery list"
slug: slice-a-walking-route
order: 5
language: python
lesson_type: coding
runtime: pyodide
summary: "Select the first two addresses without changing the full list."
seo_title: "Slice a delivery list | Python Basics"
seo_description: "Select the first two addresses without changing the full list."
seo_keywords: [python basics, python collections, beginner python]
---

A delivery driver has three addresses but wants to see only the first two. A slice such as `addresses[:2]` starts at the beginning and stops *before* index `2`. It produces a new list; `addresses` still has all three entries. The same start/stop rule applies to string slices.

The supplied `for` loop prints every address in order. A slice can also have a step: `addresses[::2]` would select every other address. Change `next_addresses` in `main.py` to a slice of the first two. **Run** should still print all three addresses, followed by `['Oak Street', 'Main Street']`. Then **Submit**.

## Your Task

1. Set `next_addresses` to a slice of the first two `addresses`.
