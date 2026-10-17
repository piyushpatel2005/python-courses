from solution import *
import ast
from pathlib import Path
import solution


def test_route_line():
    """Join the supplied name and destination with +."""
    assert solution.__file__ is not None
    tree = ast.parse(Path(solution.__file__).read_text())
    expr = next(node.value for node in tree.body if isinstance(node, ast.Assign)
                and any(isinstance(target, ast.Name) and target.id == "route_line"
                        for target in node.targets))
    names = {node.id for node in ast.walk(expr) if isinstance(node, ast.Name)}
    assert any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add)
               for node in ast.walk(expr)) and {"pathfinder", "destination"} <= names, \
        "Join pathfinder and destination with +, including the spaces and period"
    assert getattr(solution, "route_line") == "Pathfinder Adam enters Beacon Ridge."
    changed = eval(compile(ast.Expression(expr), "<route_line>", "eval"),
                   {"pathfinder": "Nia", "destination": "River Bend"})
    assert changed == "Pathfinder Nia enters River Bend."
