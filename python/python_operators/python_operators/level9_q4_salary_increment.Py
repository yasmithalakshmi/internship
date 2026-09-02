# Level 9 - Question 4
# Calculate an employee's salary after applying a percentage increment.

salary = float(input("Enter current salary: "))
increment_percent = float(input("Enter increment percentage: "))
new_salary = salary + (salary * increment_percent / 100)
print("New salary:", new_salary)
