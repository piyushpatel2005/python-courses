---
title: "Project: Unlock the Exit Gate"
slug: workshop-sign-in-project
order: 9
language: python
runtime: pyodide
lesson_type: coding
summary: "Combine branching, loops, skipping, and a route limit to unlock the exit."
seo_title: "Project: Unlock the Exit Gate | Python Basics"
seo_description: "Combine branching, loops, skipping, and a route limit to unlock the exit."
seo_keywords: [python basics, control flow, lantern atlas]
---

Ari needs two safe steps to reach the exit beacon. Tile 2 is broken, so map other tiles in order until the route limit is met. This combines `for` / `range`, `continue`, `break`, and `if` / `else`. The print calls make the route visible without `input()`. Edit **main.py**, press **Run** after each change, then **Submit**. Completed output: `Path: 1 3 `, `Steps: 2`, `Gate: Unlocked`.

## Your Tasks

1. Loop over tiles 1 through 6. Skip tile 2 with `continue`; append each other tile as `f"{tile} "` to `path` and increase `steps`.
2. After counting a safe step, use `break` when `steps == gate_limit`.
3. After the loop, use `if` / `else` to set `gate_status` to `"Unlocked"` when `steps == gate_limit`, or `"Sealed"` otherwise. At a limit of 8, only five safe tiles exist, so the gate stays sealed.

Ari restored the route to the exit beacon; later levels will add reusable functions and richer inventory.
