import ast
from pathlib import Path
import solution
from solution import upper_labels, long_labels


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


def with_different_labels(tree):
    for node in tree.body:
        if (isinstance(node, ast.Assign) and any(isinstance(target, ast.Name)
                and target.id == "beacon_labels" for target in node.targets)):
            replacement = ast.List(elts=[ast.Constant(value=value)
                for value in ("East", "W", "West", "Summit")], ctx=ast.Load())
            node.value = ast.copy_location(replacement, node.value)
            break
    else:
        assert False, "Keep the supplied beacon_labels fixture."
    namespace = {"print": lambda *args: None}
    exec(compile(ast.fix_missing_locations(tree), "<changed labels>", "exec"), namespace)
    return namespace


def test_upper_labels():
    """Map the supplied labels to uppercase"""
    assert upper_labels == ["N", "NORTH", "E", "SOUTH"]
    tree = pipeline("upper_labels", "map", "beacon_labels")
    assert with_different_labels(tree)["upper_labels"] == ["EAST", "W", "WEST", "SUMMIT"], (
        "Map the supplied labels, not just the sample values.")


def test_long_labels():
    """Filter uppercase labels by length"""
    assert long_labels == ["NORTH", "SOUTH"]
    tree = pipeline("long_labels", "filter", "upper_labels")
    assert with_different_labels(tree)["long_labels"] == ["EAST", "WEST", "SUMMIT"], (
        "Filter uppercase labels by length for different beacons too.")
