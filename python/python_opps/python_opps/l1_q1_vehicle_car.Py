# Level 1: IS-A Relationship - Question 1
# Create a Vehicle class and a Car class

class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def display_info(self):
        print(f"Vehicle: {self.name}, Color: {self.color}")


class Car(Vehicle):
    def __init__(self, name, color, doors):
        super().__init__(name, color)
        self.doors = doors
    
    def display_info(self):
        super().display_info()
        print(f"Doors: {self.doors}")


# Example usage
car = Car("Toyota", "Red", 4)
car.display_info()
