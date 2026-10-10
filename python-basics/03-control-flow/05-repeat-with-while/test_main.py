import ast
from pathlib import Path
import solution as s

def test_four_countdown_ticks():
    source = Path(s.__file__).read_text()
    tree = ast.parse(source)
    assert isinstance(tree.body[0], ast.Assign) and tree.body[0].value.value == 4, "Start the beacon counter at 4"
    assert s.pulses == 0, "Keep the decrement so the countdown terminates"
