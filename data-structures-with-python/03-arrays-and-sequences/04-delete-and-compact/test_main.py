from solution import *

def test_01_step():
    """Reject invalid indices without changing the array."""
    for values in ([], [5, 8, 13]):
        array = Array(values)
        for index in (-1, len(values) + 0, len(values) + 2):
            before = (list(array._data), array.size, array.capacity)
            try:
                array.delete(index)
                assert False, "Reject the index."
            except IndexError:
                pass
            assert (list(array._data), array.size, array.capacity) == before

def test_02_step():
    """Close the gap while preserving all remaining references."""
    for index in (0, 1, 2):
        array = Array([3, 7, 11, 19])
        expected = array.snapshot()
        expected.pop(index)
        try:
            array.delete(index)
        except NotImplementedError:
            pass
        assert array._data[:len(expected)] == expected

def test_03_step():
    """Reduce the occupied count by exactly one."""
    array = Array([3, 7, 11, 19])
    try:
        array.delete(1)
    except NotImplementedError:
        pass
    assert array.size == 3

def test_04_step():
    """Release the reference in the newly unused tail slot."""
    array = Array([3, 7, 11, 19])
    try:
        array.delete(1)
    except NotImplementedError:
        pass
    assert array._data[3] is None

def test_05_complete_operation():
    """Remove a valid item, close its gap, and clear the spare slot."""
    for initial in ([None], [1, 2, 2, 4], [[], [], []]):
        for index in range(len(initial)):
            array = Array(initial)
            storage, capacity = array._data, array.capacity
            expected = list(initial)
            removed = expected.pop(index)
            assert array.delete(index) is removed
            assert array.snapshot() == expected and array.size == len(expected)
            assert array._data is storage and array.capacity == capacity
            assert all(item is None for item in array._data[array.size:])
    array = Array([3, 1, 3])
    while array.size:
        array.delete(0)
    assert array.snapshot() == [] and array._data == [None] * array.capacity
    for index in (-1, 0, 1):
        before = (list(array._data), array.size, array.capacity)
        try:
            array.delete(index)
            assert False
        except IndexError:
            pass
        assert (list(array._data), array.size, array.capacity) == before
    array.append(8)
    assert array.snapshot() == [8]
    _technique(Array.delete, loop=True, forbidden=('pop', 'remove', 'insert', 'append'))
    import ast, inspect, textwrap
    assert not any(isinstance(n, ast.Slice) for n in ast.walk(ast.parse(textwrap.dedent(inspect.getsource(Array.delete))))), "Compact with indexed assignments."

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

