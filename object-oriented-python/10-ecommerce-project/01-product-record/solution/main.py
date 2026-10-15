from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    price_cents: int

    def __post_init__(self):
        if not isinstance(self.sku, str) or not self.sku.strip():
            raise ValueError("sku must be nonempty")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("name must be nonempty")
        if type(self.price_cents) is not int or self.price_cents < 0:
            raise ValueError("price must be nonnegative integer cents")


if __name__ == "__main__":
    try:
        print(Product("MUG", "Mug", 1250))
        print(Product("BAD", "Invalid price", -1))
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
