# abstract class Animal with an abstract method sound(). Create Dog and Cat classes that implement sound().


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

Dog().sound() 
Cat().sound() 