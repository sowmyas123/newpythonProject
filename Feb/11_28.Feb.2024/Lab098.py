class A:
    def methodA(self):
        return "method A"
    
class B(A):
    def methodB(self):
        return "method B"
    
class C(A):
    def methodC(self):
        return "method C"
    
class D(B,C):
    def methodD(self):
        return "Method D"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())