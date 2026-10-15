from solution import *

def test_01_step():
    """Reject invalid n before performing the algorithm."""
    for n in (-1, 13):
        try:
            fibonacci_tree(n)
            assert False, "Reject n outside 0 through 12."
        except ValueError:
            pass
    for n in (1.5, True):
        try:
            fibonacci_tree(n)
            assert False, "Use the supplied integer validation."
        except TypeError:
            pass

def test_02_step():
    """Return both direct Fibonacci bases with one call each."""
    assert fibonacci_tree(0) == (0, 1)
    assert fibonacci_tree(1) == (1, 1)

def test_03_complete_operation():
    """Count both recursive subtrees, including their base calls."""
    values = [0, 1]
    calls = [1, 1]
    for n in range(2, 13):
        values.append(values[-1] + values[-2])
        calls.append(1 + calls[-1] + calls[-2])
    for n in range(13):
        assert fibonacci_tree(n) == (values[n], calls[n])
    for n in (-1, 13):
        try:
            fibonacci_tree(n)
            assert False
        except ValueError:
            pass
    _technique(fibonacci_tree, recursive=True)

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
