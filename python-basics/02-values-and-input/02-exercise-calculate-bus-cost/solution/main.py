riders_per_group = 3
groups = 7
capacity = 25
fare_per_rider = 4
fare_total = riders_per_group * groups * fare_per_rider
open_seats = capacity - riders_per_group * groups
print("Fare total:", fare_total)
print("Open seats:", open_seats)
