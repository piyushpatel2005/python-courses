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


class OrderRegistry:
    def __init__(self):
        self.orders = {}
        self.statuses = {}

    def get(self, order_id):
        return self.orders[order_id]

    def track(self, order_id):
        return self.statuses[order_id]

    def advance(self, order_id, status):
        current = self.track(order_id)
        following = {"placed": "shipped", "shipped": "delivered"}
        if following.get(current) != status:
            raise ValueError("invalid status transition")
        self.statuses[order_id] = status

    def add(self, order):
        if order.order_id in self.orders:
            raise ValueError("duplicate order")
        self.orders[order.order_id] = order
        self.statuses[order.order_id] = "placed"


def money(cents):
    return f"{cents // 100}.{cents % 100:02d}"


class Invoice:
    def __init__(self, order):
        self.order = order

    def lines(self):
        return [f"{sku} | {name} | {quantity} x | ${money(subtotal)}"
                for sku, name, quantity, subtotal in self.order.lines]

    def render(self):
        parts = [f"Order {self.order.order_id}"]
        parts.extend(self.lines())
        parts.append(f"Total: ${money(self.order.total_cents)}")
        return "\n".join(parts)



class Shop:
    def __init__(self, catalog):
        self.catalog = catalog
        self.cart = Cart(catalog)
        self.registry = OrderRegistry()
        self.checkout_service = CheckoutService()
        self.next_order = 1

    def products(self):
        return "\n".join(f"{p.sku} | {p.name} | ${money(p.price_cents)}" for p in self.catalog.all()) or "No products"

    def add(self, sku, quantity):
        self.cart.add(sku, quantity)
        return f"Added {sku} x {quantity}"

    def remove(self, sku):
        return f"Removed {sku}" if self.cart.remove(sku) else f"Not in cart: {sku}"

    def cart_text(self):
        rows, total = self.cart.summary()
        lines = [f"{sku} | {name} | {quantity} x | ${money(subtotal)}" for sku, name, quantity, subtotal in rows]
        return "\n".join(lines + [f"Cart total: ${money(total)}"])

    def checkout(self):
        order_id = f"O{self.next_order}"
        order = self.checkout_service.checkout(self.cart, order_id)
        self.registry.add(order)
        self.next_order += 1
        return f"Created {order_id}"

    def orders(self):
        return "\n".join(self.registry.orders) or "No orders"

    def track(self, order_id):
        return f"{order_id}: {self.registry.track(order_id)}"

    def show(self, order_id):
        return Invoice(self.registry.get(order_id)).render()

    def status(self, order_id, state):
        self.registry.advance(order_id, state)
        return self.track(order_id)

    def execute(self, command):
        parts = command.split()
        if parts == ["products"]:
            return self.products()
        if len(parts) == 3 and parts[0] == "add":
            return self.add(parts[1], int(parts[2]))
        if len(parts) == 2 and parts[0] == "remove":
            return self.remove(parts[1])
        if parts == ["cart"]:
            return self.cart_text()
        if parts == ["checkout"]:
            return self.checkout()
        if parts == ["orders"]:
            return self.orders()
        if len(parts) == 2 and parts[0] == "track":
            return self.track(parts[1])
        if len(parts) == 2 and parts[0] == "show":
            return self.show(parts[1])
        if len(parts) == 3 and parts[0] == "status":
            return self.status(parts[1], parts[2])
        raise ValueError("invalid command")


def run_session(shop, commands):
    responses = []
    for command in commands:
        if command.strip() == "quit":
            break
        try:
            responses.append(shop.execute(command))
        except (ValueError, KeyError) as error:
            responses.append("Error: " + str(error))
    return responses


PRODUCTS = (Product("MUG", "Mug", 1250), Product("TEA", "Tea", 575))
DEFAULT_COMMANDS = (
    "products", "add MUG 2", "add TEA 1", "remove TEA", "cart",
    "checkout", "orders", "track O1", "status O1 shipped",
    "show O1", "quit",
)


def main(commands=None):
    shop = Shop(Catalog(PRODUCTS))
    responses = run_session(shop, DEFAULT_COMMANDS if commands is None else commands)
    for response in responses:
        print(response)
    return responses


if __name__ == "__main__":
    try:
        responses = main()
        if responses is None:
            print("Complete main to start the session.")
    except Exception as error:
        print("Probe:", type(error).__name__, str(error))
