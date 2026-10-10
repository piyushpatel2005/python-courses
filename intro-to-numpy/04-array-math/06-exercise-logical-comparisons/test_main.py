from solution import *
import numpy as np

def test_window():
    """Return a boolean mask with inclusive bounds"""
    assert np.array_equal(in_window(np.array([1, 4, 7, 10]), 4, 7), [False, True, True, False])
    assert np.array_equal(in_window(np.array([8, 3, 6]), 5, 8), [True, False, True])
    result = in_window(np.array([3, 4, 5, 7, 8]), 4, 7)
    assert isinstance(result, np.ndarray) and result.dtype.kind == "b", "Return a boolean NumPy mask."
    assert np.array_equal(result, [False, True, True, True, False])
    assert np.array_equal(in_window(np.array([4, 5, 6]), 5, 5), [False, True, False])

def test_matches_window():
    assert _uses_call("matches_window", "array_equal"), "Use np.array_equal for this task."
    """Compare the entire boolean array and its shape"""
    readings = np.array([1, 4, 7, 10])
    assert matches_window(readings, np.array([False, True, True, False]), 4, 7) is True
    assert matches_window(readings, np.array([False, True, False, False]), 4, 7) is False
    assert matches_window(readings, np.array([[False, True, True, False]]), 4, 7) is False
    assert matches_window(np.array([8, 3, 6]), np.array([True, False, True]), 5, 8) is True


def _source_tree():
    import ast
    import solution as submitted
    with open(submitted.__file__, encoding="utf-8") as source:
        return ast.parse(source.read())


def _uses_call(function_name, method):
    import ast
    function = next(node for node in _source_tree().body
                    if isinstance(node, ast.FunctionDef) and node.name == function_name)
    return any(isinstance(node, ast.Call) and
               ((isinstance(node.func, ast.Attribute) and node.func.attr == method) or
                (isinstance(node.func, ast.Name) and node.func.id == method))
               for node in ast.walk(function))
