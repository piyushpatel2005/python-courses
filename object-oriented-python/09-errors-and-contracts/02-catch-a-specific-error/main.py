def player_label(directory, player_id):
    pass


if __name__ == "__main__":
    try:
        print(player_label({4: "Fern"}, 9))
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
