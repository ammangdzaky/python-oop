class Animal:
    def __init__(self, name, species, color):
        self.name = name
        self.species = species
        self.color = color
        
    def info(self):
        print("\nini adalah info dari super class:")
        print(f"name = {self.name} \nspecies = {self.species} \ncolor = {self.color}")

class Cat(Animal):
    
    def __init__(self,name,species,color):
        super().__init__(name,species,color)
        
    # override method -> artinya menimpa method dari superclass
    def info(self):
        print("\nini adalah info dari sub class:")
        print(f"type = CAT \nname = {self.name} \nspecies = {self.species} \ncolor = {self.color}")

class Chicken(Animal):
    
    def __init__(self,name,species,color):
        super().__init__(name,species,color)
        
neko = Cat("sumbul", "anggora", "orange")
manuk = Chicken("el gato", "kate", "red")

neko.info() # -> object dari class cat dengan override method
manuk.info() # -> object dari class chicken tanpa override method