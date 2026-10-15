from solution import *

def test_01_step():
    """Reject invalid n before performing the algorithm."""
    for n in (-1, 101):
        try:
            fibonacci_memo(n)
            assert False, "Reject n outside 0 through 100."
        except ValueError:
            pass
    for n in (1.5, True):
        try:
            fibonacci_memo(n)
            assert False, "Use the supplied integer validation."
        except TypeError:
            pass

def test_02_step():
    """Compute Fibonacci values before optimizing repeated work."""
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    for n, value in enumerate(expected):
        assert fibonacci_memo(n)[0] == value

def test_03_complete_operation():
    """Reuse cached answers within a call, not across separate calls."""
    a, b = 0, 1
    for n in range(31):
        expected_misses = 1 if n < 2 else n + 1
        assert fibonacci_memo(n) == (a, expected_misses)
        a, b = b, a + b
    assert fibonacci_memo(8) == (21, 9)
    assert fibonacci_memo(2) == (1, 3)
    assert fibonacci_memo(8) == (21, 9)
    for n in (-1, 101):
        try:
            fibonacci_memo(n)
            assert False
        except ValueError:
            pass
    _technique(fibonacci_memo, recursive=True)
    import sys
    count = 0
    def profile(frame, event, arg):
        nonlocal count
        if event == 'call' and frame.f_code.co_filename == fibonacci_memo.__code__.co_filename:
            count += 1
    old = sys.getprofile()
    try:
        sys.setprofile(profile)
        assert fibonacci_memo(12) == (144, 13)
    finally:
        sys.setprofile(old)
    assert count < 100, "Actually reuse cached results rather than recomputing the tree."

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
