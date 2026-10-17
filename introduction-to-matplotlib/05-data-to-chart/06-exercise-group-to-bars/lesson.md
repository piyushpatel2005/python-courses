---
title: "Exercise: Average trips by route"
slug: exercise-group-to-bars
order: 6
language: python
lesson_type: coding
pyodide_packages: ["matplotlib", "pandas"]
summary: "Exercise: Average trips by route using an explicit Matplotlib Figure and Axes."
seo_title: "Exercise: Average trips by route | Neighborhood Signals Matplotlib"
seo_description: "A transit table records multiple journey times for each route. The chart should show route means rather than individual trips."
seo_keywords: ["matplotlib", "python charts", "exercise group to bars"]
---
A transit table records multiple journey times for each route. The chart should show route means rather than individual trips.

Group by `route`, select `minutes`, and use `mean()`. Keeping the route labels with the grouped values avoids a misleading bar order.

Edit `main.py`, press **Run** to inspect the figure, then **Submit** to check the change.

## Your Tasks

1. In `plot_route_means`, group the DataFrame by `route`, average `minutes`, and draw one bar for each route.
2. Label the x-axis `Route` and y-axis `Mean trip (minutes)`.
