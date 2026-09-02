# 10. Create a Company class that stores employees and provides methods to add, remove, search, and display employees.

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, name):
        self.employees.append(name)

    def remove_employee(self, name):
        if name in self.employees:
            self.employees.remove(name)
            print(name, "removed")
        else:
            print(name, "not found")

    def search_employee(self, name):
        if name in self.employees:
            print(name, "found")
        else:
            print(name, "not found")

    def display_employees(self):
        for name in self.employees:
            print(name)

company = Company()
company.add_employee("Anu")
company.add_employee("Bhavya")
company.display_employees()
company.search_employee("Anu")
company.remove_employee("Bhavya")
