import numpy as np
from solution import *


def test_exercise_transform_grid():
    assert _uses("transform_panel", "matrix"), "Use the matrix operation requested for transform_panel."
    for a, b in [([[2, 3, 5], [7, 1, 4]], [[1, 2], [0, 1], [2, 0]]), ([[3, 8], [4, 1], [5, 7]], [[2, 1, 0], [1, 0, 3]])]:
        left, right = np.array(a), np.array(b)
        assert np.array_equal(transform_panel(left, right), left @ right)
        assert transform_panel(left, right).shape == (left.shape[0], right.shape[1])


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
