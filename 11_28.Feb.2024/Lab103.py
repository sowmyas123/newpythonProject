#Method Overloading
#Pythond doesn't support method overloading in traditional sense
#here we will have same name of function with different parameter

class MathUtil:
    def add(self, a, b=0, c=0):
        return a+b+c
    
    #def add(self, a, b): #we cannot call another method with name add, this is not advisable in python
    #pass

math = MathUtil()
op0 = math.add(1)
opp1 = math.add(1,2)
opp3 = math.add(1,2,3) #we can call 1 or 2 or 3 parameters also because we have set default values for b and c
