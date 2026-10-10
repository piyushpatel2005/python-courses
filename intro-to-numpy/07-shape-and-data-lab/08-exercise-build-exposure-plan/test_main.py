import numpy as np
from solution import *

def test_01_hold_settings():
    assert _uses("hold_settings", "repeat"), "Use the repeat operation requested for hold_settings."
    for settings, frames in ((np.array([1, 4, 7]), 2), (np.array([9, 3]), 3)):
        assert np.array_equal(hold_settings(settings, frames), np.repeat(settings, frames))

def test_02_cycle_settings():
    assert _uses("cycle_settings", "tile"), "Use the tile operation requested for cycle_settings."
    for settings, cycles in ((np.array([1, 4, 7]), 2), (np.array([9, 3]), 3)):
        assert np.array_equal(cycle_settings(settings, cycles), np.tile(settings, cycles))


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
