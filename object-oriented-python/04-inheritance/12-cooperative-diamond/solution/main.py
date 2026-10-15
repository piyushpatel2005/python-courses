class Document:
    def build(self, events):
        events.append("document")
        return events

class Signed(Document):
    def build(self, events):
        events.append("signed")
        return super().build(events)

class Dated(Document):
    def build(self, events):
        events.append("dated")
        return super().build(events)

class Report(Signed, Dated):
    pass


if __name__ == "__main__":
    try:
        events = []
        print("Build order:", Report().build(events))
        print("Shared list:", events)
    except Exception as error:
        print("Not ready:", type(error).__name__, str(error))
