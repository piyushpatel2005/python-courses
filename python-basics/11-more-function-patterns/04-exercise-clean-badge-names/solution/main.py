beacon_labels = ["N", "North", "E", "South"]
upper_labels = list(map(lambda label: label.upper(), beacon_labels))
long_labels = list(filter(lambda label: len(label) >= 4, upper_labels))
print("Upper:", upper_labels)
print("Long:", long_labels)
