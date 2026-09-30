contact = {"name": "Ivy", "visits": 2}
visitor = contact["name"]
contact["visits"] = 3
phone = contact.get("phone", "not provided")
print(visitor, contact, phone)
