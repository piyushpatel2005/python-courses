class BracketFormatter:
    def format(self, text):
        return f"[{text}]"

class QuestHUD:
    def __init__(self, formatter):
        self.formatter = formatter

    def publish(self, text):
        return self.formatter.format(text)


if __name__ == "__main__":
    try:
        hud = QuestHUD(BracketFormatter())
        print(hud.publish("Lantern found"))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
