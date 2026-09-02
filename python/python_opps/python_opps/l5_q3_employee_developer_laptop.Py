# Level 5: Combined Relationships - Question 3
# Employee → Developer (IS-A) and Developer HAS-A Laptop

class Laptop:
    def __init__(self, model):
        self.model = model


class Employee:
    def __init__(self, name):
        self.name = name


class Developer(Employee):
    def __init__(self, name, laptop):
        super().__init__(name)
        self.laptop = laptop
    
    def code(self):
        print(f"{self.name} is coding on {self.laptop.model}")


# Example usage
laptop = Laptop("Dell XPS")
dev = Developer("John", laptop)
dev.code()
