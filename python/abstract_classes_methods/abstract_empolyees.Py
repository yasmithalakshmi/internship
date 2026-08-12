#abstract class Employee with an abstract method work(). Implement it in Developer and Tester.
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass
class Developer(Employee):
    def work(self):
        print("Writing code.")
class Tester(Employee):
    def work(self):
        print("Testing code.")
Developer().work()
Tester().work()