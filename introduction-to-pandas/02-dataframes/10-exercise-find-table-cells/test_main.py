from solution import *
import pandas as pd

import ast
from pathlib import Path
import solution as submitted

def _tree():
    return ast.parse(Path(submitted.__file__).read_text())

def _uses_attribute(function, attribute):
    nodes = [node for node in _tree().body if isinstance(node, ast.FunctionDef) and node.name == function]
    assert nodes and any(isinstance(node, ast.Attribute) and node.attr == attribute for node in ast.walk(nodes[0])), f"Use {attribute} inside {function}."


def test_01_labeled_cell():
    """Use loc with the supplied row and column labels."""
    _uses_attribute("labeled_cell", "loc")
    for table in [pd.DataFrame({"sold": [5, 8], "cost": [2, 3]}, index=["am", "pm"]), pd.DataFrame({"cost": [4, 9], "sold": [13, 7]}, index=[20, 10])]:
        for row in table.index:
            for column in table.columns:
                assert labeled_cell(table, row, column) == table.loc[row, column]

def test_02_positioned_cell():
    """Use iloc with the supplied row and column positions."""
    _uses_attribute("positioned_cell", "iloc")
    table = pd.DataFrame({"sold": [5, 8], "cost": [2, 3]}, index=[20, 10])
    for row in range(2):
        for column in range(2):
            assert positioned_cell(table, row, column) == table.iloc[row, column]
