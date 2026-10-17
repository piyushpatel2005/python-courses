---
title: 'Exercise: Label Beacon Charge'
slug: exercise-ticket-counts
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: 'Convert valid charge text and recover from invalid values.'
seo_title: 'Exercise: Label Beacon Charge | Python Basics'
seo_description: 'Convert valid charge text and recover from invalid values.'
seo_keywords: [python try except exercise, traceback, ValueError]
---

A charge label should still be readable when its source text is blurred. First write a helper that turns text into a number, using zero for invalid text. Then let a second helper use that result in a label.

Catch `ValueError` specifically. A bare `except` can hide a different bug that you need to see.

Edit `main.py` and Submit after each helper; the tests check them separately. Run shows the label examples once the second helper is complete.

## Your Tasks

1. Complete `charge_value(text)` to return `int(text)` or `0` when it raises `ValueError`, using `try`/`except ValueError`.
2. Complete `charge_label(text)` to return `"Charge: <count>"` using `charge_value(text)`.
