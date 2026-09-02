# Level 1: IS-A Relationship - Question 5
# Create a Shape class and a Rectangle class

class Shape:
    def __init__(self, color):
        self.color = color
    
    def area(self):
        print("Area calculation depends on the shape")


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


# Example usage
rect = Rectangle("Blue", 5, 10)
print(f"Color: {rect.color}")
print(f"Area: {rect.area()}")
