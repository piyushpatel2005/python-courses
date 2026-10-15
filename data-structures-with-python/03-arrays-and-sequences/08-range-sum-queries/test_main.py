from solution import *

def test_01_step():
    """Reject invalid boundaries before reading the prefix table."""
    for values in ([], [2, 5, 8]):
        report = PrefixSums(values)
        before = list(report.prefix)
        for start, stop in ((-1, 0), (0, len(values) + 1), (1, 0)):
            try:
                report.range_sum(start, stop)
                assert False
            except ValueError:
                pass
            assert report.prefix == before

def test_02_complete_operation():
    """Answer all valid half-open ranges without scanning or mutation."""
    for values in ([], [4], [2, -5, 7, 7, 0]):
        report = PrefixSums(values)
        before = list(report.prefix)
        for start in range(len(values) + 1):
            for stop in range(start, len(values) + 1):
                assert report.range_sum(start, stop) == sum(values[start:stop])
                assert report.prefix == before
        for start, stop in ((-1, 0), (0, len(values) + 1), (1, 0)):
            try:
                report.range_sum(start, stop)
                assert False
            except ValueError:
                pass
            assert report.prefix == before
    class Counted(list):
        def __init__(self, values):
            super().__init__(values)
            self.reads = 0
        def __getitem__(self, index):
            assert not isinstance(index, slice)
            self.reads += 1
            return super().__getitem__(index)
    report = PrefixSums(list(range(30)))
    report.prefix = Counted(report.prefix)
    assert report.range_sum(4, 28) == sum(range(4, 28))
    assert report.prefix.reads <= 2, "Use the two stored boundary totals."
    _technique(PrefixSums.range_sum, forbidden=('sum',))

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
