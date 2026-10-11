import ast
import inspect
import textwrap
from solution import signal_total

def test_signal_total():
    """A shrinking recursive call sums the signals"""
    assert signal_total([]) == 0
    assert signal_total([4]) == 4
    assert signal_total([2, 3, 1]) == 6
    assert signal_total([7, 1, 5]) == 13
    tree = ast.parse(textwrap.dedent(inspect.getsource(signal_total)))
    def is_first(node):
        return (isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name)
                and node.value.id == "signals" and isinstance(node.slice, ast.Constant)
                and node.slice.value == 0)
    def is_rest_call(node):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == "signal_total" and len(node.args) == 1):
            return False
        rest = node.args[0]
        return (isinstance(rest, ast.Subscript) and isinstance(rest.value, ast.Name)
                and rest.value.id == "signals" and isinstance(rest.slice, ast.Slice)
                and isinstance(rest.slice.lower, ast.Constant) and rest.slice.lower.value == 1
                and rest.slice.upper is None)
    assert any(isinstance(n, ast.Return) and isinstance(n.value, ast.BinOp)
               and isinstance(n.value.op, ast.Add) and is_first(n.value.left)
               and is_rest_call(n.value.right) for n in ast.walk(tree)), (
        "Return the first signal plus a recursive call on signals[1:].")
