---
slug: data-structures-with-python
title: Data Structures with Python
description: Build Python data structures and algorithms one operation at a time, with visual traces, typed code, tests, and practical projects.
language: python
summary: Practice memory models, linked structures, searching, sorting, trees, heaps, graphs, tries, range queries, and disjoint sets in 210 coding lessons.
seo_title: Data Structures with Python
seo_description: Learn Python data structures through 210 hands-on lessons, visual algorithm traces, typed implementations, tests, and an integrated dispatch project.
seo_keywords:
  - Python data structures
  - Python algorithms
  - linked lists
  - trees and graphs
  - algorithm complexity
modules:
  - slug: memory-and-cost
    title: "Memory and algorithm cost"
    sort_order: 1
  - slug: recursion
    title: "Recursion and iteration"
    sort_order: 2
  - slug: arrays-and-sequences
    title: "Arrays and sequence patterns"
    sort_order: 3
  - slug: singly-linked-lists
    title: "Build a singly linked list"
    sort_order: 4
  - slug: linked-list-variants
    title: "Doubly linked, circular, and skip lists"
    sort_order: 5
  - slug: stacks
    title: "Stacks and their applications"
    sort_order: 6
  - slug: queues-and-deques
    title: "Queues and deques"
    sort_order: 7
  - slug: hash-tables
    title: "Build and use hash tables"
    sort_order: 8
  - slug: searching
    title: "Searching sorted and unsorted data"
    sort_order: 9
  - slug: sorting
    title: "Sorting algorithms"
    sort_order: 10
  - slug: trees-and-bst
    title: "Binary trees and search trees"
    sort_order: 11
  - slug: heaps-and-priority
    title: "Heaps and priority queues"
    sort_order: 12
  - slug: graph-models
    title: "Represent and build graphs"
    sort_order: 13
  - slug: graph-traversal
    title: "Breadth-first and depth-first traversal"
    sort_order: 14
  - slug: shortest-paths
    title: "Weighted graphs and shortest paths"
    sort_order: 15
  - slug: bits-and-sets
    title: "Bits and sets"
    sort_order: 16
  - slug: tries
    title: "Tries and prefix lookup"
    sort_order: 17
  - slug: range-structures
    title: "Fenwick and segment trees"
    sort_order: 18
  - slug: disjoint-sets
    title: "Disjoint-set union"
    sort_order: 19
  - slug: combinatorial-search
    title: "Combinatorial search"
    sort_order: 20
  - slug: dispatch-project
    title: "Project: a dispatch workbench"
    sort_order: 21
---

# Data Structures with Python

A queue keeps waiting jobs in order. A heap chooses the next urgent job. A graph describes which places are connected, while a trie finds words that share a prefix. Each structure makes some operations convenient and others expensive. This course helps you see those trade-offs and implement the operations yourself.

You will work through 210 coding lessons. The explanations introduce the idea beside the editor, and the starter leaves the new behavior for you to write. Diagrams show the values, links, boundaries, and intermediate states that code alone can hide. Most exercises add one operation; later exercises combine the operations into a useful program.

## Before you begin

You should be comfortable with Python functions, loops, lists, dictionaries, classes, constructors, instance methods, and basic exception handling. The object-oriented Python course is suitable preparation. You do not need prior knowledge of algorithms or complexity analysis.

Code uses type hints to describe expected inputs, outputs, and stored values. Early lessons explain the notation, and later lessons explain unfamiliar types where they appear. Type hints help you read a contract; they do not automatically validate values at runtime.

## How practice works

Read the explanation and visual trace, then work through the short numbered tasks in `main.py`. Each task has its own check, so you can submit after a small change rather than finish the whole lesson at once. Run uses the supplied probe to show what your code does. Submit checks additional inputs and edge cases. Each lesson has a reference solution for comparison after you have tried your own approach.

The starter is intentionally incomplete but runnable. You do not need to copy code from a previous lesson: a continuing build includes the earlier completed operations. The next method is left unfinished. All examples use small in-memory inputs and run in the lesson workspace, without installation, external services, or a blocking keyboard prompt.

A quiz follows each section. These questions ask you to explain behavior and choose between structures, while coding tasks test whether your implementation works.

## The route through the course

Start with object references, copying, and counting work. Learn recursion before using it to traverse a tree or divide a sorting problem. Arrays and prefix sums introduce index boundaries; linked lists replace those indices with explicit links.

Build singly linked, doubly linked, circular, and skip lists. Then use stacks, queues, ring buffers, and deques to manage order. Construct hash tables with collision handling before studying search and sort algorithms in detail.

Trees introduce recursive structure, and binary search trees make the cost of tree height visible. Heaps and priority queues support scheduling. Graphs then combine adjacency representations with breadth-first search, depth-first search, cycle detection, and shortest paths.

The later sections cover bit masks, sets, tries, Fenwick trees, segment trees, and disjoint-set union. Combinatorial search gives you practice managing choices, repetition, and backtracking. The final dispatch workbench brings several structures together in a scripted console application.

## What the tests check

Tasks define behavior for cases such as empty structures, missing keys, duplicate values, boundary indices, and disconnected graphs. Tests use more than the visible example. When a lesson asks you to implement a specific algorithm, its checks may also inspect the requested technique or operation trace rather than accept a built-in shortcut.

Complexity claims describe a stated input model and implementation. You will distinguish worst-case, expected, and amortized costs, count auxiliary space, and see why a short Python expression is not automatically a constant-time operation. Small traces make these costs observable without unreliable stopwatch tests.
