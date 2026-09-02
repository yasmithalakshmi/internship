# Level 5: Combined Relationships - Question 1
# Vehicle → Car (IS-A) and Car HAS-A Engine

class Engine:
    def start(self):
        print("Engine started!")


class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Vehicle: {self.name}")


class Car(Vehicle):
    def __init__(self, name, engine):
        super().__init__(name)
        self.engine = engine
    
    def start_car(self):
        self.display()
        self.engine.start()


# Example usage
engine = Engine()
car = Car("Toyota", engine)
car.start_car()
