# 6. Create an Employee class with a method that accepts working days and calculates salary.

class Employee:
    def salary(self, working_days):
        return working_days * 500

emp = Employee()
print(emp.salary(22))
