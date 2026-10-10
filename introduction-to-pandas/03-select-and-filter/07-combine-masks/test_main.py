from solution import *
import pandas as pd

def test_both_rules():
    """Keep only the stall satisfying both rules"""
    pd.testing.assert_frame_equal(result, table.loc[(table["baskets"] >= 4) & (table["aisle"] == "east")])
    changed = _rerun_with_fixture('table', 'pd.DataFrame({"stall": list("ABCDE"), "baskets": [4, 3, 8, 1, 7], "aisle": ["east", "east", "west", "west", "east"]}, index=list("vwxyz"))')
    pd.testing.assert_frame_equal(changed["result"], changed["table"].loc[(changed["table"]["baskets"] >= 4) & (changed["table"]["aisle"] == "east")])


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
