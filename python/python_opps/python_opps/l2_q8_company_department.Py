# Level 2: HAS-A Relationship - Question 8
# Create a Company class that HAS-A multiple Department objects

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
    
    def info(self):
        print(f"  Department: {self.dept_name}")


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.departments = []
    
    def add_department(self, department):
        self.departments.append(department)
    
    def display_info(self):
        print(f"Company: {self.company_name}")
        print("Departments:")
        for dept in self.departments:
            dept.info()


# Example usage
company = Company("Tech Corp")
company.add_department(Department("Engineering"))
company.add_department(Department("HR"))
company.add_department(Department("Sales"))
company.add_department(Department("Finance"))
company.display_info()
