#Match case is a inbuilt condition
#switch
numbers = int(input("Enter the number 1-6\n"))
match numbers: #Break is not needed in case of Match and case
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case 4:
        print("You have entered 4")
    case 5:
        print("You have entered 5")
    case _:
        print("No idea")


browser = input("Enter the browser name \n")
match browser:
    case "chrome":
        print("chrome is executed")
    case "firefox":
        print("firefox is executed")
    case _:
        print("no browser found")