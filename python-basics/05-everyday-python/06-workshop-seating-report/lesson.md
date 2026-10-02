---
title: Final Mission — Restore the Beacon
slug: workshop-seating-report
order: 6
language: python
lesson_type: coding
runtime: pyodide
summary: Combine loops, functions, and conditions to report the energy Ari needs to restore a beacon.
seo_title: "Python Beginner Mini Project: Beacon Energy | Python Basics"
seo_description: Build a final Lantern Atlas beacon report with loops, functions, and formatted text.
seo_keywords: [python mini project, beginner python exercise, loops, functions, f strings]
hints:
  - Start total at 0 and add each number in shard_energy.
  - If gathered exceeds target, return 0 instead of a negative value.
  - Use your first two helpers to assemble the report string.
---

# Final mission: restore the beacon

Ari reaches the final beacon. Add the energy from collected shards, calculate how much more energy the beacon can hold, and show a one-line status before unlocking the exit. No terminal prompts, device files, classes, recursion, or enums are required.

For a different part of the map, the same loop pattern can count cave crystals:

```python
def count_crystals(pouches):
    total = 0
    for amount in pouches:
        total += amount
    return total

print(count_crystals([2, 1]))  # 3
```

The starter supplies function names and sample data. Work from the first helper to the final report. With the supplied sample, Run should end with `North Beacon: 3 energy, 5 needed`.

## Your Tasks

1. Complete `energy_total(shard_energy)` to return the sum of the list using a loop (an empty list totals zero).
2. Complete `energy_needed(target, gathered)` to return `target - gathered` when positive, or `0` when the target is reached or exceeded.
3. Complete `beacon_report(name, target, shard_energy)` using your two helpers to return `"<name>: <gathered> energy, <needed> needed"` with actual values. Run and Submit.

The restored beacon lights Ari’s exit route.
