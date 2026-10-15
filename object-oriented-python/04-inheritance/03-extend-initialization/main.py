class Ability:
    def __init__(self, title):
        self.title = title

    def label(self):
        return f"Ability: {self.title}"

class CooldownAbility(Ability):
    def __init__(self, title, cooldown):
        pass  # TODO: complete the requested behavior.


if __name__ == "__main__":
    try:
        ability = CooldownAbility("Dash", 14)
        print(ability.label(), ability.cooldown)
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
