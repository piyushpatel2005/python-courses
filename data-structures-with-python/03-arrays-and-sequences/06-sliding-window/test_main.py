from solution import *

def test_01_step():
    """Reject zero, negative, and oversized window widths."""
    for values, width in (([], 1), ([2], 0), ([2], -1), ([2, 3], 3)):
        try:
            max_window_sum(values, width)
            assert False
        except ValueError:
            pass

def test_02_step():
    """Initialize the total from the first complete window."""
    for values in ([8], [3, -7, 2], [-8, -2, -4]):
        assert max_window_sum(values, len(values)) == sum(values)

def test_03_complete_operation():
    """Find the best full-width window, including negative totals."""
    for values in ([5], [-8, -2, -6], [2, 2, 2, 2], [4, -7, 9, 0, 3, -2]):
        before = list(values)
        for width in range(1, len(values) + 1):
            expected = max(sum(values[i:i + width]) for i in range(len(values) - width + 1))
            assert max_window_sum(values, width) == expected
        assert values == before
    for values, width in (([], 1), ([1], 0), ([1, 2], 3), ([1], -1)):
        try:
            max_window_sum(values, width)
            assert False
        except ValueError:
            pass
    class Counted(list):
        def __init__(self, values):
            super().__init__(values)
            self.reads = 0
        def __getitem__(self, index):
            assert not isinstance(index, slice), "Slide by indexed outgoing and incoming values."
            self.reads += 1
            return super().__getitem__(index)
    values = Counted(range(40))
    assert max_window_sum(values, 20) == sum(range(20, 40))
    assert values.reads <= 3 * len(values), "Do not rescan every window."
    _technique(max_window_sum, loop=True, forbidden=('sum',))

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
