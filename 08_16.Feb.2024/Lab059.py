#Filter - It can filter the items from the list based on logic and it will return less no of item
number = [1, 2, 3, 4, 5, 6, 7]
even_numbers = filter(lambda i:i%2 != 0, number)
print(list(even_numbers))

#instead of lambda expression we can also have function

number = [1,2,3,4,5,6]
def even(num):
    return num%2 == 0
even_numbers = filter(even, number)
print(list(even_numbers))

#using lambda
number = [6,7,8,9,10]
even_lambda = lambda x : x%2 == 0
even_numbers = filter(even, number)
print(list(even_numbers))