contact = {"name": "Maya", "phone": "555-0102"}
name = contact["name"]
contact["phone"] = "555-0130"
email = contact.get("email", "not provided")
print(name, contact, email)
