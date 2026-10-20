import ast
import inspect
import solution
from solution import shipping_cost

def test_shipping_call():
    """Print the shipping cost for three kilograms."""
    assert shipping_cost(3) == 15
    tree = ast.parse(inspect.getsource(solution))
    assert any(
        isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Name) and node.value.func.id == "print"
        and len(node.value.args) == 1
        and isinstance(node.value.args[0], ast.Call)
        and isinstance(node.value.args[0].func, ast.Name)
        and node.value.args[0].func.id == "shipping_cost"
        and len(node.value.args[0].args) == 1
        and isinstance(node.value.args[0].args[0], ast.Constant)
        and node.value.args[0].args[0].value == 3
        for node in tree.body
    ), "Print shipping_cost(3), not a fixed answer."
