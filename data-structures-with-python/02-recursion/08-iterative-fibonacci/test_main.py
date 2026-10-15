from solution import *

def test_01_step():
    """Reject invalid n before performing the algorithm."""
    for n in (-1, 101):
        try:
            fibonacci_loop(n)
            assert False, "Reject n outside 0 through 100."
        except ValueError:
            pass
    for n in (1.5, True):
        try:
            fibonacci_loop(n)
            assert False, "Use the supplied integer validation."
        except TypeError:
            pass

def test_02_step():
    """Advance the two values to the requested Fibonacci index."""
    a, b = 0, 1
    for n in range(20):
        assert fibonacci_loop(n)[0] == a
        a, b = b, a + b

def test_03_complete_operation():
    """Advance adjacent Fibonacci values without overwriting needed state."""
    a, b = 0, 1
    for n in range(101):
        assert fibonacci_loop(n) == (a, n)
        a, b = b, a + b
    for n in (-1, 101):
        try:
            fibonacci_loop(n)
            assert False
        except ValueError:
            pass
    _technique(fibonacci_loop, loop=True)
    import ast, inspect, textwrap
    tree = ast.parse(textwrap.dedent(inspect.getsource(fibonacci_loop)))
    assert not any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'fibonacci_loop' for node in ast.walk(tree)), "Use iteration in this variation."

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
