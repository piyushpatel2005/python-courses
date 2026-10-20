import ast
from pathlib import Path
import solution
from solution import discounted_prices, within_budget


def pipeline(name, operation, source):
    assert solution.__file__ is not None
    tree = ast.parse(Path(solution.__file__).read_text())
    assignments = [node for node in tree.body if isinstance(node, ast.Assign)
                   and any(isinstance(target, ast.Name) and target.id == name
                           for target in node.targets)]
    assert len(assignments) == 1, f"Set {name} once."
    value = assignments[0].value
    assert (isinstance(value, ast.Call) and isinstance(value.func, ast.Name)
            and value.func.id == "list" and len(value.args) == 1), (
        f"Set {name} from list({operation}(...)).")
    call = value.args[0]
    assert (isinstance(call, ast.Call) and isinstance(call.func, ast.Name)
            and call.func.id == operation and len(call.args) == 2
            and isinstance(call.args[0], ast.Lambda)
            and isinstance(call.args[1], ast.Name) and call.args[1].id == source), (
        f"Use {operation} with a lambda on {source} to set {name}.")
    return tree


def with_different_prices(tree):
    for node in tree.body:
        if (isinstance(node, ast.Assign) and any(isinstance(target, ast.Name)
                and target.id == "supply_prices" for target in node.targets)):
            replacement = ast.List(elts=[ast.Constant(value=value)
                for value in (1, 8, 9, 15)], ctx=ast.Load())
            node.value = ast.copy_location(replacement, node.value)
            break
    else:
        assert False, "Keep the supplied supply_prices fixture."
    namespace = {"print": lambda *args: None}
    exec(compile(ast.fix_missing_locations(tree), "<changed prices>", "exec"), namespace)
    return namespace


def test_discounted_prices():
    """Map the supplied prices after a $1 coupon."""
    assert discounted_prices == [3, 8, 1, 11]
    tree = pipeline("discounted_prices", "map", "supply_prices")
    assert with_different_prices(tree)["discounted_prices"] == [0, 7, 8, 14], (
        "Apply the coupon to each supplied price, not just the sample values.")


def test_within_budget():
    """Filter discounted prices at or below $8."""
    assert within_budget == [3, 8, 1]
    tree = pipeline("within_budget", "filter", "discounted_prices")
    assert with_different_prices(tree)["within_budget"] == [0, 7, 8], (
        "Filter the discounted prices, including exactly $8.")
