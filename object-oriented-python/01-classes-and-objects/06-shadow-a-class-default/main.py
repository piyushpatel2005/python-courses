class GameItem:
    cooldown_turns = 7

def set_cooldown(item, turns):
    pass


# Supplied console probe: keep this below your implementation.
if __name__ == "__main__":
    try:
        first, second = GameItem(), GameItem()
        set_cooldown(first, 14)
        print("Cooldown turns:", first.cooldown_turns, second.cooldown_turns, GameItem.cooldown_turns)
    except (NameError, AttributeError, TypeError, ValueError) as error:
        print("Not ready yet:", error)
