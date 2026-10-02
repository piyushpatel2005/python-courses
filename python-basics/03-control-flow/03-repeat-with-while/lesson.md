---
title: "Demo: Pulse a Beacon with while"
slug: repeat-with-while
order: 3
language: python
runtime: pyodide
lesson_type: coding
summary: "Watch a bounded countdown restore a beacon."
seo_title: "Demo: Pulse a Beacon with while | Python Basics"
seo_description: "Watch a bounded countdown restore a beacon."
seo_keywords: [python basics, control flow, lantern atlas]
---

A beacon pulses while its counter is positive. `while` checks before every turn; the indented body decrements `pulses` so it stops. The starter prints `Pulse 3`, `Pulse 2`, `Pulse 1`, then `Beacon steady`.

![While loop flowchart showing condition, body, and exit](while-loop-flow.svg "Check before each turn")

Change only the starting `pulses` from `3` to `4` in **main.py**. Press **Run** for an extra `Pulse 4`, then **Submit**. Never remove the decrement or the loop may not end.

## Your Tasks

1. Start `pulses` at `4`.
