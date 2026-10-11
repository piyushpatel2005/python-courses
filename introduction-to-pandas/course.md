---
slug: introduction-to-pandas
title: "Introduction to Pandas: Community Data Desk"
description: "Learn to organize, clean, combine, and explain tabular data with hands-on Python exercises."
summary: "Build small, useful data reports with Series and DataFrames, then put your skills together in a complete market-data project."
language: python
level: Beginner
format: Coding lessons, guided examples, projects, and quizzes
seo_title: "Introduction to Pandas | Hands-on Python Data Analysis"
seo_description: "Practice Pandas with short coding exercises on tables, filtering, missing values, joins, groups, dates, and a complete data report."
seo_keywords: [pandas course, python data analysis, pandas dataframe, pandas exercises, data cleaning]
modules:
  - slug: foundations
    title: "1. Meet Labeled Data"
    sort_order: 1
  - slug: dataframes
    title: "2. Build and Inspect Tables"
    sort_order: 2
  - slug: select-and-filter
    title: "3. Find the Rows You Need"
    sort_order: 3
  - slug: clean-data
    title: "4. Make Messy Data Usable"
    sort_order: 4
  - slug: combine-tables
    title: "5. Put Tables Together"
    sort_order: 5
  - slug: summarize-groups
    title: "6. Tell the Story in Numbers"
    sort_order: 6
  - slug: files-and-dates
    title: "7. Read, Write, and Understand Dates"
    sort_order: 7
  - slug: final-project
    title: "8. Build a Market Report"
    sort_order: 8
---

# Your community data desk

A community market records its stalls, orders, and event days. One sheet has the sales; another has the stall names. Some records are incomplete. You'll use pandas to bring these records together and answer questions such as which stalls sold the most and how sales changed from day to day.

The tables stay small enough to check by eye. Before trusting a calculation, you'll be able to point to the rows it used.

## Before you begin

You should be comfortable with Python variables, lists, dictionaries, functions, and `import`. You don't need spreadsheet or statistics experience. We'll explain the table vocabulary and calculations as they appear.

The course editor is ready to run the supplied examples. You don't need to download market data or install a package to start. The import `import pandas as pd` gives pandas its usual short name, `pd`.

## How to practise

Most topics start with a working example in `main.py`. Make the requested small change and use **Run** to inspect what happened. The following exercise uses different data so you can try the same idea yourself.

**Submit** checks the numbered tasks. You can submit partly finished work to find out which steps are working; you don't have to finish the whole exercise first. A short quiz closes each section.

When a result surprises you, compare the input and output tables. Check the row labels, column names, and values separately. Those details often explain why a selection or calculation behaved differently from what you expected.

## What you'll build

- Start with a **Series**, a line of values with labels, then a **DataFrame**, a table with named columns.
- Choose rows and columns, write filters, and put results in a useful order.
- Handle missing cells and inconsistent text without losing track of the original records.
- Match related tables and summarise groups of rows.
- Read and write small data samples, then work with dates.

The final section brings these skills together in a market report. You'll build it in stages, checking the intermediate tables before producing the summary.

Begin with the labeled-data introduction. You'll see why a row's label can matter just as much as its value.
