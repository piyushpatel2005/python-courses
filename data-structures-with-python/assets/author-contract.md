# Authoring contract

This is maintainer material. Read `curriculum-plan.json` and preserve the exact module/lesson paths and orders. The original user outline is in `source-outline.md`.

## Learner and teaching style

Assume Python basics plus classes, constructors, instance methods, and ordinary exceptions. Teach algorithms from the beginning. This is a practice-first course following the object-oriented-python format, not a translation of a book. Every lesson has an incomplete runnable coding starter and a meaningful implementation task. Explain the idea, representation, invariant, steps, edge cases, and cost in the left pane before asking for code. A short example must differ from the assessed input/implementation. Do not paste the finished algorithm into prose. A new structure or algorithm usually deserves 250–450 useful words; a narrow continuation can be shorter. Do not fill lessons with repeated generic paragraphs or restate the task to meet a length target.

Use concrete, original examples and a patient, natural voice. Show how a learner can reason from a tiny trace. Explain why preserving a pointer, boundary, or invariant matters. Distinguish implementation exercises from using Python's built-ins. Gradually move from traced examples to complete algorithms. One new method or coherent operation per stage is preferable to an entire data structure in one task.

Do not mention LeetCode, HackerRank, any other reference platform, the supplied book, its publisher, or JavaScript in learner prose, SEO, hints, quizzes, starter comments, or solutions. Reference provenance belongs only in maintainer assets. Do not copy the book's prose, figures, data, code, or quiz questions. The book is conceptual research, not a template to translate. Parent owns original SVG/.excalidraw diagrams.

## InterCourses runtime and type hints

The course is specifically for the `intercourses/` platform's browser Pyodide Python runtime, not a terminal/server Python course. Set `language: python` and `runtime: pyodide`; use only compatible standard-library features. The user has excluded browser verification from the remaining scope. Review cohesive teaching, prerequisite order, atomic tasks, and cumulative code; use native/source checks where useful. Do not claim actual InterCourses browser Run/Submit acceptance. No blocking input, server execution, network, local disk dependency, pip installation, or new-Python-version-only APIs.

User explicitly requests type hints where possible. Annotate learner-facing function/method parameters and returns, and meaningful state attributes, in both starters and solutions. Use readable built-in generics such as `list[int]`, `dict[str, int]`, `tuple[int, int]`, and `Node | None`; use `from __future__ import annotations` to avoid premature forward-reference evaluation. Explain the basic notation early and unfamiliar hints locally. Do not let elaborate generics obscure the algorithm, and do not grade annotations unless annotations are the explicit task. For flexible payloads choose simple appropriate annotations and explain the supported input contract rather than misleadingly declaring a more general type. Previously authored unannotated files must be updated consistently, preserving cumulative handoffs and probes. Keep Python implementation details out of learner prose unless needed for the concept.

## Files and grading

Each exact planned lesson directory contains:
- lesson.md with valid YAML: title, slug, numeric order, language: python, lesson_type: coding, summary, seo_title, seo_description, seo_keywords. Use two-space indented metadata lists. Hints optional, only actionable and tied to a task.
- main.py: syntactically valid, incomplete, with guarded supplied Run probe under `if __name__ == "__main__":`. No blocking input, filesystem dependency, network, or external package.
- test_main.py: `from solution import *`; synchronous zero-argument top-level `def test_*` functions. Put learner symbol lookups inside tests, not at module import time. No pytest fixtures/parametrization/raises, async tests, or test classes. Display names/docstrings should explain the behavior.
- solution/main.py: complete standalone solution, keeping supplied scaffolding and probes.
- files.yaml containing exactly `files:` then `  - path: main.py`. Test and solution remain hidden.

User correction: tasks must be small, atomic, easy to follow, and individually testable. Do not force one task/test per lesson. Under `## Your Tasks`, give each independent learner change a short numbered instruction and one corresponding synchronous test, in displayed order. Separate independent validation, state initialization, mutation, and result construction when a broad implementation task bundles them. Explain reasoning and algorithm steps before the task list rather than packing a specification into one sentence. Keep genuinely inseparable behavior together; do not split into meaningless keystrokes or add a checkbox for every incidental edge case.

Design the starter for incremental progress: supply earlier functionality and runnable placeholders so a completed first task earns its check without requiring later tasks. Execute every cumulative task prefix for multi-task lessons and verify the exact passing prefix, not just its count. No already-passing 'keep the supplied code' checks. Every starter must Run without an uncaught exception and fail every current task; every solution must Run and pass all tests. Starter probes may catch unfinished behavior and say what is missing.

Require actual behavior, not fixed Console strings. Test empty/singleton, duplicates, missing values, boundaries, multiple independent instances, and mutation isolation where relevant. Use small deterministic model comparisons and wrong-algorithm mutants. If implementing a particular algorithm is the explicit task, reject built-in `sorted`/`sort`/dict/set substitutes with a narrowly scoped technique check or operation/invariant trace; do not overconstrain valid alternatives. No elapsed-time grading. Never teach unsafe inputs without defined behavior.

Every module has quiz/index.yaml and four qNN.md questions following the actual OOP quiz schema. Quote `true`/`false` answers. Include explanations tied to taught concepts, not untaught trivia.

## Cumulative code

When building a class step-by-step, next starter preserves previously completed definitions and adds only the new stub, new probe, and clearly explained scaffolding. Compare preceding solution definitions by AST. Do not require copying code across lessons. Tests focus on the current change while author-side regression checks ensure later stages preserve earlier contracts. A new variation can start a fresh implementation only if the prose explicitly says so. Do not use helpers from future lessons without supplying and explaining them.

## Python and algorithm caveats

- Distinguish language behavior from CPython layout. `id()` is an identity token, not a portable memory address. A list stores references, copying it is shallow. Avoid brittle size/address assertions.
- State the cost model. O(1) arithmetic assumes bounded-size values; arbitrary-size integers and exponentiation are not constant-time merely because the source uses one operator. Count work, not wall-clock time.
- Recursion consumes stack frames and Python does not guarantee tail-call elimination. Keep examples small; do not raise recursion limits or time exponential runs. Teach the sorted-halving premise within the early recursive-binary-search lesson before its later dedicated search treatment.
- List append is amortized O(1); front insert/pop shifts references. Binary search is O(log n) comparisons, sorted list insertion O(n). Prefix sum construction O(n), query O(1), updates to static prefixes O(n).
- Linked deletion after a known predecessor can be O(1), finding it O(n). Check head/tail/size invariants and detach links carefully. Skip-list tests use explicit reproducible levels, with expected—not guaranteed—logarithmic behavior under the randomized model.
- Hash equality and collisions are distinct; teaching hash functions are not secure. Python string hash values are process-dependent. Expected hash lookup assumes a suitable distribution/load; worst case O(n), plus key hashing/comparison costs.
- A BST is not automatically balanced. Use O(h), worst O(n), and clarify duplicate policy. Define height convention consistently in each self-contained exercise.
- Use min-heap-compatible standard-library APIs available in the platform runtime; implement max heaps without relying on newly introduced max-heap helpers. heapify O(n), push/pop O(log n), root peek O(1). Stable priority ties need a counter, not comparison of arbitrary tasks.
- Graph contracts state directedness, self-loop/duplicate policy, neighbor order, missing vertices, and weighting. BFS visits on enqueue; shortest-hop paths require unweighted/equal-weight edges. Dijkstra requires nonnegative weights, stale heap-entry checks, and explicit unreachable behavior. State actual implementation time/space bounds.
- Python bitwise operations are not restricted to 32-bit integers. Use nonnegative values or explicit masks for fixed-width exercises; explain `~x == -x - 1` where relevant.
- Fenwick indexing conversion, lowbit progress, segment intervals, and DSU representative identity need explicit contracts. Do not require one particular DSU root when multiple valid roots exist. Compression plus union-by-size has amortized inverse-Ackermann cost, not a strict per-call constant guarantee.

## Review and verification

Load course-lesson, course-reviewer, and humanizer skills. Read actual content guide, loader, and comparable OOP examples. Re-read every lesson with its starter/test/solution twice for teaching flow and natural wording. Execute all examples, starter/solution tests, representative mutants, and cumulative regressions. Save per-module evidence in assets/audit-XX-YY.json with exact paths and source hashes. Keep test-generated bytecode/caches outside course (`-B` / PYTHONDONTWRITEBYTECODE=1).

Only edit assigned modules and your own audit file. Do not edit root manifest, other modules, shared assets, app code, gitlinks, or commits. Parent integrates final review evidence and performs source/native checks. Browser acceptance is excluded by the user's revised scope; native checks must not be described as browser acceptance.
