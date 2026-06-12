tasks = ["done", "pending", "done", "pending", "pending"]
count_tasks = 0
for task in tasks:
    if task == "pending":
        count_tasks += 1

print(f"Pending count: {count_tasks}")