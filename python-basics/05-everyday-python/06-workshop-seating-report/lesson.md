---
title: Final Mission — Restore the Beacon
slug: workshop-seating-report
order: 6
language: python
lesson_type: coding
runtime: pyodide
summary: Combine loops, functions, and conditions to report the energy Adam needs to restore a beacon.
seo_title: "Python Beginner Mini Project: Beacon Energy | Python Basics"
seo_description: Build a final Lantern Atlas beacon report with loops, functions, and formatted text.
seo_keywords: [python mini project, beginner python exercise, loops, functions, f strings]
hints:
  - Start total at 0 and add each number in shard_energy.
  - If gathered exceeds target, return 0 instead of a negative value.
  - Use your first two helpers to assemble the report string.
---

# Final mission: restore the beacon

Adam reaches the final beacon with a handful of energy shards. Your report will tell the player how much energy they've gathered and how much more they need to restore it.

Start with the total. In another part of the map, this function counts crystals across several pouches:

```python
def count_crystals(pouches):
    total = 0
    for amount in pouches:
        total += amount
    return total

print(count_crystals([2, 1]))  # 3
```

The total starts at zero. Each pass through the loop adds one pouch's crystals. If the list is empty, the loop does nothing and the total stays zero. Use that same pattern for shard energy.

The second helper works out the shortfall. Once the beacon has enough energy, it needs zero more, even if Adam gathered extra. The report function then calls both helpers and puts their results into one string.

Edit the supplied functions in `main.py`; the sample data and print calls are already there. Work on one helper at a time and use Submit to check it. Run will still end with `None` until you complete the report function. The finished sample should end with `North Beacon: 3 energy, 5 needed`.

## Your Tasks

1. Complete `energy_total(shard_energy)` to add the list's values with a loop and return the total. An empty list returns `0`.
2. Complete `energy_needed(target, gathered)` to return the shortfall, `target - gathered`, but never less than `0`.
3. Complete `beacon_report(name, target, shard_energy)` to return `"<name>: <gathered> energy, <needed> needed"`, using your two helpers for the values.

The report gives Adam the next goal: collect the missing energy before leaving through the beacon's exit route.
