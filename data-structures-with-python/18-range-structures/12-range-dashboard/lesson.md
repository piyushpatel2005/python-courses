---
title: "Report changing ranges"
slug: "range-dashboard"
order: 12
language: "python"
runtime: pyodide
lesson_type: "coding"
summary: "Combine a Fenwick sum and segment minimum behind one consistent half-open reporting interface."
seo_title: "Report changing ranges | Python data structures"
seo_description: "Combine a Fenwick sum and segment minimum behind one consistent half-open reporting interface."
seo_keywords:
  - "Python"
  - "report changing ranges"
  - "fenwick and segment trees"
---

# Report changing ranges

A small readings dashboard needs both the total and the minimum over a selected interval while readings change. The completed Fenwick and minimum segment trees are supplied. This project composes them rather than asking you to reimplement their algorithms.

The supplied dashboard constructor copies the integer values, creates a populated Fenwick tree, and builds a minimum tree. Its supplied `replace` method translates one public assignment into the two different update contracts. It subtracts the old value from the replacement to get a delta for Fenwick, but passes the replacement itself to the minimum tree. Then it updates its private value list.

## One interval, two summaries

Your new `report(left, right)` method returns a dictionary with exactly `sum` and `minimum` keys. Both summaries refer to public `[left,right)`, with `0 <= left <= right <= n`. Delegate to the completed structures rather than slicing the copied list. Their validation rejects invalid intervals and non-integer boundaries before returning a report.

For readings `[9, 4, 7, 2]`, interval `[1,4)` totals 13 and has minimum 2. Replacing position three with 8 changes that interval to total 19 and minimum 4. Passing 8 as a Fenwick delta would wrongly add eight to the old two. The supplied replacement method prevents that mismatch.

An empty interval reports sum zero and minimum infinity. Those are the two structures' identities. Keep both results rather than converting the empty minimum to zero, because zero might be a real reading and would obscure the empty case. An empty dashboard permits only `[0,0)` reports and no replacements.

The hint `dict[str, int | float]` describes string labels with numeric summaries; infinity accounts for the possible float. Return a fresh dictionary every time. Editing a report must not change later reports or another dashboard.

A report uses two logarithmic queries and constant result space. Replacing a reading also takes logarithmic work. Initialization here costs O(n log(n+1)) because the supplied Fenwick builder uses repeated additions, even though segment construction is linear. This completes a mutable range index with explicit, consistent public boundaries.

## Small example

```python
readings = [9, 4, 7, 2]
print(sum(readings[1:4]), min(readings[1:4]))
readings[3] = 8
print(sum(readings[1:4]), min(readings[1:4]))
```

Expected output:

```text
13 2
19 4
```

## Supplied setup

Construction, synchronized replacement, and the two-key dictionary are supplied. Each task fills one independent report entry; the sum check does not read the minimum entry.

## Your Tasks

1. Fill the report's `sum` entry by calling the Fenwick range-sum method.
2. Fill `minimum` by querying the minimum tree over the same half-open interval.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on changed inputs and boundary cases. The probe is supplied. Complete the numbered steps in order; Submit checks each step separately.
