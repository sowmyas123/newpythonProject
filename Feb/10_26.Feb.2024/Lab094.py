# Multilevel inheritance
class GF:
    
    def __init__(self):
        print("Automatically called when the object is created")
    def home(self):
        print("5bhk")


class Father(GF):
    def home2(self):
        print("GOA")


class Son(Father):
    def home3(self):
        print("Bangalore")


sowmya = Son() #here constructor is not called but when we create object constructor is automatically called i.e __init fun

