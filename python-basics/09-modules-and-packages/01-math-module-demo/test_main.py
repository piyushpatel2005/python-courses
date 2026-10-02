import ast
import inspect
import solution
from solution import beacons_needed

def test_beacon_call():
    """The revised call uses eleven sparks"""
    assert beacons_needed(11) == 3
    tree = ast.parse(inspect.getsource(solution))
    assert any(
        isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Name) and node.value.func.id == "print"
        and len(node.value.args) == 1
        and isinstance(node.value.args[0], ast.Call)
        and isinstance(node.value.args[0].func, ast.Name)
        and node.value.args[0].func.id == "beacons_needed"
        and len(node.value.args[0].args) == 1
        and isinstance(node.value.args[0].args[0], ast.Constant)
        and node.value.args[0].args[0].value == 11
        and eval(compile(ast.Expression(node.value.args[0]), "<beacon call>", "eval"), {"beacons_needed": beacons_needed}) == 3
        for node in tree.body
    ), "Print the result of beacons_needed(11), not a comment or literal."
