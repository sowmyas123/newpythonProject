# Assignment operator
name = "sowmya"
# it will store the value of variable literal to identifier i.e sowmya is stored in name

#unary operator - it is applied to single value or single literal
#+ and - are the unary operator
age = +76 #no need to mention +
print(age)
mybank_balance = -100 #for negative values we need to mention - operator
print(mybank_balance)

#Not operator it is also unary operator , Not works with boolean data type
#Not operator is also called as negations
is_married = True
print(is_married)
print(not is_married) #not operator will do reverse of the variable

# is operator - is identity operator
# is operator returns True or False
a = 5
b = 5
print(a is b) #True

a = 5
b = "sowmya"
print(a is b) #False
#it returns False because a and b identities are different a is integer and b is string

a = 5
b = 'C'
print(a is b)

my_list = [1,2,3]
my_list2 = [1,2,3,4]
print(my_list is my_list2)
