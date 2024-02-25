class cal:
    def sum(self, a,b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a/b

    
object_ref = cal()
result1 = object_ref.sum(3,4)
result2 = object_ref.sub(2,9)
result3 = object_ref.mul(3,8)
result4 = object_ref.div(90,4)
print(result1)
print(result2)
print(result3)
print(result4)
