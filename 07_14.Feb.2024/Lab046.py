# *args -  means we can pass any no of arguments
def sum(a, b, c):
    return a + b + c


r = sum(1, 2, 3)


# print(r)

# in case if we want to add new number we have to keep on adding instead of that we can use *args means we can call any no of arguments
# *args is nothing but a list

def print_argument(*args):
    for i in args:
        print(i, end=" ")
    
print_argument(1)
print_argument(1, 2)
print_argument(1, 2, 3)
print_argument(1, 2, 3, 4)
