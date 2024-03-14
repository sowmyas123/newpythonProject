class Car:
    name = None
    make = None
    model = None
    
    #Parameterized constructor
    def __init__(self, o_name, o_make,
                 o_model):  # init is intialization and is a special function, it will be automatically called when the object is created
        self.name = o_name
        self.make = o_make
        self.model = o_model
    
    def start_engine(self):
        print("starting a car with the name ", self.name)
        print("starting a car with the make ", self.make)
        print("starting a car with the model ", self.model)
        
lambo = Car("lambo", "v3", "2024") #when the object is created constructor function is automatically called
lambo.start_engine()

XUV = Car("XUV", "v7", "2020")
XUV.start_engine()