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
  - "Read the string you just exported, rather than rebuilding a copy of the input table."
---

# Exercise: round-trip a sales table

Before sharing a sales table, check what comes back when you read its CSV text. This is a **round trip**: DataFrame → text → DataFrame. The old row labels are deliberately left behind.

Use `to_csv(index=False)` to get the text, then read a fresh `StringIO` buffer containing that text. Return both results as a tuple so the supplied Run code can print each one.

For this exercise, `product` contains ordinary nonempty names such as `Tea` or `Jam, nuts`, and `units` contains small whole numbers without missing values. The CSV writer quotes names containing commas for you; let the reader handle those quotes.

CSV does not remember pandas dtypes. The reader infers them again: `"0012"` may become 12, `"True"` may become a boolean, and `"NA"` or an empty cell may become missing. These special-looking names are outside this exercise's input contract. For such data, choose explicit `dtype` and missing-value options when reading; dates also need parsing again.

Edit `roundtrip_table` in `main.py`, Run to inspect both results, then Submit. The recovered table should have a fresh default index.

## Your Tasks

1. Implement `roundtrip_table(frame)` to return `(csv_text, recovered_frame)` for the stated `product`/`units` inputs, omitting the old index and preserving the columns and values.
