scores = [45, 80, 50, 30, 90]
count = 0
for score in scores:
    if score >= 50:
        count += 1
print(f"Passed count: {count}")