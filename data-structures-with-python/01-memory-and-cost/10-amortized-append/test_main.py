from solution import *

def test_01_step():
    """Reject a negative count before starting the loop."""
    for bad in (-1, -7):
        try:
            append_costs(bad)
            assert False, "Raise ValueError for a negative count."
        except ValueError:
            pass

def test_02_complete_operation():
    """Charge existing-element copies only when capacity grows."""
    assert append_costs(0) == ([], 0)
    expected_costs = [1, 2, 3, 1, 5, 1, 1, 1, 9, 1, 1, 1, 1, 1, 1, 1, 17]
    for n in range(1, 18):
        capacity = 1
        while capacity < n:
            capacity *= 2
        assert append_costs(n) == (expected_costs[:n], capacity)
    assert append_costs(3)[0] is not append_costs(3)[0]
    try:
        append_costs(-1)
        assert False, "Reject negative append counts."
    except ValueError:
        pass
    _technique(append_costs, loop=True)

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
