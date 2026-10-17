from solution import *
import ast
from pathlib import Path
import solution


def test_pack_line():
    """Fill percent placeholders from the name and count."""
    assert solution.__file__ is not None
    tree = ast.parse(Path(solution.__file__).read_text())
    expr = next(node.value for node in tree.body if isinstance(node, ast.Assign)
                and any(isinstance(target, ast.Name) and target.id == "pack_line"
                        for target in node.targets))
    assert isinstance(expr, ast.BinOp) and isinstance(expr.op, ast.Mod), \
        "Use a percent-formatted string with %s and %d"
    assert isinstance(expr.left, ast.Constant) and isinstance(expr.left.value, str) \
        and "%s" in expr.left.value and "%d" in expr.left.value
    assert isinstance(expr.right, ast.Tuple) and [node.id for node in expr.right.elts
        if isinstance(node, ast.Name)] == ["pathfinder", "lanterns"], \
        "Supply pathfinder and lanterns in that order"
    assert getattr(solution, "pack_line") == "Adam carries 3 lanterns"
    changed = eval(compile(ast.Expression(expr), "<pack_line>", "eval"),
                   {"pathfinder": "Nia", "lanterns": 8})
    assert changed == "Nia carries 8 lanterns"
