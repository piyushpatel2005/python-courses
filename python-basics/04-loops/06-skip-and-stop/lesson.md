---
title: "Skip an Order and Stop Packing"
slug: skip-and-stop
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: "Compare continue and break while processing numbered orders."
seo_title: "Python continue and break | Python Basics"
seo_description: "Skip a canceled order and stop before a later order in a for loop."
seo_keywords: [python continue, python break, for loop]
---

A shop handles orders numbered 1 through 6. Order 2 was canceled, and packing stops before order 5. The supplied loop demonstrates two different instructions:

- `continue` skips the rest of this turn and goes to the next order.
- `break` ends the loop, so later order numbers are never visited.

Both checks precede the line that adds an order to `packed`. Run the starter to see that order 2 is missing and nothing after order 4 appears.

## Your Tasks

1. Skip canceled order 3 instead of order 2, while still stopping before order 5.

Edit `main.py`. **Run** should print `Packed 1 | Packed 2 | Packed 4 | `, then **Submit**. In a `while` loop with a manual counter, update the counter before `continue` or you may keep checking the same value forever.
