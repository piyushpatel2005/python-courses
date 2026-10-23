---
title: "Project: Check In Event Attendees"
slug: workshop-sign-in-project
order: 8
language: python
runtime: pyodide
lesson_type: coding
summary: "Combine a loop, skip, stop, and branch for event check-in."
seo_title: "Python Event Check-in Project | Python Basics"
seo_description: "Skip canceled registrations, stop at capacity, and report whether check-in is full."
seo_keywords: [python loops project, continue break, event attendance]
---

An event has registrations numbered 1 through 6. Registration 2 was canceled, and the room has space for two attendees. The numbers are registration IDs, not people's names. Check in valid registrations in order, stop when the room is full, and report its status.

`capacity` is the room's attendance limit. `checked_in` holds a space-separated string of registration IDs, while `attendee_count` counts actual check-ins. Build the loop in `main.py` before the status assignment. Keep the supplied print calls below your decision.

The finished program prints:

```text
Checked in: 1 3
Attendees: 2
Status: Full
```

There is a trailing space after each ID in the string. If you temporarily set `capacity` to `8`, only five valid registrations exist, so the status should be `Spaces left`. Restore `capacity = 2` before finishing.

## Your Tasks

1. Loop over registration IDs 1 through 6. Skip ID 2 with `continue`; append each other ID to `checked_in` and increase `attendee_count`.
2. After counting each check-in, use `break` when `attendee_count == capacity`.
3. After the loop, use `if` / `else` to set `status` to `"Full"` when the count reaches capacity, or `"Spaces left"` otherwise.

Press **Run** after each change and **Submit** to check progress. The next section teaches functions, so you can reuse code instead of repeating it.
