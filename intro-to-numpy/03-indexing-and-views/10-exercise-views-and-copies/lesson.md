---
title: 'Exercise: preserve a calibration snapshot'
slug: exercise-views-and-copies
order: 10
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: A new instrument must expose a live middle window and a safe snapshot of
  the same span.
seo_title: 'Exercise: preserve a calibration snapshot | NumPy'
seo_description: Create a live slice and an independent snapshot, then observe which edits reach the source.
seo_keywords:
  - NumPy
  - Python
  - views and copies
hints:
  - Use the slice `1:3` for the middle two items; add `.copy()` only for the snapshot.
---

Work with a four-reading record. Its middle two items are at indices `1` and `2`. You need a live window into that span and a separate snapshot taken before calibration.

The starter uses empty slices as placeholders, so it can run before either selection is ready. Replace those two lines, then add each edit above the return. Make the snapshot before changing the view so it begins with the original readings.

## Your Tasks

1. Set `view` to the middle-two-item slice of `record` without copying it.
2. Set `snapshot` to an independent copy of that same span.
3. Set the first item of `view` to `50`.
4. Set the first item of `snapshot` to `-5`.

Edit `main.py`, press **Run**, then **Submit** to check your progress. After all four steps, the source's second reading is `50`, while the snapshot's first reading is `-5`.

The next module applies arithmetic to whole arrays. Knowing whether an array shares storage will help you tell which readings an edit can affect.
