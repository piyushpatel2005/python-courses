import numpy as np
from solution import *


def test_exercise_transpose():
    assert _uses("rounds_first", "transpose"), "Use the transpose operation requested for rounds_first."
    for values in ([[2, 5, 8], [4, 7, 1]], [[1, 4], [7, 2], [5, 9]]):
        a = np.array(values)
        assert np.array_equal(rounds_first(a), a.T)
        assert rounds_first(a).shape == (a.shape[1], a.shape[0])


# Inspect only the learner outcome named by a task, not unrelated supplied code.
def _uses(name, technique):
    import ast
    import solution
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    nodes = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            nodes.append(node)
        elif isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            nodes.append(node.value)
    for root in nodes:
        for node in ast.walk(root):
            if technique == "slice" and isinstance(node, ast.Subscript) and any(isinstance(n, ast.Slice) for n in ast.walk(node.slice)):
                return True
            if technique == "matrix" and isinstance(node, ast.MatMult):
                return True
            if isinstance(node, ast.Attribute):
                allowed = {"transpose": {"T", "transpose"}, "matrix": {"matmul", "dot"}}
                if node.attr in allowed.get(technique, {technique}):
                    return True
    return False
