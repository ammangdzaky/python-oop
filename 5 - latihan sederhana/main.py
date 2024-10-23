### LATIHAN OOP MENYERANG DAN DISERANG

import random
import os
os.system("cls")


class hero:
    
    def __init__(self, name, health, attack, armor):
        
        if type(name) != str:
            raise TypeError("nama harus string!!!".upper())
        if type(health) != int or type(attack) != int or type(armor) != int:
            raise TypeError("health, attack, dan power harus integer".upper())
        
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        
    def menyerang(self, hero_lawan):
        print(f"{self.name} menyerang {hero_lawan.name}")
        hero_lawan.diserang(self)
        
    def diserang(self, hero_lawan):
        damage_diterima = hero_lawan.attack
        self.health -= damage_diterima/self.armor
        print(f"\t{self.name} diserang {hero_lawan.name}")
        print(f"\tsisa health {self.name} = {self.health:.1f}")
        
        

# BUAT OBJEKNYA DISINI
ambatron = hero(name="AMBATRON", health=100, armor=20, attack=random.randint(1,5))
ambatukam = hero("AMBATUKAM",100,random.randint(1,5),20) 


# PERANG ANTARA AMBATRON DAN AMBATUKAM DIMULAI!!!!
hari = 0

while True:
    print("="*50)
    ambatron.menyerang(ambatukam)
    if ambatukam.health <= 0:
        print("ambatukam kalah!!")
        break
    print("="*50)
    ambatukam.menyerang(ambatron)
    print("="*50)
    hari += 1
    if ambatron.health <= 0:
        print("ambatron kalah!!")
        break

print(f"\n\npeperangan ini menghabiskan waktu {hari} hari!!!".upper())
