import ast
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import solution as s


def _run_with_health(player_health, enemy_health):
    assert s.__file__ is not None
    tree = ast.parse(Path(s.__file__).read_text(encoding="utf-8"))
    branches = [node for node in tree.body if isinstance(node, ast.If)]
    assert branches and branches[0].orelse, "Keep the if and else branches."

    values = {"player_health": player_health, "enemy_health": enemy_health}
    supplied = set()
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in values:
                    node.value = ast.Constant(value=values[target.id])
                    supplied.add(target.id)
    assert supplied == set(values), "Keep both health assignments above the branches."

    output = StringIO()
    with redirect_stdout(output):
        exec(compile(ast.fix_missing_locations(tree), "submission.py", "exec"), {})
    return output.getvalue().strip()


def test_choose_win_or_lose():
    """Choose the game message using both health conditions."""
    cases = (
        (20, 0, "Congratulations! You win"),
        (11, 9, "Congratulations! You win"),
        (10, 9, "Sorry, you lost!"),
        (20, 10, "Sorry, you lost!"),
        (5, 0, "Sorry, you lost!"),
        (20, 20, "Sorry, you lost!"),
        (5, 20, "Sorry, you lost!"),
    )
    for player_health, enemy_health, expected in cases:
        actual = _run_with_health(player_health, enemy_health)
        assert actual == expected, (
            f"With player_health = {player_health} and enemy_health = {enemy_health}, "
            f"print {expected!r}. Win only when player_health > 10 and enemy_health < 10."
        )
