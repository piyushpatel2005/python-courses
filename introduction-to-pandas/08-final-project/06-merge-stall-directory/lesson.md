---
title: Attach the stall directory
slug: merge-stall-directory
order: 6
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Join selected sales with stall names and neighborhoods by stall_id.
seo_title: Attach the stall directory | Introduction to Pandas
seo_description: Join selected sales with stall names and neighborhoods by stall_id.
seo_keywords:
  - pandas
  - community market report
  - left merge
  - stall_id
hints:
  - "Call merge on selected, with stalls as the right-hand table and how=\"left\"."
---

# Attach the stall directory

The selected sales still have stall IDs rather than neighborhood names. Join them to the directory using the shared `stall_id`, not row positions: the directory might be in a different order.

Use a left merge so an unknown stall does not silently remove a sale. The joined row keeps its sales values and has missing directory fields. Keep `sort=False` to retain the selected sale order. The supplied directory has one row per stall ID; `validate="many_to_one"` can check that assumption and raise an error if a duplicate directory ID would multiply sales rows. The solution uses that guard.

Edit only `attach_stalls` in `main.py`. Run should attach Orchard Table/North to sale 1 and Oven Corner/South to sale 5. Submit tries reordered directories, repeated sales from one stall, and an unknown ID. Earlier helpers are supplied, not new tasks.

## Your Tasks

1. Implement `attach_stalls(selected, stalls)` as a left merge on `stall_id`, retaining selected sale order and all selected rows without mutating either input.
