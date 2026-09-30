---
title: 'Exercise: Admit visitors'
slug: exercise-skip-and-stop
order: 8
language: python
runtime: pyodide
lesson_type: coding
summary: Skip an invalid number and stop when visitor capacity is met.
seo_title: 'Exercise: Admit visitors | Python Basics'
seo_description: Skip an invalid number and stop when visitor capacity is met. Practice
  Python control flow in an editable browser lesson.
seo_keywords:
- python break continue exercise
- visitor capacity
- for loop
---

# Exercise: Admit visitors

The depot skipped a parcel number and stopped at a fixed parcel number. A gallery instead has **three places** available. Visitor number 3 has an invalid ticket, and the gallery closes admission once three valid people enter. The starter supplies `admitted`, `count`, and `capacity`; it prints both results.

Edit **main.py**, press **Run** to see `1 2 4 ` and `3` on separate lines, then press **Submit**. The first task can be checked before you add the capacity limit.

## Your Tasks

1. Loop over `range(1, 9)`; use `continue` to skip visitor 3, append each other visitor as `f"{visitor} "` to `admitted`, and increase `count`. Without the capacity limit yet, the string starts `1 2 4 ` and contains no `3`.
2. After counting an admission, use `break` when `count == capacity`. The final output must be `1 2 4 ` and `3`.
