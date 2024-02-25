my_dict = {'b': 1, 'a': 2, 'c': 3}
for k, v in my_dict.items():
    if k == 'b':
        print("b value found")
    else:
        print("b value not found")
        
op = 'b' in my_dict
print(op)