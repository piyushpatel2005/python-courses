---
title: "Default Endings and Keyword Arguments: Demo"
slug: defaults-and-keywords-demo
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: Change a default message ending while retaining an explicit override.
seo_title: "Default Endings and Keyword Arguments: Demo | Python Basics"
seo_description: Change a default message ending while retaining an explicit override.
seo_keywords: [python basics, functions and reuse, default parameters, keyword arguments, functions]
hints:
  - Change the quoted suffix in the function definition, not the calls.
---

# Default endings and keyword arguments

A short pickup message usually ends with a period, but sometimes you want an exclamation mark. Put the usual ending in the function definition so callers can omit it.

In `def message(text, suffix="."):`, `suffix` has a **default value**. Calling `message("Pickup at noon")` uses the period. Calling `message("Pickup at noon", suffix="!")` supplies a **keyword argument**, naming the parameter to override.

Run the starter to compare `Pickup at noon.` with `Pickup at noon!`.

## Your Tasks

1. Change the default `suffix` from `"."` to `"?"` in the function definition.

Keep both calls unchanged. Run again: the first line becomes `Pickup at noon?`, a question about the time; the explicit exclamation mark on the second line still wins. Submit to check your change.
