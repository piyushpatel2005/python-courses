---
slug: introduction-to-matplotlib
title: "Introduction to Matplotlib: Neighborhood Signals"
description: "Turn NumPy arrays and Pandas tables into clear, honest charts through short Python builds."
summary: "Make readable line, bar, scatter, histogram, and multi-panel charts, then build a neighborhood data dashboard."
language: python
level: Beginner
format: Coding lessons, visual experiments, projects, and quizzes
seo_title: "Introduction to Matplotlib | Hands-on Python Chart Course"
seo_description: "Practice line charts, bars, scatter plots, histograms, subplots, dates, and honest data visualization with NumPy and Pandas."
seo_keywords: [matplotlib course, python charts, numpy plotting, pandas visualization, data visualization exercises]
modules:
  - slug: first-figure
    title: "1. Draw Your First Figure"
    sort_order: 1
  - slug: readable-lines
    title: "2. Make Lines Speak Clearly"
    sort_order: 2
  - slug: chart-types
    title: "3. Choose the Right Chart"
    sort_order: 3
  - slug: plot-layout
    title: "4. Tell Stories with Panels"
    sort_order: 4
  - slug: data-to-chart
    title: "5. Plot NumPy and Pandas Data"
    sort_order: 5
  - slug: scales-and-dates
    title: "6. Handle Scales and Dates"
    sort_order: 6
  - slug: honest-visuals
    title: "7. Make Honest, Accessible Visuals"
    sort_order: 7
  - slug: final-dashboard
    title: "8. Build a Neighborhood Dashboard"
    sort_order: 8
---

# Neighborhood Signals

A neighborhood team tracks garden temperatures, library visits, and transit use. A table holds the observations, but a carefully chosen chart helps someone see what changed and what deserves attention. You will make those charts one small improvement at a time.

Begin with a Figure and its plotting area, then draw and label lines. Move through bars, scatter plots, distributions, multiple panels, dates, and scales. Bring the NumPy and Pandas skills you already have to turn real-looking records into pictures. The final project combines several views into one readable dashboard.

You should already know Python functions and lists, NumPy arrays, and Pandas Series/DataFrames. You do not need to be an artist or know statistics beyond a simple average. Each example invites a small edit; the next exercise asks you to write the pattern on new data. Edit `main.py`, press **Run** to view the chart and its console output, and press **Submit** for task-by-task feedback. Quizzes close each section.

These lessons favor the explicit `fig, ax = plt.subplots()` pattern: the figure holds the whole composition, and each Axes holds one plot. You will learn how to choose a useful chart, not just how to draw one. The datasets are small and self-contained so changing a value gives immediate visual feedback.
