---
title: Recursion and a Base Case Demo
slug: recursion-base-case-demo
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: Edit a terminating recursive countdown.
seo_title: "Recursion and a Base Case Demo | Python Basics"
seo_description: Edit a terminating recursive countdown.
seo_keywords: [python recursion, recursive base case, countdown]
---

Sometimes a function can solve a small piece, then call itself for the rest. The **base case** stops it. `step_down(0)` returns immediately; for a positive number, each call uses a smaller number. Without a reachable base case, Python eventually raises `RecursionError`. For an ordinary list, a loop is usually simpler; here recursion is an optional pattern to recognize and practice on small values.

The complete starter returns a list of numbers ending at zero. Edit `main.py`: change the sample call from `step_down(2)` to `step_down(3)`. Run to see `[3, 2, 1, 0]`, then Submit. In the next lesson, you'll build a different recursive function.

## Your Task

1. Change the sample call to `step_down(3)` without changing the function's base case.
