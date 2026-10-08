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
- Use the example above the task and check the printed result before submitting.
---

# Read JSON records

A stall registry may arrive as JSON rather than CSV. In a JSON list of objects, each object becomes a row and each key becomes a column. `pd.read_json(StringIO(text), orient="records")` expresses that layout explicitly.

The starter already reads the text. Its `lookup_names` function returns the wrong column: change only `["stall_id"]` to `["name"]`. Run to see the names, then Submit with a different registry.

## Your Tasks

1. Make `lookup_names(text)` read JSON records and return the `name` Series instead of the IDs.
