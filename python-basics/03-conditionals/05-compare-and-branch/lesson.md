---
title: "Choose a Lit Route"
slug: compare-and-branch
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: "Use comparisons and branches to advise Adam at a gate."
seo_title: "Choose a Lit Route | Python Basics"
seo_description: "Use comparisons and branches to advise Adam at a gate."
seo_keywords: [python basics, control flow, lantern atlas]
---

A boolean tells you whether a check is true. An **if statement** uses that result to choose which code runs.

The starter chooses a route from the beacon signal and the weather. Read its branches from top to bottom:

- `if signal < 8:` chooses the repair message when the signal is too low.
- `elif signal < 16 and not foggy:` checks another possibility, but only if the first check was false. Both the signal comparison and `not foggy` must be true.
- `else:` handles any case that did not match either check. It has no condition of its own.

Only the first matching branch runs. Each branch heAdamng ends with a colon, and its assignment is indented by four spaces. The unindented print call runs after the choice is made.

With `signal = 12` and `foggy = False`, **Run** shows `Follow lit path`. Change just the signal in **main.py**, run again to see `Repair beacon`, then **Submit**.

## Your Tasks

1. Set `signal` to `4`.
