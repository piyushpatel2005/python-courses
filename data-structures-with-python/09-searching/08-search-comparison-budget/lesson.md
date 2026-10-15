---
title: "Count binary-search comparisons"
slug: "search-comparison-budget"
order: 8
language: "python"
runtime: pyodide
lesson_type: "coding"
summary: "Measure actual comparator calls rather than infer work from elapsed time."
seo_title: "Count binary-search comparisons | Data structures with Python"
seo_description: "Measure actual comparator calls rather than infer work from elapsed time."
seo_keywords:
  - Python
  - search comparison budget
  - data structures
---

Two searches can return the same index while doing very different amounts of work. Add a counted binary-search variant so callers can see how much search work happened on a particular input.

This is a fresh instrumented function, not a change to the boundary helpers. It returns `(index, probes)`. Index follows the earlier any-match policy: any equal index is valid, and missing means `-1`. Probes counts calls to the supplied comparison function. Empty input returns `(-1, 0)`.

The supplied `compare_int(left, right)` returns a negative number when left is smaller, zero when equal, and a positive number when larger. It uses two primitive comparisons internally. We count one comparator invocation as one probe, not each primitive comparison. Call the comparator exactly once per visited midpoint and save its result for branch decisions. Do not call it again to decide which half to discard.

For example, searching for twelve in `[2, 7, 12, 16, 21]` visits the middle once and returns `(2, 1)`. A different target may need more probes, so do not return a theoretical logarithm as if it were a measurement. The test callback records actual calls and checks your count against that record.

Maintain the same half-open interval and strict progress rule. The input is already sorted according to the supplied comparator. The standard probe uses integers, but a reversed-order comparator can describe a descending list as well. Callback exceptions propagate; they do not count as successful search results.

For n positive items, midpoint halving uses at most `n.bit_length()` probes; for zero items it uses none. This is a worst-case bound on probes, not a claim that every search reaches it. Auxiliary space is O(1). Timing would mix algorithm work with machine load and interpreter overhead, whereas counting calls exposes the behavior directly.

## Build it in small steps

The relation helper makes the one-call rule testable on its own. The search loop then increments its counter once after each helper call and uses the returned sign for its branch.

## Your Tasks

1. Complete `compare_at` to call the comparator once for the requested item and return its relation.
2. Complete `measured_binary_search` to halve the interval and count the actual calls to that helper.

Edit `main.py` one step at a time. Run uses the supplied probe; an unfinished field or return value may print a reminder. Submit checks the numbered steps in order, so you can see each completed step before finishing the next.
