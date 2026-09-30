def safe_count(text):
    try:
        return int(text)
    except ValueError:
        return -1

print("Supply count:", safe_count("4"))
print("Unknown supply count:", safe_count("unknown"))
