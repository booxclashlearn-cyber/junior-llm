completed_days = 3
for days in range(1, 6):
    if days <= completed_days:
        print(f"Day {days}: completed.")
    else:
        print(f"Day {days}: pending")