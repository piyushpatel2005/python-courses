import numpy as np
from solution import *

def test_01_export_csv():
    assert _uses("save_grid", "savetxt"), "Use the savetxt operation requested for save_grid."
    for grid in (np.array([[6, 9], [2, 4]]), np.array([[11, 7, 3]])):
        text = save_grid(grid)
        assert text.endswith("\n")
        lines = text.strip().splitlines()
        assert len(lines) == grid.shape[0]
        assert [list(map(int, line.split(","))) for line in lines] == grid.tolist()

def test_02_import_csv():
    assert _uses("read_grid", "genfromtxt"), "Use the genfromtxt operation requested for read_grid."
    for text, expected in (("6,9\n2,4\n", [[6, 9], [2, 4]]), ("11,7,3\n", [[11, 7, 3]])):
        result = read_grid(text)
        assert result.dtype.kind in "iu" and result.shape == np.array(expected).shape
        assert np.array_equal(result, expected)
    for text, expected in (("-4\n7\n", [[-4], [7]]), ("12\n", [[12]]), (" 2, -3\n\n4, 0\n", [[2, -3], [4, 0]])):
        result = read_grid(text)
        assert result.dtype.kind in "iu" and result.shape == np.array(expected).shape
        assert np.array_equal(result, expected)


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
