def make_pizza(*topings):
    print(topings)
    for toping in topings:
        print(toping)


Sowmya = make_pizza("mushroom", "onion")
Arjun = make_pizza("mushroom", "onion", "tomatoes")
Tani = make_pizza("sweet corn", "cheese", "olives", "bellpeppers")


def make_pizza(*topings, base="wheat"):
    print(topings, base)
    for toping in topings:
        print(toping)


Sowmya = make_pizza("mushroom", "onion", base="thin")
Arjun = make_pizza("mushroom", "onion", "tomatoes")
Tani = make_pizza("sweet corn", "cheese", "olives", "bellpeppers")

# def make_pizza(*topings, *base): #multiple star parameters are not allowed in python, one argument can be multiple either topings or base
#   print(topings, base)
#   for toping in topings:
#      print(toping)
