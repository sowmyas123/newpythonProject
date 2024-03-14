#try, except and finally
#multiple exception

try:
    num1 = int(input("Enter number 1\n"))
    num2 = int(input("Enter number 2\n"))
    result = num1 / num2
    
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
else:
    print(f"Result {result}")
finally:
    print("I will be executed anyhow")
    
#if there is a problem in line no 5 & 6 i.e instead of int if we give string input line no 9 & 10 will handle
#if there is a problem in line no 7 line no 11 & 12 will handle
#if there is no problem at all line no 14 will be printed
#finally will be executed in all the conditions