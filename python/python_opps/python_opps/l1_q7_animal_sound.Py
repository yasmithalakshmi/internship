# Level 1: IS-A Relationship - Question 7
# Create an Animal class with sound() method

class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("Some generic sound")


class Dog(Animal):
    def sound(self):
        print(f"{self.name} says: Woof Woof!")


class Cat(Animal):
    def sound(self):
        print(f"{self.name} says: Meow!")


# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.sound()
cat.sound()
