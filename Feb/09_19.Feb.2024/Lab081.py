class mul_param():
    name = None # class variable
    
    def print_information(self, first_name, last_name, age):
        a = 10 #local variable
        print("Your name is ", first_name, last_name, age)
        
obj_ref = mul_param()
obj_ref.print_information("sowmya", "arjun", 35)