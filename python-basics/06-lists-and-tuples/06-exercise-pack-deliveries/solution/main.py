deliveries = ["Oak", "Elm", "Pine", "Birch"]
today = deliveries[:3]
labels = []
for destination in deliveries[:3]:
    labels.append(f"To {destination}")
print(today, labels)
