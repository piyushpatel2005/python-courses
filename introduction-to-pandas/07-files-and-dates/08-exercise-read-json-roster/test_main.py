from solution import *

def test_01_roster_changes():
    """Load both multi-row and one-row JSON rosters"""
    for text, names, shifts in [
        ('[{"name":"Mara","shift":"morning"},{"name":"Luis","shift":"evening"}]', ["Mara", "Luis"], ["morning", "evening"]),
        ('[{"name":"Ayo","shift":"late"}]', ["Ayo"], ["late"]),
    ]:
        frame = load_roster(text)
        assert list(frame.columns) == ["name", "shift"]
        assert frame.name.tolist() == names
        assert frame["shift"].tolist() == shifts
