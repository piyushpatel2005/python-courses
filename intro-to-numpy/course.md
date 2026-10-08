---
slug: intro-to-numpy
title: "Intro to NumPy: Pocket Observatory"
description: Build a pocket observatory with NumPy arrays, slicing, broadcasting, matrix operations, statistics, and shape transformations.
summary: A hands-on NumPy course built from short editable demonstrations, fresh coding exercises, practical sensor projects, and section quizzes.
language: python
level: Beginner
format: Interactive orientation, coding demos, exercises, projects, and quizzes
sort_order: 6
seo_title: Intro to NumPy Course | Build a Pocket Observatory
seo_description: Learn NumPy in the browser by building arrays, exploring sensor grids, slicing data, broadcasting corrections, and interpreting observations.
seo_keywords: [numpy tutorial, python numpy course, numpy arrays, numpy broadcasting, numpy exercises]
modules:
  - slug: launchpad
    title: "1. Launchpad: Why NumPy and Your First Array"
    sort_order: 1
  - slug: array-factory
    title: "2. Array Factory: Generate and Convert Data"
    sort_order: 2
  - slug: indexing-and-views
    title: "3. Find the Signal: Indexing, Slicing, and Views"
    sort_order: 3
  - slug: array-math
    title: "4. Tune the Signal: Vectorization and Broadcasting"
    sort_order: 4
  - slug: reductions-and-stats
    title: "5. Read the Patterns: Reductions and Statistics"
    sort_order: 5
  - slug: matrix-workshop
    title: "6. Point the Array: Matrix Operations"
    sort_order: 6
  - slug: shape-and-data-lab
    title: "7. Observation Lab: Shapes, CSV, and Final Project"
    sort_order: 7
---

# Pocket Observatory

A pocket observatory collects tiny streams of readings: sky-brightness grids, sound levels, calibration weights, and event counts. Your job is to make the readings useful. One mission asks you to find a signal in a matrix; another asks you to correct an entire row without a Python loop. The examples change settings so you learn the NumPy idea, not a single dataset.

This course turns NumPy concepts into beginner-sized steps. You will create arrays from lists and constructors; inspect dimension, shape, size, and dtype; make reproducible random data; index, slice, mask, and distinguish views from copies; apply vectorized arithmetic and broadcasting; reduce along axes and compute statistics; sort, transpose, and multiply matrices; reshape, add axes, repeat, tile, and read small CSV fixtures. The last lab brings several of these together.

Each concept has a short working example you can edit in `main.py` and a nearby exercise where you write new code on different data. Run shows your program's output; Submit Code checks each numbered task. Interactive orientation blocks have a Run button but are not a substitute for typing in the editor. Section quizzes check understanding after the practice.

## Start here

You should know Python variables, lists, loops, functions, and indexing. Open a lesson, edit `main.py`, and Run your code. `import numpy as np` gives your program the NumPy tools used throughout the course.

Outputs use small, deterministic fixtures; random-number exercises use an explicit seed. Since default integer types can vary by environment, the lessons check intended values and dtype kinds rather than relying on a particular integer width. All examples use ordinary Python code you can run in the editor; notebook-only shortcuts are replaced by focused tasks.
