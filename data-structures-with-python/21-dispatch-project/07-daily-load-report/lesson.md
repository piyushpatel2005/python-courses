---
title: "Report completed loads over a day range"
slug: daily-load-report
order: 7
language: python
runtime: pyodide
lesson_type: coding
summary: "Query completed workloads over validated half-open day ranges with a Fenwick index."
seo_title: "Report completed loads over a day range in Python"
seo_description: "Query completed workloads over validated half-open day ranges with a Fenwick index."
seo_keywords:
  - Python
  - daily-load-report
hints:
  - "Validate before querying, and pass the half-open bounds to range_sum unchanged."
---

Dispatch and undo already update the load index. Expose a report for a slice of the reporting window without scanning every completed job again.

The supplied `load_report(start, stop)` connects validation to the Fenwick adapter's `range_sum`. Bounds follow Python's half-open convention: include day start, exclude day stop. For a five-day window, `[1, 4)` includes days 1, 2, and 3. Equal bounds describe an empty range and return zero. The endpoint stop may equal `self.days`.

Validate before querying. Both bounds must be exact integers, excluding booleans, and satisfy `0 <= start <= stop <= self.days`; otherwise raise `ValueError`. Negative indexing is not supported here. Passing an unchecked negative bound into a lowbit loop would be unsafe, so validation belongs at the public boundary.

A load is recorded on the job's declared day, not on the position where it appears in history. Several completed jobs on the same day add together. Pending jobs contribute nothing. Undo subtracts exactly the units that dispatch previously added. For example, completed loads `[2, 0, 6, 1]` have a total of 6 over `[1, 3)`, regardless of dispatch order.

`LoadIndex.range_sum` subtracts two prefix totals. Its prefix loop walks downward through Fenwick blocks with `stop -= stop & -stop`. The update loop walks upward through affected blocks after converting day to day + 1. Those supplied methods are retained from stage one, so this stage asks you to connect a validated reporting API rather than rebuild the tree.

Each query takes O(log days) time and O(1) auxiliary space. The index itself takes O(days) space. Computing `sum` over a sliced load list or replaying history would miss the point of the index; the task specifically requires delegating to `range_sum`. The checkpoint reports a dispatched job's load and then shows the corrected total after undo.

## Supplied setup and small steps

The supplied public report method validates before querying. The first task checks the boundary without touching the index. The second delegates a valid range unchanged, so an inclusive-stop adjustment cannot slip into the report.

## Your Tasks

1. Complete `check_load_bounds(start, stop)` to accept only exact-integer half-open bounds within the reporting window.
2. Complete `read_load_range(start, stop)` to return the supplied index's `range_sum(start, stop)` result.

Edit `main.py`. Run shows the workload before and after undo removes its contribution. Submit checks the same operation on additional small cases.
