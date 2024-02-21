#Lambda expression
#it is used to convert functions to one liner in python just to save the length of the file

def double_my_salary(salary):
    return salary*2
result = double_my_salary(100)
print(result)

#we can write the above function in one liner using lambda expression

d_salary = lambda salary : salary * 2
print(d_salary(10))

pow_of_two = lambda num : num * 2
print(pow_of_two(5))

sum = lambda a, b, c : a + b + c #it takes multiple arguments also
print(sum(4,9,8))

say_my_name = lambda name: print("your name is ", name)
say_my_name("sowmya")