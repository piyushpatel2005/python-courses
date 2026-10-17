---
title: "Print with Percent Placeholders"
slug: printf-style-messages
order: 5
language: python
lesson_type: coding
summary: "Use percent-style placeholders to insert text and an integer into a message."
seo_title: "Percent-Style String Formatting | Python Basics"
seo_description: "Use Python's older printf-style %s and %d placeholders to print a message from variables."
seo_keywords: [python basics, percent formatting, printf style, print strings]
---

The next Gear Forge message includes both a name and a number. Joining with `+` would require `str(number)`. An older C style printf statement can put values into marked places in a string instead.

## Percent-style formatting

`%s` marks a place for text and `%d` marks a place for an integer. After the string, `%` supplies the values in the same order. With two values, put them in a tuple inside parentheses:

```python run
tool = "Rope"
length = 12
print("%s is %d meters long" % (tool, length))
```

This prints `Rope is 12 meters long`. The `%` here formats a string; earlier you used `%` between numbers to get a remainder. You may encounter percent-style formatting in older Python code. From Python 3.6 on, most developers use more friendly f-string for printing messages because it's lot easier to read and write.

## Your Tasks

In `main.py`, replace `"TODO"` with a percent-formatted string. Keep the supplied variables and print call. Use `%s` for the name, `%d` for the whole-number count, and supply the values in that order.

1. Set `pack_line` so it prints `Adam carries 3 lanterns`.

Press **Run** to inspect the message, then **Submit**.
