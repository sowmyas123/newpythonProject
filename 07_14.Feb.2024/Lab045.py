# Function is a block of code which can be executed
# they can return something - Return type
# they can't return anything - Non return type
# they have parameters
# they don't have parameters/arguments

# define the function
def say_hello():  # this is non return type and no parameters/arguments means it is not taking any input
    # write the code
    print("hello")


# call the function
say_hello()

def say_hello_arg(name):  # this is non return type and with arguments
    # write the code
    print("hello", name)

# call the function
say_hello_arg("sowmya") #if we dont pass argument here we get TypeError: say_hello_arg() missing 1 required positional argument: 'name'

def say_hello_args(name, age):  # we can also have multiple arguments
    # write the code
    print("hello", name, age)

# call the function
say_hello_args("sowmya", "true")


def say_hello_arg(name="Siri"):  # this is non return type and with arguments
    # write the code
    print("hello", name)
    
say_hello_arg() #here its taking siri as default name
say_hello_arg("Tanishka") #if we pass value it will replace the default value


def sum_number_argument_ret(a, b): #Return type function with arguments
    return a + b

result1 = sum_number_argument_ret(3,9)
result2 = sum_number_argument_ret("sowmya","Arjun")
result3 = sum_number_argument_ret(a = 434,b = 132)# we can also pass arguments like this

print(result1)
print(result2)
print(result3)

def sum_number_argument_ret(a, b):
    return a + b

result1 = sum_number_argument_ret(3, 1) # if we pass only 1 argument instead of 2 it will give an error TypeError: sum_number_argument_ret() missing 1 required positional argument: 'b'

def f1(a, b, c):
    return a + b+ c

#def f1(a=1, b=1, c=1): when we give default values like this all of the below are valid scenarios
   # return a + b+ c
    
result = f1()
result1 = f1(1)
result2 = f1(1, 2)
result3 = f1(1, 2, 3)
result4 = f1(a = 10, b= 20, c=30)
print(result)
print(result1)
print(result2)
print(result3)
print(result4)



