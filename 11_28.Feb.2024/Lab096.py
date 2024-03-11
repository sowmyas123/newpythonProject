#Hierarchical inheritance

class Vehicle:
    def info(self):
        return "This is a vehicle"
    
class Car(Vehicle):
    def info(self):
        return "This is a car"
    
class Bicycle(Vehicle):
    def info(self):
        return "This is a bicycle"
    
car = Car()
print(car.info())