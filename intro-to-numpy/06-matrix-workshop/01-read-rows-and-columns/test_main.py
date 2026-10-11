import numpy as np
from solution import *


def test_read_rows_and_columns():
    assert _uses("sensor_history", "slice"), "Use the slice operation requested for sensor_history."
    assert np.array_equal(sensor_history, grid[:, 1]) and sensor_history.shape == (grid.shape[0],)
    v = _variant({'grid': 'np.array([[11, 6, 3], [2, 15, 7], [8, 4, 9]])'})
    assert np.array_equal(v["sensor_history"], v["grid"][:, 1])


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


def _variant(fixtures):
    import ast
    import contextlib
    import io
    import solution
    with open(solution.__file__, encoding="utf-8") as source_file:
        tree = ast.parse(source_file.read())
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name in fixtures:
                node.value = ast.parse(fixtures[name], mode="eval").body
    ast.fix_missing_locations(tree)
    values = {}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(tree, "<changed supplied data>", "exec"), values)
    return values
