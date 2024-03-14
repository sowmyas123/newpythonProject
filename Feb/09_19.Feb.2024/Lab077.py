class person:
    #Attribute - are also called as Data members
    name = None
    age = None
    id = None
    Phone_no = None
    
    #Behaviour - also called as Methods but not the function
    #functions() are not used in the class
    
    def talk(self): #self is its own instance means it is the first argument of every methods
        print("i can talk")
        
    def walk(self):
        print("i am a Method") #Methods are part of classes
        print("i can walk")
        
    def sleep(self):
        return "i am sleeping"
    
def another(): #Functions are independent and are present outside the class
    print("i am a Function ")
    
    
#Objects - to create an object we need to add class name followed by ()
sowmya = person()
sowmya.name = "sowmya"
print(sowmya.name)
arjun = person()
sowmya.talk()