def player_label(directory, player_id):
    try:
        return directory[player_id]
    except KeyError:
        return "Unknown player"


if __name__ == "__main__":
    try:
        print(player_label({4: "Fern"}, 9))
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
