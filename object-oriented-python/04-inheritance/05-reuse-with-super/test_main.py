from solution import *


def test_01_reuse_with_super():
    for code, points in (("Q8", 200), ("Z1", 0), ("long code", 750)):
        item = RewardQuest(code, points)
        assert item.label() == f"Quest {code} | reward {points}"
        assert (item.code, item.points) == (code, points)
    original = Quest.label
    calls = []
    try:
        def replacement(self):
            calls.append(self.code)
            return "Revised " + self.code
        Quest.label = replacement
        assert RewardQuest("NEW", 12).label() == "Revised NEW | reward 12"
        assert calls == ["NEW"], "Call the shared label exactly once."
    finally:
        Quest.label = original
    import ast, inspect, textwrap
    source = ast.parse(textwrap.dedent(inspect.getsource(RewardQuest.label)))
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "super" for node in ast.walk(source)), "Reuse the base method through super()."
