from solution import *
import ast
from pathlib import Path
import solution


def test_beacon_line():
    """Fill named places using .format()."""
    assert solution.__file__ is not None
    tree = ast.parse(Path(solution.__file__).read_text())
    expr = next(node.value for node in tree.body if isinstance(node, ast.Assign)
                and any(isinstance(target, ast.Name) and target.id == "beacon_line"
                        for target in node.targets))
    assert isinstance(expr, ast.Call) and isinstance(expr.func, ast.Attribute) \
        and expr.func.attr == "format", "Use the string's .format() method"
    assert isinstance(expr.func.value, ast.Constant) and isinstance(expr.func.value.value, str) \
        and "{beacon}" in expr.func.value.value and "{count}" in expr.func.value.value
    assert {kw.arg: kw.value.id for kw in expr.keywords if isinstance(kw.value, ast.Name)} \
        == {"beacon": "beacon", "count": "lamps"}, \
        "Pass beacon and lamps as named values"
    assert getattr(solution, "beacon_line") == "Beacon Ridge holds 4 lanterns"
    changed = eval(compile(ast.Expression(expr), "<beacon_line>", "eval"),
                   {"beacon": "River Bend", "lamps": 8})
    assert changed == "River Bend holds 8 lanterns"
