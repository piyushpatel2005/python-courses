---
title: Mark noisy readings
slug: boolean-selection
order: 7
language: python
lesson_type: coding
pyodide_packages:
  - numpy
summary: A comparison such as `readings > 20` returns a boolean array.
seo_title: Mark noisy readings | NumPy
seo_description: Turn a comparison into a Boolean mask and replace the readings it flags.
seo_keywords:
  - NumPy
  - Python
  - boolean selection
hints:
  - Keep `readings[flagged]` on the left; change only its replacement value.
---

A sensor flags any reading beyond a safe limit.

A comparison such as `readings > 20` checks every value and returns a Boolean array, called a **mask**. For this example it is `[False, True, False, True]`: the `True` positions identify `24` and `31`. A reading of exactly `20` would not be flagged.

For these one-dimensional readings, the mask has the same length as the array. `readings[flagged]` gathers matching values into a new array. Used directly on the left of `=`, as in the starter, it replaces those slots in `readings` itself. Saving the gathered result and editing it later would only change that separate copy.

## Your Task

1. Change the replacement value to `0`; Run shows the two flagged readings cleared.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check the change.
