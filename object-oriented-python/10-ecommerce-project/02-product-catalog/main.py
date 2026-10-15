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


class Catalog:
    def get(self, sku):
        return self.products[sku]

    def all(self):
        return [self.products[sku] for sku in sorted(self.products)]

    def __init__(self, products):
        pass


if __name__ == "__main__":
    try:
        catalog = Catalog([Product("MUG", "Mug", 1250)])
        print([p.sku for p in catalog.all()])
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
