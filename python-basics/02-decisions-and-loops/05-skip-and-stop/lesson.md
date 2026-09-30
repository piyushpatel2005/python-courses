---
title: Skip and Stop a Loop
slug: skip-and-stop
order: 5
language: python
lesson_type: interactive
summary: See how continue skips one loop turn while break ends the loop entirely.
seo_title: Python break and continue Examples | Python Basics
seo_description: Run beginner Python loops to observe the difference between skipping a turn with continue and ending a loop with break.
seo_keywords: [python break, python continue, loop control]
---

# Skip and stop a loop

The workshop's tea table has one cup with a cracked handle. `continue` skips the rest of **that turn** and moves to the next number. Run this block and then change `cup == 2` to `cup == 3`.

```python run
for cup in range(1, 5):
    if cup == 2:
        continue
    print("Serve cup", cup)
```

Now the volunteers need only two serving trays. `break` ends the **entire loop**, even though `range` has more numbers waiting. Run it, then try changing the limit to `3`.

```python run
for tray in range(1, 6):
    if tray > 2:
        break
    print("Set out tray", tray)
```

In the mini-project, you will skip a ticket that cannot be used and stop once all places are filled. With a `while` loop, take extra care that a `continue` does not skip its counter update forever.
