import numpy as np
from solution import *

def test_01_shape_sky():
    assert _uses("make_sky_grid", "reshape"), "Use the reshape operation requested for make_sky_grid."
    for strip in (np.arange(6) + 3, np.arange(12) + 1):
        before = strip.copy()
        old_shape = strip.shape
        grid = make_sky_grid(strip)
        assert strip.shape == old_shape and np.array_equal(strip, before)
        assert grid.shape == (strip.size // 3, 3) and np.array_equal(grid.ravel(), strip)

def test_02_column_settings():
    assert _uses("exposure_column", "newaxis"), "Use the newaxis operation requested for exposure_column."
    for settings in (np.array([2, 5]), np.array([1, 4, 8])):
        result = exposure_column(settings)
        assert result.shape == (settings.size, 1)
        assert np.array_equal(result[:, 0], settings)


def test_03_hold_rows():
    assert _uses("hold_exposures", "repeat"), "Use the repeat operation requested for hold_exposures."
    for column in (np.array([[2], [5]]), np.array([[1], [4], [8]])):
        result = hold_exposures(column)
        assert np.array_equal(result, np.repeat(column, 2, axis=0))
        assert result.shape == (column.shape[0] * 2, 1)


def test_04_schedule_exposures():
    assert _uses("exposure_schedule", "tile"), "Use the tile operation requested for exposure_schedule."
    for settings in (np.array([2, 5]), np.array([1, 4, 8])):
        result = exposure_schedule(settings)
        expected = np.tile(np.repeat(settings[:, np.newaxis], 2, axis=0), (1, 2))
        assert np.array_equal(result, expected) and result.shape == (settings.size * 2, 2)

def test_05_export_sky():
    assert _uses("export_sky", "savetxt"), "Use the savetxt operation requested for export_sky."
    for grid in (np.array([[3, 6, 9], [2, 5, 8]]), np.array([[7, 1, 4]])):
        text = export_sky(grid)
        assert text.endswith("\n")
        assert [list(map(int, row.split(","))) for row in text.strip().splitlines()] == grid.tolist()

def test_06_import_sky():
    assert _uses("import_sky", "genfromtxt"), "Use the genfromtxt operation requested for import_sky."
    for text, expected in (("3,6,9\n2,5,8\n", [[3, 6, 9], [2, 5, 8]]), ("7,1,4\n", [[7, 1, 4]])):
        result = import_sky(text)
        assert result.dtype.kind in "iu" and np.array_equal(result, expected)
        assert result.shape == np.array(expected).shape
    for text, expected in (("-4\n7\n", [[-4], [7]]), ("12\n", [[12]]), (" 2, -3\n\n4, 0\n", [[2, -3], [4, 0]])):
        result = import_sky(text)
        assert result.dtype.kind in "iu" and result.shape == np.array(expected).shape
        assert np.array_equal(result, expected)

def test_07_observation_report():
    assert _uses("observation_report", "mean"), "Use the mean operation requested for observation_report."
    for grid, expected in ((np.array([[3, 6, 9], [2, 5, 8]]), "Rows: 2; brightest: 9; row means: 6.0, 5.0"), (np.array([[1, 2, 3]]), "Rows: 1; brightest: 3; row means: 2.0")):
        assert observation_report(grid) == expected


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
