from solution import *

def test_01_step():
    """Create an independent zero boundary even for empty input."""
    first, second = PrefixSums([]), PrefixSums([])
    assert first.prefix == [0] and second.prefix == [0]
    assert first.prefix is not second.prefix

def test_02_complete_operation():
    """Build an independent leading-zero prefix table in one pass."""
    for values in ([], [6], [0, 0], [3, -8, 3, 5]):
        original = list(values)
        result = PrefixSums(values)
        assert result.prefix == [sum(values[:i]) for i in range(len(values) + 1)]
        assert values == original
        values.append(99)
        assert result.prefix == [sum(original[:i]) for i in range(len(original) + 1)]
    first, second = PrefixSums([2, 3]), PrefixSums([2, 3])
    first.prefix.append(100)
    assert second.prefix == [0, 2, 5]
    _technique(PrefixSums.__init__, loop=True, forbidden=('sum', 'accumulate'))
    import ast, inspect, textwrap
    assert not any(isinstance(node, ast.Slice) for node in ast.walk(ast.parse(textwrap.dedent(inspect.getsource(PrefixSums.__init__))))), "Update a running total rather than resumming slices."

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
