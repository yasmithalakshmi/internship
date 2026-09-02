# 5. Create an Employee class that automatically calculates annual salary from monthly salary.

class Employee:
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

emp = Employee(60000)
print(emp.annual_salary())
