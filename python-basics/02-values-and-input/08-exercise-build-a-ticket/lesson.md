---
title: "Project: Build Ari’s Gear HUD"
slug: exercise-build-a-ticket
order: 8
language: python
lesson_type: coding
summary: "Combine response text, conversion, multiplication, and formatting."
seo_title: "Project: Build Ari’s Gear HUD | Python Basics"
seo_description: "Combine response text, conversion, multiplication, and formatting."
seo_keywords: [python basics, values and input, lantern atlas]
---

At the Gear Forge, Ari chooses three flares at six energy each. `player_text` and `flares_text` are browser-safe prefilled responses, not calls to `input()`. The starter prints each checkpoint for one assignment at a time. Edit **main.py**, press **Run** after each change, then **Submit**. The finished line reads `Gear for Ari: 3 flares, 18.00 energy`.

## Your Tasks

1. Convert `flares_text` with `int()` into `flare_count`.
2. Set `energy_cost` to `flare_count` multiplied by `flare_cost`.
3. Set `hud_line` with an f-string using `player_text`, `flare_count`, and `energy_cost` formatted to two decimals: `Gear for Ari: 3 flares, 18.00 energy`.

Ari’s HUD is ready for the Gate Trials.
