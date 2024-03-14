#Method Overriding means same name in the parent and child
#child always overrides the parent function
#super() means call my parent function

class Animal:
    def __init__(self):
        pass
    
    def sound(self):
        print("Animal Sound")
        
class Dog(Animal):
    def __init__(self):
        pass
    def sound(self):
        super().sound() #super means who is above him, i.e animal here #super() is a keyword
        print("Dog Sound")
        
animal = Animal()
animal.sound()

dog = Dog()
dog.sound()
        
