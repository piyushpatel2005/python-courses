import ast
import inspect
import solution
from solution import boxes_needed

def test_boxes_call():
    """Print the calculation for an eleven-metre row."""
    assert boxes_needed(11) == 3
    tree = ast.parse(inspect.getsource(solution))
    assert any(
        isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Name) and node.value.func.id == "print"
        and len(node.value.args) == 1
        and isinstance(node.value.args[0], ast.Call)
        and isinstance(node.value.args[0].func, ast.Name)
        and node.value.args[0].func.id == "boxes_needed"
        and len(node.value.args[0].args) == 1
        and isinstance(node.value.args[0].args[0], ast.Constant)
        and node.value.args[0].args[0].value == 11
        for node in tree.body
    ), "Print boxes_needed(11), not a fixed answer."
