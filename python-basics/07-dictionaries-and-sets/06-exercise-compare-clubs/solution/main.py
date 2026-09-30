morning_names = ["Ada", "Bo", "Ada", "Cy"]
evening_names = ["Bo", "Dee"]
morning = set(morning_names)
shared = morning & set(evening_names)
morning_only = morning - set(evening_names)
print(sorted(morning), sorted(shared), sorted(morning_only))
