# Level 3: Lists & Tuples - Question 10
# Create list of student tuples and search for a student by name

students = [("Alice", "S001"), ("Bob", "S002"), ("Charlie", "S003"), ("David", "S004"), ("Eve", "S005")]

print("Students list (name, ID):")
print(students)

name_to_find = "Charlie"

print("\nSearching for", name_to_find)
found = False
for name, student_id in students:
    if name == name_to_find:
        print("Found!", name, "- ID:", student_id)
        found = True
        break

if not found:
    print(name_to_find, "not found")
