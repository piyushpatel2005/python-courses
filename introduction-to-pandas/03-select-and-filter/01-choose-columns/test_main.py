from solution import *
import pandas as pd

def test_card_columns():
    """Card keeps stall and zone in the requested order"""
    pd.testing.assert_frame_equal(result, roster[["stall", "zone"]])
    changed = _rerun_with_fixture('roster', 'pd.DataFrame({"fee": [31, 42, 9], "zone": ["north", "south", "west"], "stall": ["Pine", "Ash", "Elm"]}, index=["r9", "r2", "r8"])')
    pd.testing.assert_frame_equal(changed["result"], changed["roster"][["stall", "zone"]])


def _rerun_with_fixture(name, expression):
    # Run the submitted source, replacing only its supplied input fixture.
    import ast
    import contextlib
    import io
    from pathlib import Path
    import solution
    tree = ast.parse(Path(solution.__file__).read_text())
    found = False
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            node.value = ast.parse(expression, mode="eval").body
            found = True
            break
    assert found, "Keep the supplied input table so your selection can be checked on different records."
    namespace = {}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(ast.fix_missing_locations(tree), "<changed-input>", "exec"), namespace)
    return namespace


def _uses(attribute, function=None):
    import ast
    from pathlib import Path
    import solution
    tree = ast.parse(Path(solution.__file__).read_text())
    if function:
        tree = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == function)
    assert any(isinstance(n, ast.Attribute) and n.attr == attribute for n in ast.walk(tree)), "Use " + attribute + " for this task, rather than a fixed answer."
