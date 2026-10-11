---
title: "Exercise: Recharge the Beacon"
slug: exercise-while
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: "Use a bounded while loop to raise beacon charge."
seo_title: "Exercise: Recharge the Beacon | Python Basics"
seo_description: "Use a bounded while loop to raise beacon charge."
seo_keywords: [python basics, control flow, lantern atlas]
---

This time, count up instead of down. The beacon starts with a charge of 10 and gains 10 per pulse until it reaches 40.

The starter supplies `beacon_charge` and a `steps` counter. Each repetition needs to update both: one records the charge, and the other counts how many pulses you used. You can use `+=` to add to an existing value, just as the demo used `-=` to subtract.

Use `while beacon_charge < 40` to check before each pulse. At 40 the loop should stop. If the starting charge already met the target, the body would not run at all.

Add the loop above the supplied print calls in **main.py**. Keep those calls outside the loop. Press **Run** to see the final charge `40` and step count `3` on separate lines, then **Submit**.

## Your Tasks

1. Add a `while` loop that raises `beacon_charge` by 10 and `steps` by 1 until the charge reaches 40.
