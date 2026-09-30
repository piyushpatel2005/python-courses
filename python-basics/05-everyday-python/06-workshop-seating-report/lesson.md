---
title: Workshop Seating Report
slug: workshop-seating-report
order: 6
language: python
lesson_type: coding
runtime: pyodide
summary: Combine loops, functions, conditions, and formatted text in a workshop seating report.
seo_title: "Python Beginner Mini Project: Workshop Seating | Python Basics"
seo_description: Build a small Python workshop seating report using lists, loops, functions, conditionals, and an f-string.
seo_keywords: [python mini project, beginner python exercise, loops, functions, f strings]
hints:
  - Start total at 0 and add each number in seat_counts.
  - If reserved is greater than capacity, return 0 instead of a negative value.
  - Use your first two helpers to assemble the report string.
---

The community workshop needs a one-line seating update. Bring together what you already know: a list of registrations, a loop to count reserved seats, a conditional to avoid negative available seats, and an f-string for the report. No terminal prompts, local files, classes, recursion, or enums are required.

For a different activity, the same pieces could look like this:

```python
def count_tools(tool_boxes):
    total = 0
    for amount in tool_boxes:
        total += amount
    return total

print(count_tools([2, 1]))  # 3
```

The starter supplies function names and sample data. Work from the first helper to the final report. With the supplied sample, Run should end with `Ceramics: 3 reserved, 5 available`.

## Your Tasks

1. Complete `seat_total(seat_counts)` to return the sum of the numbers in the list, using a loop (an empty list totals zero).
2. Complete `remaining_seats(capacity, reserved)` to return `capacity - reserved` when positive, or `0` when the workshop is full or overbooked.
3. Complete `workshop_report(name, capacity, seat_counts)` using your two helpers to return the f-string `"<name>: <reserved> reserved, <available> available"` with the actual values substituted.

Your finished report is ready for the workshop board.
