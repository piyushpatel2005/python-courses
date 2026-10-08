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
  - Read the shape of each intermediate array before editing another line.
---

# Final project: Pocket Observatory report

The Pocket Observatory has one last packet: a flat strip of sky readings. Build a short observation report from it. Reuse the same small tools in a new pipeline: arrange the strip into three-column sky rows, expand a schedule, export a CSV string, read it back, then summarize the grid. Each function can be checked independently.

`make_sky_grid` should return a grid, not edit the original strip. For `exposure_schedule`, `settings[:, np.newaxis]` makes a `(N, 1)` column. Repeating along axis 0 doubles its rows; `np.tile(held, (1, 2))` keeps that row count and copies each column across twice. For example `[2, 5]` becomes `[[2, 2], [2, 2], [5, 5], [5, 5]]`. This is deliberate duplication, unlike inserting a singleton axis alone.

Use `StringIO` for the CSV; it lasts only inside this run, so Run again to recreate it. Do not use an external file path. The report format is `Rows: N; brightest: V; row means: A, B` with one decimal place for each mean. Assume a non-empty strip with a multiple of three readings.

Edit `main.py` and Run after each function; Submit checks each numbered step in order. The finished report is the Observatory's hand-off card.

## Your Tasks

1. In `make_sky_grid(strip)`, reshape the strip to three columns with an inferred row count.
2. In `exposure_schedule(settings)`, turn settings into a column with `np.newaxis`, repeat each row twice, and tile the result into two columns.
3. In `export_sky(grid)`, return comma-delimited integer CSV text using `np.savetxt` and `StringIO`.
4. In `import_sky(text)`, read integer CSV with `np.genfromtxt`, comma delimiter and `ndmin=2`.
5. In `observation_report(grid)`, return `Rows: N; brightest: V; row means: A, B` with each row mean formatted to one decimal place.
