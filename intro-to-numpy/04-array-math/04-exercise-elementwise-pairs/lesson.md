---
title: 'Exercise: find sensor agreement'
slug: exercise-elementwise-pairs
order: 4
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: "Find one difference for each pair of sensor readings."
seo_title: 'Exercise: find sensor agreement | NumPy'
seo_description: "Find one difference for each pair of sensor readings."
seo_keywords:
  - NumPy
  - Python
  - elementwise pairs
hints:
  - 'Subtract reference readings from primary readings, in that order.'
---

A pair of rooftop sensors needs one difference per reading, not a single total. The primary and reference arrays have matching shapes.

## Your Task

1. In `difference`, return the NumPy array `primary - reference`.

Edit `main.py`, Run to check `[6 2 3]`, then Submit. A negative difference means the primary reading is lower than its reference.
