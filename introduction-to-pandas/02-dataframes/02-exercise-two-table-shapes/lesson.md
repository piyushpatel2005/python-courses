---
title: "Exercise: Assemble two tables"
slug: exercise-two-table-shapes
order: 2
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Turn supplied column lists and row records into DataFrames."
seo_title: "Exercise: Assemble two tables | Pandas for beginners"
seo_description: "Turn supplied column lists and row records into DataFrames."
seo_keywords: ["pandas", "Python data analysis", "columns and row records"]
---

The supply desk receives one batch as a dictionary of columns and another as a list of row dictionaries. Write one function for each input format. In both cases, `pd.DataFrame(...)` can build the table from the supplied argument.

Do not type the sample fruit names into the functions. The next delivery may use different column names or contain more rows. Keep the incoming names, values, and order.

## Your Tasks

1. Make `from_columns(columns)` return a DataFrame built from the supplied dictionary of column lists.
2. Make `from_records(records)` return a DataFrame built from the supplied list of row dictionaries.

Edit `main.py` and **Run** after each task. First you should see an apple table followed by `None`; when both functions are complete, the second output is a pear table. **Submit** checks each function with other deliveries.
