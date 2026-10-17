checkpoints = ["Pass", "Bridge", "Beacon", "Exit"]
today = checkpoints[:3]
labels = []
for checkpoint in checkpoints[:3]:
    labels.append(f"For {checkpoint}")
print(today, labels)
