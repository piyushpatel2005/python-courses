from solution import ability_label
import ast
import inspect
import io
from contextlib import redirect_stdout
import solution


def test_default_label():
    """An omitted mark uses a period"""
    try:
        default = ability_label("Flare")
    except TypeError:
        raise AssertionError('Give mark the default value "." in the function definition.') from None
    assert default == "Flare.", "Return name + mark so the default period appears."
    assert ability_label("Pulse", "?") == "Pulse?", "Use the supplied mark rather than a fixed ending."


def test_keyword_call():
    """The second call uses a named override"""
    source = inspect.getsource(solution)
    tree = ast.parse(source)
    prints = [
        node.value for node in tree.body
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Name) and node.value.func.id == "print"
    ]
    assert len(prints) >= 2, "Keep both supplied print calls."
    assert any(
        isinstance(call, ast.Call) and isinstance(call.func, ast.Name)
        and call.func.id == "ability_label"
        and any(keyword.arg == "mark" and isinstance(keyword.value, ast.Constant)
                and keyword.value.value == "!" for keyword in call.keywords)
        for call in prints[1].args
    ), 'Pass mark="!" by name in the second print call.'
    output = io.StringIO()
    with redirect_stdout(output):
        exec(compile(source, "solution.py", "exec"), {})
    lines = output.getvalue().strip().splitlines()
    assert len(lines) >= 2 and lines[1] == "Pulse!", "The second call should print Pulse!."
