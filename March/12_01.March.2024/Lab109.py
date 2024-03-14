#to handle any exception in python we can use
#try and except block
#try - try the code if there is an error
# except - execute except code if there is a problem in try



a = int(input("Enter num 1\n"))
b = int(input("Enter num 2\n"))

try:
    c = a/b
    print("division is", c)
except Exception as e:
    print(e)
    print("Zero division , please dont use B as zero")

print("this is a important message that we need to show to the user")
