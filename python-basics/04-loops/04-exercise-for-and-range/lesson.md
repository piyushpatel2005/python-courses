---
title: "Exercise: List Every Other Hour"
slug: exercise-for-and-range
order: 4
language: python
runtime: pyodide
lesson_type: coding
summary: "Use a stepped range for event check-in times."
seo_title: "Python Stepped range Exercise | Python Basics"
seo_description: "Build labels for check-in hours 2, 4, and 6 with a for loop."
seo_keywords: [python for exercise, stepped range, loop labels]
---

An event organizer checks sign-ins at hours 2, 4, and 6 after opening. Those are elapsed hours, not clock times. A step of two visits exactly those values.

The starter's `labels` string is empty. Use `range(2, 8, 2)`: it starts at 2, advances by 2, and stops before 8. Add a label on each turn, then leave the supplied print call after the loop.

## Your Tasks

1. Use a `for` loop with `range(2, 8, 2)` to append `f"Hour {hour} | "` to `labels`.

**Run** should print `Hour 2 | Hour 4 | Hour 6 | ` on one line. Then **Submit**.
