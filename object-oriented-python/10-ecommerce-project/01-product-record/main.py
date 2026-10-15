from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    price_cents: int

    def __post_init__(self):
        pass


if __name__ == "__main__":
    try:
        print(Product("MUG", "Mug", 1250))
        print(Product("BAD", "Invalid price", -1))
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
