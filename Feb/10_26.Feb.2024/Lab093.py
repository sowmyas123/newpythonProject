# Multilevel inheritance
class GF:
    def home(self):
        print("5bhk")


class Father(GF):
    def home2(self):
        print("GOA")


class Son(Father):
    def home3(self):
        print("Bangalore")


sowmya = Son()
sowmya.home()
sowmya.home2()
sowmya.home3()

MMD = Father()
MMD.home()
MMD.home2()
#MMD .home3() #Father cannot inherit son

gkd = GF()
gkd.home()
# gkd.home2() #GF cannot inherit father and son
# gkd.home3()
