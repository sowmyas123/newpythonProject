class car():
    color = None
    model = None
    
    def car_detaisl(self):
        print("your car details is", self.color, self.model)
    
car_color = input("enter the car color\n")
car_model = input("enter the car model\n")


car_obj_ref = car()
car_obj_ref.color = car_color
car_obj_ref.model = car_model

car_obj_ref.car_detaisl()