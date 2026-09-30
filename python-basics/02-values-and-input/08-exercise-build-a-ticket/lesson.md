---
title: "Exercise: Build a Workshop Ticket"
slug: exercise-build-a-ticket
order: 8
language: python
lesson_type: coding
summary: Build a small ticket from prefilled response text, price calculation, and an f-string.
seo_title: "Exercise: Build a Workshop Ticket | Python Basics"
seo_description: Build a small ticket from prefilled response text, price calculation, and an f-string.
seo_keywords: [python beginner project, input string conversion, f string ticket]
---

Make a ticket for a neighborhood pottery session. A real command-line app might collect a visitor name and ticket count with `input()`, which always returns text. Here `visitor_text` and `tickets_text` are safe prefilled responses so **Run** never waits for a prompt. The starter prints three checkpoints. You can complete one assignment at a time without changing the print calls.

Edit `main.py`, press **Run** after each change, and **Submit** to check each task. The finished ticket should say `Ticket for Maya: 3 seats, $18.00`.

## Your Tasks

1. Set `ticket_count` to the integer converted from `tickets_text`.
2. Set `total_cost` to `ticket_count` multiplied by `unit_cost`.
3. Set `ticket_line` with an f-string using `visitor_text`, `ticket_count`, and `total_cost` formatted to two decimals: `Ticket for Maya: 3 seats, $18.00`.
