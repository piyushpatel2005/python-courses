---
title: Print a current statement
slug: statement-report
order: 10
language: python
lesson_type: coding
summary: Finish the bank simulation with a statement that reads the accounts as they are now,
  after deposits, withdrawals, and interest credits.
seo_title: Print a current statement | Object-oriented Python
seo_description: Finish the bank simulation with a statement that reads the accounts as they are
  now, after deposits, withdrawals, and interest credits.
seo_keywords:
  - Python
  - Banking project
  - statement report
hints:
  - Iterate over sorted(self.accounts), look up each object, and collect its line.
---

Finish the bank simulation with a statement that reads the accounts as they are now, after deposits, withdrawals, and interest credits.

`statement()` returns one line per registered ID in Python’s ascending string sort order, not insertion order. Each line has the exact form `ID | owner | balance cents`, with one space on either side of each `|`. Keep the balance as an integer, including a leading minus sign for an overdrawn current account. Use the literal label `cents`, even for 1. Join lines with a newline and do not add a trailing newline. An empty registry returns `"No accounts registered."`.

Read the shared `owner` and `balance_cents` interface; the report does not need separate branches for each account type. It must not change balances or registration order. The supplied final probe performs a short session with all three specialized accounts before printing the statement.

The starter includes the completed previous stage. Only the new TODO body is unfinished; the earlier code and Console checks stay in place.

## Your Tasks

1. Implement `AccountRegistry.statement()` to return the sorted current-balance report with the exact format and empty-registry message described above.

## Run and check

Edit `main.py`, press **Run**, then **Submit**. The supplied probe also prints earlier checkpoints; its new output should be:

```text
Statement:
C-1 | Noor | -500 cents
F-1 | Sol | 20900 cents
S-1 | Mira | 12360 cents
```

The probe is supplied; you only need to finish the method. Submit checks other inputs as well.

The finished simulation can register accounts, apply their different withdrawal rules, credit integer interest, and print current balances. All data stays in memory.
