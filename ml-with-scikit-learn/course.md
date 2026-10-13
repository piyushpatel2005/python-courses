---
slug: ml-with-scikit-learn
title: Machine Learning with Scikit-Learn
description: Build, evaluate, and explain machine learning models with hands-on scikit-learn lessons and HomeHurray Inc. projects.
language: python
draft: true
summary: Work from feature tables to reliable pipelines, prediction models, and catalog recommendations using small reproducible datasets.
seo_title: Machine Learning with Scikit-Learn
seo_description: Learn preprocessing, regression, classification, model selection, clustering, text features, and recommendations through practical Python exercises.
seo_keywords:
  - scikit-learn
  - machine learning with Python
  - preprocessing pipelines
  - model evaluation
  - content recommendations
modules:
  - slug: estimator-basics
    title: "Data and the estimator interface"
    sort_order: 1
  - slug: datasets-and-quality
    title: "Datasets and data checks"
    sort_order: 2
  - slug: honest-holdouts
    title: "Holdouts before preprocessing"
    sort_order: 3
  - slug: numeric-preprocessing
    title: "Numerical preprocessing"
    sort_order: 4
  - slug: categorical-preprocessing
    title: "Categorical and mixed columns"
    sort_order: 5
  - slug: pipelines-and-regression
    title: "Pipelines and regression errors"
    sort_order: 6
  - slug: regularized-regression
    title: "Regularization and nonlinear features"
    sort_order: 7
  - slug: regression-project
    title: "Project: estimate product listing prices"
    sort_order: 8
  - slug: classifiers
    title: "Classification estimators"
    sort_order: 9
  - slug: classification-metrics
    title: "Classification metrics and thresholds"
    sort_order: 10
  - slug: trees-and-ensembles
    title: "Trees and ensembles"
    sort_order: 11
  - slug: cross-validation-and-selection
    title: "Cross-validation and model selection"
    sort_order: 12
  - slug: mixed-classification-project
    title: "Project: classify return risk at checkout"
    sort_order: 13
  - slug: inspection-and-unsupervised
    title: "Inspection and unsupervised transforms"
    sort_order: 14
  - slug: clustering-and-text
    title: "Clustering and sparse text features"
    sort_order: 15
  - slug: text-and-content-recommendations
    title: "Text models and content recommendations"
    sort_order: 16
  - slug: recommendation-evaluation
    title: "Recommendation evaluation and cold starts"
    sort_order: 17
  - slug: recommendation-project
    title: "Project: recommend home goods from catalog content"
    sort_order: 18
---

# Machine Learning with Scikit-Learn

Turn a feature table into a model you can test, inspect, and explain. You will work through small, runnable examples before applying each idea to a different exercise. Worked calculations and diagrams make the changes to your data visible.

HomeHurray Inc. is a fictional home-goods retailer. Its synthetic product, checkout, and catalog data give the projects a consistent setting. You will estimate listed prices, evaluate return-risk predictions, and build content-based recommendations. These are teaching datasets, not records from a real company or evidence of commercial performance. Named scikit-learn benchmark datasets remain separate examples.

## Before you begin

You should be comfortable with Python functions, NumPy arrays, pandas tables, and basic Matplotlib charts. Machine Learning Fundamentals provides the conceptual background. New scikit-learn interfaces are explained before you use them; mathematical notation is introduced alongside small worked examples.

## How the course works

Each focused demonstration gives you a small change to make. The following exercise asks you to use that idea with different inputs. Run your code to inspect the output, then Submit to check the requested behavior. A reference solution is available when you need to compare approaches. Every section finishes with a quiz.

The projects build across consecutive stages. Each stage includes the completed setup from the previous stage, so you can start it without relying on saved Python state. Training, validation, and test data have distinct jobs throughout: selecting a model is not the same as evaluating its final performance.

Small calculations use in-memory arrays, while larger examples and projects read the supplied CSV or JSON files with pandas. Read-only data tabs let you inspect those records, and each file-backed lesson explains its fields before the tasks. Reproducible generators and named bundled datasets provide additional examples. No external dataset download is required. The models and searches are deliberately small enough to inspect and run while learning.

## What you will build

- A product-listing-price report with a baseline, a regularized pipeline, and held-out error measurements.
- A checkout return-risk classifier with mixed feature types, training-only model selection, and a separately selected decision threshold.
- A catalog-content recommender with seen-item filtering, cold-start handling, and a time-aware evaluation protocol.

Along the way, you will practice numerical and categorical preprocessing, regression and classification, cross-validation, trees and ensembles, feature inspection, dimensionality reduction, clustering, and sparse text representations. Each report states its assumptions and limitations rather than promising that a higher score guarantees a better business decision.
