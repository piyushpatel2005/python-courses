---
title: "Mark a Route with range"
slug: count-with-for-and-range
order: 7
language: python
runtime: pyodide
lesson_type: coding
summary: "Extend a for-loop route by one map marker."
seo_title: "Mark a Route with range | Python Basics"
seo_description: "Extend a for-loop route by one map marker."
seo_keywords: [python basics, control flow, lantern atlas]
---

Use a **for loop** when you want to visit a sequence of values. In the starter, `for marker in range(1, 4):` gives `marker` the values 1, 2, and 3 in turn. The stop value, 4, is excluded.

On each turn, `labels += f"Marker {marker} | "` adds another piece of text to `labels`. It starts as an empty string, `""`. The print call runs after the loop so you see all the labels on one line.

`range()` has several useful forms:

| Expression | Values visited |
| --- | --- |
| `range(4)` | 0, 1, 2, 3 |
| `range(1, 4)` | 1, 2, 3 |
| `range(2, 8, 2)` | 2, 4, 6 |

The third argument is the step size. Unlike the previous `while` counter, a `for` loop advances to the next value automatically.

In **main.py**, change only the stop value. Press **Run** and look for `Marker 4 | ` at the end of the line, then **Submit**.

## Your Tasks

1. Change the range endpoint to `5` to include marker 4.
