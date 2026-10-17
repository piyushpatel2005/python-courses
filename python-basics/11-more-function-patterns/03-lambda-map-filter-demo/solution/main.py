frequencies = [3, 5, 7]
tuned = list(map(lambda frequency: frequency + 2, frequencies))
strong = list(filter(lambda frequency: frequency > 6, tuned))
print("Tuned:", tuned)
print("Strong:", strong)
