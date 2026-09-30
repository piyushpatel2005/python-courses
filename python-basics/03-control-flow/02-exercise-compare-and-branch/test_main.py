import ast
from pathlib import Path
import solution as s

def test_low_stock_comparison():
    assert s.low_stock is True, "Compare copies_left with 3 to compute low_stock"
    tree = ast.parse(Path(s.__file__).read_text())
    assert any(isinstance(n, ast.Compare) for n in ast.walk(tree)), "Use a comparison for low_stock"

def test_sign_for_each_stock_level():
    source = Path(s.__file__).read_text()
    tree = ast.parse(source)
    assert any(isinstance(n, ast.If) and n.orelse and isinstance(n.orelse[0], ast.If) and n.orelse[0].orelse for n in tree.body), "Use if, elif, and else"
    for quantity, expected in ((0, "Unavailable"), (2, "Almost gone"), (7, "Available")):
        variant = ast.parse(source)
        variant.body[0].value = ast.Constant(value=quantity)
        scope = {}
        exec(compile(ast.fix_missing_locations(variant), "variant.py", "exec"), scope)
        assert scope.get("sign") == expected, f"For {quantity} copies choose {expected}"
