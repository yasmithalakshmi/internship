# 3. Create a Rectangle class with a method that accepts length and width and returns the area.

class Rectangle:
    def area(self, length, width):
        return length * width

r = Rectangle()
print(r.area(10, 5))
