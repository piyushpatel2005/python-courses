---
title: "Scheduler project"
slug: "scheduler-project"
order: 14
language: "python"
runtime: "pyodide"
lesson_type: "coding"
summary: "In `Scheduler.run_due`, drain ready jobs through `now`, stopping before the first future job."
seo_title: "Scheduler project | Data structures with Python"
seo_description: "Finish a small scheduler that releases jobs when their due time arrives. The completed updating queue is supplied intact. Your new method drains only jobs due by the requested time, leaving future work queued."
seo_keywords:
  - Python
  - "Scheduler project"
---

Finish a small scheduler that releases jobs when their due time arrives. The completed updating queue is supplied intact. Your new method drains only jobs due by the requested time, leaving future work queued.

## Work through the idea

The scheduler uses an integer due time as priority: smaller means earlier. `schedule(task, due)` is supplied and delegates to the queue's update method, so scheduling an existing ID changes its due time rather than adding a second live job. Equal due times follow the order of their latest scheduling calls.

Use `peek` before removing anything. It cleans obsolete root entries and reveals the earliest live `(task, due)` pair. If its due time exceeds `now`, every other live job is also in the future, so stop. Otherwise pop that entry and append its task ID to the ready list. Repeat until the next job is future work or the queue is empty.

An empty queue makes peek raise `IndexError`; catch that specific exception to end the loop. Do not catch every exception, because a programming mistake should not look like an empty schedule. A stale entry may have an old early due time, so inspecting the raw heap root instead of the supplied peek method could release a rescheduled job too soon.

This exercise simulates scheduling by returning IDs. It does not sleep, consult a clock, launch threads, or execute callbacks. Caller-supplied times keep the behavior deterministic. A second call at the same time should not release already completed jobs again.

## Build it in checkpoints

The readiness decision belongs to `has_due(now)`. It must use the updating queue's public peek so stale early entries cannot release a rescheduled job. Catch only the empty-queue IndexError and compare the earliest live due time inclusively. Checking readiness may discard stale history, but it must not remove a live task. Once that check works, `run_due` repeatedly consumes ready IDs into its own fresh result list.

## Contract and cost

`run_due(now)` returns task IDs whose current due times are <= now, ordered by due time and stable update tickets. Remove those live jobs exactly once; retain all future jobs. Integer times may be negative. Re-scheduling a completed ID creates new work. Preserve both queue classes and the supplied scheduler setup.

Releasing d jobs and removing s stale entries costs O((d + s + 1) log(m + 1)) as an upper bound for m stored entries. Output space is O(d); queue storage still includes stale history. With a clean future root and no due work, the check is O(1).

## Your Tasks

1. In `Scheduler.has_due`, check whether the earliest live job is due, without removing that job.
2. In `Scheduler.run_due`, drain ready jobs through `now`, stopping before the first future job.

Edit `main.py`, then press **Run** to inspect the supplied probe and **Submit** to check each task. Complete the numbered changes in order. The supplied code keeps earlier operations available; you do not need to copy anything from another lesson.
