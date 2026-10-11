---
title: Read JSON records
slug: read-json-records
order: 7
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Read a JSON list of records into a DataFrame using StringIO.
seo_title: Read JSON records | Introduction to Pandas
seo_description: Read a JSON list of records into a DataFrame using StringIO.
seo_keywords:
  - pandas
  - read_json
  - JSON records
  - StringIO
hints:
  - "Keep the read_json call and select name from the DataFrame it returns."
---

# Read JSON records

The stall registry uses **JSON**, a text format for structured values. Here square brackets surround a list of records; each record is an object in braces with key-value pairs such as `"name":"Honey Table"`. JSON uses double quotes around keys and text values. The outer single quotes in `main.py` belong to the Python string, not the JSON inside it.

With `orient="records"`, `pd.read_json(StringIO(text), ...)` treats each object as a row and its keys as columns. `StringIO` supplies the text as a file-like buffer, just as it did for CSV.

The reader is already written. In `main.py`, change only the selected column in `lookup_names` from `"stall_id"` to `"name"`. Run should display Honey Table and Clay Corner instead of S1 and S2. Submit checks another registry.

## Your Tasks

1. Make `lookup_names(text)` read the JSON records and return their `name` Series instead of their IDs.
