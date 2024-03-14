#Exception is a parent of all the exception
#below errors are called as Exceptions
# #Value error - instead of int if we give string input or vice versa we get value error
#zero division error - if the number is divided by zero then we get zero division error
#syntax error - if syntax is not correct ex: if we miss except block after try then we get syntax error
#Indentation error - if the spacing is not correct
#if you know which exception is coming use that specific exception else use Exceptionerror as e

try:
    a = int(input("Enter a number \n"))
except ValueError as v: #if valueerror cannot handel then the bigger bucket exception will handle
    print(v)
except Exception as e:
    print(e)