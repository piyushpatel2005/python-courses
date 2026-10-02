from solution import prepare_seals
import solution
import inspect
import ast

def test_module_import():
    """The named helper comes from the local module"""
    tree = ast.parse(inspect.getsource(solution))
    assert any(
        isinstance(node, ast.ImportFrom)
        and node.module == "shrine_rules"
        and any(alias.name == "seal_count" and alias.asname is None for alias in node.names)
        for node in tree.body
    ), "Import seal_count from shrine_rules, not just in a comment."
    assert callable(solution.seal_count)

def test_prepare_seals():
    """The wrapper delegates to the reusable helper"""
    original = solution.seal_count
    calls = []
    def tracked(runes):
        calls.append(runes)
        return original(runes)
    try:
        solution.seal_count = tracked
        assert prepare_seals(9) == 3
        assert prepare_seals(4) == 1
        assert prepare_seals(0) == 0
        assert calls == [9, 4, 0], "Call the imported seal_count(runes) helper."
    finally:
        solution.seal_count = original
