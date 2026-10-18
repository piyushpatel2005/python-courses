import ast
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import solution as s


def _loop_and_branch():
    assert s.__file__ is not None
    tree = ast.parse(Path(s.__file__).read_text())
    loop = next((n for n in tree.body if isinstance(n, ast.For)), None)
    assert loop is not None, "Keep the supplied for loop"
    branch = next((n for n in loop.body if isinstance(n, ast.If)), None)
    assert branch is not None, "Add an if branch inside the supplied loop"
    return tree, loop, branch


def _line_for(number):
    tree, loop, _ = _loop_and_branch()
    loop.iter = ast.Call(func=ast.Name(id="range", ctx=ast.Load()),
                         args=[ast.Constant(number), ast.Constant(number + 1)], keywords=[])
    output = StringIO()
    with redirect_stdout(output):
        exec(compile(ast.fix_missing_locations(tree), "fizzbuzz.py", "exec"), {})
    return output.getvalue().strip()


def test_fizzbuzz():
    """1. Label numbers divisible by both 3 and 5."""
    _, _, branch = _loop_and_branch()
    assert any(isinstance(n, ast.And) for n in ast.walk(branch.test)), \
        "Use and in the first check for both divisors"
    for number in (15, 30):
        assert _line_for(number) == "FizzBuzz", f"{number} must print FizzBuzz"
    assert _line_for(1) == "1", "Keep the fallback for other numbers"


def test_fizz():
    """2. Label numbers divisible by 3 alone."""
    _, _, branch = _loop_and_branch()
    assert branch.orelse and isinstance(branch.orelse[0], ast.If), \
        "Add an elif branch for multiples of 3"
    for number in (3, 6, 9):
        assert _line_for(number) == "Fizz", f"{number} must print Fizz"
    assert _line_for(15) == "FizzBuzz", "Check both divisors before 3 alone"


def test_buzz():
    """3. Label numbers divisible by 5 alone and keep the fallback."""
    _, _, branch = _loop_and_branch()
    second = branch.orelse[0] if branch.orelse else None
    assert isinstance(second, ast.If) and second.orelse and isinstance(second.orelse[0], ast.If), \
        "Add an elif branch for multiples of 5"
    for number in (5, 10, 20):
        assert _line_for(number) == "Buzz", f"{number} must print Buzz"
    for number in (1, 2, 4, 7):
        assert _line_for(number) == str(number), "Keep the supplied numeric fallback"
    assert _line_for(30) == "FizzBuzz" and _line_for(6) == "Fizz"
