class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number \n"))
        except Exception as e:
            print("Enter int only as value of a")
        else:
            print(a)
        finally:
            print("Anyhow i will be printed")

x = XYZ()
x.f1()