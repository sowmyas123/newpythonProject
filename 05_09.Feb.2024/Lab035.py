# write a program that calculates and displays the letter grade for a given numerical score (eg A,B,C,D,E,F)
# based on the following grading scale
# input - score - 89
# output - B
# A = 90 - 100
# B = 80 - 89
# C = 70 - 79
# D = 60 - 69
# E = 50 - 59

# if, elif, else

# step 1 - figure out the inputs
scale = int(input("Enter the number you got: "))
# step 2 - figure out the logic i.e print A if scale is greater or equal to 90 and less than or equal 100
# step 3 - print output
if scale >= 90 and scale <= 100:
    print("grade is : A")
elif scale >= 80 and scale <= 89:
    print("grade is : B")
elif scale >= 70 and scale <= 79:
    print("grade is : c")
elif scale >= 60 and scale <= 69:
    print("grade is : D")
elif scale >= 50 and scale <= 59:
    print("grade is : E")
else:
    print("grade is: invalid input")
