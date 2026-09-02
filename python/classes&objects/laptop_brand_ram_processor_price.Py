# 6. Create a class called Laptop with properties for brand, RAM, processor, and price. Create an object and display its details.

class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

laptop = Laptop("Dell", "16GB", "Intel i5", 55000)
print("Brand:", laptop.brand)
print("RAM:", laptop.ram)
print("Processor:", laptop.processor)
print("Price:", laptop.price)
