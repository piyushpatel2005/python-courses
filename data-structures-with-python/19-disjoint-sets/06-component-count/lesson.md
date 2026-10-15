---
title: "Count remaining components"
slug: component-count
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: "Count self-linked roots to measure the remaining disconnected components."
seo_title: "Count remaining components in Python"
seo_description: "Count self-linked roots to measure the remaining disconnected components."
seo_keywords:
  - Python
  - component-count
hints:
  - "Build one self-link flag per item, then count the true flags."
---

The repair team needs the number of groups that remain disconnected. In a parent forest, every component has exactly one self-linked root. Counting those roots answers the question without choosing a preferred representative.

The supplied `component_count()` connects the two helpers below. Scan the parent list with indices and count entries where the stored parent equals its index. Do not count distinct immediate parent values. For example, the chain `4 → 2 → 0 → 0` contains several parent values but only one component.

This lesson deliberately derives the count from current state. Another design stores a counter initialized to n and decrements it on each successful union. That makes count queries O(1), but every merge path must update the counter correctly. Our class keeps two union methods for comparison; deriving the answer avoids adding bookkeeping to both. Do not add a cached counter in this exercise.

The scan takes O(n) time. This staged version stores O(n) root flags before counting them. Compression and balancing make root queries cheap, but they do not turn this full scan into O(α(n)). A structure with no sites has zero roots. A singleton has one, and an unsuccessful union leaves the count unchanged.

The checkpoint counts before and after joining two sites. During your own trace, try joining the same pair twice: only the first call changes the partition. Compression can change parent links without changing the count at all. This distinction will matter when we use union's boolean result to detect redundant edges.

## Build it in small steps

The supplied `component_count` first builds root flags, then counts them. These two short helpers let you check the self-link rule separately from the total. This staged version uses O(n) temporary space for the boolean list.

## Your Tasks

1. Complete `root_flags()` to return one boolean per parent entry, true only for self-links.
2. Complete `count_root_flags(flags)` to return how many flags are true.

Edit `main.py`. Run should show one fewer component after the successful merge. Submit checks the same operation on additional small cases.
