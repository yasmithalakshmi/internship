# Level 3: Lists & Tuples - Question 4
# Nested list with student names and 3 subject marks, calculate total and average

students = [
    ["Alice", 85, 90, 88],
    ["Bob", 75, 80, 78],
    ["Charlie", 92, 88, 95],
    ["David", 70, 75, 72]
]

print("Students with marks:")
print(students)

print("\nStudent performance:")
for student in students:
    name = student[0]
    marks = student[1:]
    total = sum(marks)
    average = total / len(marks)
    print(name, "- Total:", total, ", Average:", average)
