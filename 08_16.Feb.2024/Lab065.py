#SET - collection of unique items - unordered unique items
set3 = {1,2,3,4,5,5,5,5,4,4}
print(len(set3))
print(set3)

#we can create empty set as below
#ep1 = set()
#ep2 = {}

list1 = [45.2, 23, 45, 23, 21]
set1 = set(list1)
print(set1)

#converting tuple to set
t = ("The testing academy", "sowmya", "The testing academy", "SOWMYA")
print(set(t))

set1 = {1,2,3,4}
set2 = {4,5,6}
my_set = set1.union(set2)
print(my_set)
my_set = set1.intersection(set2)
print(my_set)
my_set = set1.difference(set2)
print(my_set)
my_set = set2.difference(set1)
print(my_set)