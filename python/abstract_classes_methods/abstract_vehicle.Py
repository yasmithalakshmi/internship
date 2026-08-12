# abstract class Vehicle with an abstract method start(). Implement it in Car and Bike.


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine started!")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started!")
        
Car().start() 
Bike().start() 