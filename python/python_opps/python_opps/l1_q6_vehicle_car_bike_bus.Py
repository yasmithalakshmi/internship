# Level 1: IS-A Relationship - Question 6
# Create a Vehicle class and Car, Bike, and Bus child classes

class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def info(self):
        print(f"Vehicle: {self.name}, Speed: {self.speed} km/h")


class Car(Vehicle):
    def __init__(self, name, speed, doors):
        super().__init__(name, speed)
        self.doors = doors
    
    def info(self):
        super().info()
        print(f"Doors: {self.doors}")


class Bike(Vehicle):
    def __init__(self, name, speed, engine_cc):
        super().__init__(name, speed)
        self.engine_cc = engine_cc
    
    def info(self):
        super().info()
        print(f"Engine: {self.engine_cc} cc")


class Bus(Vehicle):
    def __init__(self, name, speed, capacity):
        super().__init__(name, speed)
        self.capacity = capacity
    
    def info(self):
        super().info()
        print(f"Capacity: {self.capacity} passengers")


# Example usage
car = Car("Toyota", 180, 4)
bike = Bike("Honda", 150, 150)
bus = Bus("Volvo", 120, 50)

car.info()
print()
bike.info()
print()
bus.info()
