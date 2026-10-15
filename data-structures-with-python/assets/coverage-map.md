# Curriculum coverage and publication scope

Maintainer document. The user outline is preserved in `source-outline.md`; `curriculum-plan.json` fixes the ordered 210-lesson inventory. `diagram-plan.json` covers the first 40 illustrations and `additional-diagram-plan.json` adds 142 operation-specific figures. Each illustrated lesson receives an SVG and a native editable `.excalidraw` companion.

## Minimum outline coverage

| Requested area | Planned modules | Implementation and transfer practice |
| --- | --- | --- |
| Memory, algorithm cost, iterative/recursive approaches | 01–03 | References, shallow/nested copying, counted work, auxiliary space, amortized append, recursion frames, array shifts and prefix sums |
| Singly linked lists | 04 | Node links, state, traversal, prepend, append, find, insertion, head/tail/interior deletion, reversal, playlist |
| Doubly linked, circular, skip lists | 05 | Bidirectional links and history, one-lap ring traversal/removal, multi-level predecessor search/insert/remove and expected-cost caveats |
| Stack | 06 | State, push/peek/pop, brackets, postfix expressions, undo and minimum tracking |
| Queue and deque | 07 | Linked queue, peek, ring buffer, deque ends, round-robin and monotonic-window application |
| Hash table | 08 | Hashing, collision buckets, chained map operations, load factor, rehashing, open addressing and tombstones |
| Linear/binary search | 02 and 09 | Recursive and iterative search, missing/duplicate boundaries, lower/upper bounds, insertion and comparison counts |
| Bubble/selection/insertion/merge/quick sort | 10 | Separate elementary passes and complete algorithms, merges and partitions, stability and explicit mutation contracts |
| Trees and BST | 11 | Node structure, size/height, all depth-first orders, level order, search/insert/minimum, three deletion cases and validation |
| Heaps and heap sort | 12 | Array mapping, ordering, sift up/down, push/pop, bottom-up construction, min/max policy, heap sort |
| Priority queues | 12 | Stable ties, priority changes, streaming top-k and scheduling |
| Recursion | 02 | Base cases, tracing, factorial, Fibonacci, memoization, iterative alternatives, tail-call limitations, recursive binary search |
| Graph representations and operations | 13 | Adjacency lists/matrix, vertices/edges, directedness, removal and degree |
| BFS and DFS | 14 | Frontier/visited invariants, distances/paths, components, both DFS forms, cycle detection and topological ordering |
| Weighted graphs and Dijkstra | 15 | Weight representation, path cost, relaxation, scan/heap implementations, predecessors, unreachable/zero-weight cases, route planner |
| Bit manipulation and sets | 16 | Bit tests/updates/counts, masks, powers of two, set algebra, frozen keys and permissions |
| Trie | 17 | Node, insert, exact lookup, prefix lookup, collection, deletion, counts and autocomplete |
| Fenwick tree | 18 | Lowbit, state, update, prefix/range query and construction |
| Segment tree | 18 | Interval layout, build, query, point update, minimum aggregation and range reporting |
| Disjoint-set union | 19 | State, roots, union, compression, union by size, counts, redundant edges and minimum spanning forest |
| Additional reference concepts | 20 | Cartesian product, power sets, combinations, permutations, repetition distinctions and pruning |
| Integrated application | 21 | A dispatch workbench combines lookup, queue/priority order, history, reachability, routes and range totals |

## Prerequisite decisions

Recursion appears before recursive sorting and tree traversal. The early recursive binary-search exercise explains its sorted-halving premise locally; the dedicated search module later expands its boundaries and duplicate handling. Sets/dictionaries may be used as familiar Python tools before their implementation or deeper cost model is taught. Heaps and priorities precede Dijkstra; graph traversal and weighted edges precede Kruskal. Bit operations precede Fenwick lowbit. Every implementation remains self-contained in a single editable file.

## Diagram density

Most structure operations receive their own before/after or step trace. Peek illustrates a returned value with unchanged structure. Insert/remove scenes identify both retained and changed links, with explicit empty/singleton boundary cases where relevant. Array, tree, heap, graph and range figures show actual indices, values or frontiers rather than generic process boxes. The excluded lessons mostly reuse a recently explained mechanism or combine already-illustrated operations; the exclusions are deliberate, not missing assets.

## Runtime and publishing

The source is authored for InterCourses' browser Python execution and explicitly selects `runtime: pyodide`. All learner code is standard-library-only with readable type hints. Native checks are an early gate; final acceptance must use the actual application runner and Submit callback in browser Workers and compare both real content loaders.

This sibling source repository is not the application's separately checked-out content submodule. Preview using `CONTENT_DIR` pointed at `python-courses`. Publication, gitlinks, progress IDs, and deployment are not modified as part of authoring. Leave changes uncommitted for review.
