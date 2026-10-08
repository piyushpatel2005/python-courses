---
title: 'Exercise: align calibration'
slug: exercise-align-calibration
order: 6
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Add singleton axes without duplicating data.
seo_title: 'Exercise: align calibration | Intro to NumPy'
seo_description: Add singleton axes without duplicating data.
seo_keywords:
  - numpy
  - array shape
  - exercise align calibration
hints:
  - Read the shape of each intermediate array before editing another line.
---

# Exercise: align calibration

A separate sensor has four offsets. The comparison routine expects a column for row offsets and a row for time offsets. `np.newaxis` inserts an axis of length one; it does not repeat the underlying readings. These shapes let NumPy broadcast the two arrays against each other.

Edit `main.py`, Run to inspect both shapes, then Submit.

## Your Tasks

1. Return `offsets[:, np.newaxis]` from `as_column(offsets)`.
2. Return `ticks[np.newaxis, :]` from `as_row(ticks)`.
