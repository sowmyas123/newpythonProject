def sq_of_number(num):
    return num ** 2

#result = sq_of_num(10)
#print(result)

#for each item to call sq number instead of for loop we can use map() function
#map() - it takes each element from the list and execute the function on it

numbers = [1, 2, 3, 4, 5]

sq_numbers = list(map(sq_of_number, numbers)) #here 1st argument is which function u want to execute,
print(sq_numbers)                             # 2nd argument is type of list where u want to execute and it returns exactly the same list
 