---
title: 'Exercise: round-trip a sales table'
slug: exercise-csv-roundtrip
order: 10
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Write CSV text and read it back into a DataFrame without an index column.
seo_title: 'Exercise: round-trip a sales table | Introduction to Pandas'
seo_description: Write CSV text and read it back into a DataFrame without an index
  column.
seo_keywords:
- pandas
- CSV roundtrip
- to_csv
- read_csv
hints:
- Use the example above the task and check the printed result before submitting.
---

# Exercise: round-trip a sales table

Now save a small table and prove you can recover it. `to_csv(index=False)` returns text; `pd.read_csv(StringIO(text))` rebuilds the rows. Here `product` holds ordinary nonempty names such as `Tea` and `Jam, nuts` (not number-like or boolean-like strings, or missing-value markers), and `units` holds small whole numbers without missing values. Under these assumptions, the values and column types survive the round trip. By default, `read_csv` **infers types and missing values**: a text code such as `"0012"` can become the number `12`, `"True"` can become a boolean, and `"NA"` or an empty cell can become missing. For those inputs, specify column `dtype` and missing-value options when reading; dates also need explicit parsing if you want their type restored.

Edit `main.py`, Run to see the exported text and recovered table, then Submit. Do not hardcode the sample rows: the tests supply different tables, including a nondefault original index.

## Your Tasks

1. Implement `roundtrip_table(frame)` for the stated `product`/`units` inputs to return `(csv_text, recovered_frame)` where the CSV omits the old index and the recovered DataFrame contains the same columns and values.
