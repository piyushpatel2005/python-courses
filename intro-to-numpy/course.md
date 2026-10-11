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

Your observatory has readings to make sense of: a grid of sky brightness, a set of sound levels, and counts collected over time. You'll use NumPy to organise those values and work on many of them at once.

You don't need astronomy knowledge. The examples use small datasets you can inspect by eye. Some demonstrations visit an arcade or a sound board; the following exercise uses different data so you can practise the idea rather than copy an answer.

## Before you start

You should be comfortable with Python variables, lists, loops, functions, and indexing. We'll explain NumPy's array layouts and operations as we meet them. Nothing needs to be installed to use the course editor.

## How you'll practise

Most topics begin with a working `main.py` and one small change to make. The next exercise asks you to write a related operation yourself.

- **Run** shows your program's output. Compare it with the checkpoint in the lesson.
- **Submit** checks the numbered tasks. You can submit partly finished work to see which steps are working.
- A section quiz checks the ideas you've just practised.

The opening runnable examples are for reading and comparison. After those, you'll spend most of your time editing code. Projects bring several earlier skills together without requiring a new dataset or external service.

## The course path

1. **Launchpad:** turn lists into arrays, build grids and stacks, and read their shapes.
2. **Array Factory:** generate sequences and starter grids, then choose suitable number types.
3. **Find the Signal:** select readings and see when a slice shares its original data.
4. **Tune the Signal:** apply arithmetic and corrections across arrays of compatible shapes.
5. **Read the Patterns:** reduce rows or columns to totals and describe a set of readings.
6. **Point the Array:** transpose grids and combine measurements with matrix operations.
7. **Observation Lab:** rearrange shapes, read a small CSV, and put the tools together in a final project.

Random examples use a seed so you can repeat an experiment. Other examples use fixed inputs. You won't need to guess which readings a task started with.

Begin with **What is NumPy?** You'll compare a familiar Python loop with an array calculation that produces the same result.
