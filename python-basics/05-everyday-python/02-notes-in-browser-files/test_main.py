from solution import *


def test_write_note():
    """Writing a clue replaces the save file contents."""
    write_note("Trace the north rune")
    with open("atlas-save.txt", "r") as file:
        assert file.read() == "Trace the north rune", "Write text to atlas-save.txt."
    write_note("Follow the glow")
    with open("atlas-save.txt", "r") as file:
        assert file.read() == "Follow the glow", "Write mode should replace the previous clue."


def test_read_note():
    """Reading returns the full shrine note."""
    with open("atlas-save.txt", "w") as file:
        file.write("Find the map\nLight the beacon")
    assert read_note() == "Find the map\nLight the beacon", "Read the complete clue and return it."
