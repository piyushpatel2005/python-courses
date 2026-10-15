from solution import *

def test_01_step():
    """Return None before reading an empty interval."""
    for target in (-2, 0, 7):
        assert binary_search_recursive([], target) is None

def test_02_step():
    """Return a matching midpoint without searching another half."""
    for values in ([9], [2, 5, 8], [-4, 0, 3, 8, 11]):
        mid = len(values) // 2
        result = binary_search_recursive(values, values[mid])
        assert result is not None and values[result] == values[mid]

def test_03_step():
    """Keep the lower half when the target is smaller."""
    for values in ([1, 4, 8], [-5, -2, 0, 9, 12, 16, 20]):
        assert binary_search_recursive(values, values[0]) == 0

def test_04_complete_operation():
    """Search sorted intervals, including duplicates and empty bounds."""
    for values in ([], [4], [1, 1, 1], [-3, 0, 0, 2, 8], list(range(0, 128, 2))):
        before = list(values)
        for target in range(-5, 131):
            result = binary_search_recursive(values, target)
            if target in values:
                assert type(result) is int and 0 <= result < len(values)
                assert values[result] == target
            else:
                assert result is None
            assert values == before
    class Counted(list):
        def __init__(self, data):
            super().__init__(data)
            self.reads = 0
        def __getitem__(self, index):
            assert not isinstance(index, slice), "Keep index bounds rather than slicing."
            self.reads += 1
            return super().__getitem__(index)
    data = Counted(range(128))
    assert binary_search_recursive(data, 127) == 127
    assert data.reads <= 16, "Discard half the candidate interval on each miss."
    _technique(binary_search_recursive, recursive=True, forbidden=('sorted', 'sort', 'index', 'bisect', 'bisect_left', 'bisect_right'))

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
