import numpy as np
from solution import *

def test_01_column_offsets():
    assert _uses("as_column", "newaxis"), "Use the newaxis operation requested for as_column."
    for offsets in (np.array([1, 3, 5, 7]), np.array([8, 2])):
        result = as_column(offsets)
        assert result.shape == (len(offsets), 1) and np.array_equal(result[:, 0], offsets)

def test_02_row_ticks():
    assert _uses("as_row", "newaxis"), "Use the newaxis operation requested for as_row."
    for ticks in (np.array([0, 10, 20]), np.array([6, 9])):
        result = as_row(ticks)
        assert result.shape == (1, len(ticks)) and np.array_equal(result[0], ticks)


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
