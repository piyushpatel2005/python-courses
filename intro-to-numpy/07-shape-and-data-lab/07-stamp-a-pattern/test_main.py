import numpy as np
from solution import *

def test_01_repeat_each_exposure():
    assert _uses("held", "repeat"), "Use the repeat operation requested for held."
    assert np.array_equal(held, [2, 2, 2, 5, 5, 5])
    v = _variant({'exposures': 'np.array([8, 1, 7])'})
    assert np.array_equal(v["held"], np.repeat(v["exposures"], 3))


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
