---
title: "Exercise: Process a Limited Number of Orders"
slug: exercise-skip-and-stop
order: 7
language: python
runtime: pyodide
lesson_type: coding
summary: "Skip a canceled order and stop after a daily processing limit."
seo_title: "Python continue and break Exercise | Python Basics"
seo_description: "Process numbered orders while skipping cancellations and honoring a daily limit."
seo_keywords: [python continue exercise, python break, order limit]
---

A shop has orders numbered 1 through 8. Order 3 is canceled, and staff can process only three orders today. `processed_orders` collects the order numbers as text; `processed_count` counts valid orders, not canceled ones. `daily_limit` is the maximum to process.

Build the loop above the print calls in `main.py`. Before you add the stopping rule, **Run** should print `1 2 4 5 6 7 8 ` and a count of `7`. Afterward it should print `1 2 4 ` and `3`.

## Your Tasks

1. Loop over `range(1, 9)`. Use `continue` to skip order 3; for each remaining `order_number`, append `f"{order_number} "` and increase `processed_count` by 1.
2. After counting a processed order, use `break` when `processed_count == daily_limit`.

**Submit** checks these stages separately. Put the stop check after the count so the third order is included.
