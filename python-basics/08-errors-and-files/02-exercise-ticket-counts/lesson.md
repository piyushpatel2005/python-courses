---
title: 'Exercise: Label Beacon Charge'
slug: exercise-charge-counts
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: 'Convert valid charge text and recover from invalid values.'
seo_title: 'Exercise: Label Beacon Charge | Python Basics'
seo_description: 'Convert valid charge text and recover from invalid values.'
seo_keywords: [python try except exercise, traceback, ValueError]
---

Ari must label the shrine charge even when a reading is blurred. Reuse the preceding `try`/`except ValueError` pattern; a bare `except` could hide unrelated mistakes.

Edit `main.py`, **Run** to compare valid and faded readings, then **Submit**. The two helpers are checked separately.

## Your Tasks

1. Complete `charge_value(text)` to return `int(text)` or `0` when it raises `ValueError`, using `try`/`except ValueError`.
2. Complete `charge_label(text)` to return `"Charge: <count>"` using `charge_value(text)`.
