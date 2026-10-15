class Entity:
    def build(self, events):
        events.append("entity")
        return events

class GlowMixin(Entity):
    def build(self, events):
        events.append("glow")
        return super().build(events)

class TrailMixin(Entity):
    def build(self, events):
        events.append("trail")
        return super().build(events)

class LanternSprite(GlowMixin, TrailMixin):
    pass


if __name__ == "__main__":
    try:
        events = []
        print("Build order:", LanternSprite().build(events))
        print("Shared list:", events)
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
