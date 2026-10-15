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
        self.products = {}
        for product in products:
            if product.sku in self.products:
                raise ValueError("duplicate sku")
            self.products[product.sku] = product


class CartLine:
    def __init__(self, product, quantity):
        if type(quantity) is not int or quantity <= 0:
            raise ValueError("quantity must be a positive integer")
        self.product = product
        self.quantity = quantity

    @property
    def subtotal_cents(self):
        return self.product.price_cents * self.quantity


class Cart:
    def __init__(self, catalog):
        self.catalog = catalog
        self.lines = {}

    def add(self, sku, quantity):
        if type(quantity) is not int or quantity <= 0:
            raise ValueError("quantity must be a positive integer")
        product = self.catalog.get(sku)
        if sku in self.lines:
            self.lines[sku].quantity += quantity
        else:
            self.lines[sku] = CartLine(product, quantity)

    def remove(self, sku):
        if sku not in self.lines:
            return False
        del self.lines[sku]
        return True

    def summary(self):
        rows = []
        for sku in sorted(self.lines):
            line = self.lines[sku]
            rows.append((sku, line.product.name, line.quantity, line.subtotal_cents))
        return rows, sum(row[3] for row in rows)



@dataclass(frozen=True)
class Order:
    order_id: str
    lines: tuple
    total_cents: int


def snapshot_order(order_id, cart):
    rows, total = cart.summary()
    return Order(order_id, tuple(rows), total)


class CheckoutService:
    def checkout(self, cart, order_id):
        if not cart.lines:
            raise ValueError("cart is empty")
        order = snapshot_order(order_id, cart)
        cart.lines.clear()
        return order


if __name__ == "__main__":
    try:
        cart = Cart(Catalog([Product("MUG", "Mug", 1250)]))
        cart.add("MUG", 1)
        print(CheckoutService().checkout(cart, "O1"))
        print("Cart:", cart.summary())
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
