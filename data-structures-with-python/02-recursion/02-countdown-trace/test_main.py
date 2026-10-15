from solution import *

def test_01_step():
    """Reject invalid n before performing the algorithm."""
    for n in (-1, 101):
        try:
            countdown_trace(n)
            assert False, "Reject n outside 0 through 100."
        except ValueError:
            pass
    for n in (1.5, True):
        try:
            countdown_trace(n)
            assert False, "Use the supplied integer validation."
        except TypeError:
            pass

def test_02_step():
    """Visit every smaller argument down to zero."""
    for n in (1, 4, 7):
        entries = [value for label, value in countdown_trace(n) if label == 'enter']
        assert entries == list(range(n, -1, -1))

def test_03_complete_operation():
    """Record entries downward and leaves while calls return."""
    for n in (0, 1, 4, 12):
        expected = [("enter", k) for k in range(n, -1, -1)]
        expected += [("leave", k) for k in range(n + 1)]
        assert countdown_trace(n) == expected
    a = countdown_trace(2)
    a.append(("extra", 0))
    assert len(countdown_trace(2)) == 6
    for n in (-1, 101):
        try:
            countdown_trace(n)
            assert False
        except ValueError:
            pass
    _technique(countdown_trace, recursive=True)

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
