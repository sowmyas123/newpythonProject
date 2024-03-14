my_list = [1, 2, 3] #(0,1,2)
my_list2 = [1, True, "sowmya", 18.233]

#Indexing
print("Element at index 0:", my_list[0])

#changing an element
my_list[1] = 20
print("list after changing element at index 1:", my_list)

#append means add an element in the end
my_list.append(4)
print("list after appending: ", my_list)

#extend the list
my_list.extend([5,8])  # extend by list
print("list after extending:", my_list)

#insert an element
my_list.insert(1, 'a')
print("list after inserting:", my_list) #now the list heterogenous - it contains different type of elements

#remove an item
my_list.remove('a')
print("list after removing 'a':", my_list)

#copy the list
my_copy_list =  my_list.copy()
print(my_copy_list)

#clear the list
#my_list.clear()
print("Initial list: ", my_list) #after clearing everything will be deleted except copylist

print("Index of 3 in the list: ", my_list.index(3))

#sorting the list
my_copy_list.sort()
print(my_copy_list)

#reverse the list
my_copy_list.reverse()
print(my_copy_list)

#print index of all the element
print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])
print(my_copy_list[4])