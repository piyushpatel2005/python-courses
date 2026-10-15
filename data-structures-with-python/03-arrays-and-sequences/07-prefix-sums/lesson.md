---
title: "Build prefix sums with a leading zero"
slug: prefix-sums
order: 7
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `PrefixSums.__init__(values)` with a running-total loop and a fresh `prefix` list beginning with zero."
seo_title: "Build prefix sums with a leading zero | Python data structures"
seo_description: "Practice prefix sums through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - prefix sums
  - data structures practice
---

# Build prefix sums with a leading zero

A report may ask many totals for different regions of the same fixed readings. Precompute the sum before every boundary once. A later query can subtract two boundary totals instead of rescanning the region.

## Store sums at boundaries

This starts a new two-stage class, `PrefixSums`, separate from the earlier mutable `Array`. The constructor accepts a list of integers and builds `self.prefix`. Position k stores the total of the first k input values. Therefore prefix position zero contains zero, and n readings produce n + 1 prefix entries.

Start with the leading zero and a running total of zero. Visit each input value in order, add it to the running total, and append the updated total. The invariant after k iterations is that the prefix list contains every boundary sum from zero through k. Do not forget the initial boundary or confuse an element's index with the boundary after it.

```python
readings = [3, -1, 6]
first_two = readings[0] + readings[1]
first_three = first_two + readings[2]
print(first_two, first_three)  # 2 8
```

Negative values can make later prefix totals smaller than earlier ones. That is valid: prefix sums are cumulative totals, not a sorted list. Repeated values and zeros also preserve the same boundary meaning. Empty input produces `[0]`, which still describes the boundary before any elements.

![Building prefix sums for \[4,1,7,2\] gives \[0,4,5,12,14\]. Query \[1,4) subtracts prefix\[1\] from prefix\[4\] to obtain 10; an empty range subtracts the same boundary from itself.](arrays-and-sequences-prefix-sums-trace.svg)

The leading zero gives every boundary a sum; the query pictured below previews the subtraction you will implement in the next lesson.

## A snapshot of fixed data

Build a new list for every instance and do not retain an alias to the caller's mutable input. Later changes to that input must not silently change the already computed prefixes. Conversely, inspecting or changing one instance's prefix storage must not affect another instance. The integer values used here do not need nested copying.

Construction takes O(n) time and O(n) stored space under the bounded-integer model. A running sum avoids repeatedly summing larger slices, which would do quadratic work. Use an explicit loop rather than `accumulate` or repeated `sum` calls. This stage asks only for construction; the next stage preserves your completed constructor and adds constant-time range queries. Static prefix data is useful when queries greatly outnumber updates. If original readings change, rebuilding these prefixes costs O(n).

## Build in small steps

The running-total variable and traversal loop are supplied. Establish the empty-prefix boundary first. Each later loop iteration extends that same prefix table by one boundary.

## Your Tasks

1. Initialize `prefix` as a fresh list containing zero.
2. Add each value to the running total and append the new boundary sum.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
