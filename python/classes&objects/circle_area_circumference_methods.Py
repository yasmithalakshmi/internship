# 5. Create a Circle class with methods to calculate area and circumference.

class Circle:
    pi = 3.14

    def area(self, radius):
        return self.pi * radius * radius

    def circumference(self, radius):
        return 2 * self.pi * radius

c = Circle()
print("Area:", c.area(7))
print("Circumference:", c.circumference(7))
