from solution import *

def test_01_step():
    """Reject a negative size in the requested report."""
    for sizes in ([-1], [2, -3]):
        try:
            growth_report(sizes)
            assert False
        except ValueError:
            pass

def test_02_step():
    """Count actual visits for each report row."""
    sizes = [0, 1, 5, 11, 5]
    rows = growth_report(sizes)
    assert [(r[0], r[1]) for r in rows] == [(n, n) for n in sizes]

def test_03_step():
    """Count every distinct pair for each report row."""
    sizes = [0, 1, 4, 9]
    assert [row[2] for row in growth_report(sizes)] == [n * (n - 1) // 2 for n in sizes]

def test_04_complete_operation():
    """Compare measured visits, pairs, and halving reductions."""
    sizes = [0, 1, 2, 7, 14, 7, 31]
    expected = []
    for n in sizes:
        rest, halves = n, 0
        while rest > 1:
            halves += 1
            rest //= 2
        expected.append((n, n, n * (n - 1) // 2, halves))
    assert growth_report(sizes) == expected
    assert growth_report([]) == []
    try:
        growth_report([3, -1])
        assert False, "Reject negative sizes."
    except ValueError:
        pass
    _technique(growth_report, loop=True, forbidden=('log2', 'bit_length'))
    import ast, inspect, textwrap
    tree = ast.parse(textwrap.dedent(inspect.getsource(growth_report)))
    loops = [node for node in ast.walk(tree) if isinstance(node, (ast.For, ast.While))]
    assert len(loops) >= 4, "Execute the report loop, nested pair work, and halving; visits may share the outer pair loop."

def _technique(function, *, loop=False, recursive=False, forbidden=()):
    import ast
    import inspect
    import textwrap
    tree = ast.parse(textwrap.dedent(inspect.getsource(function)))
    if loop:
        assert any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree)), "Use the requested loop to perform the work."
    if recursive:
        definitions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        assert any(any(isinstance(call, ast.Call) and isinstance(call.func, ast.Name) and call.func.id == definition.name for call in ast.walk(definition)) for definition in definitions), "Use a recursive call for the smaller problem."
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else getattr(node.func, 'attr', '')
            assert name not in forbidden, "Implement this operation rather than delegating to " + name
