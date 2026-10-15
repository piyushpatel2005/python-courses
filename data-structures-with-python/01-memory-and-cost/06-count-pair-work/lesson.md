---
title: "Count pair work"
slug: count-pair-work
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `pair_matches(values)` using nested index loops; return ordered equal-value index pairs and the count of all comparisons."
seo_title: "Count pair work | Python data structures"
seo_description: "Practice count pair work through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - count pair work
  - data structures practice
---

# Count pair work

A small roster contains repeated ticket codes. To identify matching positions without a lookup table, compare each position with every position after it. This is slower than a single scan, but its mechanics make nested-loop cost visible.

## Visit each unordered pair once

The outer loop chooses a left index i. The inner loop begins at i + 1 and stops before the list length. Starting after i avoids comparing an item with itself and avoids repeating a pair in reverse. Count every comparison, even when the values are different. Append `(i, j)` only when the two values compare equal.

For four positions, the pairs are `(0, 1)`, `(0, 2)`, `(0, 3)`, `(1, 2)`, `(1, 3)`, and `(2, 3)`. The inner loop has three iterations, then two, then one, then none. Its changing length is why "two loops" does not by itself tell you the exact count.

```python
labels = ["pine", "oak", "pine"]
print(labels[0] == labels[1])  # False
print(labels[0] == labels[2])  # True
```

## Count misses too

Return `(matches, comparisons)`. Keep matches in the order produced by increasing i and then increasing j. For an empty list or a singleton, there are no pairs, so both the output list and count are empty or zero. Three equal values produce three distinct index pairs, not one unique value.

The comparison count is n(n - 1)/2, which grows quadratically: O(n²). You should discover that count by doing and counting the comparisons, not return the formula without performing the requested scan. Assume each equality comparison is bounded cost; comparing large nested objects may itself take more work. The counters use O(1) auxiliary space. The result can contain O(n²) pairs, so total additional storage including the output can also be quadratic. Do not use a dictionary or set to replace this deliberately pair-by-pair algorithm.

## Build in small steps

The two index loops and equality branch are supplied. Complete the match-recording branch first. Add the counter update outside that branch so misses count too.

## Your Tasks

1. Append `(i, j)` when the supplied equality check succeeds.
2. Count every comparison, including nonmatching pairs.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
