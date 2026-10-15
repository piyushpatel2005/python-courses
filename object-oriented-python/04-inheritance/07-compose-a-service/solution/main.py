class BracketFormatter:
    def format(self, text):
        return f"[{text}]"

class NoticeBoard:
    def __init__(self, formatter):
        self.formatter = formatter

    def publish(self, text):
        return self.formatter.format(text)


if __name__ == "__main__":
    try:
        board = NoticeBoard(BracketFormatter())
        print(board.publish("Workshop at noon"))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
