stock = {"notebooks": 12, "pens": 4}
notebook_count = stock["pens"]
print(notebook_count)
stock["pens"] = 9
print("Pens:", stock["pens"])
print("Folders:", stock.get("folders", 0))
