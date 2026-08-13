#abstract Shape class and use polymorphism to calculate the area of different shapes
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of the circle is: {3.14 * self.radius ** 2}")
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"Area of the square is: {self.side ** 2}")
s=Square(4)
c=Circle(5)
s.area()
c.area()
