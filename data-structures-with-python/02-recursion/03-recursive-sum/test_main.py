from solution import *

def test_01_step():
    """Reject a list beyond the exercise's safe recursive length."""
    for size in (101, 120):
        try:
            recursive_sum([1] * size)
            assert False
        except ValueError:
            pass

def test_02_step():
    """Give the empty suffix its direct sum of zero."""
    assert recursive_sum([]) == 0

def test_03_complete_operation():
    """Sum by advancing an index without copying suffixes."""
    for values in ([], [0], [-3], [4, -2, 4], list(range(100))):
        before = list(values)
        assert recursive_sum(values) == sum(values)
        assert values == before
    try:
        recursive_sum([1] * 101)
        assert False
    except ValueError:
        pass
    _technique(recursive_sum, recursive=True, forbidden=('sum',))
    import ast, inspect, textwrap
    tree = ast.parse(textwrap.dedent(inspect.getsource(recursive_sum)))
    assert not any(isinstance(node, ast.Slice) for node in ast.walk(tree)), "Use a boundary index instead of slicing."

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
