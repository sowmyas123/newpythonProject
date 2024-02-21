# Reverse a string
str = "Sowmya"
rev_str = " "
for c in str:
    rev_str = c + rev_str

print(rev_str)


# using functions to reverse a string
def reverse_string(str):
    rev_str = " "
    for c in str:
        rev_str = c + rev_str
    return rev_str

name = reverse_string("Arjun")
print(name)

