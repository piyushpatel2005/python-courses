class Ability:
    def __init__(self, code):
        self.code = code

    def activate(self):
        return f"Walk {self.code}"

class GlideAbility(Ability):
    def activate(self):
        return f"Glide {self.code}"


def ability_messages(abilities):
    pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        print(ability_messages([Ability("A"), GlideAbility("B")]))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
