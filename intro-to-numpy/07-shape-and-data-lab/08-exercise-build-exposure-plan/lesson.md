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
  - Read the shape of each intermediate array before editing another line.
---

# Exercise: build exposure plan

A second device asks for two schedules. One holds each setting for several frames; the other cycles through all settings several times. Choose `repeat` for adjacent identical settings and `tile` for a repeating sequence. A fixed list of answers will not work for other settings or counts.

Edit `main.py`, Run to see both schedules, then Submit.

## Your Tasks

1. Use `np.repeat` in `hold_settings(settings, frames)` to repeat each setting `frames` times.
2. Use `np.tile` in `cycle_settings(settings, cycles)` to copy the complete setting pattern `cycles` times.
