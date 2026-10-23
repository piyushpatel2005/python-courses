---
title: "Count Days with for and range"
slug: count-with-for-and-range
order: 4
language: python
runtime: pyodide
lesson_type: coding
summary: "Extend a for-loop schedule by one day."
seo_title: "Python for Loop and range | Python Basics"
seo_description: "Use range endpoints to count days in a simple schedule."
seo_keywords: [python for loop, python range, loop endpoint]
---

A four-day event needs a label for each day. A `for` loop visits values from a sequence. In `main.py`, `range(1, 4)` supplies the values 1, 2, and 3; the stop value 4 is not included.

On each turn, `labels += f"Day {day} | "` adds text to a string that started empty. The print call after the loop shows all labels on one line. Unlike a counter-driven `while`, `for` moves to its next value automatically.

| Expression | Values visited |
| --- | --- |
| `range(4)` | 0, 1, 2, 3 |
| `range(1, 4)` | 1, 2, 3 |
| `range(2, 8, 2)` | 2, 4, 6 |

The third argument is the step size.

## Your Tasks

1. Change the range endpoint to `5` so day 4 appears too.

Edit `main.py` and press **Run**. The line should end in `Day 4 | `. Then **Submit**.
