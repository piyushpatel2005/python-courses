---
title: "Echo Tower: Select Beacon Labels"
slug: exercise-clean-badge-names
order: 4
language: python
lesson_type: coding
runtime: pyodide
summary: Use map and filter to prepare beacon labels.
seo_title: "Echo Tower: Select Beacon Labels | Python Basics"
seo_description: Use map and filter to prepare beacon labels.
seo_keywords: [python map filter exercise, beacon labels]
---

The tower's display expects uppercase beacon labels, but it has room only for labels with at least four characters. The frequency demo transformed numbers; here you transform **strings**, then filter the transformed list. `list(map(...))` and `list(filter(...))` expose the results.

Edit `main.py`, Run to see the two lists, then Submit. After both steps, the Echo Tower has a clean list of labels to send toward the gate. The final game mission uses ordinary functions and loops instead of requiring these optional compact tools.

## Your Tasks

1. Set `upper_labels` to `list(map(...))` using a lambda that uppercases each item in `beacon_labels`.
2. Set `long_labels` to `list(filter(...))` using a lambda that keeps labels of at least four characters from `upper_labels`.
