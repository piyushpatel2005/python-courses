from solution import *
import pandas as pd

def test_label_window():
    _uses('loc', 'label_window')
    """Labels include stop and retain named columns"""
    for names, start, stop in [(["dawn", "noon", "night"], "dawn", "noon"), (["a", "b", "c", "d"], "b", "d")]:
        frame = pd.DataFrame({"item": list(names), "count": range(len(names)), "dock": ["X"] * len(names)}, index=names)
        pd.testing.assert_frame_equal(label_window(frame, start, stop), frame.loc[start:stop, ["item", "count"]])

def test_position_window():
    _uses('iloc', 'position_window')
    """Positions exclude stop even with nonnumeric labels"""
    for start, stop in [(1, 3), (0, 2)]:
        frame = pd.DataFrame({"item": ["A", "B", "C", "D"], "count": [1, 2, 3, 4], "dock": ["W"] * 4}, index=["z", "a", "r", "p"])
        pd.testing.assert_frame_equal(position_window(frame, start, stop), frame.iloc[start:stop, :2])

def _uses(attribute, function=None):
    import ast
    from pathlib import Path
    import solution
    tree = ast.parse(Path(solution.__file__).read_text())
    if function:
        tree = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == function)
    assert any(isinstance(n, ast.Attribute) and n.attr == attribute for n in ast.walk(tree)), "Use " + attribute + " for this task, rather than a fixed answer."
