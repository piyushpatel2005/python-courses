---
title: "Exercise: Find two counts"
slug: exercise-pick-counts
order: 9
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Series label and position selection for a community market data desk."
seo_title: "Exercise: Find two counts | Pandas for beginners"
seo_description: "Series label and position selection for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "series label and position selection"]
---
One caller knows a stall label; another knows where a count appears in the card. Keep those two requests separate. The supplied Series may arrive in any label order.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Tasks

1. Make `by_label(card, label)` return the value at the supplied index label using `loc`.
2. Make `by_position(card, position)` return the value at the supplied integer position using `iloc`.
