import numpy as np
from solution import *

def test_01_column_scan():
    assert _uses("column_scan", "ravel"), "Use the ravel operation requested for column_scan."
    for grid in (np.arange(6).reshape(2, 3), np.arange(12).reshape(4, 3)):
        assert np.array_equal(column_scan(grid), grid.T.ravel())

def test_02_check_storage():
    assert _uses("audit_scans", "shares_memory"), "Use the shares_memory operation requested for audit_scans."
    for grid in (np.arange(6).reshape(2, 3), np.arange(12).reshape(3, 4).T):
        row, col = grid.ravel(), grid.T.ravel()
        assert audit_scans(grid) == (np.shares_memory(grid, row), np.shares_memory(grid, col))


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
