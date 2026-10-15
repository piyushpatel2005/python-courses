from solution import *

def test_01_step():
    """Collect matching index pairs in nested-loop order."""
    for values in ([], [4], [1, 2], [3, 3, 3], [8, 1, 8, 1]):
        expected = [(i, j) for i in range(len(values)) for j in range(i + 1, len(values)) if values[i] == values[j]]
        assert pair_matches(values)[0] == expected

def test_02_complete_operation():
    """Visit each distinct index pair once and count misses too."""
    for values in ([], [4], [1, 2], [3, 3, 3], [8, 1, 8, 1]):
        expected = [(i, j) for i in range(len(values)) for j in range(i + 1, len(values)) if values[i] == values[j]]
        before = list(values)
        assert pair_matches(values) == (expected, len(values) * (len(values) - 1) // 2)
        assert values == before
    class Item:
        calls = 0
        def __eq__(self, other):
            Item.calls += 1
            return False
    assert pair_matches([Item() for _ in range(5)]) == ([], 10)
    assert Item.calls == 10, "Perform one equality check per pair."
    _technique(pair_matches, loop=True, forbidden=('dict', 'set', 'sorted', 'sort'))

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
