#File Handling - how to read a code and write into it using python code

#to read a file
# Function
# open("file_name", "mode")

#Mode
# r - reading (default)
# w - writing (creates a new file or truncates existing one)
# a - appending
# b - binary mode - .exe files are binary files
# + - updating (reading and writing)

# Read and write content
# Read a file
# Reading entire content: content = file_object.read()
# line = file_object.readline() for a single line
# lines = file_object.readlines() for a all lines in the list
# close the file

file = open("TestData.txt", 'r')
content = file.read()
print(content)
file.close()
