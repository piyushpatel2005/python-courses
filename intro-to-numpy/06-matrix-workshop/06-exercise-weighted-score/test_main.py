import numpy as np
from solution import *


def test_exercise_weighted_score():
    assert _uses("weighted_score", "dot"), "Use the dot operation requested for weighted_score."
    for scores, weights in [([5, 2, 4], [2, 3, 1]), ([3, 8], [4, 2])]:
        assert np.ndim(weighted_score(np.array(scores), np.array(weights))) == 0
        assert weighted_score(np.array(scores), np.array(weights)) == np.dot(scores, weights)


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
