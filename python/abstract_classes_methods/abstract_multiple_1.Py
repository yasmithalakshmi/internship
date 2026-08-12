# abstract class Vehicle with abstract methods start() and stop(). Implement both methods in Car and Bike.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car is starting.")

    def stop(self):
        print("Car is stopping.")
class Bike(Vehicle):
    def start(self):
        print("Bike is starting.")

    def stop(self):
        print("Bike is stopping.")
Car().start()
Car().stop()
Bike().start()
Bike().stop()