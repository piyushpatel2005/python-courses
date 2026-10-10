---
title: 'Final project: Pocket Observatory report'
slug: final-pocket-observatory
order: 11
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - numpy
summary: Shape a sky grid, schedule exposures, round-trip CSV, and write a report.
seo_title: 'Final project: Pocket Observatory report | Intro to NumPy'
seo_description: Shape a sky grid, schedule exposures, round-trip CSV, and write a
  report.
seo_keywords:
  - numpy
  - array shape
  - final pocket observatory
hints:
  - Finish one helper at a time; the supplied formatter handles the report punctuation.
---

# Final project: Pocket Observatory report

The Pocket Observatory has one last packet: a flat strip of sky readings. Arrange it into rows, prepare an exposure schedule, and send the grid through a CSV round trip before reporting its brightest reading and row averages.

You have used each operation already. This starter separates the schedule into small helpers so you can inspect the column, repeated rows, and final paired columns independently. The sample packet is new; assume it is non-empty and its length is a multiple of three.

## Build the schedule in stages

`np.newaxis` turns settings into a column without duplicating them. Then `np.repeat(column, 2, axis=0)` repeats whole rows. Finally, `np.tile(held, (1, 2))` keeps the row count and copies the column across twice. For settings `[2, 5]`, the finished schedule has rows `[2, 2]`, `[2, 2]`, `[5, 5]`, and `[5, 5]`.

The starter connects these helpers for the printed schedule. Each check also calls its helper directly with appropriate input, so you can earn credit one step at a time.

## Prepare the hand-off

Use the CSV pattern from the previous exercise: an empty `StringIO` buffer, `np.savetxt` with `fmt="%d"`, and `getvalue()` for the text. Read from a fresh `StringIO(text)` with `dtype=int` and `ndmin=2`. The temporary text is recreated each Run; no external file is needed.

The supplied `format_report(rows, brightest, row_means)` helper handles the final sentence and one-decimal formatting. Your `observation_report` function only needs to compute its three inputs: the row count, the overall maximum, and `np.mean(grid, axis=1)`. Return the formatted string rather than printing inside the function.

Edit `main.py` and Run after each helper. The guarded print calls let you inspect early work while later functions remain unfinished. Submit checks the following outcomes in order.

## Your Tasks

1. In `make_sky_grid(strip)`, use `reshape` to return a three-column grid with an inferred row count, without changing the strip's values or shape.
2. In `exposure_column(settings)`, use `np.newaxis` to return one column of settings.
3. In `hold_exposures(column)`, use `np.repeat` along `axis=0` to return two adjacent copies of each row.
4. In `exposure_schedule(settings)`, use `np.tile` on the supplied `held` result to return the finished two-column schedule.
5. In `export_sky(grid)`, return comma-delimited integer CSV text using `np.savetxt` and `StringIO`.
6. In `import_sky(text)`, use `np.genfromtxt` and `StringIO` to return a two-dimensional integer grid.
7. In `observation_report(grid)`, use the supplied formatter to return a report with the row count, brightest reading, and one mean per row.

For the supplied packet, the report should read `Rows: 2; brightest: 9; row means: 6.0, 5.0`. You now have a small observation packet that can be shaped, checked, and passed on as text.
