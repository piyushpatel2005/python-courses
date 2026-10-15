class NamedField:
    key = "_unfinished"

    def __set_name__(self, owner, name):
        self.key = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.key)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = value

class Contact:
    city = NamedField()
    region = NamedField()


if __name__ == "__main__":
    try:
        person = Contact()
        person.city, person.region = "Leeds", "Yorkshire"
        print(person.city, person.region)
    except (AttributeError, TypeError, ValueError, KeyError, NameError) as error:
        print("Not ready:", type(error).__name__, str(error))
