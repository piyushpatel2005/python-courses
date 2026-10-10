import numpy as np
from solution import *


def test_sine_values():
    """Compute sine values independently"""
    assert _uses_call("transform", "sin"), "Use np.sin for this task."
    for values in [([0.0, 1.5707963267948966], [1.0, 2.718281828459045]), ([3.141592653589793, -1.5707963267948966], [7.38905609893065, 2.0])]:
        angles, intensities = (np.array(v) for v in values)
        result = transform(angles, intensities)[0]
        expected = np.sin(angles)
        assert np.shape(result) == np.shape(expected), "Check the result shape."
        assert isinstance(result, np.ndarray), "Return a NumPy array."
        assert np.allclose(result, expected), "Calculate this result from the supplied readings."

def test_log_values():
    """Compute log values independently"""
    assert _uses_call("transform", "log"), "Use np.log for this task."
    for values in [([0.0, 1.5707963267948966], [1.0, 2.718281828459045]), ([3.141592653589793, -1.5707963267948966], [7.38905609893065, 2.0])]:
        angles, intensities = (np.array(v) for v in values)
        result = transform(angles, intensities)[1]
        expected = np.log(intensities)
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
