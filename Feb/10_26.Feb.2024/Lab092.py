#Single inheritance
class Father:
    __private_villa = "GOA" #this cannot be accessed by son
    gold = 5
    def drive_car(self):
        print("lambo")
        
    def threeBHKflat(self):
        print("3bhk flat")
        
    def private_villa_access(self, is_my_son): #by doing encapsulation we can access private villa
        print(self.__private_villa)
        
class Son(Father):
    pass

sowmya = Son()
print(sowmya.gold)
sowmya.drive_car()
sowmya.threeBHKflat()
sowmya.private_villa_access(True)

siddaraju = Father()
siddaraju.drive_car()
siddaraju.threeBHKflat()
siddaraju.gold
