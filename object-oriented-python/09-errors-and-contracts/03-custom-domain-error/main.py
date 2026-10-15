class LobbyFullError:
    pass


def join_lobby(remaining):
    if remaining <= 0:
        raise LobbyFullError("lobby is full")
    return remaining - 1


if __name__ == "__main__":
    try:
        join_lobby(0)
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
