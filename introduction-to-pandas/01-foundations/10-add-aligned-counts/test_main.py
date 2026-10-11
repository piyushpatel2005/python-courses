from solution import *
import pandas as pd

import ast
from pathlib import Path
import solution as submitted

def _tree():
    return ast.parse(Path(submitted.__file__).read_text())


def _rerun(name, expression):
    tree = _tree()
    found = False
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
            node.value = ast.parse(expression, mode="eval").body
            found = True
            break
    assert found, f"Keep the supplied {name} assignment."
    namespace = {}
    exec(compile(ast.fix_missing_locations(tree), str(submitted.__file__), "exec"), namespace)
    return namespace

def test_01_north_afternoon():
    """Change afternoon north to 5 and keep label-aligned addition."""
    pd.testing.assert_series_equal(morning, pd.Series([4, 7], index=["north", "south"]))
    pd.testing.assert_series_equal(afternoon, pd.Series([3, 5], index=["south", "north"]))
    pd.testing.assert_series_equal(total, morning + afternoon)
    changed = _rerun("morning", 'pd.Series([11, 2], index=["north", "south"])')
    pd.testing.assert_series_equal(changed["total"], changed["morning"] + changed["afternoon"])
