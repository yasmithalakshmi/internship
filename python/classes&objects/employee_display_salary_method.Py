# 2. Create an Employee class with a method display_salary() to display employee salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print(self.name, "salary is", self.salary)

emp = Employee("Rohit", 50000)
emp.display_salary()
