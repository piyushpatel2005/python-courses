class LibraryCart:
    def __init__(self, titles):
        self.titles = list(titles)

    def __len__(self):
        return len(self.titles)


if __name__ == "__main__":
    try:
        cart = LibraryCart(["Maps", "Birds"])
        print("Titles:", len(cart))
        cart.titles.append("Trees")
        print("After adding:", len(cart))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
