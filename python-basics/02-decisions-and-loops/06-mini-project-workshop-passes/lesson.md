---
title: Mini-project — Unlock the Gate
slug: mini-project-workshop-passes
order: 6
language: python
lesson_type: coding
summary: Combine conditions, continue, and break to collect the marks that unlock Ari’s gate.
seo_title: Python Decisions and Loops Mini-project | Python Basics
seo_description: Build a Python gate trial that skips a damaged rune and stops at the required marks.
seo_keywords: [python loop project, python break continue exercise, beacon gate]
hints:
  - Skip rune 3 before collecting a mark. Append to marks, then check required to break.
---

# Mini-project: unlock the gate

Ari needs three rune marks to unlock the next beacon path. Rune 3 is damaged, but later runes still work. `main.py` supplies `required`, `marks`, and `collected`. This trial uses both `continue` and `break`.

A `for` loop considers each rune in `range(1, 8)`. Skip the damaged rune first; otherwise append its number to `marks` and increase `collected`. When `collected` reaches `required`, stop. Then use a conditional to record the gate’s state. The supplied print lines show both results.

## Your Tasks

1. Write the loop to skip rune 3 with `continue`, append the other runes to `marks` as `f"{rune} "`, count each mark, and `break` when `collected == required`. Expect `1 2 4 `.
2. After the loop, use `if` / `else` to set `gate_status` to `"Unlocked"` if `collected == required`, or `"Sealed"` otherwise. Expect `Unlocked`.

Run the trial, then Submit. Ari can now reach the next beacon.
