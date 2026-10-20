orders = ["order 101", "order 102", "order 103", "order 104"]
today = orders[:3]
labels = []
for order_id in orders[:3]:
    labels.append(f"Pack {order_id}")
print(today, labels)
