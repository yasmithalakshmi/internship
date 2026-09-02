# Level 2: HAS-A Relationship - Question 1
# Create a Car class that HAS-A Engine object

class Engine:
    def __init__(self, type, power):
        self.type = type
        self.power = power
    
    def start(self):
        print(f"Engine ({self.type}, {self.power}hp) started!")


class Car:
    def __init__(self, name, color, engine):
        self.name = name
        self.color = color
        self.engine = engine
    
    def start(self):
        print(f"Car: {self.name} ({self.color})")
        self.engine.start()


# Example usage
engine = Engine("Petrol", 120)
car = Car("Toyota", "Red", engine)
car.start()
