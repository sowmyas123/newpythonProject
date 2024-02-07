#Take 2 numbers from user and Add 2 numbers
#Step1 = Take input
#step2 = sum
num1 = (input("Enter the first number: "))
num2 = (input("Enter the second number: "))
print(num1)
print(num2)
print(type(num1))
num3 = int(num1)+int(num2)
#here we are converting str -> int by int() method
#to convert int -> str str()
#str + str -> concat i.e combine them or join tenm
print(num3)
print(type(num3))

#OR

num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))
print(num1)
print(num2)
print(type(num1))
num3 = num1 + num2
print(num3)
print(type(num3))
