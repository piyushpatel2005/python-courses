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

Ari gathers charge readings for the Save Shrine. Some are faded; count those as zero, then store the total in `beacon-save.txt` and read it back in the same run. Files in Pyodide are temporary, not permanent device saves. The sample needs no `input()`.

Edit `main.py`, **Run** to see `Charge: 5`, then **Submit** each helper in task order.

## Your Tasks

1. Complete `total_charge(entries)` to add converted counts in a loop and treat `ValueError` entries as zero; an empty list totals zero.
2. Complete `save_beacons(entries)` to write exactly `"Charge: <total>"` to `beacon-save.txt` using `total_charge` and `with open(..., "w", encoding="utf-8")`.
3. Complete `read_beacons()` to return the whole saved file with `with open(..., "r", encoding="utf-8")`.

The shrine can now recover a faded reading and restore its in-memory save before Ari enters the Tool Library.
