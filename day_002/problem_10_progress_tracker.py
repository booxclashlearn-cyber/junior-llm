student = {
    "name": "Chilongo Kondwani",
    "total_days": 365,
    "completed_lessons": ["Variables", "Lists", "Dictionaries", "F-strings", "Conditionals"]
}
completed_count = len(student["completed_lessons"])
remaining_days = student["total_days"] - completed_count
print(f"{student['name']} has completed {completed_count} lessons. Remaining days in the year: {remaining_days}. Keep up the great work!")