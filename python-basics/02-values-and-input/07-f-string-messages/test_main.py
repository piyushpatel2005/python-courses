from solution import *
import ast
from pathlib import Path
import solution


def test_status_line():
    """Insert the supplied values with an f-string."""
    assert solution.__file__ is not None
    tree = ast.parse(Path(solution.__file__).read_text())
    expr = next(node.value for node in tree.body if isinstance(node, ast.Assign)
                and any(isinstance(target, ast.Name) and target.id == "status_line"
                        for target in node.targets))
    names = {node.value.id for node in ast.walk(expr)
             if isinstance(node, ast.FormattedValue) and isinstance(node.value, ast.Name)}
    assert isinstance(expr, ast.JoinedStr) and {"pathfinder", "coins"} <= names, \
        "Use an f-string with pathfinder and coins in braces"
    assert getattr(solution, "status_line") == "Adam found 3 coins"
    changed = eval(compile(ast.Expression(expr), "<status_line>", "eval"),
                   {"pathfinder": "Nia", "coins": 8})
    assert changed == "Nia found 8 coins"
