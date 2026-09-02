# 7. Create a Laptop class with brand, ram, storage, and price. Create three objects.

class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

laptops = [
    Laptop("HP", "8GB", "512GB", 42000),
    Laptop("Lenovo", "16GB", "1TB", 65000),
    Laptop("Asus", "32GB", "1TB", 85000)
]

for laptop in laptops:
    print(laptop.brand, laptop.ram, laptop.storage, laptop.price)
