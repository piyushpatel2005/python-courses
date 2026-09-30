badge_names = ["Li", "Mara", "Jo", "Sofia"]
upper_names = list(map(lambda name: name.upper(), badge_names))
long_names = list(filter(lambda name: len(name) >= 4, upper_names))
print("Upper:", upper_names)
print("Long:", long_names)
