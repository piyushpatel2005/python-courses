---
title: "Measure skip-list work without a stopwatch"
slug: "skip-list-tradeoffs"
order: 14
language: "python"
runtime: pyodide
lesson_type: "coding"
summary: "Implement `search_steps(key)` as a read-only top-down forward-link search returning `(found, moves)`, where moves counts successful rightward pointer moves plus one level-completion step per level, including level zero."
seo_title: "Measure skip-list work without a stopwatch | Python data structures"
seo_description: "Implement `search_steps(key)` as a read-only top-down forward-link search returning `(found, moves)`, where moves counts successful rightward pointer moves plus one level-completion step per level, including level zero."
seo_keywords:
  - "Python"
  - "skip list tradeoffs"
  - "data structures"
---

# Measure skip-list work without a stopwatch

A skip list's speed depends on its tower shape. Measure a precise kind of work instead of timing a tiny example. The new search_steps method performs the same right-then-down search and returns both membership and a movement count. Count one for every successful rightward move and one when finishing each level, including the base level. Do not count failed comparisons or the final equality check in this particular metric.

A flat structure with every node at height one is a sorted linked list with empty upper lanes. Searching near its end must walk through almost every base node. A useful spread of taller nodes can skip many of those positions. The movement count makes that difference visible without relying on machine speed.

In a randomized skip list, independent geometric heights promote progressively fewer nodes. With a level cap L proportional to log n and large enough for the expected tallest towers, search, insertion, and removal take expected O(log n) time. Expected means averaged over the random height choices, not guaranteed for every shape. An unlucky or deliberately flat arrangement can still require linear work. Our supplied heights are deterministic fixtures, so no random-performance promise applies to every fixture.

With n nodes and a maximum of L levels, the search bound is O(n+L). Fixing L forever does not preserve logarithmic scaling for arbitrarily large n. Link storage is the sum of node heights plus the sentinel's L slots: expected O(n) under the usual geometric model with suitable L, but O(nL) in the all-tall worst case.

The completed implementation remains a linked ordered index, not membership in a Python list. This final diagnostic does not change its data or replace its ordinary search method.

## Trace it first

Use five keys 6,12,18,24,30 and three levels. With every height one, searching for 30 makes four right moves and three level-completion steps. If 24 has height three, the same search can jump to 24 on the top level before descending. The final equality test still checks the base successor 30.

## Cost

The diagnostic itself takes O(n+L) worst-case time and O(1) auxiliary space. It avoids the predecessor array because it returns only membership and a count. Counts describe pointer movements, not elapsed time or exact comparison totals.

## Operation contract

Implement `search_steps(key)` as a read-only top-down forward-link search returning `(found, moves)`, where moves counts successful rightward pointer moves plus one level-completion step per level, including level zero.

## Your Tasks

1. Implement `search_steps(key)` to report membership and pointer-movement work.

## Run and check

Edit `SkipList.search_steps` in `main.py`. The earlier definitions and Run probe are supplied. Run the completed operation to see:

```text
Flat: (True, 6)
Towers: (True, 5)
```

Press **Submit** to check the tasks on additional inputs and boundary cases.
