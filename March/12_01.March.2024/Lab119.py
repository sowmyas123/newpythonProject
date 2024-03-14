#if file is present somewhere else the how to read the file
path = "/Users/arjundwarakanath/PycharmProjects/newpythonProject/Feb/febfile.txt"
with open(path) as file:
    print(file.read())
    
import os
print = (os.getcwd())