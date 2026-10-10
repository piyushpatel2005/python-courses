---
title: Join indexed areas
slug: join-indexed-areas
order: 9
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Use set_index and join to attach area managers to stalls."
seo_title: Join indexed areas | Introduction to Pandas
seo_description: "Use set_index and join to attach area managers to stalls."
seo_keywords:
  - pandas
  - join indexed areas
  - community market data
hints:
  - 'Keep set_index("area") and change only the join retention mode.'
---

# Join indexed areas

The manager lookup already uses area codes as its row index. `join` matches indexes by default. First, `a.set_index("area")` makes the booking table use those same area labels; it removes `area` from the ordinary columns in the returned table. Calling `.join(b, ...)` on that result attaches the manager column.

The current inner join drops W because the lookup has no W entry. Change it to a left join so Elm remains visible with a missing manager. The N row should still name Ada. This is the same retention choice as a left merge, with keys stored in indexes instead of two named columns.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Change `how` to `left` in `attach_areas`.
