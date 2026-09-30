---
title: 'Project: Workshop sign-in'
slug: workshop-sign-in-project
order: 9
language: python
runtime: pyodide
lesson_type: coding
summary: Combine comparisons, branches, loops, skipping, and capacity in a small sign-in
  program.
seo_title: 'Project: Workshop sign-in | Python Basics'
seo_description: Combine comparisons, branches, loops, skipping, and capacity in a
  small sign-in program. Practice Python control flow in an editable browser lesson.
seo_keywords:
- python control flow project
- python loops exercise
- workshop sign in
---

# Project: Workshop sign-in

A community workshop has two seats. Ticket 2 is illegible, so issue passes to other ticket numbers in order until capacity is reached. The starter provides the limit, blank records, and print statements. This combines a comparison with `if`, `for` over `range`, `continue` to skip the unusable ticket, and `break` to end admission. Finish with a status selected by `if` / `else`. No terminal `input()` is needed: the fixed ticket numbers make Run repeatable in the browser.

Edit **main.py**, press **Run** to see `Passes: 1 3 `, `Issued: 2`, and `Status: Full` on separate lines; press **Submit** to check each task.

## Your Tasks

1. Loop over ticket numbers 1 through 6. Skip ticket 2 with `continue`; issue every other number by appending `f"{ticket} "` to `passes` and increasing `issued`. At this stage, the string starts `1 3 ` and has no ticket 2.
2. After counting each admission, use `break` when `issued == capacity`. Now the supplied output shows `Passes: 1 3 ` and `Issued: 2`.
3. After the loop, use `if` / `else` to set `status` to `"Full"` when `issued == capacity`, or `"Open"` otherwise. The supplied output shows `Status: Full`; if capacity is 8, all five valid tickets are issued and status is `Open`.

The sign-in desk is ready: you can now decide, repeat, skip, and stop within one small program.
