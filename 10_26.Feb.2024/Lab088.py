class Myclass:
    def __init__(self):
        self.name = "sowmya"
        
    def public_func(self):
        print("public function()")
        
    def __privatefunc(self): #this is not allowed to call the fucntion
        print("This is private")
        
    def public_fn_private(self): #this function is inside the class so this is allowed to access the private fun i.e
        self.__privatefunc() #if we encapsulate private within the class we are allowed to access private fun & variables
        
        
a = Myclass()
a.public_func()
#a.__privatefunc() # direct private function  is not allowed this provides security
