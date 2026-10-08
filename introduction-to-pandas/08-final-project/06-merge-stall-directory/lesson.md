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
- Read the previous completed function above the new stub; Run for a checkpoint, then
  Submit.
---

# Attach the stall directory

Sales have IDs, while the stall directory has the names and neighborhoods needed in a public report. Merge on the shared `stall_id`. A **left** join keeps every selected sale, even if a new stall has not yet been added to the directory; its name will be missing rather than the sale silently disappearing.

All four prior functions are complete in this starter. Add only `attach_stalls`, Run to inspect joined columns, then Submit with a directory in a different order and an unknown ID.

## Your Tasks

1. Implement `attach_stalls(selected, stalls)` as a left merge on `stall_id`, keeping selected sale order and all selected rows without mutating either input.
