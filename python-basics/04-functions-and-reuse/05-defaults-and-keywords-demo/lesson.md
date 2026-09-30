---
title: "Defaults and Keywords: Demo"
slug: defaults-and-keywords-demo
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: Set a default parameter and override it with a keyword argument.
seo_title: "Defaults and Keywords: Demo | Python Basics"
seo_description: Set a default parameter and override it with a keyword argument.
seo_keywords: [python basics, defaults and keywords demo, python practice]
hints:
  - Change the quoted suffix in the function definition, not the call.
---

# Defaults and Keywords: Demo

A default supplies a value when an argument is omitted. Keywords identify which parameter receives a value, so `badge("Jo", suffix="!")` is clear at the call site. The first call omits `suffix`; the second explicitly overrides it. Change the default in the definition from `.` to `?`, then Run: the first printed line changes, while the keyword-override line stays `Jo!`.

## Your Tasks

1. Change the default `suffix` to `?`; keep the explicit keyword-override call.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.
