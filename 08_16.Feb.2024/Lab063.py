x = 3 #single assignment
a,b = 2,3 #multiple assignment
q,w,e = (4,5,6)# in tuple also we can do multiple assignment

#Nested tuples
#tuples within tuples
hero1 = ("Batman", "Spiderman")
hero2 = ("wonder woman", "Diana prince")
awesome_team = (hero1, hero2)
print(awesome_team)
print(awesome_team[0])
print(awesome_team[0][1])
print(awesome_team[1][1])

#how to search in tuple
cities = ("London", "Paris", "The US", "Bangalore")
print("Mandya" in cities)
print("Paris" in cities)


