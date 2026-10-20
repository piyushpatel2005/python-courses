import ast
import inspect
import textwrap
from solution import delivery_total


def test_delivery_total():
    """A shrinking recursive call sums the daily counts."""
    assert delivery_total([]) == 0
    assert delivery_total([4]) == 4
    assert delivery_total([2, 3, 1]) == 6
    assert delivery_total([7, 1, 5]) == 13
    tree = ast.parse(textwrap.dedent(inspect.getsource(delivery_total)))

    def is_first(node):
        return (isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name)
                and node.value.id == "daily_deliveries" and isinstance(node.slice, ast.Constant)
                and node.slice.value == 0)

    def is_rest_call(node):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == "delivery_total" and len(node.args) == 1):
            return False
        rest = node.args[0]
        return (isinstance(rest, ast.Subscript) and isinstance(rest.value, ast.Name)
                and rest.value.id == "daily_deliveries" and isinstance(rest.slice, ast.Slice)
                and isinstance(rest.slice.lower, ast.Constant) and rest.slice.lower.value == 1
                and rest.slice.upper is None)

    assert any(isinstance(n, ast.Return) and isinstance(n.value, ast.BinOp)
               and isinstance(n.value.op, ast.Add) and is_first(n.value.left)
               and is_rest_call(n.value.right) for n in ast.walk(tree)), (
        "Return the first count plus a recursive call on daily_deliveries[1:].")
