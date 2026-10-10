---
title: 'Mini Project: Restore the Save Shrine'
slug: mini-project-attendance-log
order: 5
language: python
lesson_type: coding
runtime: pyodide
summary: 'Recover charges, write a shrine save, and read it back.'
seo_title: 'Mini Project: Restore the Save Shrine | Python Basics'
seo_description: 'Recover charges, write a shrine save, and read it back.'
seo_keywords: [python mini project, error handling, file handling]
---

Collect several shrine readings into one save. Some readings are faded; treat those as zero and add the valid numbers. Then write the total to `beacon-save.txt` and read it back in the same run.

The save is a temporary browser file. The starter supplies the readings, so you do not need `input()`.

Build the helpers in `main.py` in task order and Submit after each one. Run shows `Charge: 5` once the save and read helpers work; unfinished helpers may still print `None`.

## Your Tasks

1. Complete `total_charge(entries)` to add converted counts in a loop and treat `ValueError` entries as zero; an empty list totals zero.
2. Complete `save_beacons(entries)` to write exactly `"Charge: <total>"` to `beacon-save.txt` using `total_charge` and `with open(..., "w", encoding="utf-8")`.
3. Complete `read_beacons()` to return the whole saved file using `with open(..., "r", encoding="utf-8")`.
