from solution import note, saved_note

def test_note_round_trip():
    assert note == "Check the north door"
    assert saved_note == note
