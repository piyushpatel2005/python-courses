import ast
import inspect
import solution
from solution import signal_strength

def test_beacon_call():
    """The local module function is called with three marks"""
    assert signal_strength(3) == 15
    tree = ast.parse(inspect.getsource(solution))
    assert any(
        isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Name) and node.value.func.id == "print"
        and len(node.value.args) == 1
        and isinstance(node.value.args[0], ast.Call)
        and isinstance(node.value.args[0].func, ast.Name)
        and node.value.args[0].func.id == "signal_strength"
        and len(node.value.args[0].args) == 1
        and isinstance(node.value.args[0].args[0], ast.Constant)
        and node.value.args[0].args[0].value == 3
        and eval(compile(ast.Expression(node.value.args[0]), "<beacon call>", "eval"), {"signal_strength": signal_strength}) == 15
        for node in tree.body
    ), "Print the result of signal_strength(3), not a comment or literal."
