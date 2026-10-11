shards = 23
per_lamp = 4
lamps = shards // per_lamp
spare = shards % per_lamp
print("Lamps:", lamps)
print("Spare shards:", spare)
