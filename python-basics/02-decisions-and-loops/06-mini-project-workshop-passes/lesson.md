---
title: Mini-project — Workshop Passes
slug: mini-project-workshop-passes
order: 6
language: python
lesson_type: coding
summary: Combine a for loop, conditions, continue, and break to issue a limited number of workshop passes.
seo_title: Python Decisions and Loops Mini-project | Python Basics
seo_description: Complete a small Python project that skips an unusable ticket, stops at workshop capacity, and reports whether sign-in is full.
seo_keywords: [python loop project, python break continue exercise, workshop sign in]
hints:
  - Skip ticket 3 before issuing a pass. Append to passes, then check capacity to break.
---

# Mini-project: workshop passes

The sign-in desk can issue three passes. Ticket 3 is smudged and cannot be used; the next ticket can still get a pass. Another volunteer already prepared `passes`, `issued`, and a fixed set of ticket numbers in the editor. Unlike the tea-table demo, here you need **both** `continue` and `break`.

A `for` loop considers each ticket in `range(1, 8)`. Check the unusable ticket first; otherwise append its number to `passes` and increase `issued`. When `issued` reaches `capacity`, stop. After the loop, use a conditional to record the desk's final state. The supplied print lines show the result.

## Your Tasks

1. Write the loop to skip ticket 3 with `continue`, issue the other tickets into `passes` as `f"{ticket} "`, count each issue, and `break` when `issued == capacity`. Expect `1 2 4 `.
2. After the loop, use `if` / `else` to set `desk_status` to `"Full"` if `issued == capacity`, or `"Open"` otherwise. Expect `Full`.

The pass desk is ready: you have used comparisons and loops to handle a real limit without an interactive prompt.
