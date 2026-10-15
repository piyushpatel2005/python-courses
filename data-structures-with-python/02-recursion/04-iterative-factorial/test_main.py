from solution import *

def test_01_step():
    """Reject invalid n before performing the algorithm."""
    for n in (-1, 101):
        try:
            factorial_loop(n)
            assert False, "Reject n outside 0 through 100."
        except ValueError:
            pass
    for n in (1.5, True):
        try:
            factorial_loop(n)
            assert False, "Use the supplied integer validation."
        except TypeError:
            pass

def test_02_step():
    """Accumulate the factorial product across the supplied factors."""
    import math
    for n in (0, 1, 2, 5, 9):
        assert factorial_loop(n)[0] == math.factorial(n)

def test_03_complete_operation():
    """Multiply every factor from one through n and count the work."""
    import math
    for n in (0, 1, 2, 4, 7, 15, 100):
        assert factorial_loop(n) == (math.factorial(n), n)
    for n in (-1, 101):
        try:
            factorial_loop(n)
            assert False
        except ValueError:
            pass
    _technique(factorial_loop, loop=True, forbidden=('factorial', 'prod'))

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
