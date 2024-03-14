#Multiple Inheritance

class Father:
    def father_money(self):
        return "5"
    
    def home(self):
        return "This is from the father"
        
class Mother:
    def mother_money(self):
        return "15"
    
    def home(self):
        return "This is from the Mother"
        
class Son(Father, Mother): #here whoever is the first one that method will be called first
    pass

son = Son()
print(Son.mro()) #this will tell which one is called first
print(son.father_money())
print(son.mother_money())
print(son.home())

#MRO - Method Resolution Order, multiple inheritance cannot be done in Jave,this problem is
#solved in python using MRO i.e whoever is the first one that method will be called first