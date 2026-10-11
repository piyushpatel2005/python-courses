import numpy as np
from solution import *


def test_total():
    """Compute total independently"""
    assert _uses_call("extremes", "sum"), "Use np.sum for this task."
    for values in [[9, 3, 14, 6], [21, 4, 4, 12, 30], [7, 7, 1, 7], [-2, -9, -1]]:
        readings = np.array(values)
        result = extremes(readings)[0]
        expected = np.sum(readings)
        assert np.shape(result) == np.shape(expected), "Check the result shape."
        assert np.allclose(result, expected), "Calculate this result from the supplied readings."

def test_minimum():
    """Compute minimum independently"""
    assert _uses_call("extremes", "min"), "Use np.min for this task."
    for values in [[9, 3, 14, 6], [21, 4, 4, 12, 30], [7, 7, 1, 7], [-2, -9, -1]]:
        readings = np.array(values)
        result = extremes(readings)[1]
        expected = np.min(readings)
        assert np.shape(result) == np.shape(expected), "Check the result shape."
        assert np.allclose(result, expected), "Calculate this result from the supplied readings."

def test_maximum():
    """Compute maximum independently"""
    assert _uses_call("extremes", "max"), "Use np.max for this task."
    for values in [[9, 3, 14, 6], [21, 4, 4, 12, 30], [7, 7, 1, 7], [-2, -9, -1]]:
        readings = np.array(values)
        result = extremes(readings)[2]
        expected = np.max(readings)
        assert np.shape(result) == np.shape(expected), "Check the result shape."
        assert np.allclose(result, expected), "Calculate this result from the supplied readings."

def test_min_index():
    """Compute min index independently"""
    assert _uses_call("extremes", "argmin"), "Use np.argmin for this task."
    for values in [[9, 3, 14, 6], [21, 4, 4, 12, 30], [7, 7, 1, 7], [-2, -9, -1]]:
        readings = np.array(values)
        result = extremes(readings)[3]
        expected = np.argmin(readings)
        assert np.shape(result) == np.shape(expected), "Check the result shape."
        assert np.allclose(result, expected), "Calculate this result from the supplied readings."

def test_max_index():
    """Compute max index independently"""
    assert _uses_call("extremes", "argmax"), "Use np.argmax for this task."
    for values in [[9, 3, 14, 6], [21, 4, 4, 12, 30], [7, 7, 1, 7], [-2, -9, -1]]:
        readings = np.array(values)
        result = extremes(readings)[4]
        expected = np.argmax(readings)
        assert np.shape(result) == np.shape(expected), "Check the result shape."
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
