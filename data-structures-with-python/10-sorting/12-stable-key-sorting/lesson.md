---
title: "Stable key sorting"
slug: "stable-key-sorting"
order: 12
language: "python"
runtime: "pyodide"
lesson_type: "coding"
summary: "In `insert_record`, fill the returned gap with the saved original record."
seo_title: "Stable key sorting | Data structures with Python"
seo_description: "A repair desk wants jobs ordered by urgency while keeping arrival order among equally urgent jobs. Numeric sorting alone cannot reveal whether ties were preserved. Build a stable insertion-sort variation that compares a chosen key but returns the original records."
seo_keywords:
  - Python
  - "Stable key sorting"
---

A repair desk wants jobs ordered by urgency while keeping arrival order among equally urgent jobs. Numeric sorting alone cannot reveal whether ties were preserved. Build a stable insertion-sort variation that compares a chosen key but returns the original records.

## Work through the idea

Suppose three records arrive as `(2, "oak")`, `(1, "pine")`, and `(2, "elm")`. Sorting by the first field puts pine first, but oak must remain before elm. The names are payload, not tie-breakers. Comparing whole tuples would silently use the names when priorities match.

Begin with a shallow copy of the input so shifts do not reorder the caller's list. For each next record, save both the record and its key. Shift preceding records only while their keys are strictly larger. Put the saved record into the gap after all equal-key predecessors. This reuses insertion sort's reasoning while changing what each comparison means.

The `key` argument is a callable: `key(record)` extracts the comparable value. A small lambda such as `lambda row: row[0]` is just a function selecting one field. This exercise recomputes predecessor keys during shifting for simplicity, so assume the callable is deterministic, side-effect-free, and inexpensive. It must not mutate the records.

## Build it in checkpoints

The outer copy-and-loop controller is supplied. In `shift_records`, move strictly larger-key predecessors right and return the gap index. In `insert_record`, the supplied lines save the original record and call that helper. Your second change fills the gap. Keys belong only in comparisons; the result must still contain the original record objects.

## Contract and cost

Return a new stable ascending list without changing the input sequence or the contained records. Keep object identity: this is a shallow copy, not a deep copy. Empty input returns a new empty list. Use insertion shifts and key comparisons, not `sorted`, `sort`, or whole-record comparisons. This is an explicitly fresh variation rather than a change to the earlier in-place numeric helper.

Worst-case time is O(n²) key comparisons and calls, assuming O(1) key extraction. The copied result uses O(n) space; shifting uses O(1) additional state. Stability is an ordering guarantee, not a claim that records were cloned.

## Your Tasks

1. In `shift_records`, shift records with larger keys and return the gap position.
2. In `insert_record`, fill the returned gap with the saved original record.

Edit `main.py`, then press **Run** to inspect the supplied probe and **Submit** to check each task. Complete the numbered changes in order. The supplied code keeps earlier operations available; you do not need to copy anything from another lesson.
