# 5. Create a Person class with name, age, and city. Create two objects and display their information.

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

p1 = Person("Anil", 25, "Pune")
p2 = Person("Sita", 30, "Delhi")

print("Person 1:", p1.name, p1.age, p1.city)
print("Person 2:", p2.name, p2.age, p2.city)
