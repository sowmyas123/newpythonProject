# Loop
# Loop is if we want to repeat a block of code multiple times we use loops
#range(start, stop, step) from it has to start, where it has to stop and how much it is to step

for i in range(6):
    print("Hi", i)
    print(i) # range starts from index 0 i.e 0 to 5

for i in range(1, 6): #here range starts from 1 to 5
        print(i)

for i in range(1,20,2): #here 2 is stepby i.e it returns alternate numbers
    print(i)

#if you want print "hello world" ten times

for i in range(1,11):
    print("Hello world", i)