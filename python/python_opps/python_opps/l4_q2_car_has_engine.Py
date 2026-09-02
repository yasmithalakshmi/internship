# Level 4: Identify the Relationship - Question 2
# A Car has an Engine - HAS-A Relationship (Composition)

class Engine:
    def start(self):
        print("Engine started!")


class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start_car(self):
        print("Car starting...")
        self.engine.start()


# Example usage
car = Car()
car.start_car()
