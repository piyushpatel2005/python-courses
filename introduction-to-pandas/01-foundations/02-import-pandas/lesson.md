---
title: "Import pandas for a stall card"
slug: import-pandas
order: 2
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Read the pandas import and edit a Series built from a list."
seo_title: "Import pandas for a stall card | Pandas for beginners"
seo_description: "Read the pandas import and edit a Series built from a list."
seo_keywords: ["pandas", "Python data analysis", "import pandas as pd"]
---

The first line, `import pandas as pd`, loads pandas and gives it the short name `pd`. That is why the next line can call `pd.Series(...)` rather than `pandas.Series(...)`.

The list inside the parentheses supplies this card's values: `4`, `6`, and `3`. We have not supplied names this time, so pandas prints the labels `0`, `1`, and `2` on the left. The counts are on the right. You will work with those default labels shortly.

## Your Task

1. Change the last value in the list used to create `counts` from `3` to `7`.

Edit `main.py` and press **Run**. The last row should now pair label `2` with count `7`. Leave the import and `print(counts)` in place, then **Submit**.
