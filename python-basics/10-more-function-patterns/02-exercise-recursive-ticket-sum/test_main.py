import ast
import inspect
import textwrap
from solution import bundle_total

def test_bundle_total():
    assert bundle_total([]) == 0
    assert bundle_total([4]) == 4
    assert bundle_total([2, 3, 1]) == 6
    tree = ast.parse(textwrap.dedent(inspect.getsource(bundle_total)))
    assert any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "bundle_total" for n in ast.walk(tree)), "Use a recursive call on the shorter list."
