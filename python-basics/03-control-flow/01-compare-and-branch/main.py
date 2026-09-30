temperature = 12
raining = False
if temperature < 8:
    advice = "Wear a coat"
elif temperature < 16 and not raining:
    advice = "Take a jacket"
else:
    advice = "Travel light"
print(advice)
