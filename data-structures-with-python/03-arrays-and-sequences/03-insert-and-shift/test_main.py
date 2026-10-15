from solution import *

def test_01_step():
    """Reject invalid indices without changing the array."""
    for values in ([], [5, 8, 13]):
        array = Array(values)
        for index in (-1, len(values) + 1, len(values) + 2):
            before = (list(array._data), array.size, array.capacity)
            try:
                array.insert(index, 99)
                assert False, "Reject the index."
            except IndexError:
                pass
            assert (list(array._data), array.size, array.capacity) == before

def test_02_step():
    """Preserve the suffix while opening an insertion gap."""
    for index in (0, 1, 2):
        array = Array([3, 7, 11])
        old = array.snapshot()
        try:
            array.insert(index, 99)
        except NotImplementedError:
            pass
        assert array._data[index + 1:len(old) + 1] == old[index:]

def test_03_step():
    """Place the exact payload in the insertion gap."""
    array = Array([3, 7, 11])
    payload = []
    try:
        array.insert(1, payload)
    except NotImplementedError:
        pass
    assert array._data[1] is payload

def test_04_complete_operation():
    """Open a gap safely at the front, middle, or end."""
    for initial in ([], [None], [1, 2, 2, 4]):
        for index in range(len(initial) + 1):
            array = Array(initial)
            value = []
            expected = list(initial)
            expected.insert(index, value)
            assert array.insert(index, value) is None
            assert array.snapshot() == expected and array.get(index) is value
            assert array.size == len(expected) and len(array._data) == array.capacity
            assert all(x is None for x in array._data[array.size:])
    array = Array([1, 2, 3])
    array.append(4)
    storage = array._data
    array.insert(2, 9)
    assert array._data is storage and array.snapshot() == [1, 2, 9, 3, 4]
    for index in (-1, array.size + 1):
        before = (array.snapshot(), array.size, array.capacity)
        try:
            array.insert(index, 0)
            assert False
        except IndexError:
            pass
        assert (array.snapshot(), array.size, array.capacity) == before
    _technique(Array.insert, loop=True, forbidden=('insert', 'append', 'extend', 'sorted', 'sort'))
    import ast, inspect, textwrap
    assert not any(isinstance(n, ast.Slice) for n in ast.walk(ast.parse(textwrap.dedent(inspect.getsource(Array.insert))))), "Use indexed shifts, not slicing."

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
            if (isinstance(node.func, ast.Attribute)
                    and isinstance(node.func.value, ast.Name)
                    and node.func.value.id == 'self'
                    and name == 'append'):
                continue  # Delegating an end insertion to the completed method is valid.
            assert name not in forbidden, "Implement this operation rather than delegating to " + name

