import numpy as np
from solution import *


def test_round_totals():
    """Compute round totals independently"""
    assert _uses_call("totals", "sum"), "Use np.sum for this task."
    for values in [[[4, 8, 2], [6, 3, 7]], [[2, 7], [8, 1], [4, 6]]]:
        scores = np.array(values)
        result = totals(scores)[0]
        expected = np.sum(scores, axis=0)
        assert np.shape(result) == np.shape(expected), "Check the result shape."
        assert isinstance(result, np.ndarray), "Return a NumPy array."
        assert np.allclose(result, expected), "Calculate this result from the supplied readings."

def test_player_totals():
    """Compute player totals independently"""
    assert _uses_call("totals", "sum"), "Use np.sum for this task."
    for values in [[[4, 8, 2], [6, 3, 7]], [[2, 7], [8, 1], [4, 6]]]:
        scores = np.array(values)
        result = totals(scores)[1]
        expected = np.sum(scores, axis=1)
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
