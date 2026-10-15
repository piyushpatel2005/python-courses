---
title: "Play and consume the next recording"
slug: "playlist-project"
order: 12
language: "python"
runtime: pyodide
lesson_type: "coding"
summary: "Implement `play_next()` to return and remove the first title using `remove_head()`, or return `None` without mutation when the playlist is empty."
seo_title: "Play and consume the next recording | Python data structures"
seo_description: "Implement `play_next()` to return and remove the first title using `remove_head()`, or return `None` without mutation when the playlist is empty."
seo_keywords:
  - "Python"
  - "playlist project"
  - "data structures"
---

# Play and consume the next recording

Your list now supports the editing operations a small playlist needs. The last stage adds a narrow playback interface. The list's internal deletion method returns a node; a playback caller needs only the title. A wrapper can translate between these two contracts without repeating pointer manipulation.

For this project, playlist titles are strings. None is reserved for the signal that playback has nothing left. The generic LinkedList can still hold other values, but this interface deliberately uses a narrower domain. An empty playback request is normal, so it returns None instead of exposing remove_head's IndexError.

For a nonempty playlist, delegate the structural change to remove_head and return its value. That reuse matters: remove_head already handles detachment, singleton cleanup, and size. Reimplementing the same links here creates a second place for bugs. The supplied Run session appends titles and consumes the first one; you only implement play_next.

The node chain remains the source of truth. Do not keep a second Python list of titles or a separate playback index. After playback, prepend and append should operate on the remaining chain, and reverse should reorder only recordings that have not played.

This finishes the singly linked list build. The next module starts new representations for backward navigation and circular traversal; it will not silently change the meaning of these methods.

## Trace it first

A reading queue `chapter one -> chapter two -> None` plays chapter one and leaves chapter two as both endpoints. The next call returns chapter two and clears both endpoints. A third call returns None. Appending chapter three afterward must make it immediately playable.

## Cost

Each play_next call is O(1) time and O(1) auxiliary space. Consuming n titles takes O(n) total time, excluding any actual audio or text processing.

## Operation contract

Implement `play_next()` to return and remove the first title using `remove_head()`, or return `None` without mutation when the playlist is empty.

## Your Tasks

1. Implement `play_next()` by delegating removal to `remove_head()`.

## Run and check

Edit `LinkedList.play_next` in `main.py`. The earlier definitions and Run probe are supplied. Run the completed operation to see:

```text
Playing: Dawn
Remaining: ['Rain', 'Harbor']
```

Press **Submit** to check the tasks on additional inputs and boundary cases.
