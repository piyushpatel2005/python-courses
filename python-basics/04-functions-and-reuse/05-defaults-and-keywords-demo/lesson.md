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

At the workshop, an ability label gets a default mark when Ari omits that argument. `ability_mark("Glow", suffix="!")` overrides it by name. The first call uses the default; the second uses `!`.

Edit the default in `main.py` from `.` to `?`. Run: the first line becomes `Glow?`, while the keyword call remains `Glow!`. Then Submit.

## Your Tasks

1. Change the default `suffix` to `?`; keep the keyword override call.
