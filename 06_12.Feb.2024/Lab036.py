# For
# while
# if else
# if elif else
# switch - there is no switch in python instead of that we have
# Match and Case -> alternate name of switch
# Break and Continue
# Functions - there are 3 types
# 1. Non return type
# 2. Return type
# 3. Builtin functions
# args and **kwargs
# lambda expression - we can convert long functions to one line fucntion by using lambda function


#Break
#For - > 1 to 10 -> range (1,11)
#if i == 5 -> break from the loop -> i.e come out of the loop

for counter in range(1,11):
    if counter == 5:
        break
    print(counter) #here 5 is not printed in the output
print("outside the loop")


for counter in range(1,11):
    print(counter)     #here 5 is also printed in the ouput
    if counter == 5:
        break
print("outside the loop")