# Level 3: Dictionaries
# Write Python code for all the questions below.

# 1. Create a dictionary containing student name, age, course, and marks. Print all values.
# 2. Create a dictionary and access a value using its key.
# 3. Create a dictionary and add a new key-value pair.
# 4. Create a dictionary and update the value of an existing key.
# 5. Create a dictionary and remove a key-value pair using pop().
# 6. Create a dictionary and remove the last inserted item using popitem().
# 7. Create a dictionary and print all keys using keys().
# 8. Create a dictionary and print all values using values().
# 9. Create a dictionary and print all key-value pairs using items().
# 10. Create a dictionary of student marks and check whether a particular student exists.
# 11. Create a dictionary of 5 products and their prices. Print all products whose price is greater than ₹1,000.
# 12. Create a dictionary of student names and marks. Find the student with the highest marks without using max().
# 13. Create a dictionary of employee names and salaries. Calculate the average salary.
# 14. Create a dictionary of numbers and their squares.
# 15. Create a dictionary containing numbers from 1 to 10 as keys and their cubes as values.

# Solutions
student = {"name": "Priya", "age": 20, "course": "Python", "marks": 88}
print("1. Student values:", list(student.values()))
print("2. Access age:", student["age"])

student["city"] = "Bangalore"
print("3. After adding city:", student)

student["marks"] = 92
print("4. Updated marks:", student)

student.pop("city")
print("5. After pop(city):", student)

employee = {"name": "Ravi", "salary": 50000}
employee["designation"] = "Developer"
print("6. popitem() ->", employee.popitem())
print("7. Keys:", student.keys())
print("8. Values:", student.values())
print("9. Items:", student.items())

marks_dict = {"Anu": 78, "Mithu": 85, "Kavi": 92}
print("10. Does Kavi exist?", "Kavi" in marks_dict)

products = {"Laptop": 45000, "Phone": 25000, "Headphones": 1200, "Monitor": 8000, "Tablet": 18000}
expensive = {p: v for p, v in products.items() if v > 1000}
print("11. Products above ₹1,000:", expensive)

student_marks = {"Asha": 78, "Bharat": 92, "Chitra": 85, "David": 70}
highest_student = ""
highest_mark = 0
for name, mark in student_marks.items():
    if mark > highest_mark:
        highest_mark = mark
        highest_student = name
print("12. Highest marks student:", highest_student, highest_mark)

salaries = {"Alice": 45000, "Bob": 60000, "Charlie": 55000}
total_salary = 0
for value in salaries.values():
    total_salary += value
avg_salary = total_salary / len(salaries)
print("13. Average salary:", avg_salary)

square_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("14. Numbers and squares:", square_dict)

cube_dict = {n: n ** 3 for n in range(1, 11)}
print("15. Cubes from 1 to 10:", cube_dict)
