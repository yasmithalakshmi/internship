# Level 3: Lists & Tuples - Question 1
# Create list of tuples with student name and marks, display students above 75

students = [("Alice", 85), ("Bob", 70), ("Charlie", 92), ("David", 78), ("Eve", 65)]

print("Students list (name, marks):")
print(students)

print("\nStudents with marks above 75:")
for name, marks in students:
    if marks > 75:
        print(name, "-", marks)
