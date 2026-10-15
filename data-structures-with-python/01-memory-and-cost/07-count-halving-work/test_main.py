from solution import *

def test_01_step():
    """Reject a negative count before starting the loop."""
    for bad in (-1, -7):
        try:
            halving_trace(bad)
            assert False, "Raise ValueError for a negative count."
        except ValueError:
            pass

def test_02_step():
    """Record the starting size before any reduction."""
    for n in (2, 3, 17):
        sizes, count = halving_trace(n)
        assert sizes and sizes[0] == n

def test_03_complete_operation():
    """Record each actual halving until at most one remains."""
    for n in range(65):
        sizes = []
        remaining = n
        while remaining > 1:
            sizes.append(remaining)
            remaining //= 2
        assert halving_trace(n) == (sizes, len(sizes))
    try:
        halving_trace(-1)
        assert False, "Reject a negative region size."
    except ValueError:
        pass
    _technique(halving_trace, loop=True, forbidden=('log', 'log2', 'bit_length'))

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
