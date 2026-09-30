from solution import *


def test_write_note():
    """Writing a note replaces the file contents"""
    write_note("Tables near the window")
    with open("workshop-note.txt", "r") as file:
        assert file.read() == "Tables near the window", "Write text to workshop-note.txt."
    write_note("New location")
    with open("workshop-note.txt", "r") as file:
        assert file.read() == "New location", "Opening in write mode should replace the previous note."


def test_read_note():
    """Reading returns the full note"""
    with open("workshop-note.txt", "w") as file:
        file.write("Bring paper\nBring pens")
    assert read_note() == "Bring paper\nBring pens", "Read the entire note and return it."
