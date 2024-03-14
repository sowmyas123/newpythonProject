class VWOloginpage():
    email = None
    password = None
    
    def __init__(self, email, password):
        self.username = email
        self.password = password
        
    def loginconfirm(self):
        if self.password == "Pass123":
            print("you are allowed to enter")
        else:
            print("invalid user")
            
sowmya = VWOloginpage("sowmya@sowmya.com", "123")
sowmya.loginconfirm()

arjun = VWOloginpage("arjun@arjun.com", "Pass123")
arjun.loginconfirm()

print(id(sowmya))
print(id(arjun))
    