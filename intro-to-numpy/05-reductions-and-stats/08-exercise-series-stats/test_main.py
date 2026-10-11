import numpy as np
from solution import *


def test_mean():
    """Compute mean independently"""
    assert _uses_call("describe", "mean"), "Use np.mean for this task."
    for values in [[40.0, 44.0, 48.0], [2.0, 3.0, 3.0, 12.0], [5.0, 5.0, 5.0]]:
        readings = np.array(values)
        result = describe(readings)[0]
        expected = np.mean(readings)
        assert np.shape(result) == np.shape(expected), "Check the result shape."
        assert np.allclose(result, expected), "Calculate this result from the supplied readings."

def test_median():
    """Compute median independently"""
    assert _uses_call("describe", "median"), "Use np.median for this task."
    for values in [[40.0, 44.0, 48.0], [2.0, 3.0, 3.0, 12.0], [5.0, 5.0, 5.0]]:
        readings = np.array(values)
        result = describe(readings)[1]
        expected = np.median(readings)
        assert np.shape(result) == np.shape(expected), "Check the result shape."
        assert np.allclose(result, expected), "Calculate this result from the supplied readings."

def test_variance():
    """Compute variance independently"""
    assert _uses_call("describe", "var"), "Use np.var for this task."
    for values in [[40.0, 44.0, 48.0], [2.0, 3.0, 3.0, 12.0], [5.0, 5.0, 5.0]]:
        readings = np.array(values)
        result = describe(readings)[2]
        expected = np.var(readings)
        assert np.shape(result) == np.shape(expected), "Check the result shape."
        assert np.allclose(result, expected), "Calculate this result from the supplied readings."

def test_std():
    """Compute std independently"""
    assert _uses_call("describe", "std"), "Use np.std for this task."
    for values in [[40.0, 44.0, 48.0], [2.0, 3.0, 3.0, 12.0], [5.0, 5.0, 5.0]]:
        readings = np.array(values)
        result = describe(readings)[3]
        expected = np.std(readings)
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
