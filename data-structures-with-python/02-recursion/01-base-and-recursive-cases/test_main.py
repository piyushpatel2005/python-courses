from solution import *

def test_01_step():
    """Reject invalid n before performing the algorithm."""
    for n in (-1, 101):
        try:
            steps_to_zero(n)
            assert False, "Reject n outside 0 through 100."
        except ValueError:
            pass
    for n in (1.5, True):
        try:
            steps_to_zero(n)
            assert False, "Use the supplied integer validation."
        except TypeError:
            pass

def test_02_step():
    """Return zero directly for the empty reduction problem."""
    assert steps_to_zero(0) == 0

def test_03_complete_operation():
    """Reduce the argument to zero and return through the calls."""
    for n in (0, 1, 2, 7, 32, 100):
        assert steps_to_zero(n) == n
    for n in (-1, 101):
        try:
            steps_to_zero(n)
            assert False, "Reject arguments outside 0 through 100."
        except ValueError:
            pass
    try:
        steps_to_zero(1.5)
        assert False
    except TypeError:
        pass
    _technique(steps_to_zero, recursive=True)

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
