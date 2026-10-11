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

def test_01_positioned_value():
    """Use iloc to select row position 1 and column position 1."""
    assert any(isinstance(node, ast.Attribute) and node.attr == "iloc" for node in ast.walk(_tree())), "Use iloc for the positional lookup."
    assert chosen == 11
    changed = _rerun("table", 'pd.DataFrame({"stall": ["soap", "rice"], "sold": [31, 17]}, index=[20, 10])')
    assert changed["chosen"] == 17
