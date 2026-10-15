---
title: "Choose a nested copy boundary"
slug: nested-copy-boundaries
order: 4
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `copy_rows(rows)` with a fresh outer list and a separate shallow copy for each row occurrence."
seo_title: "Choose a nested copy boundary | Python data structures"
seo_description: "Practice nested copy boundaries through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - nested copy boundaries
  - data structures practice
---

# Choose a nested copy boundary

A seating editor has a list of rows, and each row is a list of seat labels. The editor must be able to change row membership without changing the original seating plan. Copying only the outer list leaves the rows shared, so this time copy one more level.

## A two-level contract

The input is a list of row lists. Build a fresh outer list, then build a fresh list for every row occurrence. Copy the references stored in each row, rather than recursively copying the cells. If a cell itself is mutable, it will still be shared. This is a chosen boundary, not a general deep-copy routine.

```python
badge = {"name": "Robin"}
row = [badge]
row_copy = list(row)
row_copy.append({"name": "Ari"})
print(len(row))                  # 1
print(row_copy[0] is badge)      # True
```

The example copies one row. Your function must repeat that operation for every row, including empty ones. Accumulate the copies in order. Do not use `[same_row] * count` to construct independent rows: multiplication repeats references and would make several positions share one new row.

![Two distinct outer lists point to the same inner list \[17, 23\]. Copying each inner list creates independent inner lists; changing the copied inner list does not alter the original.](shallow-copy-nested-lists.svg)

The lower panel copies the inner list too, so replacing a cell in the copied row leaves the original row unchanged.

## Repeated input rows

If the same row object appears twice in the source, create two separate row copies. This policy lets an editor change one occurrence without affecting the other. Preserve the cell references inside both copies. A loop that appends the original row would only reproduce the shallow-copy behavior from the preceding lesson.

Let r be the number of rows and c the total number of cell positions across all rows. Creating r row lists and copying c references takes O(r + c) time and O(r + c) new storage. Including r matters: a hundred empty rows still require a hundred separate row containers. No shape is assumed; rows may have different lengths. The original list and every original row must remain unchanged after a caller edits the returned rows.

## Build in small steps

The starter supplies the fresh outer list, row loop, and return. Your change is the row-copy operation inside the loop. A comprehension is also valid.

## Your Tasks

1. Append a shallow copy of each row to the supplied result list.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
