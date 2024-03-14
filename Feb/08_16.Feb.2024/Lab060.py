#Tuple - collection of items
#list - is also a collection of items
#list are mutable in nature and can be changed

my_list = [1,2,3,4,5,6]
my_list[0] = 343
print(my_list)

#tuples are immutable in nature and cant be changed, means we cannot assign new value to the existing one
my_tuple = (4,5,6,7,8,9)
#my_tuple[0] = 23 # here we get type error
print(my_tuple)
print(type(my_list))
print(type(my_tuple))
print(len(my_tuple))

new_tuple = tuple(my_list) #Converting list to tuple
print(new_tuple)