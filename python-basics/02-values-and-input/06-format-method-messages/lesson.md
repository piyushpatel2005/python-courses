---
title: "Fill a Message with .format()"
slug: format-method-messages
order: 6
language: python
lesson_type: coding
summary: "Insert values into a string with positional and named .format() placeholders."
seo_title: "Format Strings with .format() | Python Basics"
seo_description: "Learn positional and named placeholders for Python string formatting."
seo_keywords: [python basics, string format method, format placeholders, print strings]
---

A message can also mark places for values with braces `{}`. The string's `.format()` method fills those places when the code runs. This avoids joining many pieces with `+` and works with numbers without calling `str()` yourself.

## Positional and named places

With empty braces, values go into the message from left to right. Named braces show which value belongs where:

```python run
place = "Depot"
maps = 2
print("{} holds {} maps".format(place, maps))
print("{place} holds {count} maps".format(place=place, count=maps))
```

Both lines say `Depot holds 2 maps`. In the second line, `{count}` matches the `count=` argument. The variable passed on its right is `maps`. You can also write `{0}` and `{1}` to refer to arguments by position, but use names when they make a longer message easier to follow.

## Your Tasks

In `main.py`, replace `"TODO"` with a string followed by `.format(...)`. Use named places `{beacon}` and `{count}` and pass the supplied variables as their values.

1. Set `beacon_line` so it prints `Beacon Ridge holds 4 lanterns`.

Press **Run** to see the result, then **Submit**. The next lesson shows a shorter way to put variables into a string.
