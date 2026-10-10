import numpy as np
from solution import *


def test_exercise_sort_grid():
    assert _uses_call("ordered_nights", "sort"), "Use np.sort for this task."
    for values in ([[7, 2, 5], [6, 9, 1]], [[8, 2], [4, 3], [1, 7]]):
        a = np.array(values)
        original = a.copy()
        assert np.array_equal(ordered_nights(a), np.sort(a, axis=1))
        assert np.array_equal(a, original)


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
