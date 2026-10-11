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

def test_01_preview():
    """Use head(3) to keep the first three rows and all columns."""
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "head" for node in ast.walk(_tree())), "Use head for the preview."
    pd.testing.assert_frame_equal(preview, sales.head(3))
    changed = _rerun("sales", 'pd.DataFrame({"stall": ["fig", "pear", "soap", "rice"], "sold": [17, 2, 0, 1]}, index=[8, 3, 5, 2])')
    pd.testing.assert_frame_equal(changed["preview"], changed["sales"].head(3))
