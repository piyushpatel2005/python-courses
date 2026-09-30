from solution import *
import solution as _solution

import ast as _ast
from pathlib import Path as _Path

def _source_tree():
    return _ast.parse(_Path(_solution.__file__).read_text())

def _assignment(name):
    for node in _source_tree().body:
        if isinstance(node, _ast.Assign) and any(isinstance(t, _ast.Name) and t.id == name for t in node.targets):
            return node.value
    raise AssertionError(f"Assign a value to {name}")

def _uses_name(node, name):
    return any(isinstance(part, _ast.Name) and part.id == name for part in _ast.walk(node))

def _output():
    from contextlib import redirect_stdout
    from io import StringIO
    from pathlib import Path
    output = StringIO()
    with redirect_stdout(output):
        exec(compile(Path(_solution.__file__).read_text(), _solution.__file__, "exec"), {})
    return output.getvalue().strip().splitlines()

def test_price_label():
    """Show the updated price to two decimal places"""
    assert price == 3.75 and _output() == ["Bread: $3.75"] and any(isinstance(n, _ast.JoinedStr) and _uses_name(n, "price") and any(isinstance(part, _ast.FormattedValue) and part.format_spec is not None for part in _ast.walk(n)) for n in _ast.walk(_source_tree())), "Change only price to 3.75"
