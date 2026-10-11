---
title: Choose a Gate Signal
slug: exercise-compare-and-branch
order: 4
language: python
lesson_type: coding
summary: Build three small branches to choose a gate signal from its remaining charge.
seo_title: Python if, elif, else Exercise | Python Basics
seo_description: Practice one conditional branch at a time while Adi checks a beacon gate.
seo_keywords: [python if else, python elif, python conditions]
hints:
  - Keep gate_signal = "Not set" above your branches so unfinished cases still run.
  - Align if, elif, and else. End each branch heading with a colon and indent its assignment by four spaces.
  - Check zero first. Zero is also less than four, but Python runs only the first matching branch.
---

A gate uses its remaining charge to choose a signal: **Sealed**, **Flickering**, or **Open**. You will add each branch separately so you can check one case before writing the next.

You have used comparisons to get `True` or `False`. An `if` statement uses that result to choose what happens next.

## See how a choice works

This lantern uses a different set of values. Predict its message, then press **Run** below.

```python run
wicks = 2
if wicks == 0:
    message = "Dark"
elif wicks < 3:
    message = "Dim"
else:
    message = "Bright"
print(message)
```

The result is `Dim`. Follow the checks from top to bottom:

- `if wicks == 0`: false, so Python skips `"Dark"`.
- `elif wicks < 3`: true, so Python chooses `"Dim"`.
- `else`: skipped because a previous branch already matched.

Only one branch runs. Once Python finds a true condition, it skips the remaining branches in that chain.

Put a colon at the end of each branch heading. Indent its assignment by four spaces. Keep `if`, `elif`, and `else` aligned; `else` has no condition.

## Set up your gate

In **main.py**, the charge is already set to `2`. The `"Not set"` value is a temporary message for cases you have not written yet. Keep that assignment, add your branches below it, and leave `print(gate_signal)` at the end with no indentation.

Build one branch at a time. Press **Submit** after each task: its matching check can pass even while later branches are unfinished.

## Your Tasks

1. Add an `if charge_left == 0:` branch that sets `gate_signal` to `"Sealed"`.
2. Add an `elif charge_left < 4:` branch that sets `gate_signal` to `"Flickering"`.
3. Add an `else:` branch that sets `gate_signal` to `"Open"`.

## Try each route

Change only the supplied `charge_left` value and press **Run**:

| After completing | Try this charge | You should see |
| --- | --- | --- |
| Task 1 | `0` | `Sealed` |
| Task 2 | `2` | `Flickering` |
| Task 3 | `4` | `Open` |

While a branch is unfinished, seeing `Not set` for its charge is expected. Restore `charge_left` to `2` when you finish, then **Submit** to check all three routes.

Notice the boundary: `3` is still `Flickering`, but `4` is `Open`. Zero must be checked first because it also satisfies `< 4`.

The gate now has a message for each charge range. Next, you will repeat an action with a loop: first counting beacon pulses, then recharging a beacon.
