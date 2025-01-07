class hero: #template
    pass

hero_1 = hero() #object
hero_2 = hero() #object
hero_3 = hero() #object

hero_1.name = "alucard"
hero_1.power = 1000

hero_2.name = "rusdi"
hero_2.power = 10000

hero_3.name = "angela"
hero_3.power = 10

print("\n")

print("hero 1:")
print(hero_1)
print(hero_1.__dict__)
print(f"hero_1 name = {hero_1.name}")
print(f"hero_1 power = {hero_1.power}")

print("\n")