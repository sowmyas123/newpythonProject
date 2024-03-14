name = "batman"
print(len(name)) #len is length of the name
print(name[0]) #0 is the index
print(name[4])
print(name[5]) #gets error index error: string index out of range
print(len(name)-1)
print(name[len(name)-1]) #first will get lenght of the name and then the name i.e character

#String ae immutable in nature means it cannot be changed or modified
string ="Hello"
string[0] = "P" #typeerror: 'str' object does not support item assignment
# we can replace the string but cannot change
print(string)

string = "Hi"
string = "Sowmya" #is possible
#string[0] = "P" e
print(string)