"""Replay every atomic submission for modules 13–15 with CPython.

Run with InterCourses backend's Python and PYTHONPATH=.../backend/src for
real backend-loader checks. This does not claim Pyodide or application UI coverage.
Task markers in starter/reference are edit recipes; audit hashes bind each prefix.
"""
from __future__ import annotations
import ast
import contextlib
import hashlib
import io
import json
from pathlib import Path
import re
import sys
import types

ROOT = Path(__file__).resolve().parent.parent
PLAN = json.loads((ROOT / 'assets/curriculum-plan.json').read_text())
MODULES = [m for m in PLAN['modules'] if m['order'] in [13, 14, 15]]

def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def load(source: str) -> types.ModuleType:
    module = types.ModuleType('solution')
    sys.modules['solution'] = module
    exec(compile(source, '<learner>', 'exec'), module.__dict__)
    return module

def grade(source: str, tests: str) -> tuple[list[bool], list[str]]:
    load(source)
    scope: dict[str, object] = {}
    exec(compile(tests, '<checks>', 'exec'), scope)
    outcomes: list[bool] = []
    errors: list[str] = []
    for name, function in scope.items():
        if name.startswith('test_') and callable(function):
            try:
                function()
                outcomes.append(True)
                errors.append('')
            except Exception as exc:
                outcomes.append(False)
                errors.append(type(exc).__name__ + ': ' + str(exc))
    return outcomes, errors

def probe(source: str) -> str:
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        exec(compile(source, '<run-probe>', 'exec'), {'__name__': '__main__'})
    return output.getvalue().strip()

def prefix_source(starter: str, solution: str, completed: int) -> str:
    source = starter
    for i in range(1, completed + 1):
        pattern = rf'(?m)^ *# Task {i}\n[\s\S]*?^ *# End task {i}$'
        old = re.findall(pattern, source)
        new = re.findall(pattern, solution)
        assert len(old) == len(new) == 1, (i, len(old), len(new))
        source = source.replace(old[0], new[0], 1)
    return source

def definitions(source: str) -> dict[str, str]:
    return {node.name: ast.dump(node, include_attributes=False) for node in ast.parse(source).body if isinstance(node, (ast.FunctionDef, ast.ClassDef))}

def verify() -> dict[str, object]:
    report: dict[str, object] = {'runtime': sys.version, 'scope': 'CPython every prefix, supplied probes, structural and backend-loader checks; not browser acceptance', 'lessons': [], 'quizzes': [], 'continuity': [], 'diagram_conflicts': []}
    try:
        from app.content.loader import _load_lesson_dir, _load_module_quiz
        from app.companion_code_extensions import DEFAULT_COMPANION_CODE_EXTENSIONS
        loader_available = True
    except ImportError as exc:
        loader_available = False
        report['loader_unavailable'] = str(exc)
    for module in MODULES:
        previous = None
        for lesson in module['lessons']:
            relative = module['directory'] + '/' + lesson['directory']
            directory = ROOT / relative
            starter = (directory/'main.py').read_text()
            reference = (directory/'solution/main.py').read_text()
            tests = (directory/'test_main.py').read_text()
            markdown = (directory/'lesson.md').read_text()
            nodes = [n for n in ast.parse(tests).body if isinstance(n, ast.FunctionDef) and n.name.startswith('test_')]
            tasks = re.findall(r'^\d+\. ', markdown.split('## Your Tasks')[1], re.M)
            assert len(tasks) == len(nodes) >= 1, relative
            for n in nodes:
                assert not n.args.args, (relative, n.name)
            for source in [starter, reference]:
                for node in ast.walk(ast.parse(source)):
                    if isinstance(node, ast.FunctionDef):
                        assert node.returns is not None, (relative, node.name, 'return annotation')
                        assert all(a.annotation is not None for a in node.args.args if a.arg not in ['self', 'cls']), (relative, node.name, 'parameter annotation')
            row = {'path': relative, 'tasks': len(tasks), 'test_names': [n.name for n in nodes], 'hashes': {name: digest((directory/name).read_text()) for name in ['lesson.md', 'main.py', 'solution/main.py', 'test_main.py', 'files.yaml']}, 'prefixes': []}
            for k in range(len(tasks)+1):
                source = prefix_source(starter, reference, k)
                actual, errors = grade(source, tests)
                expected = [i < k for i in range(len(tasks))]
                assert actual == expected, (relative, k, actual, expected, errors)
                # Repeat each check in isolation, matching the same source.
                isolated=[]
                for n in nodes:
                    load(source); scope = {}; exec(tests, scope)
                    try:
                        scope[n.name](); isolated.append(True)
                    except Exception:
                        isolated.append(False)
                assert isolated == expected, (relative,k,'isolation')
                row['prefixes'].append({'completed': k, 'expected': expected, 'actual': actual, 'sha256': digest(source), 'stdout': probe(source), 'errors': errors})
            assert grade(reference, tests)[0] == [True]*len(tasks), relative
            row['reference_stdout'] = probe(reference)
            # Execute explanatory fences separately; they need no hidden context.
            fences = re.findall(r'```python\n(.*?)```', markdown, re.S)
            row['examples'] = [probe(s) for s in fences]
            if loader_available:
                loaded = _load_lesson_dir(directory, content_path=relative+'/lesson.md', course_slug=PLAN['slug'], module_slug=module['slug'], code_extensions=DEFAULT_COMPANION_CODE_EXTENSIONS)
                assert loaded and loaded.slug == lesson['slug'] and loaded.sort_order == lesson['order']
                assert loaded.runtime == 'pyodide' and loaded.lesson_type == 'coding'
                assert len(loaded.code_files)==1 and loaded.code_files[0].path=='main.py'
                assert loaded.solution_code_files and loaded.solution_code_files[0].path=='main.py'
                row['backend_loader'] = 'passed'
            # Preserve every preceding completed definition, except the explicit fresh directed variant.
            if previous is not None and not (module['order']==13 and lesson['order']==6):
                before = definitions(previous)
                after = definitions(starter)
                for name, old in before.items():
                    if name in ['Graph', 'DirectedGraph']:
                        old_node = next(n for n in ast.parse(previous).body if isinstance(n,ast.ClassDef) and n.name==name)
                        new_node = next(n for n in ast.parse(starter).body if isinstance(n,ast.ClassDef) and n.name==name)
                        old_methods = {n.name: ast.dump(n,include_attributes=False) for n in old_node.body if isinstance(n,ast.FunctionDef)}
                        new_methods = {n.name: ast.dump(n,include_attributes=False) for n in new_node.body if isinstance(n,ast.FunctionDef)}
                        assert all(new_methods.get(k)==v for k,v in old_methods.items()), (relative, name)
                    else:
                        assert after.get(name)==old, (relative,name,'changed preceding definition')
                report['continuity'].append({'into':relative,'prior_definitions':list(before),'passed':True})
            previous = reference
            report['lessons'].append(row)
        quizdir = ROOT/module['directory']/'quiz'
        qfiles=sorted(quizdir.glob('q*.md'))
        assert len(qfiles)==4
        if loader_available:
            quiz = _load_module_quiz(ROOT/module['directory'], 'python')
            assert quiz and len(quiz.questions)==4
        report['quizzes'].append({'module':module['directory'], 'count':len(qfiles),'hashes':{f.name:digest(f.read_text()) for f in qfiles},'backend_loader':loader_available})
    report['totals']={'lessons':len(report['lessons']), 'tasks':sum(r['tasks'] for r in report['lessons']), 'prefixes':sum(len(r['prefixes']) for r in report['lessons']), 'quiz_questions':sum(q['count'] for q in report['quizzes'])}
    return report

def algorithm_checks() -> dict[str, object]:
    """Independent small models and intentional wrong implementations."""
    import random
    rng = random.Random(131415)
    traversal_source = (ROOT/'14-graph-traversal/10-topological-order/solution/main.py').read_text()
    weighted_source = (ROOT/'15-shortest-paths/08-route-planner/solution/main.py').read_text()
    traversal = load(traversal_source)
    weighted = load(weighted_source)
    graph_cases = 0
    for size in range(1, 8):
        for trial in range(12):
            labels = [f'v{i}' for i in range(size)]
            adj = {v: [w for w in labels if rng.random() < 0.22] for v in labels}
            start = labels[trial % size]
            # Layer expansion is an independent reference for hop distance.
            distances = {start: 0}
            layer = [start]
            depth = 0
            while layer:
                following = []
                for v in layer:
                    for w in adj[v]:
                        if w not in distances:
                            distances[w] = depth + 1
                            following.append(w)
                layer = following
                depth += 1
            assert traversal.bfs_distances(adj, start) == distances
            assert traversal.bfs(adj, start) == list(distances)
            assert traversal.dfs_iterative(adj, start) == traversal.dfs_recursive(adj, start)
            assert set(traversal.dfs_iterative(adj, start)) == set(distances)
            # A topological result must obey every arrow, or agree with cycle detection.
            cyclic = traversal.directed_cycle(adj)
            try:
                order = traversal.topological_order(adj)
            except ValueError:
                assert cyclic
            else:
                assert not cyclic
                positions = {v: i for i, v in enumerate(order)}
                assert len(order) == size
                assert all(positions[v] < positions[w] for v in adj for w in adj[v])
            # Independent repeated relaxation (Bellman-Ford) checks weighted answers.
            graph = {v: [(w, rng.randrange(6)) for w in adj[v]] for v in adj}
            expected = {v: float('inf') for v in graph}
            expected[start] = 0
            for _ in range(size - 1):
                for v, edges in graph.items():
                    for w, cost in edges:
                        expected[w] = min(expected[w], expected[v] + cost)
            before = json.dumps(graph)
            for search in [weighted.dijkstra_scan, weighted.dijkstra_heap]:
                actual, parents = search(graph, start)
                assert actual == expected
                for target in labels:
                    path = weighted.reconstruct_weighted_path(actual, parents, target)
                    if expected[target] == float('inf'):
                        assert path == []
                    else:
                        assert path[0] == start and path[-1] == target
                        assert len(path) == len(set(path))
                        assert weighted.path_cost(graph, path) == expected[target]
            assert json.dumps(graph) == before
            graph_cases += 1
    # Reject invalid edges even if they are outside the reachable component.
    validation_cases = 0
    for invalid in [-1, 2.5, True, float('nan'), float('inf')]:
        for search in [weighted.dijkstra_scan, weighted.dijkstra_heap]:
            try:
                search({'s': [], 'x': [('x', invalid)]}, 's')
            except ValueError:
                validation_cases += 1
            else:
                raise AssertionError('Unreachable invalid edge was accepted')
    # A stale pop must not rescan the outgoing list; validation accounts for one scan.
    class CountedEdges(list):
        def __init__(self, values: list[tuple[str, int]]) -> None:
            super().__init__(values)
            self.scans: int = 0
        def __iter__(self):
            self.scans += 1
            return super().__iter__()
    outgoing = CountedEdges([('t', 1)])
    stale_graph = {'s': [('a', 9), ('b', 2)], 'a': outgoing, 'b': [('a', 3)], 't': []}
    weighted.dijkstra_heap(stale_graph, 's')
    assert outgoing.scans == 2, outgoing.scans
    mutants = [
        ('13-graph-models/03-add-undirected-edge', 'self.adj[b].append(a)', 'pass', 'one-way undirected insertion'),
        ('13-graph-models/07-adjacency-matrix', '[[0 for _ in labels] for _ in labels]', '[[0 for _ in labels]] * len(labels)', 'aliased matrix rows'),
        ('14-graph-traversal/02-bfs-traversal', 'frontier.popleft()', 'frontier.pop()', 'LIFO instead of BFS'),
        ('14-graph-traversal/04-bfs-path', 'path.reverse()', 'pass', 'backward path returned'),
        ('14-graph-traversal/09-directed-cycle', 'return color == 1', 'return color != 0', 'finished vertex treated as cycle'),
        ('14-graph-traversal/10-topological-order', 'counts[neighbor] -= 1', 'counts[neighbor] += 1', 'dependency counts increase'),
        ('15-shortest-paths/03-relax-edge', 'distance + weight', 'distance + 1', 'hop count instead of weighted cost'),
        ('15-shortest-paths/05-dijkstra-heap', 'return queued_distance != current_distance', 'return False', 'stale entries accepted'),
        ('15-shortest-paths/06-reconstruct-weighted-path', 'path.reverse()', 'pass', 'weighted route reversed'),
        ('15-shortest-paths/07-unreachable-and-zero-weights', 'return distance != inf', 'return bool(distance) and distance != inf', 'zero treated as unreachable'),
    ]
    mutant_results = []
    for relative, old, new, label in mutants:
        directory = ROOT/relative
        source = (directory/'solution/main.py').read_text()
        assert old in source
        source = source.replace(old,new,1)
        outcomes, errors = grade(source, (directory/'test_main.py').read_text())
        assert not all(outcomes), (relative,label)
        mutant_results.append({'path':relative,'mutation':label,'actual':outcomes,'rejected':True})
    return {'deterministic_random_graphs':graph_cases,'invalid_weight_rejections':validation_cases,'stale_outgoing_scans_including_validation':outgoing.scans,'mutants':mutant_results}

if __name__ == '__main__':
    result=verify()
    result['algorithm_checks']=algorithm_checks()
    result['diagram_conflicts']=[{'lesson':'14-graph-traversal/07-dfs-iterative','file':'graph-traversal-dfs-iterative-trace.svg','status':'left unchanged and unreferenced','reason':'Figure uses eager mark-on-push vertex stack with parent(C)=A; lesson uses iterator frames exactly matching recursive discovery, so C is discovered through D in the shown square. Parent should replace the figure with active iterator frames and their remaining-neighbor positions.'}]
    placements=json.loads((ROOT/'assets/diagrams/placements-extra-11-15.json').read_text())
    result['diagram_review']=[{'lesson':p['lesson'],'file':p['file'],'sha256':digest((ROOT/p['lesson']/p['file']).read_text()),'referenced':p['file'] in (ROOT/p['lesson']/'lesson.md').read_text()} for p in placements if p['lesson'][:2] in ['13','14','15']]
    result['diagram_visual_review']='Four rendered contact sheets inspected; compatible traces referenced with explicit list-order captions. SVG and Excalidraw files not edited.'
    (ROOT/'assets/audit-13-15.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['totals'],indent=2))
