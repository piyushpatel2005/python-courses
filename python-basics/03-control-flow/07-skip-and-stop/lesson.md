---
title: Skip with continue, stop with break
slug: skip-and-stop
order: 7
language: python
runtime: pyodide
lesson_type: coding
summary: Distinguish skipping one iteration from leaving the loop.
seo_title: Skip with continue, stop with break | Python Basics
seo_description: Distinguish skipping one iteration from leaving the loop. Practice
  Python control flow in an editable browser lesson.
seo_keywords:
- python continue
- python break
- loop control
---

# Skip with continue, stop with break

At a depot, parcel 2 is damaged and should not be loaded. `continue` skips the rest of **this turn**; `break` leaves the **whole loop**. The starter visits parcels 1 through 6, skips 2, and stops when parcel 5 is reached. It prints `Loaded 1 | Loaded 3 | Loaded 4 | `. The checks must happen before appending a label.

Edit **main.py**: change the skipped parcel from `2` to `3`. Press **Run**; the result should be `Loaded 1 | Loaded 2 | Loaded 4 | `. Then press **Submit** to check the change. Be cautious with `continue` in a `while` loop: update the counter before skipping, or the loop may never end.

## Your Task

1. Change the skipped parcel from `2` to `3` so the printed load includes parcel 2 but not parcel 3.
