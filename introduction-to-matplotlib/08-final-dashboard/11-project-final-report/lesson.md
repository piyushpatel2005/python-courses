---
title: 'Project stage 3: Publish a careful report'
slug: project-final-report
order: 11
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Finish the four-panel dashboard with coverage counts and a noncausal interpretation.'
seo_title: 'Project stage 3: Publish a careful report | Introduction to Matplotlib'
seo_description: 'Finish the four-panel dashboard with coverage counts and a noncausal interpretation.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'project'
  - 'stage'
  - '3'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Project stage 3: Publish a careful report

Your dashboard now has all four views. Give the viewer context below the panels: how many garden days remain after cleaning, how many dates were actually paired, and a reminder that paired observations do not prove cause and effect. Return the same counts in `report(...)` for a short written handoff. The example has a missing garden reading on May 3, so a raw row count would be misleading.

**Reading the finished example:** A rise in the temperature line does not by itself explain any change in visits. The branch bars compare total visits over the available records, not rates normalized for opening hours. The transit line is summed route rides, not a count of distinct people; a rider may take multiple routes. The scatter includes only matched dates. Before making a policy claim, ask whether different coverage or another factor explains the pattern.

Edit `main.py`, press **Run** to inspect the figure, then **Submit**. The checks also use different observations, not just the values shown here.

## Your Tasks

1. Return a report with cleaned `garden_days`, `shared_days`, `library_visits`, `transit_rides`, and a noncausal `caveat`, computed from `prepare_signals`.
2. Add a readable figure-level note showing garden and shared-day counts and the noncausal caveat; leave room for it beneath the panels.

The report now separates what the plots show from what they cannot establish. Share the dashboard with that distinction intact.
