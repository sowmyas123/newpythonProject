# Dictonary - is unordered key value pair key and value
name = "sowmya"
# key - name
# value - sowmya
# we can create empty dictonary as below
my_dict = {}
my_dict2 = dict()
print(type(my_dict))
print(type(my_dict2))

phonebook = {"Batman": 9876543210, "spiderman": 8765432109, "wonderwoman": 7654321098}
print(len(phonebook))
print(phonebook["Batman"])  # to get individual phone no we have to keys and not index

phonebook2 = dict(Thor=2345, Master=324, sir=987)
print(phonebook2["sir"])
print(phonebook2.get('sir'))

sowmya_details = dict(name="sowmya", age=40, address="Bengaluru")
arjun_details = {"name": "arjun", "50": 79, "address": "Tumkur"}
print(arjun_details["50"])
print(arjun_details.get("address"))

my_dict = {'a': 1, 'b': 45, 'c': 23, 'a':29} #keys cannot be duplicated but values can be duplicated last key will be kept
print(len(my_dict))
print(my_dict)

