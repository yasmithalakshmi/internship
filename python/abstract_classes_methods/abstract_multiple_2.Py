#abstract class Shape with abstract methods area() and perimeter(). Implement them in Rectangle and Circle.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width * self.height)
        

    def perimeter(self):
        print(2 * (self.width + self.height))
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(3.14 * self.radius ** 2)

    def perimeter(self):
        print(2 * 3.14 * self.radius)
r=Rectangle(4, 6)
c=Circle(5)
r.area()
r.perimeter()
c.area()
c.perimeter()