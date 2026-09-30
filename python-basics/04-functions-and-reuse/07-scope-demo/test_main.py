from solution import inside_room, room

def test_local_room():
    """Only the local room changes"""
    assert inside_room() == "Workshop"
    assert room == "Atrium"
