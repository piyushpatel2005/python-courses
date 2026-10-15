from solution import *


def test_descriptor_delete():
    first, second = PlayerProfile(), PlayerProfile()
    first.badge, second.badge = "Scout", "Guide"
    first.note = "Keep unrelated data"
    del first.badge
    assert first.note == "Keep unrelated data"
    assert first.badge is None and second.badge == "Guide"
    assert PlayerProfile.badge.key not in first.__dict__
    del first.badge
    first.badge = "Explorer"
    assert first.badge == "Explorer"
    assert isinstance(PlayerProfile.badge, CachedBadge)
