# abstract class Vehicle with instance variables brand and model. Add abstract methods start() and stop().
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print(f"{self.brand} {self.model} is starting.")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping.")
class Bike(Vehicle):
    def start(self):
        print(f"{self.brand} {self.model} is starting.")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping.")
car = Car("Toyota", "Camry")
car.start()
car.stop()
bike = Bike("Yamaha", "MT-07")
bike.start()
bike.stop()