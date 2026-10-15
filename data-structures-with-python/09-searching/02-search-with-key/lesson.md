---
title: "Search records through a key function"
slug: "search-with-key"
order: 2
language: "python"
runtime: pyodide
lesson_type: "coding"
summary: "Compare one chosen field while preserving first-match order and record identity."
seo_title: "Search records through a key function | Data structures with Python"
seo_description: "Compare one chosen field while preserving first-match order and record identity."
seo_keywords:
  - Python
  - search with key
  - data structures
---

A record can contain several fields, but a search usually cares about one of them. A key function extracts that field. It lets the scan stay the same while callers decide what counts as a match.

This is a fresh generalization of linear search. `search_with_key(records, target, key)` calls `key(record)` for each visited record and compares the extracted value to target. It returns the first matching index or `-1`, just like the previous lesson. The target is already the extracted value; do not apply key to it.

For a separate example, records might be `[("reed", 5), ("stone", 8)]`. A key function `lambda row: row[1]` chooses the second tuple field, so a target of eight matches index one. `lambda` creates a small callable expression. A named function with the same behavior works too. The annotation `Callable[[object], object]` says the callback accepts one record and returns its comparison value; the actual record shape is the caller's contract.

Call the callback once per visited record, in left-to-right order. Stop after the first match. This matters when extraction is expensive or when the caller records which items were inspected. Do not sort the records, build an index, or call the callback for every record before searching. Those choices change the work and may change observable behavior.

Empty input returns `-1` without calling key. Duplicate extracted keys select the first record. Do not mutate the records or their fields, and let any exception from the callback propagate rather than pretending a failed extraction means missing.

The scan uses O(1) extra space and up to n callback calls and equality checks. Its total cost includes extraction and comparison. If each is constant-time, the worst case is O(n); a match at the first record is O(1).

## Build it in small steps

The supplied scan already calls the key function. Finish its missing result before adding the successful early return.

## Your Tasks

1. Return `-1` when no extracted key matches the target.
2. Return the first matching record index while calling the key function once per visited record.

Edit `main.py` one step at a time. Run uses the supplied probe; an unfinished field or return value may print a reminder. Submit checks the numbered steps in order, so you can see each completed step before finishing the next.
