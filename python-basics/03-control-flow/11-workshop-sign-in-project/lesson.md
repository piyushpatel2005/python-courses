---
title: "Project: Unlock the Exit Gate"
slug: workshop-sign-in-project
order: 11
language: python
runtime: pyodide
lesson_type: coding
summary: "Combine branching, loops, skipping, and a route limit to unlock the exit."
seo_title: "Project: Unlock the Exit Gate | Python Basics"
seo_description: "Combine branching, loops, skipping, and a route limit to unlock the exit."
seo_keywords: [python basics, control flow, lantern atlas]
---

Adam needs two safe steps to reach this level's exit beacon. Tile 2 is broken. Map the other tiles in order, stop once you have enough steps, and report whether the gate can open.

This project combines the loop, skip, stop, and branch patterns you have practiced. The starter supplies the route limit and print calls. In **main.py**, build the path above the `gate_status` assignment, then replace that placeholder with a decision after the loop.

Press **Run** after each change and **Submit** to check your progress. The completed program should show:

```text
Path: 1 3
Steps: 2
Gate: Unlocked
```

There is a space after each tile in the path string. If you temporarily raise `gate_limit` to 8, only five safe tiles are available, so the final status should be `Sealed`. Restore the limit to 2 before finishing.

## Your Tasks

1. Build `path` with a loop over tiles 1 through 6: skip tile 2 with `continue`, and for each safe tile append `f"{tile} "` to `path` and increase `steps` by 1.
2. After counting a safe step, use `break` when `steps == gate_limit`.
3. After the loop, use `if` / `else` to set `gate_status` to `"Unlocked"` when `steps == gate_limit`, or `"Sealed"` otherwise.

The route now responds to both hazards and limits. In the Ability Workshop, you will put reusable pieces of code into functions.
