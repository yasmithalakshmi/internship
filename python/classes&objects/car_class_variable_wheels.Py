# 3. Create a Car class with a class variable number_of_wheels. Display it using different objects.

class Car:
    number_of_wheels = 4

    def __init__(self, brand):
        self.brand = brand

c1 = Car("Audi")
c2 = Car("BMW")

print(c1.brand, c1.number_of_wheels)
print(c2.brand, Car.number_of_wheels)
