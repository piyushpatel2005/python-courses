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

Echo Tower is an optional detour into two more function patterns. The final mission will use ordinary functions and loops; it will not depend on recursion or lambdas.

A recursive function calls itself. In this countdown, each call uses a smaller number until the base case at zero stops the calls. Without a stopping case, the calls eventually raise `RecursionError`.

Read `pulse_steps` in `main.py`. `pulse_steps(0)` returns `[0]`. The call for `1` puts `1` in front of that result, making `[1, 0]`; the call for `2` then makes `[2, 1, 0]`.

Change the sample call to use `3`. Run should show `Tower pulses: [3, 2, 1, 0]`, then Submit. Keep this example small; a loop is usually simpler for a long countdown.

## Your Task

1. Change the sample call to `pulse_steps(3)` without changing the base case.
