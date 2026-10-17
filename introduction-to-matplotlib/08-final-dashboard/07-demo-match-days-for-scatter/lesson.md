---
title: 'Demo: Match days before scatter'
slug: demo-match-days-for-scatter
order: 7
language: python
lesson_type: coding
runtime: pyodide
pyodide_packages:
  - matplotlib
  - numpy
  - pandas
summary: 'Merge two daily tables so each scatter point is one shared day.'
seo_title: 'Demo: Match days before scatter | Introduction to Matplotlib'
seo_description: 'Merge two daily tables so each scatter point is one shared day.'
seo_keywords:
  - 'matplotlib'
  - 'python visualization'
  - 'neighborhood signals'
  - 'demo'
  - 'match'
  - 'days'
hints:
  - 'Check the Axes labels, data and limits before changing the style.'
---

# Demo: Match days before scatter

A scatter plot needs genuine pairs. Garden temperatures and library visits are in separate tables; sorting each independently and plotting row positions could pair the wrong days. An inner merge on `day` keeps only dates in both tables. Change the annotation from a causal claim to a careful description of matched observations.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Set the chart title to `Matched garden and library days`.
