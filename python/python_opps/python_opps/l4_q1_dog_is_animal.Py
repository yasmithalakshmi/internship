# Level 4: Identify the Relationship - Question 1
# A Dog is an Animal - IS-A Relationship (Inheritance)

class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("Some sound")


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks: Woof!")


# Example usage
dog = Dog("Buddy")
dog.make_sound()
