def sum_of_num (a,b):
    return (a + b)

result = sum_of_num(898.32892,9)
print(result)


result = sum_of_num("sowmya", " B S") #for strings concatenation will happen
print(result)

result = sum_of_num("sowmya", 123) # we get error TypeError: can only concatenate str (not "int") to str
print(result)
