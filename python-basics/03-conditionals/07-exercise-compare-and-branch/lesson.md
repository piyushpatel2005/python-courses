---
title: "Exercise: Report Available Seats"
slug: exercise-compare-and-branch
order: 7
language: python
lesson_type: coding
summary: "Write three branches for available seats at an event."
seo_title: "Python if, elif, else Exercise | Python Basics"
seo_description: "Practice ordered branches with an event's remaining seat count."
seo_keywords: [python if else, python elif, event seats]
hints:
  - Keep seat_message = "Not set" above the branches so unfinished cases can still run.
  - Align if, elif, and else; end each heading with a colon and indent the assignment.
  - Check zero before fewer than four, because zero also meets the second comparison.
---

Let's take a look at an example of a parking place which wants to post a message about available parkings.

```python run
parking_spots = 2
if parking_spots == 0:
    message = "Full"
elif parking_spots < 3:
    message = "Almost full"
else:
    message = "Spaces available"
print(message)
```

It prints `Almost full`. Python skips the first branch because two is not zero, takes the second conditional branch because `parking_spots` is less than 3, and skips `else` block.

## Your Tasks

An event organizer wants a short message about the remaining seats for an event. He wants to print
- `Sold out` when there are no seats left
- `Few seats left` when there are one to three seats left
- `Seats available` for four or more. 
The input `seats_left` counts seats.

In `main.py`, the starting seat count is `2`. Keep the temporary `"Not set"` message so unwritten cases still run, and put your branches before the unindented print call. **Submit** after each task to check your progress.

1. Add `if seats_left == 0:` and set `seat_message` to `"Sold out"`.
2. Add `elif seats_left < 4:` and set `seat_message` to `"Few seats left"`.
3. Add `else:` and set `seat_message` to `"Seats available"`.

| After completing | Try `seats_left` | Expected message |
| --- | --- | --- |
| Task 1 | `0` | `Sold out` |
| Task 2 | `2` | `Few seats left` |
| Task 3 | `4` | `Seats available` |

Change only `seats_left` to try each case with **Run**. Restore it to `2` before the final **Submit**. 

Next is FizzBuzz, a short fun game to practice the skills you learned in this section.
