---
title: Number Beacon Markers with for and range
slug: number-supply-kits
order: 4
language: python
lesson_type: coding
summary: Use for and range to label four markers on Ari’s beacon trail.
seo_title: Python for Loop and range Exercise | Python Basics
seo_description: Practice Python for loops and range with numbered beacon markers.
seo_keywords: [python for loop, python range, loop labels]
hints:
  - range(1, 5) gives 1, 2, 3, 4; the stop value is excluded.
---

# Number beacon markers

Ari lays numbered markers along the route. When the number of repetitions is known, `for` can walk through a `range`. For example, a separate cave has three crystals:

```python
for crystal in range(1, 4):
    print("Crystal", crystal)
# Crystal 1, Crystal 2, Crystal 3
```

`range(start, stop)` includes the start but **not** the stop. `range(3)` starts at zero. `main.py` provides an empty string and prints it afterward. Build four labels without typing every number separately.

## Your Task

1. Write a `for marker_number in range(1, 5)` loop that appends `f"Marker {marker_number}; "` to `markers` on each turn. Run to see all four, then Submit.
