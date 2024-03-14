#String concat
str1 = "Hello"
str2 = "world"
str3 = str1 + str2
print(str3)

#name = "sowmya"
#age = 34
#r = name + age
#print(r) #gives concatenation error - TypeError: can only concatenate str (not "int") to str

#if we convert integer to string then concatenation is poosible
name = "sowmya"
age = 34
r = name + str(age)
print(r)

g = "Hi"
#g+= "siri" # g+ is same as g = g + siri
g = g + "siri"
print(g)

#Increment and Decrement operator
x = 4
x += 1
print(x)

y = 8
y -= 1
print(y)

#post increment and pre increment i.e ++ and -- are not allowed in python