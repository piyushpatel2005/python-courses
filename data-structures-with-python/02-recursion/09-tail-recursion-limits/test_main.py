from solution import *

def test_01_step():
    """Reject invalid n before performing the algorithm."""
    for n in (-1, 101):
        try:
            tail_sum(n)
            assert False, "Reject n outside 0 through 100."
        except ValueError:
            pass
    for n in (1.5, True):
        try:
            tail_sum(n)
            assert False, "Use the supplied integer validation."
        except TypeError:
            pass

def test_02_step():
    """Preserve the caller's accumulator at the base case."""
    for initial in (0, 7, -3):
        assert tail_sum(0, initial) == initial

def test_03_complete_operation():
    """Carry completed work into the final recursive call."""
    for n in (0, 1, 5, 31, 100):
        for initial in (0, 8, -4):
            assert tail_sum(n, initial) == initial + n * (n + 1) // 2
    for n in (-1, 101):
        try:
            tail_sum(n)
            assert False
        except ValueError:
            pass
    _technique(tail_sum, recursive=True)
    import ast, inspect, textwrap
    tree = ast.parse(textwrap.dedent(inspect.getsource(tail_sum)))
    assert any(isinstance(node, ast.Return) and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == 'tail_sum' for node in ast.walk(tree)), "Return the recursive call directly in the tail case."

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
