import numpy as np
from solution import *

def test_01_unroll_rows():
    assert _uses("unroll_counts", "ravel"), "Use the ravel operation requested for unroll_counts."
    for grid in (np.array([[3, 1], [4, 2]]), np.arange(12).reshape(3, 4)):
        result = unroll_counts(grid)
        assert result.shape == (grid.size,) and np.array_equal(result, grid.ravel())

def test_02_pack_four_columns():
    assert _uses("pack_counts", "reshape"), "Use the reshape operation requested for pack_counts."
    for values in (np.arange(8), np.arange(12) + 9):
        result = pack_counts(values)
        assert result.shape == (values.size // 4, 4)
        assert np.array_equal(result.ravel(), values)


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
