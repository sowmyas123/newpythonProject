# car - is a class
#Object - tesla, lambo, bmw

class car:
    name = None
    color = None
    model = None
    engine = None
    speed = None
    
    def start_engine(self):
        print("start the engine")
        
    def drive(self):
        print("drive")
        
    def car_break(self):
        print("break")
        
    def who_is_driving(self):
        print("I am driving -> " + self.name) #self is used to access the variables/attributes
        
tesla_obj_ref = car()
lambo_obj_ref = car()

tesla_obj_ref.name = "Tesla"
lambo_obj_ref.name = "Lambo"

tesla_obj_ref.who_is_driving()
lambo_obj_ref.who_is_driving() #who_is_driving function is same in both the case but it behaves differently based on the reference
