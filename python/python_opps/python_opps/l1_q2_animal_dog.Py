# Level 1: IS-A Relationship - Question 2
# Create an Animal class and a Dog class

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def info(self):
        super().info()
        print(f"Breed: {self.breed}")


# Example usage
dog = Dog("Buddy", 5, "Labrador")
dog.info()
