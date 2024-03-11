class GF:
    def car(self):
        return "old car"
    
class F(GF):
        def car(self):
            return "honda civic"
        
class S(F):
    #def car(self):
        #return "Lambo"
        pass
    
Son = S()
print(Son.car())