from solution import add_minutes
import ast
import inspect
import io
from contextlib import redirect_stdout
import solution


def test_duration_argument():
    """The call passes the new minutes"""
    assert add_minutes(12) == 14, "Keep the supplied function: it adds 2 to its input."
    source = inspect.getsource(solution)
    tree = ast.parse(source)
    print_calls = [
        node.value for node in tree.body
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Name) and node.value.func.id == "print"
    ]
    assert any(
        isinstance(arg, ast.Call) and isinstance(arg.func, ast.Name)
        and arg.func.id == "add_minutes" and len(arg.args) == 1
        and isinstance(arg.args[0], ast.Constant) and arg.args[0].value == 12
        for call in print_calls for arg in call.args
    ), "Change the argument in the supplied print call to 12."
    output = io.StringIO()
    with redirect_stdout(output):
        exec(compile(source, "solution.py", "exec"), {})
    assert output.getvalue().strip() == "14", "Keep the print call so Run displays 14."
