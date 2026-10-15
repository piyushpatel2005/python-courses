class Entity:
    pass

class GlowMixin(Entity):
    pass

class TrailMixin(Entity):
    pass

class LanternSprite(GlowMixin, TrailMixin):
    pass


def mro_names(cls):
    return [base.__name__ for base in cls.__mro__]


if __name__ == "__main__":
    try:
        print("Direct bases:", [base.__name__ for base in LanternSprite.__bases__])
        print("Full order:", mro_names(LanternSprite))
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
