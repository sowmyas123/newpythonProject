#side1 == Side 2 == side 3 -> Equilateral triange
#side1 == side2 or side1 == side 3 or side2 == side3-> isoceles triange
#else scalene triangle

side1 = float(input("Enter the side1\n"))
side2 = float(input("Enter the side2\n"))
side3 = float(input("Enter the side3\n"))

if side1 == side2  == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("isoceles triangle")
else:
    print("Scalene triangle")


