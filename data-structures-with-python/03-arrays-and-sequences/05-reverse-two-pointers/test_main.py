from solution import *

def test_01_step():
    """Swap the first unmatched endpoint pair in place."""
    for original in ([2, 9], [3, 5, 7, 11]):
        values = list(original)
        assert reverse_in_place(values) is values
        assert values[0] == original[-1] and values[-1] == original[0]

def test_02_complete_operation():
    """Swap inward pairs in place, including odd and empty inputs."""
    for original in ([], [1], [2, 2], [1, 2, 3], [-4, 0, 7, 7, 9, 2]):
        values = list(original)
        assert reverse_in_place(values) is values
        assert values == original[::-1]
        assert reverse_in_place(values) is values and values == original
    _technique(reverse_in_place, loop=True, forbidden=('reverse', 'reversed', 'sorted', 'sort', 'list'))
    import ast, inspect, textwrap
    tree = ast.parse(textwrap.dedent(inspect.getsource(reverse_in_place)))
    assert not any(isinstance(node, (ast.Slice, ast.ListComp)) for node in ast.walk(tree)), "Use swaps rather than a copied sequence."

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
