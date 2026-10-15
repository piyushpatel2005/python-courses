---
title: "Answer half-open range-sum queries"
slug: range-sum-queries
order: 8
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `PrefixSums.range_sum(start, stop)` with boundary validation and two prefix reads, returning the total for `[start, stop)`."
seo_title: "Answer half-open range-sum queries | Python data structures"
seo_description: "Practice range sum queries through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - range sum queries
  - data structures practice
---

# Answer half-open range-sum queries

The prefix table already stores every total from the beginning of the data. To total a smaller region, remove the part before that region. Add one query method to the `PrefixSums` class without rebuilding or rescanning its data.

## Subtract boundary totals

The completed constructor is supplied unchanged. `prefix[stop]` includes every value before stop. `prefix[start]` includes the unwanted values before start. Subtracting the second from the first leaves exactly the half-open interval `[start, stop)`: start is included and stop is excluded.

Suppose the original readings are `[7, -4, 2, 9]`. The boundary sums are `[0, 7, 3, 5, 14]`. The interval from boundary one to boundary three contains -4 and 2. Its total is the sum before boundary three minus the sum before boundary one. The leading zero lets the same rule handle a range starting at the beginning.

```python
boundary_totals = [0, 6, 8, 13]
print(boundary_totals[3] - boundary_totals[1])  # 7
print(boundary_totals[2] - boundary_totals[2])  # 0
```

The second subtraction represents an empty range. No special scan or replacement value is needed because subtracting a boundary from itself gives zero.

![Values \[3, 8, 2, 6\] have prefix sums \[0, 3, 11, 13, 19\]. Range \[1, 3) includes values 8 and 2. Subtract prefix\[1\] from prefix\[3\] to get 10.](prefix-sum-half-open-range.svg)

The two selected boundaries enclose values 8 and 2, while subtracting removes everything before the left boundary.

## Validate both boundaries together

Accept integer bounds satisfying `0 <= start <= stop <= n`, where n is one less than the prefix-table length. Empty ranges are valid, including `[n, n)`. Negative bounds, reversed bounds, and stops beyond n raise `ValueError`. Check before accessing storage so Python's negative indexing cannot quietly give a plausible but wrong total.

Each valid query reads two prefix values and subtracts them, taking O(1) time and O(1) auxiliary space under the bounded-integer model. Construction remains O(n) time and storage. The table describes the data at construction time; the class has no update operation. Changing an original reading would require rebuilding affected static prefixes, O(n) in the worst case.

Do not call `sum`, slice the prefix list, or retain the original values for rescanning. The useful payoff of the previous stage is answering many varied intervals from the same unchanged table. Querying must not mutate that table or affect later answers.

## Build in small steps

The constructor is preserved and size is derived for you. First enforce the boundary contract. Then replace the placeholder result with the subtraction; no loop or new storage is needed.

## Your Tasks

1. Raise `ValueError` unless `0 <= start <= stop <= size`.
2. Return the difference between the stop and start prefix totals.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
