#abstract class Shape with a constructor that accepts a color. Add an abstract method area().
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        print(3.14 * self.radius ** 2)
area = Circle("red", 5)
area.area()
