---
title: Clean the sale rows
slug: clean-sale-rows
order: 3
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Convert types, remove repeated IDs and discard unusable sales.
seo_title: Clean the sale rows | Introduction to Pandas
seo_description: Convert types, remove repeated IDs and discard unusable sales.
seo_keywords:
  - pandas
  - community market report
  - drop_duplicates
  - to_numeric
  - to_datetime
hints:
  - "Assign each operation back to cleaned or its named column. Leave the copy and reset-index return in place."
---

# Clean the sale rows

The sample repeats sale ID 2 and leaves one unit count blank. Clean these rows before multiplying amounts. The completed import is supplied; make the changes inside `clean_sales` in `main.py`.

The starter creates a copy and returns a fresh index. Add one cleaning operation at each task comment, then Run or Submit. Run keeps working while later comments are unfinished. The tests use separate inputs for each operation, so removing duplicates does not require date conversion to be complete.

Keep the first occurrence of each `sale_id`, even if a later copy looks more usable. Convert `sold_at` with `pd.to_datetime(..., format="%Y-%m-%d", errors="coerce")`. These inputs are timezone-free year-month-day dates; a bad date becomes `NaT`. For each amount column, `pd.to_numeric(..., errors="coerce")` turns a bad numeric value into a missing value. Neither conversion drops a row by itself.

After conversion, `dropna(subset=[...])` removes rows missing a required date or amount. Finally keep positive units and prices of zero or more; a free item is allowed, but a return with negative units is outside this sales report. The supplied copy protects the original sheet for an audit.

Run begins at six raw and six returned rows. After duplicate removal there are five. With every task finished, the clean sale IDs are 1, 2, 4, and 5.

## Your Tasks

1. Remove repeated `sale_id` values from `cleaned`, keeping the first occurrence.
2. Convert `cleaned["sold_at"]` to datetimes in year-month-day format, coercing invalid values to `NaT`.
3. Convert `cleaned["units"]` to numbers, coercing invalid values to missing.
4. Convert `cleaned["unit_price"]` to numbers, coercing invalid values to missing.
5. Remove rows missing any of `sold_at`, `units`, or `unit_price`.
6. Keep only rows with `units > 0` and `unit_price >= 0`.
