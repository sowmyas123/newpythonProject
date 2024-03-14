class Password:
    
    def __init__(self,password):
        self.__password = password
        self.public_var = 10
        
    def get_password(self, is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("Invalid")
            
    def set_password(self, password):
        if len(password) > 10:
            self.__password = password
            print("set to correct", password)
        else:
            print("Not allowed, weak password")
        
        
pwd = Password("Hacker123")
#print(pwd.public_var)
pwd.get_password(True)
pwd.set_password("sowmya123456")
#print(pwd.__password)
