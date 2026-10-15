---
title: "Queue pending job IDs"
slug: pending-queue
order: 2
language: python
runtime: pyodide
lesson_type: coding
summary: "Queue known job IDs in FIFO order while suppressing duplicate active requests."
seo_title: "Queue pending job IDs in Python"
seo_description: "Queue known job IDs in FIFO order while suppressing duplicate active requests."
seo_keywords:
  - Python
  - pending-queue
hints:
  - "Claiming controls active membership; queue appends happen at the right end."
---

The catalog describes jobs, but a catalog entry is not yet a dispatch request. Add a FIFO intake queue that stores IDs, leaving the records in the catalog. This avoids copying the same record into several containers.

`enqueue(job_id)` looks up the ID with the supplied `_job` method. Unknown IDs raise `KeyError`. If the ID is already in `active`, return `False` without appending another copy. Otherwise append it to the right of `pending`, add it to `active`, and return `True`.

For example, if requests arrive for `roof-check`, `pipe-check`, and then `roof-check` again, the pending order contains only the first two IDs. The third request is a duplicate, not a request to move the earlier job to the back. After a job is dispatched it will remain active, preventing accidental redispatch. The later undo operation releases that ID.

A supplied `take_pending()` removes and returns the leftmost ID, or returns `None` for an empty queue. It is an internal transfer operation for the next stage: it does not remove the ID from `active`. An ID being moved from intake to the priority heap must remain protected against duplicate submissions. The checkpoint calls it only to make FIFO order visible.

A `deque` supports append and left-pop without shifting all waiting IDs. Under the usual dictionary and set hashing assumptions, enqueue and this transfer are expected O(1) operations. Space grows with the number of active IDs. The deque belongs to each workbench instance, so requests in one depot cannot appear in another.

Only implement the intake operation now. Priority scheduling will deliberately change the service order later, while using FIFO arrival order to settle equal priorities. Keeping those policies separate makes it clear which container is responsible for each decision.

## Supplied setup and small steps

The supplied `enqueue` wrapper checks that the ID exists before calling either helper. Claiming an ID controls duplicate requests; appending controls order. Test those responsibilities separately, then Run the wrapper that connects them.

## Your Tasks

1. Complete `claim_id(job_id)` to add an inactive ID and return `True`, or return `False` without changing an already-active ID.
2. Complete `append_pending(job_id)` to append the validated, claimed ID to the right end of the queue.

Edit `main.py`. Run transfers the two waiting IDs in arrival order, then returns `None`. Submit checks the same operation on additional small cases.
