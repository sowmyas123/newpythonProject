#Polymorphism
#Poly - means Many
#Morphism - forms
#it has 2 concepts Method overloading and Method Overriding

class Shape:
    
    def area(self):
        print("Area fo the shape")
        
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14*self.radius*self.radius

Shape1 = Rectangle(3,4)
print(Shape1.area())

Shape2 = Circle(10)
print(Shape2.area())

Shape3 = Shape()
print(Shape3.area())

