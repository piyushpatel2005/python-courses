---
title: "Build a frequency index"
slug: "frequency-index"
order: 12
language: "python"
runtime: pyodide
lesson_type: "coding"
summary: "Apply the completed chained table to count exact string occurrences."
seo_title: "Build a frequency index | Data structures with Python"
seo_description: "Apply the completed chained table to count exact string occurrences."
seo_keywords:
  - Python
  - frequency index
  - data structures
---

A workshop log contains repeated material labels. Build an index that answers how often each exact label occurred. This application returns to the completed separate-chaining `HashTable` from the rehash lesson; it does not use the probing variant. All table methods are supplied again, so nothing needs to be copied between editors.

Create a fresh table for each call. Reserve `max(1, 2 * len(words))` buckets. This keeps the maximum live load at one half because the number of distinct labels cannot exceed the number of input occurrences. The `max` here only chooses capacity; it is not doing the counting task. Duplicate labels will make the actual load lower.

For every word, try to read its count. A missing key raises `KeyError`, so start that count at zero. Write the incremented count with put. An update must replace the old count rather than add a second pair. Preserve exact spelling and case; `"tin"` and `"Tin"` are different keys, and the empty string is also a valid label.

For a separate example, labels `"felt"`, `"cord"`, `"felt"` leave felt with count two and cord with count one. Return the table itself, not a sorted list or a built-in dictionary. A caller can use get, entries, and load_factor to inspect the result. The input list stays unchanged, and a later call must not inherit earlier counts.

With n words of bounded length and suitable distribution, this is expected O(n) time. More precisely, include the total characters hashed and compared. Our deterministic teaching hash can still suffer collisions; repeated long bucket scans can make worst-case work quadratic in n. Space is O(n) buckets and at most O(n) stored pairs. The constructor's allocation is included in those costs.

## Build it in small steps

Handle one word in `increment_count` first. The index-building function then supplies a fresh table and the loop over words.

## Your Tasks

1. Complete `increment_count` to create a count of one or increase an existing count.
2. Complete `frequency_index` to create the sized table and apply that helper to each word.

Edit `main.py` one step at a time. Run uses the supplied probe; an unfinished field or return value may print a reminder. Submit checks the numbered steps in order, so you can see each completed step before finishing the next.
