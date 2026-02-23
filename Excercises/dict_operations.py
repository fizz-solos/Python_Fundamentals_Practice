students = {"Alice": 85, "Bob": 92, "Charlie": 78}

students["David"] = 88

for name, grade in students.items():
    print(f"{name}: {grade}")

Highest = 0
for value in students.values():
    if value > Highest:
        Highest = value
print(f"Highest grade using loop: {Highest}")

max_grade = max(students.values())
print(f"Highest grade: {max_grade}")