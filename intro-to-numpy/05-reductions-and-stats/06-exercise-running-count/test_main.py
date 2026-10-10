import numpy as np
from solution import *


def test_exercise_running_count():
    assert _uses_call("running_count", "cumsum"), "Use np.cumsum for this task."
    for values in ([2, 5, 1], [8, 0, 3, 6]):
        assert np.array_equal(running_count(np.array(values)), np.cumsum(values))


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
