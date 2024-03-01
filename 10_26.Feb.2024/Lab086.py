# Class - Blueprint to create something
# Object - a real entity created from the class
# Person - Sowmya, Arjun, Siri, Tani - Real world entity
# OOPS - oops concepts says that every object and the class that you create they can have some features

#Encapsulation - whatever the data members / class variables  we have used and the functions we have are closed within
# a single blueprint - wrapping or binding the data variables with the methods
# reason for encapsulation is to hide the important variables

class Car:
    name = None
    password = "123" #here we can print the password outside to hide this we use encapsulation
    
    def __init__(self, name):
        self.name = name
    
    def printname(self): # we are binding the data variable name with the method
        print(self.name)
        
XUV = Car("XUV")
XUV.printname()

lambo = Car("lambo")
lambo.printname()

print(XUV.name)
print(XUV.password)
        