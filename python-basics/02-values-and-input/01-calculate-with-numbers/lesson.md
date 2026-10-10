---
title: "Demo: Divide Beacon Shards"
slug: calculate-with-numbers
order: 1
language: python
lesson_type: coding
summary: "Use floor division and remainder to fill lamps."
seo_title: "Demo: Divide Beacon Shards | Python Basics"
seo_description: "Use floor division and remainder to fill lamps."
seo_keywords: [python basics, values and input, lantern atlas]
---

At the **Gear Forge**, each lamp needs four shards. With 17 shards, you can fill four lamps and have one shard left. The starter calculates both amounts from the same values.

`shards // per_lamp` uses **floor division**. For these positive whole numbers, it counts complete groups of four. `shards % per_lamp` uses the **remainder** operator to find what is left after those groups.

Python also has the arithmetic operators you will use in the next exercise:

| Operator | Use |
| --- | --- |
| `+` | Add |
| `-` | Subtract |
| `*` | Multiply |
| `/` | Divide, producing a float |
| `**` | Raise to a power |

Multiplication happens before addition. Parentheses let you change the order: `(2 + 3) * 4` adds first, while `2 + 3 * 4` multiplies first. Write numbers without quotes when you want arithmetic rather than text.

In **main.py**, leave the calculations and print calls as supplied. Change the shard count, then press **Run**. Look for `Lamps: 5` and `Spare shards: 3`; **Submit** checks the edit.

## Your Tasks

1. Set `shards` to `23`.
