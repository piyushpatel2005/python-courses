class Quantity:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get("_quantity", 0)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Quantity must not be negative")
        instance._quantity = value

class Stock:
    quantity = Quantity()


if __name__ == "__main__":
    try:
        item = Stock()
        item.quantity = 7
        print(item.quantity)
        try:
            item.quantity = -1
        except ValueError:
            print("Rejected:", item.quantity)
        else:
            print("Negative value accepted")
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
