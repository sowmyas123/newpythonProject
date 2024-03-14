#Abstraction - means hiding the implementation details and showing what is required/important details
#we can do 2 ways
#Abstract base class
#Abstract base methods

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
        
        @abstractmethod
        def sound(self):
            pass
        
class Dog(Animal):
    def sound(self):
        return "Bow Bow"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
    
dog = Dog("Rancho")
print("Bow Bow")

cat = Cat("Kitty")
print("Meow")
