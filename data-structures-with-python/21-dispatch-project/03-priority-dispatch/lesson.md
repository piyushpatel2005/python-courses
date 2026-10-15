---
title: "Dispatch by stable priority"
slug: priority-dispatch
order: 3
language: python
runtime: pyodide
lesson_type: coding
summary: "Dispatch by urgency with FIFO ties, recording completion history and workload."
seo_title: "Dispatch by stable priority in Python"
seo_description: "Dispatch by urgency with FIFO ties, recording completion history and workload."
seo_keywords:
  - Python
  - priority-dispatch
hints:
  - "Use the current sequence in the returned entry, then advance it for the next arrival."
---

Waiting jobs should be served by urgency, with arrival order breaking ties. A FIFO queue alone cannot do both. Transfer pending IDs into a min-heap whose entries are `(priority, sequence, job_id)`.

The supplied `_stage_pending()` drains the intake queue from the left. For each ID it reads the catalog priority, pushes a heap entry, and advances a monotonic sequence counter. Two entries never share a sequence number. That prevents the heap from using a job ID as the tie-breaker and keeps the ordering stable even when IDs sort differently from arrival order.

The supplied `dispatch()` works by staging all new pending jobs, returning `None` if the heap is empty, and otherwise popping the smallest entry. Pass its ID to the supplied `_complete(job_id)` helper and return that helper's result. `_complete` records the ID on the history stack and adds its workload to the Fenwick load index. Those supplied effects give the next lessons real dispatch data to undo and report.

For example, a routine job arriving before an urgent one is still served later. Two urgent jobs arriving in the order `zeta`, then `alpha`, must retain that order; alphabetic ID order is irrelevant. A newly queued more urgent job can also overtake work already in the heap, because each call stages new arrivals before choosing.

A dispatched ID stays in `active`. Registering is not an update API, and direct edits to internal catalog records are outside this project's contract. The saved priority therefore remains consistent. The later undo operation provides the supported route for re-enqueueing a completed job.

Transferring k arrivals into a heap of q jobs costs O(k log(q+k)); selecting one costs O(log(q+k)). Recording the load adds O(log days). A quiet dispatch with no work returns `None` and changes neither history nor loads. Space is proportional to stored jobs, heap entries, history, and reporting days.

## Supplied setup and small steps

The supplied transfer loop asks `priority_entry` for each heap tuple. The supplied `dispatch` then calls `take_ready` and records completion through `_complete`. Your tasks are the stable tuple and the heap removal, not history or load bookkeeping.

## Your Tasks

1. Complete `priority_entry(job_id)` to return `(priority, sequence, job_id)` and advance the sequence counter once.
2. Complete `take_ready()` to pop and return the smallest heap entry's ID, or `None` when empty.

Edit `main.py`. Run should choose the urgent jobs first while keeping their arrival order. Submit checks the same operation on additional small cases.
