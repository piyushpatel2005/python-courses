---
title: Skip and Stop a Gate Trial
slug: skip-and-stop
order: 5
language: python
lesson_type: interactive
summary: See how continue skips a blocked rune while break ends a gate trial.
seo_title: Python break and continue Examples | Python Basics
seo_description: Run Python loops that skip a blocked rune or stop after enough gate keys.
seo_keywords: [python break, python continue, loop control]
---

# Skip and stop a gate trial

One rune on Ari’s path is cracked. `continue` skips the rest of **that turn** and moves to the next rune. Run this block to see which runes remain.

```python run
for rune in range(1, 5):
    if rune == 2:
        continue
    print("Trace rune", rune)
```

The gate needs only two keys. `break` ends the **entire loop**, even if `range` has more values waiting.

```python run
for key in range(1, 6):
    if key > 2:
        break
    print("Collect key", key)
```

In the next trial you will skip a damaged rune and stop once the gate has enough marks. In a `while` loop, be careful not to skip its counter update with `continue`.
