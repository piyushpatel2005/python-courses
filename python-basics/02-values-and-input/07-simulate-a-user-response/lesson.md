---
title: "Demo: Read a Pathfinder Name"
slug: simulate-a-user-response
order: 7
language: python
lesson_type: coding
summary: "Use a browser-safe prefilled response as a name."
seo_title: "Demo: Read a Pathfinder Name | Python Basics"
seo_description: "Use a browser-safe prefilled response as a name."
seo_keywords: [python basics, values and input, lantern atlas]
---

A program running in a terminal can ask for a name with `input("Name: ")`. It pauses while the person types, then returns their response as a string.

These browser exercises use prefilled values instead of waiting at a prompt. In **main.py**, `pathfinder = "Nia"` stands in for a typed response. Change that value directly; do not add an `input()` call here.

This distinction matters for numbers too. A terminal user who types digits still gives `input()` a string. You would convert that text with `int()` or `float()` before doing arithmetic, just as you did in the previous exercise.

Keep the supplied f-string and change the name. Press **Run** to see `Gear ready for Adam`, then **Submit**.

## Your Tasks

1. Set `pathfinder` to `"Adam"`.
