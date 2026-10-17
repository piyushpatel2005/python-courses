---
title: "Let the question choose the chart"
slug: choose-by-question
order: 11
language: python
lesson_type: coding
pyodide_packages:
  - matplotlib
summary: "A garden report asks either which bed grew more or how harvest weights vary."
seo_title: "Let the question choose the chart | Python Charts"
seo_description: "Named categories suggest bars; a list of individual numeric observations suggests a histogram. The question determines the chart, not the palette."
seo_keywords: [Python charts, matplotlib, "choose by question"]
hints:
  - "Keep the compare branch unchanged."
---
A garden report asks either which bed grew more or how harvest weights vary.

Named categories suggest bars; a list of individual numeric observations suggests a histogram. The question determines the chart, not the palette.

The sample asks for a distribution, but the unmatched branch falls back to bars. Make one small edit so Run changes the visible chart to a histogram. The function accepts new data, so the same choice works for other observations.

## Your Task

1. Replace `"spread"` with `"distribution"` in the branch condition.

Edit `main.py`, press **Run** to view the figure, then **Submit** to check your change.
