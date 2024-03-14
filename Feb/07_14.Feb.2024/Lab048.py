def make_pizza(*toppings, base="wheat"):  # we can assign null value to the base
    print(toppings, base)
    for topping in toppings:
        print(topping)
        return toppings, base  # we can return multiple things in python


Sowmya_t, Sowmya_b = make_pizza("mushroom", "onion")
#Arjun = make_pizza("mushroom", "onion", "cheese", base="thin")
print(Sowmya_t)
print(Sowmya_b)
