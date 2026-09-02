# 2. Create a class called Car and create three objects with different values.

class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

car1 = Car("Toyota", "Corolla", 2020, 1800000)
car2 = Car("Honda", "Civic", 2022, 2200000)
car3 = Car("Maruti", "Swift", 2021, 900000)

print("Car 1:", car1.brand, car1.model, car1.year, car1.price)
print("Car 2:", car2.brand, car2.model, car2.year, car2.price)
print("Car 3:", car3.brand, car3.model, car3.year, car3.price)
