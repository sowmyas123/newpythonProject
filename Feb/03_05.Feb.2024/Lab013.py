#Strings are bunch of characters
#strings can be represented by double quotes "" or single quotes ''

name ="sowmya"
name2 = 'sowmya'
print(name)
print(name2)
print(type(name))
print(type(name2))

dir = "C://abc.txt"
print(dir)

dir = 'C://abc.txt'
print(dir)

dir = 'C:\abc\abc.txt'
print(dir)
#\a has a special meaning thats why it is not printed inthe output

dir = "C:\\abc\\abc.txt"
print(dir)

dir = "C:\somedir\some dir"
print(dir)

dir ='C:\somedir\some dir'
print(dir)

#for special characters like \a \n we need to use \\a \\n
dir = "C:\nsomedir\some dir" #\n new line is added
print(dir)

#raw string
#is helpful in the directory paths
dir = r'C:\nsomedir\some dir'
print(dir)

#format String f
#if we use curly braces in format string variable name is replaced with variable value
s = "Amit"
print(f"your name is {s}")

first_name = "Sowmya"
last_name = "Siddaraju"
print(f"your name is {first_name} {last_name}")
#it works with single quote also

#if we dont use f in print statement then the value of names are not replaced
first_name = "Sowmya"
last_name = "Siddaraju"
print("your name is {first_name} {last_name}")

first_name = "Sowmya"
last_name = "Siddaraju"
age = 35
isMarried = True
print(f"your name is {first_name} {last_name}, your age is {age}, are you Married {isMarried}")