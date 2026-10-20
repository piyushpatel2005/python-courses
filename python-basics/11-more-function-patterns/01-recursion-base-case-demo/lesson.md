---
title: "A recursive countdown"
slug: recursion-base-case-demo
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: Trace a recursive countdown and identify the call that stops it.
seo_title: "Recursive Countdowns and Base Cases | Python Basics"
seo_description: Trace a short recursive countdown to see how a base case stops further calls.
seo_keywords: [python recursion, recursive countdown, base case]
---

A workshop organizer wants a short countdown to opening day. A recursive function calls itself with a smaller value. In `days_left`, the call with zero returns `[0]` without calling itself again. That is the **base case**. Without one, the calls would eventually raise `RecursionError`.

Read `days_left` in `main.py`. `days_left(0)` gives `[0]`; `days_left(1)` puts `1` before it, giving `[1, 0]`. One more call gives `[2, 1, 0]`. A loop is generally simpler for a long countdown, but this short one makes the stopping point easy to see.

## Your Task

1. Change the sample call to `days_left(3)` without changing the function.

Edit `main.py` and press **Run**. You should see `Days until opening: [3, 2, 1, 0]`. Then press **Submit**.
