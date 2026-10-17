---
title: "Exercise: Connect counts in day order"
slug: exercise-sort-table-line
order: 8
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "pandas"]
summary: "Exercise: Connect counts in day order using an explicit Matplotlib Figure and Axes."
seo_title: "Exercise: Connect counts in day order | Neighborhood Signals Matplotlib"
seo_description: "A community pantry export lists collection days out of order. Plot the count trend in time order, even when incoming rows move around."
seo_keywords: ["matplotlib", "python charts", "exercise sort table line"]
---
A community pantry export lists collection days out of order. Plot the count trend in time order, even when incoming rows move around.

Sort the entire DataFrame before selecting its `day` and `parcels` columns. Sorting the two columns separately breaks the pairs.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. In `plot_parcels`, sort rows by `day` and plot the corresponding parcel counts as one line.
2. Label the x-axis `Day` and y-axis `Parcels (boxes)`.
