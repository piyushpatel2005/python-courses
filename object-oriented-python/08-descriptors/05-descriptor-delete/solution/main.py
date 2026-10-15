class CachedLabel:
    key = "_label"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.key)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        instance.__dict__.pop(self.key, None)

class Draft:
    label = CachedLabel()


if __name__ == "__main__":
    try:
        first, second = Draft(), Draft()
        first.label, second.label = "old", "keep"
        del first.label
        print(first.label, second.label)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
