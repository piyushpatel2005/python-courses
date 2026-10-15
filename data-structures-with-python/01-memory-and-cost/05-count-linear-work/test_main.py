from solution import *

def test_01_step():
    """Accumulate the total inside the supplied loop."""
    for values in ([], [6], [-5, 2, 6], [3, 3]):
        result = sum_with_work(iter(values))
        assert result[0] == sum(values)

def test_02_complete_operation():
    """Sum every value and count each loop visit."""
    for values in ([], [0], [-4], [2, 2, -1], list(range(17))):
        before = list(values)
        assert sum_with_work(values) == (sum(values), len(values))
        assert values == before
    class Stream:
        def __iter__(self):
            yield 5
            yield -2
    assert sum_with_work(Stream()) == (3, 2)
    _technique(sum_with_work, loop=True, forbidden=('sum', 'len'))

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
