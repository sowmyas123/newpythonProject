#Function - is a block of code which will help to execute some task
#In Return type functions
#we need to define a function or
#we need to call a function - builtin function

#Non Return type function
#1. define the function
def greet():
    print("Hello, How are you?")

#2. Call the function
greet()  # it does not return anything # we can call this function many times
greet()
greet()
greet()
greet()

#OR we can also use for loop
for i in range(5):
    greet()


#this is also calling the function
result = greet()
print(result) #output is None means it doesn't return anything




