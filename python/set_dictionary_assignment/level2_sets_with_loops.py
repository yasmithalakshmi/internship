# Level 2: Sets with Loops
# Write Python code for all the questions below.

# 1. Create a set of numbers and print only the even numbers.
# 2. Create a set of numbers and print only the odd numbers.
# 3. Create two sets of student names and find students who are present in both sets.
# 4. Create two sets of student names and find students who are present only in the first set.
# 5. Create two sets of numbers and find all unique numbers from both sets.
# 6. Create a set of numbers and find the largest number without using max().
# 7. Create a set of numbers and find the smallest number without using min().
# 8. Create a list of duplicate student names and use a set to display only unique names.
# 9. Create two sets representing students enrolled in Python and Java. Find students enrolled in both courses.
# 10. Create two sets representing students who attended two different events. Find students who attended exactly one event.

# Solutions
numbers_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("1. Even numbers:", [n for n in numbers_set if n % 2 == 0])
print("2. Odd numbers:", [n for n in numbers_set if n % 2 != 0])

students_python = {"Asha", "Bharat", "Chitra", "David"}
students_java = {"Bharat", "David", "Esha", "Fiza"}
print("3. Common students:", students_python & students_java)
print("4. Only in Python:", students_python - students_java)
print("5. All unique numbers:", students_python | students_java)

numbers_set2 = {12, 45, 78, 3, 99, 56}
max_value = None
for num in numbers_set2:
    if max_value is None or num > max_value:
        max_value = num
print("6. Largest number:", max_value)

min_value = None
for num in numbers_set2:
    if min_value is None or num < min_value:
        min_value = num
print("7. Smallest number:", min_value)

student_names = ["Asha", "Asha", "Bharat", "Chitra", "Asha", "David", "Bharat"]
print("8. Unique names:", set(student_names))

python_students = {"Asha", "Bharat", "Chitra"}
java_students = {"Bharat", "David", "Esha"}
print("9. Students in both courses:", python_students & java_students)

event1 = {"Asha", "Bharat", "Chitra"}
event2 = {"Bharat", "David", "Esha"}
print("10. Attended exactly one event:", (event1 | event2) - (event1 & event2))
