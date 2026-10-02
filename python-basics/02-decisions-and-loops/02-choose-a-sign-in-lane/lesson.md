---
title: Choose a Gate Signal
slug: choose-a-sign-in-lane
order: 2
language: python
lesson_type: coding
summary: Use if, elif, and else to choose a gate signal from its remaining charge.
seo_title: Python if, elif, else Exercise | Python Basics
seo_description: Practice conditional branches while Ari checks a beacon gate.
seo_keywords: [python if else, python elif, python conditions]
hints:
  - Start with the most restrictive case, charge_left == 0, then test for a small positive charge.
---

# Choose a gate signal

Ari needs one message from the beacon gate before crossing. In a different room, a lantern might be checked like this:

```python
wicks = 2
if wicks == 0:
    message = "Dark"
elif wicks < 3:
    message = "Dim"
else:
    message = "Bright"
print(message)  # Dim
```

Python checks conditions from top to bottom and runs **only the first matching branch**. A colon begins a block; indent its body by four spaces. `else` covers everything left. In `main.py`, `charge_left` is supplied and the final line prints your result.

## Your Task

1. Replace the placeholder `gate_signal` with an `if` / `elif` / `else` chain: set it to `"Sealed"` when `charge_left == 0`, `"Flickering"` when `charge_left < 4`, and `"Open"` otherwise. Edit `main.py`, Run to see the signal for 2 units, then Submit.
