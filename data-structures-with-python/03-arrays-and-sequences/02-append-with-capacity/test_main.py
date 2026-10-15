from solution import *

def test_01_step():
    """Ensure one spare slot before the new value is written."""
    array = Array([4, 7])
    try:
        array.append(9)
    except NotImplementedError:
        pass
    assert array.capacity == 4 and array._data[:2] == [4, 7]
    spare = Array()
    try:
        spare.append(9)
    except NotImplementedError:
        pass
    assert spare.capacity == 1

def test_02_step():
    """Write the exact payload into the next unused slot."""
    array = Array()
    payload = []
    try:
        array.append(payload)
    except NotImplementedError:
        pass
    assert array._data[0] is payload

def test_03_complete_operation():
    """Append into spare space or grow once without losing references."""
    array = Array()
    model = []
    capacity = 1
    other = Array(["untouched"])
    for value in [None, 5, 5, [], 9, 0, -2, 8, 11]:
        old_storage = array._data
        was_full = len(model) == capacity
        if was_full:
            capacity *= 2
        assert array.append(value) is None
        model.append(value)
        assert array.snapshot() == model and array.size == len(model)
        assert array.capacity == capacity and len(array._data) == capacity
        assert array.get(array.size - 1) is value
        if not was_full:
            assert array._data is old_storage
        assert all(item is None for item in array._data[array.size:])
    assert other.snapshot() == ["untouched"]
    _technique(Array.append, forbidden=('append', 'insert', 'extend'))

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
