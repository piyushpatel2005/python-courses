---
title: "Project: Workshop Receipts"
slug: project-workshop-receipts
order: 9
language: python
runtime: pyodide
lesson_type: coding
summary: Build reusable receipt calculations and a printed workshop summary.
seo_title: "Project: Workshop Receipts | Python Basics"
seo_description: Build reusable receipt calculations and a printed workshop summary.
seo_keywords: [python basics, project workshop receipts, python practice]
hints:
  - Return values from each function; the supplied print combines them.
---

# Project: Workshop Receipts

Build a tiny receipt engine for workshop supply bags. One helper calculates a bag's total, then another labels it. Unlike a one-off print, these functions can process many bags. This is the section payoff: once both tasks pass, you have a reusable two-stage program.

## Your Tasks

1. Complete `bag_total(count, price)` so it returns their product for any bag.
2. Complete `receipt(name, amount)` so it returns `name: $amount` using the given values.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.
