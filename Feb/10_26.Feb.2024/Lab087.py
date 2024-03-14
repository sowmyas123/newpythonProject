# there are 3 different types of data members/ class variables
class Car:
    name = None
    password = "123"
    
    def __init__(self):
        self.public_var = "public"     #public - anyone can access it
        self._protected_var = "protected@123"
        self.__private_var = "pass@123"
        
    def _protectedmethod(self):
        print("protected method")
        
    def __privatemethod(self):
        print("Private")
    
    def printname(self):  # we are binding the data variable name with the method
        print(self.name)


XUV = Car()
XUV.printname()

#lambo = Car("lambo")
#lambo.printname()

print(XUV.public_var)
print(XUV._protected_var)
