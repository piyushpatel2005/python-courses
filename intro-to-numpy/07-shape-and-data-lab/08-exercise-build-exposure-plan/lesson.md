---
title: 'Exercise: build exposure plan'
slug: exercise-build-exposure-plan
order: 8
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Create adjacent copies and cycling copies of a schedule.
seo_title: 'Exercise: build exposure plan | Intro to NumPy'
seo_description: Create adjacent copies and cycling copies of a schedule.
seo_keywords:
  - numpy
  - array shape
  - exercise build exposure plan
hints:
  - Use frames as the repeat count and cycles as the tile count.
---

# Exercise: build exposure plan

A different device uses settings `[1, 4, 7]`. It needs one schedule that holds each setting for several frames and another that cycles through the complete sequence.

Use the function parameters so the device can change both its settings and its counts. With a count of two, the held schedule starts `[1 1 4 4]`, while the cycling schedule starts `[1 4 7 1]`. Both functions should return one-dimensional arrays.

Fill in `main.py` one helper at a time. The supplied print calls let you compare the two orders before Submit checks other settings and counts.

## Your Tasks

1. Implement `hold_settings(settings, frames)` with `np.repeat`, making `frames` adjacent copies of each setting.
2. Implement `cycle_settings(settings, cycles)` with `np.tile`, making `cycles` copies of the complete pattern.
