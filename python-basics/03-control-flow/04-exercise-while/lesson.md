---
title: 'Exercise: Charge a device'
slug: exercise-while
order: 4
language: python
runtime: pyodide
lesson_type: coding
summary: Use a bounded while loop to count charging steps.
seo_title: 'Exercise: Charge a device | Python Basics'
seo_description: Use a bounded while loop to count charging steps. Practice Python
  control flow in an editable browser lesson.
seo_keywords:
- python while exercise
- charge counter
- loops
---

# Exercise: Charge a device

The misting timer counted down. Here a portable radio charges **up** from 10% to 40% in 10-point steps. `while charge < 40` stops before a turn starting at 40. The starter supplies the starting charge and a counter.

Edit **main.py**, press **Run** to see `40` and `3` on separate lines, then press **Submit**.

## Your Task

1. Add a `while` loop that increases `charge` by 10 and `steps` by 1 each turn until charge reaches 40. The supplied print lines should show a 40% charge after three steps.
