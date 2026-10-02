---
title: "Echo Tower: The Base Case"
slug: recursion-base-case-demo
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: Trace a terminating recursive beacon countdown.
seo_title: "Echo Tower: The Base Case | Python Basics"
seo_description: Trace a terminating recursive beacon countdown.
seo_keywords: [python recursion, base case, Echo Tower]
---

Ari reaches the Echo Tower, where the first beacon needs a countdown before it can receive a signal. A recursive function calls itself with a smaller number; the **base case** stops the calls at zero. Without that stop, Python eventually raises `RecursionError`.

In `main.py`, `pulse_steps(0)` returns `[0]`. Each positive step prepends its number and calls `pulse_steps(number - 1)`. Change the sample call from `pulse_steps(2)` to `pulse_steps(3)`. Run to see `Tower pulses: [3, 2, 1, 0]`, then Submit. Keep the base case. For a large list, a loop is usually simpler; this is practice tracing small recursive calls.

## Your Task

1. Change the sample call to `pulse_steps(3)` without changing the base case.
