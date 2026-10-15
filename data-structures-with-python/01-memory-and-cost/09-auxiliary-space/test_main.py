from solution import *

def test_01_step():
    """Initialize both extremes from a real reading, not zero."""
    for value in (-6, 4, 12):
        assert extremes(iter([value])) == (value, value)
    assert extremes(iter([])) is None

def test_02_step():
    """Keep the smallest reading seen so far."""
    for values in ([8, 3, 6], [-2, -9, -4], [7, 7, 1]):
        assert extremes(iter(values))[0] == min(values)

def test_03_complete_operation():
    """Summarize one traversal without copying or sorting readings."""
    for values in ([], [6], [3, 8], [-8, -2, -5], [0, 0], [5, -4, 5, 1]):
        expected = (min(values), max(values)) if values else None
        assert extremes(iter(values)) == expected
        before = list(values)
        assert extremes(values) == expected and values == before
    _technique(extremes, loop=True, forbidden=('list', 'sorted', 'sort', 'min', 'max', 'append', 'extend', 'dict', 'set'))
    import ast, inspect, textwrap
    tree = ast.parse(textwrap.dedent(inspect.getsource(extremes)))
    assert not any(isinstance(node, (ast.ListComp, ast.DictComp, ast.SetComp, ast.Slice)) for node in ast.walk(tree)), "Keep only the extrema instead of copying or collecting the input."

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
