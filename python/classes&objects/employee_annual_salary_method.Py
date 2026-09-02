# 9. Create an Employee class with a method to calculate annual salary.

class Employee:
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

emp = Employee(45000)
print("Annual salary:", emp.annual_salary())
