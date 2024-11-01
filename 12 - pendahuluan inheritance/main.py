'''

inheritance -> pewarisan 

class 1 = super class, class 2 = sub class

class Superclass:
    pass

class Subclass(Superclass):
    pass

'''

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
class Assasin(Hero):
    pass

class Mage(Hero):
    pass

saber = Assasin("Saber", 100)
eudora = Mage("Eudora", 90)

print(saber.name)
print(eudora.health)
