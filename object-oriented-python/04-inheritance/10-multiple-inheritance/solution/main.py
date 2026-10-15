class LabelMixin:
    def print_label(self):
        return f"Item {self.code}"

class JournalMixin:
    def journal_path(self):
        return f"/journal/{self.code}"

class QuestCard(LabelMixin, JournalMixin):
    def __init__(self, code):
        self.code = code


if __name__ == "__main__":
    try:
        card = QuestCard("K9")
        print(card.print_label())
        print(card.journal_path())
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
