---
title: "Project: report calibrated peaks"
slug: calibrated-panel-finish
order: 10
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: 'Continue the panel project with a maximum reading for each derived channel.'
seo_title: "Project: report calibrated peaks | Intro to NumPy"
seo_description: 'Continue the panel project with a maximum reading for each derived channel.'
seo_keywords: [numpy, arrays, matrices]
hints:
  - calibrated_channels puts channels in rows, so axis=1 reduces across nights.
---

Keep the same panel and calibration from the previous lesson. Both finished helpers are already in `main.py`, and the first print shows the calibrated channel rows.

Add one peak reading for each channel. Call `calibrated_channels` to get the channel-by-night array, then use `np.max(..., axis=1)` to reduce across the nights. This leaves one maximum for each channel row. If you worked with the untransposed matrix product instead, the night axis would be `axis=0`.

Run the starter to see the existing channel table. Fill in `channel_peaks`, Run again to see the peaks beside it, then Submit.

## Your Task

1. Implement `channel_peaks(grid, calibration)` to return the maximum across each row of the calibrated channel table.

The panel now has a calibration table and a peak summary. Next, you will change how a flat packet is arranged without changing its readings.
