from solution import *


def test_01_extend_initialization():
    for title, cooldown in (("Dash", 14), ("Glide", 9), ("", 0)):
        ability = CooldownAbility(title, cooldown)
        assert ability.title == title and ability.cooldown == cooldown
        assert ability.label() == f"Ability: {title}"
    calls = []
    original = Ability.__init__
    try:
        def tracking(self, title):
            calls.append(title)
            self.title = title.upper()
        Ability.__init__ = tracking
        item = CooldownAbility("evening", 18)
        assert calls == ["evening"], "Delegate base initialization once."
        assert item.title == "EVENING" and item.cooldown == 18
    finally:
        Ability.__init__ = original
    import ast, inspect, textwrap
    source = ast.parse(textwrap.dedent(inspect.getsource(CooldownAbility.__init__)))
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "super" for node in ast.walk(source)), "Use super() for the base initializer."
