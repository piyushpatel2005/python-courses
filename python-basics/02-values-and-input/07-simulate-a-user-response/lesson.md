---
title: "Demo: A Prefilled User Response"
slug: simulate-a-user-response
order: 7
language: python
lesson_type: coding
summary: Handle a browser-safe prefilled response like a Python input string.
seo_title: "Demo: A Prefilled User Response | Python Basics"
seo_description: Handle a browser-safe prefilled response like a Python input string.
seo_keywords: [python input concept, prefilled input string, browser python]
---

In a terminal program, `input("Your name: ")` **pauses** until someone types a response and returns it as a string. This browser editor has no interactive prompt: calling `input()` here could leave Run waiting, so the runnable example uses a prefilled string instead. A real terminal might use `visitor = input("Your name: ")`; here the line `visitor = "Noor"` stands in for that response. Even numeric responses from `input()` are strings and need `int()` or `float()` before arithmetic.

The working program makes a reservation line from a prefilled response. Change **only** `visitor` to `"Ivy"`. Edit `main.py`, press **Run** to see `Seat for Ivy`, then **Submit**. The final exercise will combine a prefilled response with conversion, arithmetic, and formatting.

## Your Task

1. Change the visitor response to the string `"Ivy"`.
