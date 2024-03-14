#by inheriting a class known as exception we can create our own customexception

class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message) #super() is parent i.e Exception
        
balance = 100
withdraw_amount = int(input("Enter the amount you can withdraw\n"))

if withdraw_amount > balance:
    raise MyCustomException("Balance is low")
else:
    print("Total after withdraw", balance - withdraw_amount)