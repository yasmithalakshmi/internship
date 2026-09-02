# 4. Create a Rectangle class with methods to calculate area and perimeter.

class Rectangle:
    def area(self, length, width):
        return length * width

    def perimeter(self, length, width):
        return 2 * (length + width)

r = Rectangle()
print("Area:", r.area(5, 4))
print("Perimeter:", r.perimeter(5, 4))
