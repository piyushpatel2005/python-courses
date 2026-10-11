import numpy as np
from solution import *


def test_night_totals():
    """Compute night totals independently"""
    assert _uses_call("panel_basics", "sum"), "Use np.sum for this task."
    for values in [[[4, 6, 2], [8, 3, 7]], [[3, 1], [5, 9], [7, 2]]]:
        grid = np.array(values)
        result = panel_basics(grid)[0]
        expected = np.sum(grid, axis=1)
        assert np.shape(result) == np.shape(expected), "Check the result shape."
        assert isinstance(result, np.ndarray), "Return a NumPy array."
        assert np.allclose(result, expected), "Calculate this result from the supplied readings."

def test_sensor_means():
    """Compute sensor means independently"""
    assert _uses_call("panel_basics", "mean"), "Use np.mean for this task."
    for values in [[[4, 6, 2], [8, 3, 7]], [[3, 1], [5, 9], [7, 2]]]:
        grid = np.array(values)
        result = panel_basics(grid)[1]
        expected = np.mean(grid, axis=0)
        assert np.shape(result) == np.shape(expected), "Check the result shape."
        assert isinstance(result, np.ndarray), "Return a NumPy array."
        assert np.allclose(result, expected), "Calculate this result from the supplied readings."


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
