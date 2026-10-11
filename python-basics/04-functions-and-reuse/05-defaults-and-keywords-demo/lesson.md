---
title: "Default Ability Marks: Demo"
slug: defaults-and-keywords-demo
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: Use a default ability mark and override it with a keyword argument.
seo_title: "Default Ability Marks: Demo | Python Basics"
seo_description: Use a default ability mark and override it with a keyword argument.
seo_keywords: [python basics, functions and reuse, lantern atlas]
hints:
  - Change the quoted suffix in the function definition, not the call.
---

# Default Ability Marks: Demo

Most ability labels use the same ending, so you shouldn't need to supply it every time.

In `def ability_mark(name, suffix="."):`, the `suffix` parameter has a **default value**. Calling `ability_mark("Glow")` uses that period. Calling `ability_mark("Glow", suffix="!")` supplies a different ending by name; `suffix="!"` is a **keyword argument**.

Run the starter and compare its two lines: `Glow.` and `Glow!`.

## Your Tasks

1. Change the default value of `suffix` from `"."` to `"?"` in the function definition.

Keep both calls unchanged. Run `main.py` again: the first line should become `Glow?`, while the second stays `Glow!`. The explicit argument wins over the default. Submit to check your change.
