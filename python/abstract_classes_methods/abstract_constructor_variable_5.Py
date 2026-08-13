# abstract class Product with product name and price. Add an abstract method calculate_discount().
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass
class clothing(Product):
    def calculate_discount(self):
        discount = self.price * 0.5
        print(f"Discount for {self.name} is: {discount}")
class footwear(Product):
    def calculate_discount(self):
        discount = self.price * 0.3
        print(f"Discount for {self.name} is: {discount}")
class accessories(Product):
    def calculate_discount(self):
        discount = self.price * 0.2
        print(f"Discount for {self.name} is: {discount}")
cloths=clothing("kurti set", 1000)
shoes=footwear("Sandal", 2000)
accessory=accessories("necklace", 500)
cloths.calculate_discount()
shoes.calculate_discount()
accessory.calculate_discount()