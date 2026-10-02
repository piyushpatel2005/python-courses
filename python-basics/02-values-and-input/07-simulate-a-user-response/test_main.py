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

def test_pathfinder():
    """Display the new prefilled pathfinder response"""
    assert pathfinder == "Ari" and _output() == ["Gear ready for Ari"] and any(isinstance(n, _ast.JoinedStr) and _uses_name(n, "pathfinder") for n in _ast.walk(_source_tree())), "Set pathfinder to Ari"
