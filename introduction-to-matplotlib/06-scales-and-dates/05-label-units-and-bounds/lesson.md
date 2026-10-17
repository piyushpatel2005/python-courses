---
title: "Show units and honest axis bounds"
slug: label-units-and-bounds
order: 5
language: python
lesson_type: coding
pyodide_packages: ["matplotlib"]
summary: "Show units and honest axis bounds using an explicit Matplotlib Figure and Axes."
seo_title: "Show units and honest axis bounds | Neighborhood Signals Matplotlib"
seo_description: "The community hall has a maximum occupancy. The axis should show zero and the full capacity, not crop the upper limit of the count."
seo_keywords: ["matplotlib", "python charts", "label units and bounds"]
---
The community hall has a maximum occupancy. The axis should show zero and the full capacity, not crop the upper limit of the count.

`set_ylim(0, capacity)` gives the y-axis a meaningful range. Set the example capacity to 24 instead of 20, leaving headroom above the peak.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. Set the upper y-axis limit to 24 while keeping the lower limit at zero.
