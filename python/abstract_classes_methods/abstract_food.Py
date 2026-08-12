# abstract class Food with an abstract method prepare(). Implement it using Pizza and Burger.
from abc import ABC, abstractmethod
class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass
class Pizza(Food):
    def prepare(self):
        print("Preparing pizza.")

class Burger(Food):
    def prepare(self):
        print("Preparing burger.")
Pizza().prepare()
Burger().prepare()