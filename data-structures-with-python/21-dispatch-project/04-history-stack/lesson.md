---
title: "Undo the latest completed dispatch"
slug: history-stack
order: 4
language: python
runtime: pyodide
lesson_type: coding
summary: "Undo the latest completion and restore its workload and resubmission eligibility."
seo_title: "Undo the latest completed dispatch in Python"
seo_description: "Undo the latest completion and restore its workload and resubmission eligibility."
seo_keywords:
  - Python
  - history-stack
hints:
  - "Pop from the history end, subtract the recorded load, and release the ID in separate helpers."
---

The dispatcher can reverse the most recent completion. History is a stack because the latest action is the first one undone. This project does not attempt arbitrary cancellation or undo a real-world delivery.

`dispatch()` already appends completed IDs to `history` and adds their units to the load index. The supplied `undo()` acts as the inverse of that recorded completion. If history is empty, return `None`. Otherwise pop the last ID, read its catalog record, subtract its units from the same reporting day, remove the ID from `active`, and return it.

For example, if completed history is `['roof', 'gate']`, undo returns `gate` and leaves `['roof']`. It does not remove a pending job or the most urgent remaining heap entry. The returned job remains in the catalog, and the user can choose to enqueue it again. Undo itself does not enqueue it automatically; that policy keeps reversal separate from resubmission.

The state change has one meaning across three representations: this job is no longer a completed active job. Popping history but forgetting the load subtraction leaves a misleading report. Subtracting units without releasing the active ID prevents the user from resubmitting the job. Keep these updates together inside the one undo operation.

All history entries were created by `_complete` from validated records, so there should be a matching catalog entry and active ID. Do not silently ignore broken internal state; callers are expected to use the public methods rather than edit these containers directly. Repeated undo on empty history is harmless and leaves loads unchanged.

The list pop and set removal are O(1) under the usual hashing assumptions, while the Fenwick update costs O(log days). Auxiliary space is O(1). The checkpoint dispatches and reverses one job so you can see history shrink and the ID become eligible for intake again.

## Supplied setup and small steps

The supplied `undo` wrapper coordinates three small helpers. Each test prepares its own state, so popping history does not need a working load reversal, and load reversal does not need a working pop. Complete them in the listed order.

## Your Tasks

1. Complete `pop_history()` to remove the latest completed ID, or return `None` when empty.
2. Complete `reverse_load(job_id)` to subtract that catalog record's units from its declared day.
3. Complete `release_id(job_id)` to remove the completed ID from `active`, without enqueueing it.

Edit `main.py`. Run reverses one completion and confirms that the job can be enqueued again. Submit checks the same operation on additional small cases.
