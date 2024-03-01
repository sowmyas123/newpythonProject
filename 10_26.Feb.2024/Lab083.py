#class name first letter should be always capital letter
class Person:
    #class variable / Instance variable
    name = None #incase if we give any name here, when the object is called same name will print for both the object
    # in that we use constructor
    age = None
    
    def walk(self): #self will access class variables
        a = 10 #local variable
        print("Hi your name is ", self. name)
        print("Hi your age is", self.age)
        print(a)
        
sowmya = Person()
sowmya.walk()