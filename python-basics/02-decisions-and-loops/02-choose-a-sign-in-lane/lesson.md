---
title: Choose a Sign-in Lane
slug: choose-a-sign-in-lane
order: 2
language: python
lesson_type: coding
summary: Use if, elif, and else to choose one sign-in message from the available seats.
seo_title: Python if, elif, else Exercise | Python Basics
seo_description: Practice Python conditional branches and indentation by choosing a workshop sign-in message from a seat count.
seo_keywords: [python if else, python elif, python conditions]
hints:
  - Start with the most restrictive case, seats_left == 0, then test for a small number of remaining seats.
---

# Choose a sign-in lane

The sign-in desk needs one message about remaining seats. In a different situation, a volunteer might sort donation boxes like this:

```python
boxes = 2
if boxes == 0:
    message = "No boxes"
elif boxes < 3:
    message = "Ask for more boxes"
else:
    message = "Boxes ready"
print(message)  # Ask for more boxes
```

Python checks conditions from top to bottom and runs **only the first matching branch**. The colon begins a block; indent its body by four spaces. `else` covers everything left. In the editor, `seats_left` is supplied and the last line prints your result.

## Your Task

1. Replace the placeholder `lane` with an `if` / `elif` / `else` chain: set it to `"Waitlist"` when `seats_left == 0`, `"Last seats"` when `seats_left < 4`, and `"Open"` otherwise. Run the code to see the message for 2 seats.
