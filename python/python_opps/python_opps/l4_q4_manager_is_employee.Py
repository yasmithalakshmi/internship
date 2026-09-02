# Level 4: Identify the Relationship - Question 4
# A Manager is an Employee - IS-A Relationship (Inheritance)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        print(f"{self.name} is working")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def manage_team(self):
        print(f"{self.name} is managing {self.team_size} people")


# Example usage
manager = Manager("John", 80000, 10)
manager.work()
manager.manage_team()
