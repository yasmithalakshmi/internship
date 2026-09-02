# Level 3: Lists & Tuples - Question 3
# Create list of tuples with employee name, designation, salary, find highest salary

employees = [("John", "Developer", 60000), ("Jane", "Manager", 80000), ("Bob", "Tester", 50000), ("Alice", "Lead", 90000)]

print("Employees list (name, designation, salary):")
print(employees)

highest_salary = employees[0][2]
highest_emp = employees[0][0]

for name, designation, salary in employees:
    if salary > highest_salary:
        highest_salary = salary
        highest_emp = name

print("\nEmployee with highest salary:", highest_emp, "-", highest_salary)
