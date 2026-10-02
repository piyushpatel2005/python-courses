---
title: "Exercise: Check Gate Signal"
slug: exercise-compare-and-branch
order: 2
language: python
runtime: pyodide
lesson_type: coding
summary: "Choose a gate status from its remaining sparks."
seo_title: "Exercise: Check Gate Signal | Python Basics"
seo_description: "Choose a gate status from its remaining sparks."
seo_keywords: [python basics, control flow, lantern atlas]
---

The route demo used a signal reading; this gate uses **sparks left**. Compute a boolean for fewer than three sparks. Choose `Sealed` for zero, `Fading` for a low signal, and `Open` otherwise. Check zero first. Edit **main.py**, press **Run** for `True` and `Fading`, then **Submit**.

## Your Tasks

1. Set `low_signal` using `sparks_left < 3`.
2. Use `if` / `elif` / `else` to set `gate_status` to `Sealed` for zero, `Fading` when `low_signal` is true, or `Open` otherwise.
